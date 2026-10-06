
from django.urls import path, re_path
from . import views

# urlpatterns = [
# path('home/',views.home)
#]
urlpatterns = [
    path('my-view/', views.my_view, name='my_view'),
    path('home/', views.home),
    path('items/', views.items),
    path('items-list/', views.itemsList),
    path('marks/<int:mark>/', views.marks),
    re_path(r'user/(?P<username>[\w.@+-]+)/?$', views.user_profile),
    re_path(r'products/(?P<productId>[\d]{5})/?$', views.Products),
    path('about/', views.about),
    path('menu/', views.menu),
    path('menu1/', views.menu1),
    path('', views.base),
    path('baseAbout/', views.baseAbout),

    # restaurant app
    path('restaurantMenu/', views.restaurantMenu, name='restaurant_menu'),
    path('restaurantAbout/', views.restaurantAbout, name='restaurant_about'),
    path('restaurantHome/', views.restaurantHome, name='restaurant_home'),
    path('simpleForm/',views.simpleForm),
    path('templateForm/', views.templateForm, name='template_form'),
    path('formValidation/', views.formValidation, name='form_validation'),
]