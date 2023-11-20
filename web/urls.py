from django.urls import path
from . import views
from .views import DashBoardView, UpdatedView, UserUpdatedView, RolUpdatedView


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
]
