# Generated by Django 4.1.3 on 2023-05-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentfor',
            name='related',
            field=models.CharField(default='', max_length=80),
        ),
    ]