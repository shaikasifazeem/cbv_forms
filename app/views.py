from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView
class School(ListView):
    model=School
    template_name='school_list.html'
    context_object_name='SFO'
    queryset=['sname']
