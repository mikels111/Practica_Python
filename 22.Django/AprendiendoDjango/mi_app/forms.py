from django import forms
from django.core import validators

# Este fichero es para hacer forms basados en clases


class FormArticle(forms.Form):
    title = forms.CharField(
        label='Título',
        max_length=40,
        required=True,
        widget=forms.TextInput(  # para describir el input de tipo text
            attrs={  # los atributos de la etiqueta
                'placeholder': 'Titulo',
                'class': 'titulo_form_article'
            }
        ),
        validators=[  # para que te salgan los mensajes de los validadores hay que poner el atributo(el de arriba) required en true
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator(
                '^[A-Za-z0-9ñ ]*$', 'El titulo está mal formado', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label='Contenido',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Contenido',
                'class': 'content_form_article'
            }
        ),  # el widget es para describir que es un textarea
        validators=[
            validators.MaxLengthValidator(20,'Máximo 20 caracteres')
        ]
    )
    # content.widget.attrs.update({ #otra manera de meter los atributos
    #     'placeholder': 'Contenido',
    #     'class': 'content_form_article',
    #     'id':'content'
    #     })

    public_options = [(1, 'Si'), (0, 'No')]

    public = forms.TypedChoiceField(  # select
        label='publicado',
        choices=public_options
    )
