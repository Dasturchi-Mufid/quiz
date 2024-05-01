from main import models

from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = ['name',]

class CustomQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ['name']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    quiz = CustomQuizSerializer()
    class Meta:
        model = models.Question
        fields = ['id','code','name','quiz','options']
