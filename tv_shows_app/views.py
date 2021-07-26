from django.shortcuts import render, HttpResponse, redirect
from .models import Show

def index(request):
    return redirect("/shows")

def new(request):
    return render(request, 'new.html')

def create(request):
    título = request.POST['título']
    canal = request.POST['canal']
    fecha = request.POST['fecha']
    desc = request.POST['desc']
    Show.objects.create(title = título, network=canal, release_date=fecha, desc=desc)
    Show.objects.last().id
    return redirect('/shows/' + str(Show.objects.last().id))

def mostrar(request, id):
    context = {'show': Show.objects.get(id=id),}
    return render(request, "show.html", context)

def shows(request):
    context = {'shows': Show.objects.all()}
    return render(request, "shows.html", context)

def editar(request, id):
    context = {'show': Show.objects.get(id=id),}
    return render(request, "edit.html", context)

def update(request, id):
    show_id = id
    showcito = Show.objects.get(id=int(show_id))
    showcito.title = request.POST['título']
    showcito.network = request.POST['canal']
    showcito.release_date = request.POST['fecha']
    showcito.desc = request.POST['desc']
    librito.save()
    return redirect('/shows/' + str(show_id))

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')
