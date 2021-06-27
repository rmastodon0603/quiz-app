from django.forms import ModelForm
from .models import Question
from django import forms

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question_text','right_asnwer']
		widgets = {
			'true_or_false': forms.RadioSelect
		}