from django.urls import path

from . import views

urlpatterns = [
    path('blackbox', views.blackbox, name='blackbox'),
    path('blackbox_results', views.blackbox_results, name='blackbox_results'),
    path('stan1', views.stan1, name='stan1'),
    path('stan2', views.stan2, name='stan2'),
    path('stan3', views.stan3, name='stan3'),
    path('stan4', views.stan4, name='stan4'),
    path('stan5', views.stan5, name='stan5'),
    path('use_case_login', views.use_case_login, name='use_case_login'),
    path('use_case_home', views.use_case_home, name='use_case_home'),
    path('use_case_add_invoice', views.use_case_add_invoice, name='use_case_add_invoice'),
    path('use_case_add_company', views.use_case_add_company, name='use_case_add_company'),
    path('web_apps', views.web_apps, name='web_apps'),
]