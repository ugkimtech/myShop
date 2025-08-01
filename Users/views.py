from django.shortcuts import render, redirect
from decimal import Decimal
from .models import *
from django.http import HttpResponse
from Users.logic.stock import StockManager
from Users.logic.sales import SalesManager
from Users.logic.expenditure import ExpenditureManager


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Users.objects.create(username=username, email=email, password=password)
        print('\n\nuser created =>', username, email, password,'\n\n')
        return redirect('users:home')
    return render(request, 'create_user.html')


def get_users(request):
    users = Users.objects.all()
    for user in users:
        print('\n',user.username, user.email, user.password,'\n')
    return HttpResponse(users)


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = Users.objects.filter(username = uname).first()
        if user != None:
            if user.password == password:
                print('\n\n user ==> ',user.username, user.password)
                return redirect('users:home')
            return render(request, 'login.html',{'msg':'Invalid credentials'})
        return render(request, 'login.html',{'msg':'Invalid credentials'})
    return render(request, 'login.html')


def dashboard(request):
    status = Status.objects.get(id = 1)
    items = ItemList.objects.all()
    sales = Sales.objects.all()
    stock = AvailableStock.objects.all()
    hist = StockHistory.objects.all()
    exp = Expenditure.objects.all()
    data = {
        'status':status,
        'items':items,
        'sales':sales,
        'stock':stock,
        'history': hist,
        'expenditures':exp,
    }
    for item in items:
        print('\n', item.item)
    
    return render(request, 'dashboard.html',data)


def add_item(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        add_item = StockManager()
        try:
            add_item.register_item(item)
        except Exception as e:
            return HttpResponse(e)
        return redirect('users:home')
    return redirect('users:home')


def add_stock(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        qty = float(request.POST.get('qty'))
        total_buying_price = Decimal(request.POST.get('total_buying_price'))
        selling_price_each = Decimal(request.POST.get('selling_price_each'))
        source = request.POST.get('source')

        stock = StockManager()
        stock.new_stock(item, qty, total_buying_price, selling_price_each, source)
        return redirect('users:home')
    return redirect('users:home')


def add_sale(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        quantity = float(request.POST.get('quantity'))

        sales = SalesManager()
        sales.add_sale(item, quantity)
        return redirect('users:home')
    return redirect('users:home')


def expenditure(request):
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        reason = request.POST.get('reason')

        exp = ExpenditureManager()
        exp.expend(amount, reason)
        return redirect('users:home')
    return redirect('users:home')


def view_status(request):
    status = Status.objects.filter(id=1).first()
    return render(request, 'status.html', {'status':status})

def init_status(request):
        Status.objects.create(available_cash=0, stock_amount=0, weight=0, profits=0, development=0)
        st = Status.objects.filter(id=1)
        #st = Status.objects.all()
        for s in st:
            print(s.development)
            return HttpResponse(s.development)
        return HttpResponse(st)