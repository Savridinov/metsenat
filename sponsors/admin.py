from django.contrib import admin
from .models import Sponsors


@admin.register(Sponsors)
class SponsorsAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'status', 'sponsorship_amount')
    list_filter = ('status', 'is_organization')
    ordering = ('sponsorship_amount',)   #'spent_amount'
    list_display = ('full_name', 'status', 'sponsorship_amount',)
    readonly_fields = ('reg_date', )