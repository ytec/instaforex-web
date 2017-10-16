from django import forms

class FormModel(forms.Form):
    name = forms.CharField(max_length=40,
                            required=True,
                            initial='Su nombre')

    surnames = forms.CharField(max_length=100,
                                required=False,
                                initial='Sus apellidos' )

    direcc = forms.CharField(max_length=40,
                            required=False,
                            initial='Su ciudad' )

    direcc2 = forms.CharField(max_length=40,
                            required=False,
                            initial='Su ciudad' )

    city = forms.CharField(max_length=40,
                            required=False,
                            initial='Su ciudad' )

    cp = forms.CharField(max_length=6,
                        required=True,
                        initial='Su codigo postal' )

    language = forms.CharField(max_length=2,
                                required=False,)
    email = forms.EmailField()

    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                    error_message = ("Numero de telefono deve tener este formato: '+999999999'"), required=False,)
