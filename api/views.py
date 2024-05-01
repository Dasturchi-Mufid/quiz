from django.shortcuts import render
from rest_framework import generics
from . import serializers
from main import models
from rest_framework.decorators import api_view
from rest_framework.response import Response

class QuizApiView(generics.ListAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer


class QuestionApiView(generics.ListAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


@api_view(['GET'])
def get_quiz(request,code):
    quiz = models.Quiz.objects.get(code=code)
    questions = models.Question.objects.filter(quiz__code=quiz.code)
    serializer = serializers.QuestionSerializer(questions,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_question(request,code):
    question = models.Question.objects.get(code=code)
    options = models.Option.objects.filter(question__code=question.code)
    serializer = serializers.OptionSerializer(options,many=True)
    return Response({
        'question': question.name,
        'option':serializer.data
        })
