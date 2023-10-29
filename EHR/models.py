from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

NHSNumberValidator = RegexValidator(regex=r"^\d{10}$", message="Must be 10 digits only")


class Person(models.Model):
    given = models.CharField(max_length=32)
    family = models.CharField(max_length=32)
    nhs_number = models.CharField(max_length=10, validators=[NHSNumberValidator])
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.given} {self.family} ({self.birthdate})"

    def get_absolute_url(self):
        return reverse("person_detail", args=[self.pk])

class Code(models.Model):
    concept_code = models.BigIntegerField()
    term_code = models.BigIntegerField()
    text = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    significant = models.BooleanField()
    active = models.BooleanField()
    date = models.DateField()
    
    def __str__(self):
        return self.text

