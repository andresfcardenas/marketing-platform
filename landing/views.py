#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

def landing(request):
    return render(request, 'landing/index.html', {})