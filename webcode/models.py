from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from db.models import StudentDegree, StatusOfSponsorship, Gender


class EEI(models.Model):
    name = models.CharField(max_length=512)


class Sponsors(models.Model):
    full_name = models.CharField(max_length=512)
    phone_number = PhoneNumberField(unique=True)
    sponsorship_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9, choices=StatusOfSponsorship.choices, default=StatusOfSponsorship.NEW)
    is_organization = models.BooleanField(default=False)
    organiztion_name = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name}'


class Students(models.Model):
    full_name = models.CharField(max_length=512)
    phone_number = PhoneNumberField(unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
    type = models.CharField(max_length=7, choices=StudentDegree.choices, default=StudentDegree.BAKLAVR)
    eei = models.ForeignKey(EEI, on_delete=models.PROTECT)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sponsor = models.ManyToManyField(Sponsors, through='SponsorStudent', related_name='student')

    def __str__(self):
        return f'{self.full_name}'


class SponsorStudent(models.Model):
    sponsor = models.ForeignKey(Sponsors, on_delete=models.PROTECT)
    student = models.ForeignKey(Students, on_delete=models.PROTECT)
    amount = models.FloatField()
    created_date = models.DateField(auto_now_add=True)