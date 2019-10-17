from django import forms
from .models import *

# Форма регистрации нового Рекрута 
class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['name', 'age', 'planet', 'email']

# Форма Теста нового Рекрута
class QuestionForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    answer = forms.BooleanField()

# Форма одобрения Ситхом Рекрута
class RecruitApproveForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    approved = forms.BooleanField(required=False, help_text='Одобрить рекрута')
