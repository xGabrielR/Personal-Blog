# Generated by Django 4.0.3 on 2022-03-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_center',
            field=models.TextField(blank=True, null=True, verbose_name='Contexto'),
        ),
    ]