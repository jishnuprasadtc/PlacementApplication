# Generated by Django 4.2.6 on 2023-12-06 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_jobs_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category'),
        ),
    ]
