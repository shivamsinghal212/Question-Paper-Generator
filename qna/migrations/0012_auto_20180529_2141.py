# Generated by Django 2.0.5 on 2018-05-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0011_auto_20180529_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
