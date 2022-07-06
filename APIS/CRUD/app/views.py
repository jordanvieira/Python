from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros



def home(request):
    data = {}
    data['db']= Carros.objects.all()
    return render(request, 'index.html',data)


def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)


def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(resquest, pk):
    data={}
    data['db'] = Carros.objects.get(pk=pk)
    return render(resquest, 'view.html', data)