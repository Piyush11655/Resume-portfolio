# Generated by Django 4.2.3 on 2024-06-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_about_resume_alter_about_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ImageField(null=True, upload_to='about'),
        ),
    ]
