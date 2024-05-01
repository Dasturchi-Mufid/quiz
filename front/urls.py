from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('',views.index,name='index'),
    path('quiz/<str:code>/',views.quiz_detail,name='quiz_detail'),
]
