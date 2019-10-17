from django.db import models
from django.urls import reverse

# Модель Планет
class Planet(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название планеты')

    class Meta:
        ordering = ['name']
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

    def __str__(self):
        return self.name

# Модель Ситхов
class Sith(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='siths', verbose_name='Планета', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:SithPage', args=[self.slug])

# Модель Рекрутов
class Recruit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    age = models.PositiveSmallIntegerField(blank=True, verbose_name='Возраст')
    email = models.CharField(max_length=255, unique=True, verbose_name='Email')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='recruits', verbose_name='Планета', blank=True)
    finished = models.BooleanField(default=False, verbose_name='Прошел тест')
    

    class Meta:
        ordering = ['name']
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:RecruitPage', args=[self.id, self.email])

# Модель отношения Рекрута к Ситху
class RecruitToSith(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name='recruit_siths', verbose_name='Рекрут', blank=True)
    sith = models.ForeignKey(Sith, on_delete=models.CASCADE, related_name='sith_to_recruit', verbose_name='Ситх', blank=True)
    approved = models.BooleanField(default=False, verbose_name='Принят')

    class Meta:
        ordering = ['sith']
        verbose_name = 'Рекрут-Ситх'
        verbose_name_plural = 'Рекрут-Ситх'

# Модель вопроса
class Question(models.Model):
    question = models.TextField(blank=True, verbose_name='Вопрос')

    class Meta:
        ordering = ['question']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question

# Модель ответа с привязкой к определенному вопросу
class Answer(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name='answers', verbose_name='Ответ рекрута', blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions', verbose_name='Вопрос', blank=True)
    value = models.BooleanField(default=False, verbose_name='Ответ')

    class Meta:
        ordering = ['recruit']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    
    def __str__(self):
        return self.question.question
