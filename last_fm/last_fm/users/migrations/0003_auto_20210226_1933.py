# Generated by Django 3.1.7 on 2021-02-27 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_telefono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='telefono',
            new_name='age',
        ),
    ]
