from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        send_mail(
            'Вопрос с сайта Game Chairs',
            question,
            'from@example.com',  # Замените на вашу почту
            ['dizbalancer719@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse('Спасибо за ваш вопрос!')
    return render(request, 'chairs/home.html')