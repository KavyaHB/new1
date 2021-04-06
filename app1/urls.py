from django.urls import path
from app1 import views

app_name="app1"


urlpatterns=[
    path('',views.index,name="index"),
    path('app1/',views.hello,name="app1"),
    path('sam/',views.sample_app1,name="sample2"),
]