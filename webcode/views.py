from django.shortcuts import render
from django.views.generic import CreateView
from .serializers import *
from .models import *


class SponsorsCreate(CreateView):
    pass
