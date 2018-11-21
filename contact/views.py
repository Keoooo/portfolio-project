from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import ContactForm


def contactpage(request):
    return render(request, 'contact/homepage.html')

