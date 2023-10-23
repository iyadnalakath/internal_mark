# Generated by Django 4.2.6 on 2023-10-20 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projectaccount", "0007_remove_account_semester_account_semester"),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="semester",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_semester",
                to="projectaccount.semester",
            ),
        ),
    ]
