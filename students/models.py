from django.db import models
from django.db.models import Sum
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError

from db.models import StudentDegree, Gender, StatusOfSponsorship
from sponsors.models import Sponsors


class EEI(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Students(models.Model):
    full_name = models.CharField(max_length=512)
    phone_number = PhoneNumberField(unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    degree = models.CharField(max_length=7, choices=StudentDegree.choices, default=StudentDegree.BAKLAVR)
    eei = models.ForeignKey(EEI, on_delete=models.PROTECT)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sponsors = models.ManyToManyField(Sponsors, through='SponsorStudent', related_name='student')
    reg_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}'


class SponsorStudent(models.Model):
    sponsor = models.ForeignKey(Sponsors, related_name='sponsorstudent', on_delete=models.PROTECT)
    student = models.ForeignKey(Students, related_name='studentsponsor', on_delete=models.PROTECT)
    amount = models.FloatField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.full_name} sponsored by {self.sponsor.full_name}'

    def clean(self):
        if self.amount > self.sponsor.sponsorship_amount:
            raise ValidationError('You don\'t have enough money')
        if self.amount > self.student.contract_amount:
            raise ValidationError('You exceed the value of the contract')
        if self.sponsor.status != StatusOfSponsorship.VERIFAYED:
            raise ValidationError('At first you must verifayed')

