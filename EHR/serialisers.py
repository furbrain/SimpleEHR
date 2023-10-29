from rest_framework import serializers
from .models import Person, Code

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'given', 'family', 'nhs_number', 'birthdate', 'code_set']
        depth = 1

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['concept_code', 'term_code', 'text', 'person', 'significant','active','date']
