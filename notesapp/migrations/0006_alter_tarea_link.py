# Generated by Django 4.2.3 on 2023-08-08 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0005_tarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='link',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
