from django.shortcuts import render, redirect

from .models import Pizza
from .models import Topping
from .forms import PizzaForm, ToppingForm

# Create your views here.
def  index(request):
    """This will be the home page for the Pizzeria"""
    return render(request, 'Pizzeria/index.html')

def pizzas(request):
    """Show all Pizzas on file"""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas':pizzas}
    return render(request, 'Pizzeria/pizzas.html', context)

"""def toppings(request):
    toppings = Toppings.objects.order_by('date_added')
    context = {'toppings':toppings}
    return render(request, 'Pizzeria/toppings.html', context)"""
#I might have to add some toppings to the pizzas so they can show up on the page. This code might be unne

def pizza(request, pizza_id):
    """Show toppings for specific pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request,'Pizzeria/pizza.html', context)

#When defining a new view in the views file we use the name of the URL which is used to access the file NOT the name of the form (new_pizza not PizzaForm).
def new_pizza(request):
    """Adding a new pizza"""
    if request.method != 'POST':
        #No data submitted then create a blank form
        form = PizzaForm()
    else:
        #POST the data submitted and process the data
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pizzeria:pizzas')
    
    #Display a blank or invalid form
    context = {'form':form}
    return render(request, 'Pizzeria/new_pizza.html', context)

def new_topping(request, pizza_id):
    """Adding a new topping"""
    pizza = Pizza.objects.get(id=pizza_id)
    
    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('Pizzeria:pizza', pizza_id=pizza_id)
    
    #Display blank or invalid form 
    context = {'pizza': pizza, 'form':form}
    return render(request, 'Pizzeria/new_topping.html', context)
        