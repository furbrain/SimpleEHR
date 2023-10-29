from django.forms import ModelForm, TextInput

from EHR.models import Code


class CodeForm(ModelForm):
    class Meta:
        model = Code
        fields = ['text', 'concept_code', 'term_code', 'date', 'significant', 'active']
        widgets = {
            'concept_code': TextInput(attrs={"readonly":"true"}),
            'term_code': TextInput(attrs={"readonly": "true"}),
        }

