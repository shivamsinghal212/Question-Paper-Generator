# Generated by Django 2.0.5 on 2018-05-29 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0009_auto_20180529_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
    ]
