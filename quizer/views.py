from django.shortcuts import render
from .forms import QuestionForm
from django.shortcuts import redirect

from .models import Question

# Create your views here.

RIGHT_ANSWERS = 0

def index(request):

	context = {
		'questions': Question.objects.all(),
	}
	
	if request.method == "POST":

		radio_button_false1 = request.POST.get('flexRadioDefaultFalse1')
		radio_button_true1 = request.POST.get('flexRadioDefaultTrue1')
		radio_button_false2 = request.POST.get('flexRadioDefaultFalse2')
		radio_button_true2 = request.POST.get('flexRadioDefaultTrue2')
		radio_button_false3 = request.POST.get('flexRadioDefaultFalse3')
		radio_button_true3 = request.POST.get('flexRadioDefaultTrue3')

		print(radio_button_false1)
		print(radio_button_true1)

		global RIGHT_ANSWERS

		first_question = Question.objects.get(pk=1)
		second_question = Question.objects.get(pk=2)
		third_question = Question.objects.get(pk=3)

		print(str(first_question.right_asnwer))

		if first_question.right_asnwer == True and radio_button_true1 == "on":
			RIGHT_ANSWERS += 1

		return redirect('right_answers')

	return render(request, 'quizer.html', context=context)

def create_question(request):
	# If user == superuser


	if request.method == "POST":
		form = QuestionForm(data=request.POST)
		if form.is_valid():
			# Check answers rigth or not
			question = form.save(commit=False)
			question.save()
		return redirect('index')

	form = QuestionForm()
	return render(request, 'create_question.html', {'form': form})

def right_answers(request):
	global RIGHT_ANSWERS
	context = {
		'right_answers': RIGHT_ANSWERS,
	}
	return render(request, 'right_answers.html', context=context)