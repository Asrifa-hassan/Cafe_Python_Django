from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')

def user_home(request):
    return render(request, 'user_home.html')

def about(request):
    return render(request, 'about.html')


def coffees(request):
    data = Food_items.objects.all()
    return render(request, 'coffees.html',locals())


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def login_page(request):
    return render(request, 'login.html')


def Read_more(request):
    return render(request, 'Read_more.html')


def cofe_read(request):
    return render(request,'cofe_read.html')

def bean_read(request):
    return render(request,'bean_read.html')


def pastry_read(request):
    return render(request,'pastry_read.html')

def caffe(request):
    return render(request,'caffe.html')

def blog_read(request):
    return render(request,'blog_read.html')


def blog_read2(request):
    return render(request,'blog_read2.html')


def Registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            User.objects.get(username=email)
            return render(request, 'login.html')
        except User.DoesNotExist:
            user = User.objects.create(
                name=name,
                email=email,
                username=email,
                phone_number=phone_number,
                is_superuser=0,
                is_staff=0,
                user_type=3
            )
            user.set_password(password)
            user.save()
            return redirect(user_home)
    else:
        return render(request, 'login.html')


def login_function(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_staff == 1:
                if user.is_superuser == 1:
                    #admin
                    login(request, user)
                    return redirect(Dashboard)
                else:
                    #staff
                    pass
            else:
                #user
                login(request, user)
                return redirect(user_home)
        else:
            return render(request, 'login.html')


def logout_function(request):
    logout(request)
    return redirect(index)


#------------- admin module ----------------------------

def Dashboard(request):
    food_count = Food_items.objects.all().count()

    return render(request,'dashboard.html',locals())

def admin_products(request):
    try:
        data = Food_items.objects.all()
        return render(request, 'admin_products.html', locals())
    except:
        text = "No data found"
        return render(request, 'admin_products.html', locals())

def admin_view_product(request,id):
    try:
        data = Food_items.objects.filter(id=id)
        return render(request,'admin_view_product.html', locals())
    except:
        text = "No data found"
        return render(request, 'admin_products.html', {'text': text })


def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_id = request.POST.get('item_id')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        try:
            Food_items.objects.get(item_id=item_id)
            messages.add_message(request, messages.WARNING,"Item already exist.")
            data = Food_items.objects.all()
            return render(request, 'admin_products.html', locals())
        except:
            data = Food_items.objects.create(item_name=item_name,
                                             item_id=item_id,
                                             description=description,
                                             price=price,
                                             image=image
                                             )

            data.save()
            msg = "New Item Added Successfully,Itemcode : {}".format(item_id)
            messages.add_message(request, messages.SUCCESS, msg)
            data = Food_items.objects.all()
            return render(request, 'admin_products.html', locals())


    else:
        return render(request, 'add_item.html')
    
def edit_item(request, id):
    if request.method == "POST":
        item_name = request.POST.get('item_name')
        item_id = request.POST.get('item_id')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('Image')
        Food_items.objects.filter(id=id).update(item_name=item_name,
                                                item_id=item_id,
                                                description=description,
                                                price=price
                                                )
        instance = get_object_or_404(Food_items, id=id)
        if image:
            instance.image = image
        instance.save()
        return redirect(admin_view_product, id)
    else:
        data = Food_items.objects.filter(id=id)
        return render(request, 'edit_item.html', locals())

def delete_item(request,id):
    Food_items.objects.filter(id=id).delete()
    msg = "Item Deleted Successfully"
    messages.add_message(request, messages.SUCCESS, msg)
    data = Food_items.objects.all()
    return render(request, 'admin_products.html', locals())

def admin_orders(request):
    return render(request, 'admin_orders.html')

def cart_item(request):
    return render(request, 'cart_item.html')

def order_item(request):
    return render(request, 'order_item.html')

def admin_users(request):
    return render(request, 'admin_users.html')

def admin_view_user(request):
    return render(request, 'admin_view_user.html')
