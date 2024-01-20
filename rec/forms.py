from django import forms

from rec.models import Recruitment


class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = '__all__'
