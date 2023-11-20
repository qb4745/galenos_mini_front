from django import forms


class PagoForm(forms.Form):
    medico_id = forms.IntegerField()
    monto = forms.IntegerField()
    tipo_pago = forms.CharField(max_length=100)


class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class RolForm(forms.Form):
    name = forms.CharField(max_length=100)
