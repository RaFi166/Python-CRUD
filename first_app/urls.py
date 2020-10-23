from django.contrib import admin
from django.urls import path
from first_app import views

app_name='first_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('student', views.student, name="student"),
    path('student_info/<int:student_id>',views.student_info, name="student_info"),
    path('info_edit/<int:student_id>/', views.info_edit, name="info_edit"),
    path('student_delete/<int:student_id>', views.delete, name="delete"),
  
]