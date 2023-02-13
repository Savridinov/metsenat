from django.db import models


class StudentDegree(models.TextChoices):
    # CONSTANT = db_value, user dislpay value
    BAKLAVR = 'BR', 'Baklavr'
    MAGISTER = 'MG', 'Magister'


class StatusOfSponsorship(models.TextChoices):
    NEW = 'New'
    CHECKING = 'Checking'
    VERIFAYED = 'Verifayed'
    DENIED = 'Denied'


class Gender(models.TextChoices):
    # CONSTANT = db_value, user display value
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
