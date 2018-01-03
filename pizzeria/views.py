from django.shortcuts import render
from .models import Pizza


def index(request):
    """pizzeria的主页"""
    return render(request, 'pizzeria/index.html')


def pizzas(request):
    """显示所有的比萨"""
    pizzas = Pizza.objects.order_by()
    context = {'pizzas': pizzas}
    return render(request, 'pizzeria/pizzas.html', context)


def pizza(request, pizza_id):
    """显示单个比萨"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzeria/pizza.html', context)
