from django.shortcuts import render,redirect
from cars.models import Car,Message
from .forms import CarForm
from cars.forms import MessageForm
from django.core.paginator import Paginator

# Create your views here.
def all_cars(request):
    car = Car.objects.all().order_by('-id')
    context = {'car':car}
    return render(request,'staffpages/all_cars.html',context)

# view to add car to database
def add_cars(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)  # Include request.FILES for file uploads

        if form.is_valid():
           form.save()
           return redirect('staffpages:cars')
    
    else:
        form = CarForm()
    return render(request, 'staffpages/add_cars.html',{'form':form})

# view to update car info
def update_cars(request,car_id):
    car = Car.objects.get(pk = car_id)
    if request.method == 'POST':
       form = CarForm(request.POST, request.FILES, instance=car,)
       if form.is_valid():
          form.save()
          return redirect('staffpages:cars')
       
    else:
        form = CarForm(instance=car)
    context = {'form':form,'instance':car}
    return render(request, 'staffpages/update_cars.html',context)

# view to delete a particular Car
def delete_car(request,car_id):
    car = Car.objects.get(pk=car_id)
    car.delete()
    return redirect('staffpages:cars')

# view to render main dashboard page
def home(request):
    car_count = Car.objects.all().count
    message_count = Message.objects.all().count
    return render(request, 'staffpages/home.html',{'car_count':car_count,'message_count':message_count})

# View to render messages from customers
def messages(request):
    message = Message.objects.all()
    paginator = Paginator(message, 3) 
    page = request.GET.get('page')
    message = paginator.get_page(page)
    context = {'message':message}
    return render(request, 'staffpages/messages.html',context)

def view_message(request,message_id):
    singleMessage = Message.objects.get(pk=message_id)
    form = MessageForm(request.POST or None,instance=singleMessage)
    context ={'singleMessage':singleMessage,'form':form}
    return render(request,'staffpages/view_message.html',context)

# view to delete a particular message
def delete_message(request,message_id):
    message = Message.objects.get(pk=message_id)
    message.delete()
    return redirect('staffpages:messages')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cars = Car.objects.filter(carName__contains = searched)
        context ={'searched':searched, 'cars':cars}
        return render(request,'staffpages/search.html',context)
    else:
        return render(request,'staffpages/all_cars.html')
    

def detail_admin(request,car_id):
    adminCar = Car.objects.get(pk=car_id)
    context ={'adminCar':adminCar}
    return render(request,'staffpages/detail_admin.html',context)