from django.shortcuts import render, redirect
from datetime import date
from .forms import PagoForm, UserForm, RolForm, PacienteForm
from django.http import HttpResponseServerError, HttpResponseBadRequest
import requests
import json
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

import logging

logger = logging.getLogger(__name__)

# Create your views here.


class DashBoardView(TemplateView):
    template_name = "web/dashboard.html"


class UpdatedView(TemplateView):
    template_name = "web/updated.html"


class UserUpdatedView(TemplateView):
    template_name = "web/user_updated.html"


class RolUpdatedView(TemplateView):
    template_name = "web/rol_updated.html"


class PacienteUpdatedView(TemplateView):
    template_name = "web/paciente_updated.html"


def pago_list(request):
    response = requests.get(
        "http://54.147.37.217:8001/administracion/gestion-pagos/lista"
    ).json()
    return render(request, "web/pago_list.html", {"response": response})


def post_pago(request):
    url = "http://54.147.37.217:8001/administracion/gestion-pagos/crea"
    form = PagoForm(request.POST or None)
    if form.is_valid():
        medico_id = form.cleaned_data.get("medico_id")
        monto = form.cleaned_data.get("monto")
        tipo_pago = form.cleaned_data.get("tipo_pago")
        data = {"medico_id": medico_id, "monto": monto, "tipo_pago": tipo_pago}
        headers = {
            "Content-type": "application/json",
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return render(request, "web/form.html", {"response": response})


def pago_detail(request, pk):
    # Make a request to the API to get details for the specific Pago
    api_url = f"http://54.147.37.217:8001/administracion/gestion-pagos/lista/{pk}"
    response = requests.get(api_url)

    if response.status_code // 100 == 2:
        pago_from_api = response.json()
        print(f"pago from api: {pago_from_api}")

        return render(request, "web/pago_detail.html", {"obj": pago_from_api})
    else:
        return HttpResponseServerError("API request failed")


def pago_update(request, pk):
    api_url = f"http://54.147.37.217:8001/administracion/gestion-pagos/lista/{pk}"
    response = requests.get(api_url)

    if response.status_code // 100 == 2:
        pago_from_api = response.json()
        print(f"pago from api: {pago_from_api}")

        form = PagoForm(initial=pago_from_api)

        if request.method == "POST":
            form = PagoForm(request.POST)
            if form.is_valid():
                updated_data = {
                    "medico_id": form.cleaned_data["medico_id"],
                    "monto": form.cleaned_data["monto"],
                    "tipo_pago": form.cleaned_data["tipo_pago"],
                }

                headers = {
                    "Content-type": "application/json",
                }

                update_url = f"http://54.147.37.217:8001/administracion/gestion-pagos/modifica/{pk}"
                update_response = requests.put(
                    update_url, data=json.dumps(updated_data), headers=headers
                )

                # Check if the update was successful
            if update_response.status_code // 100 == 2:
                return redirect("web:updated")
            else:
                return HttpResponseServerError("API update request failed")

        return render(
            request, "web/pago_update.html", {"form": form, "obj": pago_from_api}
        )
    else:
        return HttpResponseServerError("API request failed")


def pago_delete(request, pk):
    delete_url = f"http://54.147.37.217:8001/administracion/gestion-pagos/elimina/{pk}"
    delete_response = requests.delete(delete_url)

    if delete_response.status_code // 100 == 2:
        return redirect("web:pago-list")
    else:
        return HttpResponseServerError("API delete request failed")


def user_list(request):
    response = requests.get(
        "http://54.147.37.217:8000/administracion/usuarios/gestion/lista/"
    ).json()
    return render(request, "web/user_list.html", {"response": response})


def post_user(request):
    url = "http://54.147.37.217:8000/administracion/usuarios/gestion/crea/"
    form = UserForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        data = {"username": username, "email": email, "password": password}
        headers = {"Content-type": "application/json"}

        response = requests.post(url, data=json.dumps(data), headers=headers)
        print(f"respuesta status: {response.status_code}")
        if response.status_code // 100 == 2:
            # Successful API request, render the template with the response
            return render(request, "web/form.html", {"response": response})
        else:
            # API request was not successful, handle the error accordingly
            return HttpResponseServerError("API request failed")
    else:
        # Form is not valid, handle the error or return an appropriate response
        return HttpResponseBadRequest("Invalid form data")


def user_detail(request, pk):
    # Make a request to the API to get details for the specific Pago
    api_url = f"http://54.147.37.217:8000/administracion/usuarios/gestion/lista/{pk}"
    response = requests.get(api_url)

    if response.status_code // 100 == 2:
        user_from_api = response.json()
        print(f"user from api: {user_from_api}")

        return render(request, "web/user_detail.html", {"obj": user_from_api})
    else:
        return HttpResponseServerError("API request failed")


def user_update(request, pk):
    api_url = f"http://54.147.37.217:8000/administracion/usuarios/gestion/lista/{pk}/"
    response = requests.get(api_url)

    if response.status_code // 100 == 2:
        user_from_api = response.json()
        print(f"pago from api: {user_from_api}")

        form = UserForm(initial=user_from_api)

        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                updated_data = {
                    "username": form.cleaned_data["username"],
                    "email": form.cleaned_data["email"],
                    "password": form.cleaned_data["password"],
                }

                headers = {
                    "Content-type": "application/json",
                }

                update_url = f"http://54.147.37.217:8000/administracion/usuarios/gestion/modifica/{pk}/"
                print(f"1 update url : {update_url}")
                print(f"2 updated data : {json.dumps(updated_data)}")
                print(f"3 headers : {headers}")
                update_response = requests.put(
                    update_url, data=json.dumps(updated_data), headers=headers
                )

                # Check if the update was successful
                print(f"4 update response : {update_response}")
                if update_response.status_code // 100 == 2:
                    return redirect("web:user-updated")

                else:
                    return HttpResponseServerError("API update request failed")
        return render(
            request, "web/user_update.html", {"form": form, "obj": user_from_api}
        )
    else:
        return HttpResponseServerError("API request failed")


def user_delete(request, pk):
    delete_url = (
        f"http://54.147.37.217:8000/administracion/usuarios/gestion/elimina/{pk}"
    )
    delete_response = requests.delete(delete_url)

    if delete_response.status_code // 100 == 2:
        return redirect("web:user-list")
    else:
        return HttpResponseServerError("API delete request failed")


def rol_list(request):
    response = requests.get(
        "http://54.147.37.217:8000/administracion/usuarios/gestion/roles/lista/"
    ).json()
    return render(request, "web/rol_list.html", {"response": response})


def post_rol(request):
    url = "http://54.147.37.217:8000/administracion/usuarios/gestion/roles/"
    form = RolForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        data = {"name": name}
        headers = {"Content-type": "application/json"}

        response = requests.post(url, data=json.dumps(data), headers=headers)
        print(f"respuesta status: {response.status_code}")
        if response.status_code // 100 == 2:
            # Successful API request, render the template with the response
            return render(request, "web/form_rol.html", {"response": response})
        else:
            # API request was not successful, handle the error accordingly
            return HttpResponseServerError("API request failed")
    else:
        # Form is not valid, handle the error or return an appropriate response
        return HttpResponseBadRequest("Invalid form data")


def rol_detail(request, pk):
    # Make a request to the API to get details for the specific Pago
    api_url = (
        f"http://54.147.37.217:8000/administracion/usuarios/gestion/roles/lista/{pk}"
    )
    response = requests.get(api_url)

    if response.status_code // 100 == 2:
        rol_from_api = response.json()
        print(f"user from api: {rol_from_api}")

        return render(request, "web/rol_detail.html", {"obj": rol_from_api})
    else:
        return HttpResponseServerError("API request failed")


def rol_update(request, pk):
    api_url = (
        f"http://54.147.37.217:8000/administracion/usuarios/gestion/roles/lista/{pk}/"
    )
    response = requests.get(api_url)

    if response.status_code // 100 == 2:
        rol_from_api = response.json()
        print(f"rol from api: {rol_from_api}")

        form = RolForm(initial=rol_from_api)

        if request.method == "POST":
            form = RolForm(request.POST)
            if form.is_valid():
                updated_data = {
                    "name": form.cleaned_data["name"],
                }

                headers = {
                    "Content-type": "application/json",
                }

                update_url = f"http://54.147.37.217:8000/administracion/usuarios/gestion/roles/modifica/{pk}/"
                update_response = requests.put(
                    update_url, data=json.dumps(updated_data), headers=headers
                )

                # Check if the update was successful
            if update_response.status_code // 100 == 2:
                return redirect("web:rol-updated")
            else:
                return HttpResponseServerError("API update request failed")

        return render(
            request, "web/rol_update.html", {"form": form, "obj": rol_from_api}
        )
    else:
        return HttpResponseServerError("API request failed")


def rol_delete(request, pk):
    delete_url = (
        f"http://54.147.37.217:8000/administracion/usuarios/gestion/roles/elimina/{pk}/"
    )
    delete_response = requests.delete(delete_url)

    if delete_response.status_code // 100 == 2:
        return redirect("web:rol-list")
    else:
        return HttpResponseServerError("API delete request failed")


# pacientes
def paciente_list(request):
    response = requests.get(
        "http://44.221.17.219:8000/galenos/web/pacientes/lista"
    ).json()
    return render(request, "web/paciente_list.html", {"response": response})


def post_paciente(request):
    url = "http://44.221.17.219:8000/galenos/web/pacientes/crea"
    form = PacienteForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        rut = form.cleaned_data.get("rut")
        nombres = form.cleaned_data.get("nombres")
        apellidos = form.cleaned_data.get("apellidos")
        prevision_type = form.cleaned_data.get("prevision_type")
        telefono = form.cleaned_data.get("telefono")
        direccion = form.cleaned_data.get("direccion")
        comuna = form.cleaned_data.get("comuna")
        fecha_nacimiento = form.cleaned_data.get("fecha_nacimiento")

        # Convert date to string
        fecha_nacimiento_str = fecha_nacimiento.strftime("%Y-%m-%d")

        data = {
            "email": email,
            "username": email,
            "password": password,
            "rut": rut,
            "nombres": nombres,
            "apellidos": apellidos,
            "prevision_type": prevision_type,
            "telefono": telefono,
            "direccion": direccion,
            "comuna": comuna,
            "fecha_nacimiento": fecha_nacimiento_str,
        }
        headers = {"Content-type": "application/json"}
        print(f"1 data : {data}")

        response = requests.post(url, data=json.dumps(data), headers=headers)
        print(f"respuesta status: {response.status_code}")

        if response.status_code // 100 == 2:
            # Successful API request, render the template with the response
            return render(
                request, "web/form_paciente_post.html", {"response": response}
            )
        else:
            # API request was not successful, handle the error accordingly
            return HttpResponseServerError("API request failed")
    else:
        # Form is not valid, handle the error or return an appropriate response
        return HttpResponseBadRequest("Invalid form data")


def paciente_detail(request, pk):
    # Make a request to the API to get details for the specific Pago
    api_url = f"http://44.221.17.219:8000/galenos/web/pacientes/lista/{pk}"
    response = requests.get(api_url)

    if response.status_code // 100 == 2:
        paciente_from_api = response.json()
        print(f"user from api: {paciente_from_api}")

        return render(request, "web/paciente_detail.html", {"obj": paciente_from_api})
    else:
        return HttpResponseServerError("API request failed")


def paciente_update(request, pk):
    api_url = f"http://44.221.17.219:8000/galenos/web/pacientes/lista/{pk}"
    response = requests.get(api_url)

    if response.status_code // 100 == 2:
        paciente_from_api = response.json()
        print(f"paciente_from_api: {paciente_from_api}")

        form = PacienteForm(initial=paciente_from_api)

        if request.method == "POST":
            form = PacienteForm(request.POST)

            if form.is_valid():
                fecha_nacimiento_str = form.cleaned_data["fecha_nacimiento"].strftime(
                    "%Y-%m-%d"
                )

                updated_data = {
                    "email": form.cleaned_data["email"],
                    "username": form.cleaned_data["email"],
                    "password": form.cleaned_data["password"],
                    "rut": form.cleaned_data["rut"],
                    "nombres": form.cleaned_data["nombres"],
                    "apellidos": form.cleaned_data["apellidos"],
                    "prevision_type": form.cleaned_data["prevision_type"],
                    "telefono": form.cleaned_data["telefono"],
                    "direccion": form.cleaned_data["direccion"],
                    "comuna": form.cleaned_data["comuna"],
                    "fecha_nacimiento": fecha_nacimiento_str,
                }

                headers = {
                    "Content-type": "application/json",
                }

                update_url = (
                    f"http://44.221.17.219:8000/galenos/web/pacientes/modifica/{pk}"
                )
                print(f"1 update url : {update_url}")
                print(f"2 updated data : {json.dumps(updated_data)}")
                print(f"3 headers : {headers}")
                update_response = requests.put(
                    update_url, data=json.dumps(updated_data), headers=headers
                )

                # Check if the update was successful
                print(f"4 update response : {update_response}")
                if update_response.status_code // 100 == 2:
                    return redirect("web:paciente-updated")

                else:
                    return HttpResponseServerError("API update request failed")
        return render(
            request,
            "web/paciente_update.html",
            {"form": form, "obj": paciente_from_api},
        )
    else:
        return HttpResponseServerError("API request failed")


def paciente_delete(request, pk):
    delete_url = f"http://44.221.17.219:8000/galenos/web/pacientes/elimina/{pk}"
    delete_response = requests.delete(delete_url)

    if delete_response.status_code // 100 == 2:
        return redirect("web:paciente-list")
    else:
        return HttpResponseServerError("API delete request failed")
