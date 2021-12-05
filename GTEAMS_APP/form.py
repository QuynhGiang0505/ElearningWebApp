from django import forms
from django.db import models
from django.forms import fields
from GTEAMS_APP.models import article_blog
from GTEAMS_APP.models import Contact

class CreateNewContact(forms.ModelForm):
    class Meta:
        model= Contact
        fields=(
            'name',
            'email',
            'title',
            'content'
        )




