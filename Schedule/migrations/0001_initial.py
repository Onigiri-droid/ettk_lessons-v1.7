# Generated by Django 4.0.4 on 2022-06-14 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinet_name', models.CharField(max_length=20, verbose_name='Кабинет')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20, verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=30, verbose_name='Название пары')),
            ],
            options={
                'verbose_name': 'Занятие',
                'verbose_name_plural': 'Занятия',
            },
        ),
        migrations.CreateModel(
            name='Subgroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subgroups_name', models.CharField(max_length=3, verbose_name='Номер подгруппы')),
            ],
            options={
                'verbose_name': 'Подгруппа',
                'verbose_name_plural': 'Подгруппы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(default=1, verbose_name='Номер пары')),
                ('date', models.DateField(verbose_name='Дата пары')),
                ('reduction', models.BooleanField(default=False, verbose_name='Сокращенный день?')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schedule.cabinet', verbose_name='Кабинет')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schedule.group', verbose_name='Группа')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schedule.lesson', verbose_name='Занятие')),
                ('subgroups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schedule.subgroups', verbose_name='Подгруппы')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schedule.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
    ]
