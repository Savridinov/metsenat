from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class EEI(models.Model):
    name = models.CharField(max_length=512)


class Sponsors(models.Model):
    STATUS = [('NEW', 'New'),
              ('Checking', 'Checking'),
              ('Verifayed', 'Verifayed'),
              ('Denied', 'Denied'),
              ]

    full_name = models.CharField(max_length=512)
    phone_number = PhoneNumberField(unique=True)
    sponsorship_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9, choices=STATUS, default='New')
    is_organization = models.BooleanField(default=False)
    organiztion_name = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateField(auto_now_add=True)


class Students(models.Model):
    TYPE = [
        ('Baklavr', 'Barlavr'),
        ('Magistr', 'Magistr'),
    ]

    full_name = models.CharField(max_length=512)
    phone_number = PhoneNumberField(unique=True)
    type = models.CharField(max_length=7, choices=TYPE, default='Baklavr')
    eei = models.ForeignKey(EEI, on_delete=models.PROTECT)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sponsor = models.ManyToManyField(Sponsors, through='SponsorStudent', related_name='student')


class SponsorStudent(models.Model):
    sponsor = models.ForeignKey(Sponsors, on_delete=models.PROTECT)
    student = models.ForeignKey(Students, on_delete=models.PROTECT)
    amount = models.FloatField()
    created_date = models.DateField(auto_now_add=True)