# Generated by Django 4.2 on 2023-05-10 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='raspisanie',
            options={'verbose_name': 'Расписание', 'verbose_name_plural': 'Расписания'},
        ),
        migrations.RenameField(
            model_name='raspisanie',
            old_name='day',
            new_name='title',
        ),
    ]