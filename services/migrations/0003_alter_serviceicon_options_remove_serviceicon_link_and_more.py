# Generated by Django 5.1.3 on 2024-12-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_serviceicon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceicon',
            options={'verbose_name': '(Service seifesi 2 )', 'verbose_name_plural': '(Service seifesi 2)'},
        ),
        migrations.RemoveField(
            model_name='serviceicon',
            name='link',
        ),
        migrations.AlterField(
            model_name='serviceicon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='service_images/'),
        ),
    ]
