# Generated by Django 4.0.1 on 2022-01-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, default='Anonymous', max_length=50),
        ),
    ]
