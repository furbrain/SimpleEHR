from rest_framework import serializers
from .models import Person, Code

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['given', 'family', 'nhs_number', 'birthdate', 'code_set']

class CodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Code
        fields = ['concept_code', 'term_code', 'text', 'person', 'significant','active','date']
