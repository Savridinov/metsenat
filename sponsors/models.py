from django.db import models
from rest_framework.exceptions import ValidationError

from db.models import StatusOfSponsorship, Gender
# from phonenumber_field.modelfields import PhoneNumberField


class Sponsors(models.Model):
    full_name = models.CharField(max_length=512)
    # phone_number = PhoneNumberField(unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True, null=True)
    sponsorship_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9, choices=StatusOfSponsorship.choices, default=StatusOfSponsorship.NEW)
    is_organization = models.BooleanField(default=False)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}'

    def clean(self):
        if not self.is_organization and self.organization_name:
            raise ValidationError('A person does\'t have organization name')
        if self.is_organization and not self.organization_name:
            raise ValidationError('Need organiztion name')
        if not self.is_organization and not self.gender:
            raise ValidationError('A gender of organization? huh??')
        if not self.is_organization and not self.gender:
            raise ValidationError('Who ar you? Male or Female')

