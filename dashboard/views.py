from django.shortcuts import render
from django.db.models import Sum
from Animals.models import Animal
from Milk.models import Milk
from Sales.models import Sale
from Expense.models import Expense
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.timezone import now
from datetime import timedelta
from django.http import HttpResponse
from .utils import generate_pdf


def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required


def dashboard(request):

    # ===== TOTALS =====
    total_animals = Animal.objects.count()

    total_milk = Milk.objects.aggregate(
        total=Sum('total_qty')
    )['total'] or 0

    total_revenue = Sale.objects.aggregate(
        total=Sum('total_revenue')
    )['total'] or 0

    total_expense = Expense.objects.aggregate(
        total=Sum('amount')
    )['total'] or 0

    profit = total_revenue - total_expense

    # ===== RECENT DATA =====
    recent_milk = Milk.objects.all().order_by('-date')[:5]
    recent_sales = Sale.objects.all().order_by('-date')[:5]

    # ===== MONTHLY ANALYTICS =====
    months = []
    milk_data = []
    sales_data = []
    expense_data = []

    for i in range(5, -1, -1):
        month_date = now() - timedelta(days=30*i)

        months.append(month_date.strftime("%b"))

        milk_data.append(
            Milk.objects.filter(date__month=month_date.month,date__year=month_date.year)
            .aggregate(total=Sum('total_qty'))['total'] or 0
        )

        sales_data.append(
            Sale.objects.filter(date__month=month_date.month,date__year=month_date.year)
            .aggregate(total=Sum('total_revenue'))['total'] or 0
        )

        expense_data.append(
            Expense.objects.filter(date__month=month_date.month,date__year=month_date.year)
            .aggregate(total=Sum('amount'))['total'] or 0
        )

    context = {
        "total_animals": total_animals,
        "total_milk": total_milk,
        "total_revenue": total_revenue,
        "total_expense": total_expense,
        "profit": profit,

        "recent_milk": recent_milk,
        "recent_sales": recent_sales,

        "months": months,
        "milk_data": milk_data,
        "sales_data": sales_data,
        "expense_data": expense_data,
    }

    return render(request, "dashboard/dashboard.html", context)
@login_required
def download_report(request):

    context = {
        "total_animals": Animal.objects.count(),
        "total_milk": Milk.objects.aggregate(total=Sum('total_qty'))['total'] or 0,
        "total_revenue": Sale.objects.aggregate(total=Sum('total_revenue'))['total'] or 0,
        "total_expense": Expense.objects.aggregate(total=Sum('amount'))['total'] or 0,
    }

    context["profit"] = context["total_revenue"] - context["total_expense"]

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dairy_report.pdf"'

    generate_pdf(response, context)

    return response