# Generated by Django 2.2.6 on 2019-10-16 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название планеты')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['question'],
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(blank=True, verbose_name='Возраст')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='Email')),
                ('planet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruits', to='mainapp.Planet', verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Рекрут',
                'verbose_name_plural': 'Рекруты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('planet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='siths', to='mainapp.Planet', verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Ситх',
                'verbose_name_plural': 'Ситхи',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RecruitToSith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False, verbose_name='Принят')),
                ('recruit', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruit_siths', to='mainapp.Recruit', verbose_name='Рекрут')),
                ('sith', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sith_to_recruit', to='mainapp.Sith', verbose_name='Ситх')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=False, verbose_name='Ответ')),
                ('question', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='mainapp.Question', verbose_name='Вопрос')),
                ('recruit', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='mainapp.Recruit', verbose_name='Ответ рекрута')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ['value'],
            },
        ),
    ]