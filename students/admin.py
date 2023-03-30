from django.contrib import admin
from .models import Students, SponsorStudent, EEI

admin.site.register(SponsorStudent)
admin.site.register(EEI)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'eei')
    list_filter = ('degree', 'gender')
    list_display = ('full_name', 'gender', 'contract_amount')
    # ordering = ('alloted_amount', 'contract_amount')
    readonly_fields = ('reg_date', 'updated_time')

