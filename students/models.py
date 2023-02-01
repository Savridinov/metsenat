from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from db.models import StudentDegree, Gender
from sponsors.models import Sponsors


class EEI(models.Model):
    name = models.CharField(max_length=512)


class Students(models.Model):
    full_name = models.CharField(max_length=512)
    phone_number = PhoneNumberField(unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True, null=True)
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