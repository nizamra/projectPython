from django import forms
from .models import *

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['firstName', 
        'lastName',
        'about',
        'email',
        'birthDate',
        'passwd',
        # 'createdAt', #django.core.exceptions.FieldError: 'createdAt' cannot be specified for User model form as it is a non-editable field
        # 'updatedAt', #django.core.exceptions.FieldError: 'updatedAt' cannot be specified for User model form as it is a non-editable field
        'mobile',
        'status',
        'privilage',
        'gender',
        'cv',
        'img',
        'raters',
        'rate',
        'location']
