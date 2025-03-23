from django.urls import path
from . import views
urlpatterns = [
    path('', views.student_info, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('delete/',views.delete,name='delete_students'),
]
