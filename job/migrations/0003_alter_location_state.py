# Generated by Django 5.0.4 on 2024-04-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]