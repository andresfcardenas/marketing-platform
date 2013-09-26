#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from landing.forms import LandingForm
from store.models import Product
from store.models import Store


def home(request):
    """Render the landing page
    """
    product_list = Product.objects.all().order_by('-created_at')[:10]
    store_list = Store.objects.all().order_by('-created_at')[:10]
    product_chocolate = Product.objects.filter(
        category__name='Chocolates'
    ).order_by('-created_at')[:4]

    product_cupcakes = Product.objects.filter(
        category__name='Cupcakes'
    ).order_by('-created_at')[:4]

    product_postres = Product.objects.filter(
        category__name='Postres'
    ).order_by('-created_at')[:4]

    if request.is_ajax() and request.method == 'POST':
        form = LandingForm(
            request.POST,
        )
        if form.is_valid():
            form.save()
            email_message = EmailMessage(
                u'[Ligu] Hemos recibido su solicitud en Ligu.',
                'Hola {0}, \
                \nPara nosotros es muy importante ayudarlo \
                \na encontrar el regalo ideal para esa persona especial\
                \npor este motivo uno de nuestros asesores estará \
                \ncontactandose contigo lo más pronto posible para ayudarte.'.format(form.cleaned_data['name']),
                to=[form.cleaned_data['email']],
                headers={'Reply-To': settings.EMAIL_REPLY_TO},
            )
            email_message.content_subtype = 'html'
            email_message.send()

            send_mail(
                u'[Ligu] Alguien quiere comprar en Ligu!.',
                u'Una persona esta interesada en comprar en Ligu \
                \nLos datos de la persona son: \
                \nNombre = {0} \
                \nCorreo = {1}'.format(
                    form.cleaned_data['name'],
                    form.cleaned_data['email'],
                ),
                'no-responder@ligu.co',
                settings.EMAIL_REPLY_TO,
            )
            return HttpResponse('ok')
    else:
        form = LandingForm()

    return render(request, 'home.html', {
        'form': form,
        'product_list': product_list,
        'store_list': store_list,
        'product_chocolate': product_chocolate,
        'product_cupcakes': product_cupcakes,
        'product_postres': product_postres,
    })