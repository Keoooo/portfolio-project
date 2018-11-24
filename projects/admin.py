from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PortfolioExample

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'

admin.site.register(PortfolioExample, SummernoteModelAdmin)

