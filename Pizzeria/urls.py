"""Defines URL patterns for Pizzeria"""

from django.urls import path 

from . import views 

app_name = 'Pizzeria'
urlpatterns = [
    #Home Page 
    path('', views.index, name='index'),
    #Page that shows all Pizza 
    path('pizzas/', views.pizzas, name='pizzas'),
    #Detail page for a single pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    #Page for adding a new pizza
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    #Page for adding a new topping to each pizza
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping' ),
   
]
#Link each url to a page displaying pizza with corresponding toppings. This is going to be challenging. 