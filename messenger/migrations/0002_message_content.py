# Generated by Django 4.2.7 on 2023-11-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(default='Valor predeterminado'),
        ),
    ]