# Generated by Django 2.0.7 on 2018-12-12 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pals', '0008_auto_20180708_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_field',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
