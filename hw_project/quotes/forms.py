from django.forms import ModelForm, CharField,TextInput, DateField, DateInput, ModelChoiceField, Select, Textarea, ModelMultipleChoiceField, SelectMultiple
from .models import Author, Quote, Tag


class QuoteForm(ModelForm):
    quote = CharField(widget=Textarea(attrs={"class": "form-control", "rows": "5"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'), widget=Select(attrs={"class": "form-select"}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"),widget=SelectMultiple(attrs={"size": "12",}))

    class Meta:
        model = Quote
        fields = ['author', 'quote', 'tags', ]

class TagForm(ModelForm):
    name = CharField(max_length=30, min_length=2, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Tag
        fields = ['name', ]

class AuthorForm(ModelForm):
    fullname = CharField(max_length=40, min_length=2, widget=TextInput(attrs={"class": "form-control"}))
    born_date  = DateField(widget=DateInput(attrs={"class": "form-control"})) 
    born_location = CharField(max_length=150,widget=TextInput(attrs={"class": "form-control",}),)
    description = CharField(max_length=40, min_length=30, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date',"born_location", 'bio',  ]