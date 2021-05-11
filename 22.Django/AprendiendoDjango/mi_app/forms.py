from django import forms

class FormArticle(forms.Form):
    title= forms.CharField(
        label='Título'
    )

    content= forms.CharField(
        label='Contenido',
        widget=forms.Textarea#el widget es para que se vea como textarea
    )