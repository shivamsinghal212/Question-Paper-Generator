# Generated by Django 2.0.5 on 2018-05-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0010_auto_20180529_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.CharField(max_length=20),
        ),
    ]
