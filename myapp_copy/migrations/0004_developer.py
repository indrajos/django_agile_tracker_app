# Generated by Django 4.2.5 on 2023-10-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_story_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('developer_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
