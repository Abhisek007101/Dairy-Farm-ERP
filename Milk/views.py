from django.shortcuts import render, redirect, get_object_or_404

from .models import Milk
from .forms import MilkForm
from django.contrib.auth.decorators import login_required

@login_required

def milk_list(request):

    records = Milk.objects.all()

    return render(
        request,
        "milk/list.html",
        {"records": records}
    )


def milk_create(request):

    form = MilkForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("milk_list")

    return render(
        request,
        "milk/create.html",
        {"form": form}
    )


def milk_update(request, pk):

    milk = get_object_or_404(Milk, pk=pk)

    form = MilkForm(
        request.POST or None,
        instance=milk
    )

    if form.is_valid():
        form.save()
        return redirect("milk_list")

    return render(
        request,
        "milk/update.html",
        {"form": form}
    )


def milk_delete(request, pk):

    milk = get_object_or_404(Milk, pk=pk)

    if request.method == "POST":
        milk.delete()
        return redirect("milk_list")

    return render(
        request,
        "milk/delete.html",
        {"milk": milk}
    )
