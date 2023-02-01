from django.contrib import admin
from .models import Sponsors

@admin.register(Sponsors)
class SponsorsAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'status')
    list_filter = ('status',)
    ordering = ('sponsorship_amount',)   #'spent_amount'