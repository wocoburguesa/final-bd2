# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import HttpResponseRedirect, Http404

from circuits.forms import CircuitForm
from circuits.models import Circuit
from circuits.utils import circuit_category_list


def show_home(request):
    pass

def  privacy_policy(request):
    return render(request,
            'website/privacy_policy.html',
            {},
        )


def terms_of_use(request):
    return render(request,
            'website/terms_of_use.html',
            {},
        )


def who_we_are(request):
    return render(request,
            'website/who_we_are.html',
            {},
        )


def about_worldrat(request):
    return render(request,
            'website/about_worldrat.html',
            {},
        )
