from django.urls import path
from . import views
from .views import (
    DashBoardView,
    UpdatedView,
    UserUpdatedView,
    RolUpdatedView,
    PacienteUpdatedView,
    ReservaCreateView,
    ReservaUpdatedView,
    CorreoCreateView,
)


app_name = "web"

urlpatterns = [
    path("", DashBoardView.as_view(), name="crud-dashboard"),
    path("form", views.post_pago, name="formulario"),
    path("form_user", views.post_user, name="formulario-user"),
    path("form_rol", views.post_rol, name="formulario-rol"),
    path("updated", UpdatedView.as_view(), name="updated"),
    path("pago/", views.pago_list, name="pago-list"),
    path("pago/details/<int:pk>/", views.pago_detail, name="pago-detail"),
    path("pago/update/<int:pk>/", views.pago_update, name="pago-update"),
    path("pago/delete/<int:pk>", views.pago_delete, name="pago-delete"),
    path("user/", views.user_list, name="user-list"),
    path("user/details/<int:pk>/", views.user_detail, name="user-detail"),
    path("user/update/<int:pk>/", views.user_update, name="user-update"),
    path("user_updated", UserUpdatedView.as_view(), name="user-updated"),
    path("user/delete/<int:pk>", views.user_delete, name="user-delete"),
    path("rol/", views.rol_list, name="rol-list"),
    path("rol/details/<int:pk>/", views.rol_detail, name="rol-detail"),
    path("rol/update/<int:pk>/", views.rol_update, name="rol-update"),
    path("rol_updated", RolUpdatedView.as_view(), name="rol-updated"),
    path("rol/delete/<int:pk>", views.rol_delete, name="rol-delete"),
    path("paciente/", views.paciente_list, name="paciente-list"),
    path("form_paciente_post", views.post_paciente, name="formulario-paciente-post"),
    path("paciente/details/<int:pk>/", views.paciente_detail, name="paciente-detail"),
    path("paciente/update/<int:pk>/", views.paciente_update, name="paciente-update"),
    path("paciente_updated", PacienteUpdatedView.as_view(), name="paciente-updated"),
    path("paciente/delete/<int:pk>", views.paciente_delete, name="paciente-delete"),
    path("reserva/", views.reserva_list, name="reserva-list"),
    path("reserva/crear/", ReservaCreateView.as_view(), name="reserva-create"),
    path("form_reserva_post", views.post_reserva, name="formulario-reserva-post"),
    path("reserva/details/<int:pk>/", views.reserva_detail, name="reserva-detail"),
    path("reserva/update/<int:pk>/", views.reserva_update, name="reserva-update"),
    path("reserva_updated", ReservaUpdatedView.as_view(), name="reserva-updated"),
    path(
        "reserva_updated/delete/<int:pk>", views.reserva_delete, name="reserva-delete"
    ),
    path("correo/crear/", CorreoCreateView.as_view(), name="correo-create"),
    path("form_correo_post", views.post_correo, name="formulario-correo-post"),
]
