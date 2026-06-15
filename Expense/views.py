from django.shortcuts import render, redirect, get_object_or_404

from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required

def expense_list(request):

    expenses = Expense.objects.all()

    return render(
        request,
        "Expense/list.html",
        {"expenses": expenses}
    )


def expense_create(request):

    form = ExpenseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("expense_list")

    return render(
        request,
        "Expense/create.html",
        {"form": form}
    )


def expense_update(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk
    )

    form = ExpenseForm(
        request.POST or None,
        instance=expense
    )

    if form.is_valid():
        form.save()
        return redirect("expense_list")

    return render(
        request,
        "Expense/update.html",
        {"form": form}
    )


def expense_delete(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk
    )

    if request.method == "POST":
        expense.delete()
        return redirect("expense_list")

    return render(
        request,
        "Expense/delete.html",
        {"expense": expense}
    )