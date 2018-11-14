from django.shortcuts import render
from .models import PortfolioExample


def homepage(request):
	examples = PortfolioExample.objects
	return render(request, 'portexample/homepage.html', {'PortfolioExample':examples})

