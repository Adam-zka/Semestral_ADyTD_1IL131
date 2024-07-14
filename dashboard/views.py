from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .dash_app import app


def dash_view(request):
    return render(request, 'dashboard/dash.html', {})
