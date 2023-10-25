from django.core.validators import RegexValidator
from django.db import models

NHSNumberValidator = RegexValidator(regex=r"^\d{10}$", message="Must be 10 digits only")


class Person:
    given = models.CharField(max_length=32)
    family = models.CharField(max_length=32)
    nhs_number = models.CharField(max_length=10, validators=[NHSNumberValidator])
    birthdate = models.DateField()


class Code:
    concept_code = models.BigIntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    significant = models.BooleanField()
    active = models.BooleanField()
    date = models.DateField()

