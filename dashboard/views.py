from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from main import models


def index(request):
    quizzes = models.Quiz.objects.filter(author=request.user.id)
    return render(request, 'index.html', {'quizzes':quizzes})


def quiz_list(request):
    quizzes = models.Quiz.objects.all()
    return render(request, 'quiz/list.html', {'quizzes':quizzes})


def quiz_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quiz = models.Quiz.objects.create(name=name, author=request.user)
        return redirect('quiz_detail', quiz.code)
    
    return render(request, 'quiz/create.html')


def quiz_detail(request, code):
    quiz = models.Quiz.objects.get(code=code)
    questions = models.Question.objects.filter(quiz=quiz)
    context = {
        'quiz':quiz,
        'questions':questions
    }
    return render(request, 'quiz/detail.html', context)


def question_create(request, code):
    quiz = models.Quiz.objects.get(code=code)
    if request.method == 'POST':
        question = models.Question.objects.create(
            name=request.POST['question'],
            quiz=quiz
            )
        models.Option.objects.create(
            name = request.POST['correct_option'],
            question = question,
            is_correct = True
        )
        for option in request.POST.getlist('options'):
            models.Option.objects.create(
            name = option,
            question = question,
            is_correct = False
            )
        return redirect('question_detail',question.code)
    return render(request,'question/create.html', {'quiz':quiz})


def question_detail(request, code):
    question = models.Question.objects.get(code=code)
    options = models.Option.objects.filter(question=question)
    context = {
        'question':question,
        'options':options
    }
    return render(request, 'question/detail.html', context)


def question_delete(request, code):
    question = models.Question.objects.get(code=code)
    question.delete()
    return redirect('quiz_detail', question.quiz.code)


def question_update(request, code):
    question = models.Question.objects.get(code=code)
    print(request.POST)
    if request.method == 'POST':
        question.name = request.POST['name']
        question.save()
        return redirect('question_detail', question.code)
def log_in(request):

    if request.method == 'POST':  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    return render(request, 'auth/login.html')


def log_out(request):
    logout(request)
    messages.success(request, 'logout success')
    return redirect('index')

"""
Quiz Create +++, List +++, Detail +++
Question Create +++, Detail ---
Option Create +++ ---
"""