from django.urls import path
from . import views

urlpatterns = [
    path('quiz/',views.QuizApiView.as_view()),
    path('questions/',views.QuestionApiView.as_view()),
    path('quiz/<str:code>/', views.get_quiz),
    path('question/<str:code>/', views.get_question),
]
