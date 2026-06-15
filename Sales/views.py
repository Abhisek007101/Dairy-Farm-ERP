from django.shortcuts import render, redirect, get_object_or_404

from .models import Sale
from .forms import SaleForm
from django.contrib.auth.decorators import login_required

@login_required

def sale_list(request):

    sales = Sale.objects.all()

    return render(
        request,
        "Sales/list.html",
        {"sales": sales}
    )


def sale_create(request):

    form = SaleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("sale_list")

    return render(
        request,
        "Sales/create.html",
        {"form": form}
    )


def sale_update(request, pk):

    sale = get_object_or_404(Sale, pk=pk)

    form = SaleForm(
        request.POST or None,
        instance=sale
    )

    if form.is_valid():
        form.save()
        return redirect("sale_list")

    return render(
        request,
        "Sales/update.html",
        {"form": form}
    )


def sale_delete(request, pk):

    sale = get_object_or_404(Sale, pk=pk)

    if request.method == "POST":
        sale.delete()
        return redirect("sale_list")

    return render(
        request,
        "Sales/delete.html",
        {"sale": sale}
    )