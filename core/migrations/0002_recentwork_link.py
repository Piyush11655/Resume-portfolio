# Generated by Django 5.0.2 on 2024-06-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recentwork',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Work link'),
        ),
    ]