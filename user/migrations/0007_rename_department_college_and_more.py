# Generated by Django 4.2.4 on 2023-11-14 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_rename_college_department_and_more"),
    ]

    operations = [
        migrations.RenameModel(old_name="Department", new_name="College",),
        migrations.RenameField(
            model_name="student", old_name="department", new_name="college",
        ),
    ]
