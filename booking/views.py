from django.shortcuts import render, redirect, get_object_or_404
from .models import Table
from .forms import ReservationsForm

def hall(request):
    tables = Table.objects.all()

    return render(request, "hall.html", {
        "tables" : tables
    })

def reserve(request, table_id):

    table = get_object_or_404(Table, id=table_id)

    if request.method == "POST":

        form = ReservationsForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.table = table

            reservation.save()

            return redirect("hall")
        
    else:
        form = ReservationsForm()
    
    return render(request, "reserve.html", {
        "form" : form 
    })