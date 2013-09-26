#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template.loader import render_to_string


from store.models import Store
from store.models import Product
from userprofile.models import ProviderRequest
from userprofile.forms import UserRegistrationForm
from userprofile.forms import ProviderRequestForm


def ajax_login(request):
    """Logs in a user via ajax.
    """
    if request.is_ajax():
        if request.user.is_authenticated():
            return HttpResponse('Usted ya está autenticado.')

        elif request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request, form.get_user())

                return HttpResponse('ok')

        else:
            form = AuthenticationForm()

        return render(request, 'registration/ajax_login.html', {
            'form': form,
        })

    raise Http404


def ajax_register(request):
    """Show the registration form via ajax
    """
    if request.is_ajax():
        form = UserRegistrationForm()

        return render(request, 'registration/ajax_registration_form.html', {
            'form': form,
        })

    raise Http404


def ajax_provider_request(request):
    """This view create a new provider request.
    """
    if request.is_ajax():
        if request.method == 'POST':
            form = ProviderRequestForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                product = form.cleaned_data['product']
                phone = form.cleaned_data['phone']
                more_info = form.cleaned_data['more_info']
                provider_request = ProviderRequest.objects.create(
                    name=name,
                    email=email,
                    product=product,
                    phone=phone,
                    more_info=more_info,
                )

                provider_request.save()

                email_message = EmailMessage(
                    u'[Ligu] Hemos recibido su solicitud en Ligu.',
                    'Para nosotros es muy importante tenerlo en cuenta \
                    \ncomo uno de nuestros proveedores en Ligu, por este \
                    \npor este motivo uno de nuestros asesores estará \
                    \ncontactandose contigo lo más pronto posible.',
                    to=[provider_request.email],
                    headers={'Reply-To': settings.EMAIL_REPLY_TO},
                )
                email_message.content_subtype = 'html'
                email_message.send()

                send_mail(
                    u'[Ligu] Alguien quiere ser proveedor en Ligu!.',
                    u'Una persona esta interesada en ser proveedoraa de Ligu \
                    \nLos datos de la persona son: \
                    \nNombre = {0} \
                    \nCorreo = {1} \
                    \nProducto que ofrece = {2} \
                    \nTelefono de contacto = {3} \
                    \nMas informacion proporcionada por la persona = {4}'.format(
                        provider_request.name,
                        provider_request.email,
                        provider_request.product,
                        provider_request.phone,
                        provider_request.more_info,
                    ),
                    'no-responder@ligu.co',
                    settings.EMAIL_REPLY_TO,
                )
                return HttpResponse('ok')

        else:
            form = ProviderRequestForm()

        return render(request, 'userprofile/ajax_provider_request.html', {
            'form': form,
        })

    raise Http404


@login_required
def dashboard(request):
    """This view show process the list store
    """
    try:
        store = Store.objects.get(created_by=request.user)
    except ObjectDoesNotExist:
        store = False
    products_list = Product.objects.filter(store=store).exclude(quantity__lte=0)
    return render(request, 'userprofile/dashboard.html', {
        'store': store,
        'products_list': products_list,
        'slug': store,
    })
