# Generated by Django 4.1.2 on 2022-10-14 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bakshe_cholo_app", "0011_busdriver_alter_profile_user_type"),
    ]

    operations = [
        migrations.RenameModel(old_name="BusDriver", new_name="Bus",),
    ]
