from django import forms


class PagoForm(forms.Form):
    medico_id = forms.IntegerField()
    monto = forms.IntegerField()
    tipo_pago = forms.CharField(max_length=100)
