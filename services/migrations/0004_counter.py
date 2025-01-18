# Generated by Django 5.1.3 on 2024-12-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_serviceicon_options_remove_serviceicon_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('label', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
