from django.urls import path
from Aplication import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('school', views.school, name='School'),
    path('professor', views.professor, name='Professor'),
    path('student', views.student, name='Student'),
    path('goodJob', views.goodJob, name='GoodJob'),
    path('searchStudent', views.searchStudent, name='SearchStudent'),
    path('search/', views.search)
]