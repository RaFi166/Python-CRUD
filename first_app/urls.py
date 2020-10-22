from django.contrib import admin
from django.urls import path
from first_app import views

app_name='first_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('student_form', views.student_form, name="student_form"),
]