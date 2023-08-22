from django import forms


class MLModelTextForm(forms.Form):
    question = forms.CharField(label='Вопрос', max_length=1000)
    context = forms.CharField(
        label='Контекст',
        max_length=100000,
    )
