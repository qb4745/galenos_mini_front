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


class PacienteForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=20)
    nombres = forms.CharField(max_length=255)
    apellidos = forms.CharField(max_length=255)
    prevision_type = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=200)
    comuna = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()


class ReservaForm(forms.Form):
    id_paciente = forms.IntegerField()
    id_medico = forms.IntegerField()
    fecha = forms.DateField()
    hora_inicio = forms.TimeField()
    hora_termino = forms.TimeField()


class CorreoForm(forms.Form):
    date = forms.DateField()
