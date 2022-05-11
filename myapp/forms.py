from dataclasses import field
from django.db import models
from django.forms import ModelForm, Field


from.models import User

class UserForm(ModelForm):
    class Meta:
        model=User
        fields='__all__'