from django.db import models


class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    medico_id = models.IntegerField()
    monto = models.IntegerField()
    tipo_pago = models.CharField(
        max_length=255
    )  # Ajusta la longitud según tus necesidades
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.id} - Medico ID: {self.medico_id}, Monto: {self.monto}, Tipo: {self.tipo_pago}, Fecha: {self.fecha_pago}"
