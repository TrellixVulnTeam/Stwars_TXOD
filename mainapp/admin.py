from django.contrib import admin
from .models import *


class PlanetAdmin(admin.ModelAdmin):
    list_display = ['name']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']

class RecruitQuestionInlines(admin.TabularInline):
    model = Answer
    readonly_fields = ['question', 'value']

class SithAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class RecruitAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'planet', 'email']
    inlines = [RecruitQuestionInlines]




class RecruitQuestionAdmin(admin.ModelAdmin):
    list_display = ['recruit', 'question', 'value']
    readonly_fields = ['question', 'value']

    class Meta:
        model = Answer


class RecruitToSithAdmin(admin.ModelAdmin):
    list_display = ['sith', 'recruit', 'approved']
    readonly_fields = ['sith', 'recruit']

admin.site.register(Planet, PlanetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Sith, SithAdmin)
admin.site.register(Recruit, RecruitAdmin)
admin.site.register(Answer, RecruitQuestionAdmin)
admin.site.register(RecruitToSith, RecruitToSithAdmin)

