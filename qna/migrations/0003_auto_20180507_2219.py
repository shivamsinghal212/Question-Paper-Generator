# Generated by Django 2.0.5 on 2018-05-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_questions_klass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='klass',
            field=models.CharField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VII')], max_length=10),
        ),
        migrations.AlterField(
            model_name='questions',
            name='subject',
            field=models.CharField(choices=[('SC', 'Science'), ('MT', 'Mathematics'), ('SST', 'Social Studies'), ('EN', 'English')], max_length=50),
        ),
    ]
