import random 
from django import template
from django.urls import reverse
from ecomapp.models import *
from django.contrib import messages
from django.utils.translation import gettext as _
register = template.Library()
from django_filters import rest_framework as filters
from django.shortcuts import render


@register.simple_tag
def Catego():
    a=Category.objects.all()
    return a
