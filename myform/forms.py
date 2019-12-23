from django import forms
from myform.models import Person

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('first_name', 'last_name', 'mobile', 'email', 'bio')