from django.urls import path 
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [ 
    path('index/', views.company, name='company'),
    path('customer/<str:customers>/', views.customer_view, name='customer'),
    path('salesindex/', views.salesindex_view, name='salesindex.html'),
    path('salesindex/', views.salesindex, name='salesindex.html'),
    path('salesindex/sales.html', views.sales, name='sales'),
    path('salesindex/', views.salesindex_view, name='salesindex'),
    path('get-salesperson-data', views.get_salesperson_data, name='get_salesperson_data'),
    path('branch/', views.branch, name='branch.html'),
    path('branch/', views.branch_view, name='branch'),
    path('branch/<str:branch>/', views.branch_view, name='branch'),
    path('chair/', views.chair, name='chair'),
    path('c2stage/<str:customers>/<str:Perfer>', views.c2stage, name='c2stage'),
    path('test/', views.satisfaction_form, name='satisfaction_form'),
]