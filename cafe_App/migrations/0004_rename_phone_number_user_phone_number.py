# Generated by Django 5.0.6 on 2024-07-17 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_App', '0003_remove_user_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Phone_number',
            new_name='phone_number',
        ),
    ]
