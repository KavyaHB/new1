from django.urls import path
from app2 import views

app_name="app2"

urlpatterns=[
    path('',views.index,name="index"),
    path('sample2/',views.sample2,name="sample2"),
    path("abc/",views.sample_app2,name="abc"),
]