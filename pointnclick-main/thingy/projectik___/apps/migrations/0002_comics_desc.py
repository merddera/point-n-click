# Generated by Django 4.1.3 on 2023-02-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comics',
            name='desc',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
