# Generated by Django 4.0 on 2021-12-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('rank', models.IntegerField(default=1, help_text='Очередность показа', verbose_name='Позиция')),
                ('is_approved', models.BooleanField(default=True, verbose_name='Активно')),
                ('top_code', models.TextField(blank=True, verbose_name='Код после <body>')),
                ('bottom_code', models.TextField(blank=True, verbose_name='Код перед </body>')),
                ('header_code', models.TextField(blank=True, verbose_name='Код в <header>')),
            ],
            options={
                'verbose_name': 'Счетчик',
                'verbose_name_plural': 'Счетчики',
                'ordering': ['is_approved', 'rank', 'title'],
            },
        ),
        migrations.CreateModel(
            name='EmailLogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Лог ошибок',
                'verbose_name_plural': 'Логи ошибок',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('password', models.CharField(max_length=255, verbose_name='Пароль')),
                ('port', models.PositiveSmallIntegerField(default=587, verbose_name='Порт')),
                ('tls', models.BooleanField(default=True, verbose_name='Использовать TLS')),
                ('host', models.CharField(max_length=255, verbose_name='Хост провайдера')),
            ],
            options={
                'verbose_name': 'Глобальные настройки почты',
            },
        ),
    ]