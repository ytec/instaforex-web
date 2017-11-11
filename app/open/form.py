from django import forms

class FormModelAnonymus(forms.Form):
    name = forms.CharField(max_length=40,
                            required=True,
                            initial='Su nombre')

    surnames = forms.CharField(max_length=100,
                                required=False,
                                initial='Sus apellidos' )

    direcc = forms.CharField(max_length=40,
                            required=False,
                            initial='Direcion' )

    direcc2 = forms.CharField(max_length=40,
                            required=False,
                            initial='Continuacion de la direcion' )

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

class FormModelDemo(forms.Form):
    Name = forms.CharField(max_length=25,initial="Name")
    SurNames = forms.CharField(max_length=100,initial="SurName")
    Direcc = forms.CharField(max_length=100,initial="Direcc")
    Direcc2 = forms.CharField(max_length=100,initial="Direcc2")
    City = forms.CharField(max_length=30,initial="City")
    ZipCode = forms.CharField(max_length=10,initial="ZipCode")
    Country = forms.CharField(max_length=30,initial="Country")
    State = forms.CharField(max_length=30,initial="State")
    Email = forms.EmailField()
    Phone = forms.CharField(max_length=15,initial="Phone")
    AccountType = forms.CharField(max_length=30,initial="AccountType")
    Leverage = forms.CharField(max_length=30,initial="Leverage")
    NotificationLanguage = forms.CharField(max_length=30,initial="AccountType")
    Currency = forms.CharField(max_length=30,initial="Currency")
    DateOfBirth = forms.DateTimeField()
    AffiliateCode = forms.CharField(max_length=10,initial="1234")
    InitialDeposit = forms.CharField(max_length=20,initial="1000" )
    InvestorPassword = forms.CharField(max_length=30,initial="password")

class FormModelReal(forms.Form):
    Name = forms.CharField(max_length=25,initial="Name")
    SurNames = forms.CharField(max_length=100,initial="SurName")
    Direcc = forms.CharField(max_length=100,initial="Direcc")
    Direcc2 = forms.CharField(max_length=100,initial="Direcc2")
    City = forms.CharField(max_length=30,initial="City")
    ZipCode = forms.CharField(max_length=10,initial="ZipCode")
    Country = forms.CharField(max_length=30,initial="Country")
    State = forms.CharField(max_length=30,initial="State")
    Email = forms.EmailField()
    Phone = forms.CharField(max_length=15,initial="Phone")
    AccountType = forms.CharField(max_length=30,initial="AccountType")
    Leverage = forms.CharField(max_length=30,initial="Leverage")
    NotificationLanguage = forms.CharField(max_length=30,initial="AccountType")
    Currency = forms.CharField(max_length=30,initial="Currency")
    DateOfBirth = forms.DateTimeField()
    AffiliateCode = forms.CharField(max_length=10,initial="1234")
