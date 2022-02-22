from django.shortcuts import render
from accounts.models import *
# Create your views here.
from django.http import HttpResponse


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    order_delivered = orders.filter(status='Delivered').count()
    order_pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders,
               'order_delivered': order_delivered, 'order_pending': order_pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, customer_pk):
    customer = Customer.objects.get(id=customer_pk)
    orders = customer.order_set.all()
    total_order = orders.count()
    context = {'customer': customer, 'orders': orders, 'total_order': total_order}
    return render(request, 'accounts/customer.html', context)
