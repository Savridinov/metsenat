from django.contrib import admin
from .models import Students, SponsorStudent
admin.site.register(SponsorStudent)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'eei')
    list_filter = ('type',)
    # ordering = ('alloted_amount', 'contract_amount')

