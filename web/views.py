from django.shortcuts import render, redirect
from .forms import PagoForm
from django.http import HttpResponseServerError
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

# Create your views here.


class DashBoardView(TemplateView):
    template_name = "web/dashboard.html"


class UpdatedView(TemplateView):
    template_name = "web/updated.html"


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

    # Check if the API request was successful (status code 2xx)
    if response.status_code // 100 == 2:
        pago_from_api = response.json()
        print(f"pago from api: {pago_from_api}")

        return render(request, "web/pago_detail.html", {"obj": pago_from_api})
    else:
        # Handle the case where the API request was not successful
        # You might want to raise an exception, log an error, or handle it accordingly
        return HttpResponseServerError("API request failed")


def pago_update(request, pk):
    # Make a request to the API to get details for the specific Pago
    api_url = f"http://54.147.37.217:8001/administracion/gestion-pagos/lista/{pk}"
    response = requests.get(api_url)

    # Check if the API request was successful (status code 2xx)
    if response.status_code // 100 == 2:
        pago_from_api = response.json()
        print(f"pago from api: {pago_from_api}")

        # You can create a form with initial data from the API response
        form = PagoForm(initial=pago_from_api)

        if request.method == "POST":
            # If it's a POST request, update the data
            form = PagoForm(request.POST)
            if form.is_valid():
                # Extract the updated data from the form
                updated_data = {
                    "medico_id": form.cleaned_data["medico_id"],
                    "monto": form.cleaned_data["monto"],
                    "tipo_pago": form.cleaned_data["tipo_pago"],
                }

                # Define the headers for the API request
                headers = {
                    "Content-type": "application/json",
                }

                # Make a request to the API to update the data
                update_url = f"http://54.147.37.217:8001/administracion/gestion-pagos/modifica/{pk}"
                update_response = requests.put(
                    update_url, data=json.dumps(updated_data), headers=headers
                )

                # Check if the update was successful
            if update_response.status_code // 100 == 2:
                return redirect(
                    "web:updated"
                )  # Use the correct name of the URL pattern
            else:
                return HttpResponseServerError("API update request failed")

        # If it's a GET request or the form is not valid, render the update form
        return render(
            request, "web/pago_update.html", {"form": form, "obj": pago_from_api}
        )
    else:
        # Handle the case where the API request was not successful
        # You might want to raise an exception, log an error, or handle it accordingly
        return HttpResponseServerError("API request failed")


def pago_delete(request, pk):
    # Make a request to the API to delete the specific Pago
    delete_url = f"http://54.147.37.217:8001/administracion/gestion-pagos/elimina/{pk}"
    delete_response = requests.delete(delete_url)

    # Check if the delete request was successful (status code 2xx)
    if delete_response.status_code // 100 == 2:
        return redirect(
            "web:pago-list"
        )  # Redirect to the list view after successful deletion
    else:
        # Handle the case where the API request was not successful
        # You might want to raise an exception, log an error, or handle it accordingly
        return HttpResponseServerError("API delete request failed")
