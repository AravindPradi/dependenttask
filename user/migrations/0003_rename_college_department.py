# Generated by Django 4.2.4 on 2023-11-13 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_student_address_student_age_student_gender_and_more"),
    ]

    operations = [
        migrations.RenameModel(old_name="College", new_name="Department",),
    ]
