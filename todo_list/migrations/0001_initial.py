# Generated by Django 4.0.6 on 2022-11-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Задачи')),
                ('priority', models.PositiveIntegerField(verbose_name='Приоритет')),
            ],
        ),
    ]
