# Generated by Django 2.1.7 on 2019-04-03 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StepModel', '0004_auto_20190402_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stepmodel',
            name='step_text',
            field=models.CharField(default='', max_length=255),
        ),
    ]
