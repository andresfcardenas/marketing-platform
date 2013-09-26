#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from store.models import Product
from cart.forms import CartForm
from cart.models import Order
from cart.models import CartProduct


def cart_detail(request):
    """Show the cart info, and process the cart.
    """
    cart_list = []
    cart_content = request.COOKIES.get('ligucart', None)
    if cart_content:
        try:
            # Separamos las comas ',' que al ser leidas aca son '%2C'
            for element in cart_content.split('%2C'):
                amount, producto_id, product_price = element.split('_')
                product = Product.objects.get(pk=producto_id)
                cart_list.append({
                    'amount': int(amount),
                    'product': product,
                    'subtotal': int(amount) * product.price,
                    'item_quantity': range(1, product.quantity + 1)
                })
        except:
            # Si pasa algo raro borramos el listado
            cart_list = []

    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                customer_name=form.cleaned_data['name'][:100],
                customer_email=form.cleaned_data['email'],
                customer_phone=form.cleaned_data['phone'][:10],
                customer_address=form.cleaned_data['address'][:50],
                total=0,
                more_info=form.cleaned_data['message'][:100],
            )

            total = 0
            for content in cart_list:
                product = Product.objects.get(id=content['product'].id)
                product.quantity -= content['amount']
                product.save()

                CartProduct.objects.create(
                    order=order,
                    product=content['product'],
                    amount=content['amount'],
                )
                total += int(content['subtotal'])

            order.total = total
            order.save()

            message = render_to_string('cart/cart_order_email.html', {
                'name': order.customer_name,
                'cart_list': cart_list,
                'total': total,
            })
            email_message = EmailMessage(
                u'[Ligu] Hemos recibido su orden de compra.',
                message,
                to=[order.customer_email],
                headers={'Reply-To': settings.EMAIL_REPLY_TO},
            )
            email_message.content_subtype = 'html'
            email_message.send()

            provider_emails = []
            for product in cart_list:
                print(product['product'].created_by.email)
                if product['product'].created_by.email not in provider_emails:
                    provider_emails.append(product['product'].created_by.email)

            for email in provider_emails:
                product_list = []
                for product in cart_list:
                    if email == product['product'].created_by.email:
                        product_list.append(product)

                message = render_to_string('cart/cart_products_sold_email.html', {
                    'product_list': product_list,
                })

                email_message = EmailMessage(
                    u'[Ligu] Has vendido productos en Ligu!',
                    message,
                    to=[email],
                    headers={'Reply-To': settings.EMAIL_REPLY_TO},
                )
                email_message.content_subtype = 'html'
                email_message.send()
                product_list = []


            send_mail(
                u'[Notificación] Se ha generado un nuevo pedido',
                'Se ha generado la orden numero: %s' % order.id,
                'no-responder@ligu.com',
                settings.EMAIL_REPLY_TO,
            )

            response = HttpResponseRedirect(reverse('cart:cart_complete'))
            response.delete_cookie('ligucart')

            return response

    else:
        form = CartForm()

    return render(request, 'cart/cart_detail.html', {
        'form': form,
        'cart_list': cart_list,
    })


def cart_complete(request):
    """Show the cart complete purchase page.
    """
    return render(request, 'cart/cart_complete.html')
