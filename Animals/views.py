from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal
from .forms import AnimalForm
from django.contrib.auth.decorators import login_required

@login_required

def animal_list(request):
    animals = Animal.objects.all()

    return render(
        request,
        "Animals/list.html",
        {"animals": animals}
    )


def animal_create(request):

    form = AnimalForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("animal_list")

    return render(request,"Animals/create.html",{"form": form})
from django.shortcuts import get_object_or_404

def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    form = AnimalForm(request.POST or None,instance=animal)

    if form.is_valid():
        form.save()
        return redirect("animal_list")

    return render(request,"Animals/update.html",{"form": form})


def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    if request.method == "POST":
        animal.delete()
        return redirect("animal_list")

    return render(request,"Animals/delete.html",{"animal": animal})

def animal_list(request):

    query = request.GET.get("q")

    animals = Animal.objects.all()

    if query:
        animals = animals.filter(tag_id=query)

    return render(request,"Animals/list.html",{"animals": animals})