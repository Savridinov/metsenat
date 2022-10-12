from django.contrib import admin
from .models import *


@admin.register(Sponsors)
class SponsorsAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'status')
    list_filter = ('status',)
    ordering = ('sponsorship_amount', 'spent_amount')


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'eei')
    list_filter = ('type',)
    ordering = ('alloted_amount', 'contract_amount')