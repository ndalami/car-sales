from django.shortcuts import render,redirect
from . models import Car
from .forms import MessageForm

# Create your views here.
def index(request):
    car = Car.objects.all().order_by('-id')[:6]

    if request.method == 'POST':
        if request.method == 'POST':
           form = MessageForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('cars:index')
    else:
        form = MessageForm()
    context = {'car':car, 'form':form}
    return render(request,'cars/index.html',context)

def all_cars(request):
    car = Car.objects.all().order_by('-id')

    if request.method == 'POST':
        if request.method == 'POST':
           form = MessageForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('cars:index')
    else:
        form = MessageForm()

    context = {'car':car,'form':form}
    return render(request,'cars/all_cars.html',context)


def car_detail(request,car_id):
    singleCar = Car.objects.get(pk=car_id)
    context ={'singleCar':singleCar}
    return render(request,'cars/car_detail.html',context)

def search_car(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cars = Car.objects.filter(carName__contains = searched)
        context ={'searched':searched, 'cars':cars}
        return render(request,'cars/search_car.html',context)
    else:
        return render(request,'cars/all_cars.html')
    
def base(request):
    if request.method == 'POST':
        if request.method == 'POST':
           form = MessageForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('cars:base')
    
    else:
        form = MessageForm()
    return render(request, 'cars/base.html',{'form':form})
    
