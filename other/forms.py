from django import forms

from .models import Mail1, Mail2


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail1
        fields = ('first_name', 'name', 'last_name', 'email', 'phone',
                  'address', 'text', 'file',)


class MailForm2(forms.ModelForm):
    class Meta:
        model = Mail2
        fields = ('first_name', 'name', 'last_name', 'email', 'phone',
                  'address', 'text', 'file', 'organ', 'inn', 'position')

