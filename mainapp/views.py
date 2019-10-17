from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .models import *
from .forms import *

# Гллвная страница
def Main(request):
    siths = Sith.objects.all() # Список всех Ситхов на главной странице, на которой Ситх выбирает себя
    form = RecruitForm(request.POST or None) # Форма для регистрации нового Рекрута
    if request.method == "POST" and form.is_valid(): # Прием данных о новом Рекруте и их проверка
        name = form.cleaned_data['name']
        planet = form.cleaned_data['planet']
        age = form.cleaned_data['age']
        email = form.cleaned_data['email']
        new_recruit = Recruit.objects.create(name=name, planet=planet, age=age, email=email) # Создание экземляра нового Рекрута
        new_recruit.save()  # Сохранение нового Рекрута в БД
        for question in Question.objects.all(): # Проход циклом по всем вопросам имеющихся в БД и закрепление их к новому Рекруту
            answer = Answer.objects.create(recruit=new_recruit, question=question)
            answer.save()
        return HttpResponseRedirect(reverse('mainapp:RecruitPage', args=[new_recruit.id, new_recruit.email])) # Перенаправдение нового Рекрута на его страницу, где он может пройти тест один раз!
    return render(request, 'main/main_page.html', {
        'siths': siths,
        'form': form,
    })


# Страница определенного Ситха со списком всех Рекрутов
def SithPage(request, sith_slug=None):
    sith = None
    recruits = Recruit.objects.all() # Беру всех имеющихся Рекрутов из БД
    if sith_slug:
        form = RecruitApproveForm()
        sith = get_object_or_404(Sith, slug=sith_slug)
        if request.method == "POST":                     # Если Ситх одобрил кандидатуру Рекрута
            id = request.POST.get('recruit_id')          # id Рекрута
            approved = request.POST.get('approved')      # Поле 'Одобрен' в модели RecruitToSith (Отношение Рекрута к определенному Ситху)
            if approved=='on':                           # Проверка поля формы одобрения 
                approved = True
            else:
                approved = False
            recruit = get_object_or_404(Recruit, id=id)  # Беру экземпляр Рекрута по его ID
            obj, recruit_to_sith = RecruitToSith.objects.get_or_create(recruit=recruit, sith=sith, approved=approved) # Создаю модель RecruitToSith (Отношение Рекрута к определенному Ситху), если ее нет
            message = 'Approved by ' + sith.name         # Формирую сообщение о зачислении Рекрута к Ситху 
            send_mail('AcademyStarWars', message, 'samosvalom@gmail.com', [recruit.email], fail_silently=False) # Отправдяю email об одобрении ситхом
        return render(request, 'sith/sith.html', {
            'sith' : sith,
            'recruits': recruits,
            'form': form,
        })


# Страница Рекрута с тестом либо с предупреждением, что он уже прошел тест
def RecruitPage(request, id, recruit_email):
    recruit = None
    if recruit_email:
        recruit = get_object_or_404(Recruit, email=recruit_email) # 
        answers = Answer.objects.filter(recruit=recruit) # Ответы Рекрута 
        if request.method == "POST": # Если Рекрут ответил на вопросы 
            for answer in answers: # Прохожу циклом по отвечанным вопросам Рекрута, пришедших на сервер
                answer_value = request.POST.get(str(answer.id)) # Ответ на вопрос пришедший на сервер
                if answer_value =='on': # Если ответил положительно
                    answer.value=True
                    answer.save(update_fields=['value']) # То обновляю значения ответа Рекрута
            recruit.finished=True # Помечаю, что Рекрут прошел тест
            recruit.save(update_fields=['finished']) # Обновляю поле о прохождении теста Рекрутом
    return render(request, 'recruit/recruit.html', {
        'recruit': recruit,
        'answers': answers,
    })
