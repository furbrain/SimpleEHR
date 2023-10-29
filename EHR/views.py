from django.forms import inlineformset_factory, TextInput
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.viewsets import ModelViewSet

from .models import Person, Code
from EHR.forms import CodeForm
from .serialisers import PersonSerializer, CodeSerializer


# Create your views here.
class PersonListView(ListView):
    model = Person

def manage_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    widgets = {
        'text': TextInput(attrs={"class": "term"}),
        'concept_code': TextInput(attrs={"readonly": "true", "class": "concept_code"}),
        'term_code': TextInput(attrs={"readonly": "true", "class": "term_code"}),
        'date': TextInput(attrs={"class": "date_entry"}),
    }

    Code_FormSet = inlineformset_factory(Person, Code, fields=['text', 'concept_code', 'term_code', 'date',
                                                           'significant', 'active'], widgets=widgets)
    if request.method == "POST":
        formset = Code_FormSet(request.POST, request.FILES, instance=person)
        print(request.POST)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(person.get_absolute_url())
        else:
            print("Formset not valid")
    else:
        formset = Code_FormSet(instance=person)
    return render(request, "EHR/code_form.html", {"formset": formset, "person": person})

class CreateCodeView(CreateView):
    model = Code
    form_class = CodeForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['person'] = Person.objects.get(pk=self.kwargs['person'])
        print(self.request.POST)
        return data

    def form_valid(self, form):
        form.instance.person_id = self.kwargs['person']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("person_detail", args=[self.kwargs['person']])

class DeleteCodeView(DeleteView):
    model = Code

    def get_success_url(self):
        return reverse("person_detail", args=[self.ins])

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all().order_by('family', 'given')
    serializer_class = PersonSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['family', 'given', 'nhs_number', 'birthdate']
    filterset_fields = ['family', 'given', 'nhs_number', 'birthdate']
    #permission_classes = [permissions.IsAuthenticated]

class CodeViewSet(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    #permission_classes = [permissions.IsAuthenticated]