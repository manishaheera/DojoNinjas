# Generated by Django 2.2 on 2021-04-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
