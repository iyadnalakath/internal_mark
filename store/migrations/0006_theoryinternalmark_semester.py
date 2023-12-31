# Generated by Django 4.2.6 on 2023-10-25 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projectaccount", "0010_subject_role"),
        ("store", "0005_theoryinternalmark_attendance_percentage"),
    ]

    operations = [
        migrations.AddField(
            model_name="theoryinternalmark",
            name="semester",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="semester_theory_mark",
                to="projectaccount.semester",
            ),
        ),
    ]
