# Generated by Django 5.1.3 on 2025-01-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0024_alter_corefeaturevideo_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsection',
            name='whats_in_it_for_me_points_az',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='aboutsection',
            name='whats_in_it_for_me_points_en',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='aboutsection',
            name='whats_in_it_for_me_points_ru',
            field=models.JSONField(null=True),
        ),
    ]
