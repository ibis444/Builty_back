# Generated by Django 5.1.3 on 2024-12-25 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_corefeaturesection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='client_images/')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
