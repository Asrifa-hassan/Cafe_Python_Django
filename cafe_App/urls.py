from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('coffees', views.coffees, name='coffees'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('login_page', views.login_page, name='login_page'),
    path('Read_more', views.Read_more, name='Read_more'),
    path('cofe_read', views.cofe_read, name='cofe_read'),
    path('bean_read', views.bean_read, name='bean_read'),
    path('caffe', views.caffe, name='caffe'),
    path('pastry_read', views.pastry_read, name='pastry_read'),
    path('blog_read', views.blog_read, name='blog_read'),
    path('blog_read2', views.blog_read2, name='blog_read2'),
    path('register', views.Registration, name='register'),
    path('login_function', views.login_function, name='login_function'),
    path('logout', views.logout_function, name='logout'),


    # ------------ user module--------------------------
    path('user_home', views.user_home, name='user_home'),


    #------------- admin module -----------------------
    path('dashboard', views.Dashboard, name='dashboard'),
    path('admin_products', views.admin_products, name='admin_products'),
    path('admin_view_product/<int:id>', views.admin_view_product, name='admin_view_product'),
    path('add_item', views.add_item, name='add_item'),
    path('edit_item/<int:id>', views.edit_item, name='edit_item'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('admin_orders', views.admin_orders, name='admin_orders'),
    path('cart-item', views.cart_item, name='cart_item'),
    path('order_item', views.order_item, name='order_item'),
    path('admin_users', views.admin_users, name='admin_users'),
    path('admin_view_user', views.admin_view_user, name='admin_view_user'),


]