from django.urls import path
from . import views
from .views import DashBoardView, UpdatedView


app_name = "web"

urlpatterns = [
    path("", DashBoardView.as_view(), name="crud-dashboard"),
    path("pago/", views.pago_list, name="pago-list"),
    path("form", views.post_pago, name="formulario"),
    path("updated", UpdatedView.as_view(), name="updated"),
    path("pago/details/<int:pk>/", views.pago_detail, name="pago-detail"),
    path("pago/update/<int:pk>/", views.pago_update, name="pago-update"),
    path("pago/delete/<int:pk>", views.pago_delete, name="pago-delete"),
]
