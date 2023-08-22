from django.shortcuts import render

from .forms import MLModelTextForm
from .apps import CoreFunctionalityConfig


def index(request):
    answer = 'Задайте вопрос'
    template = 'index.html'
    if request.method == 'POST':
        form = MLModelTextForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            context = form.cleaned_data['context']
            ml_model = CoreFunctionalityConfig.ml_model
            answer = ml_model.get_answer(question, context)
            return render(request, template, {'form': form, 'answer': answer})

    else:
        context = {
            'question': 'Why is model conversion important?',
            'context':
                'The option to convert models between FARM '
                'and transformers gives freedom to the user and let '
                'people easily switch between frameworks.'
        }
        form = MLModelTextForm(context)

    return render(request, template, {'form': form, 'answer': answer})
