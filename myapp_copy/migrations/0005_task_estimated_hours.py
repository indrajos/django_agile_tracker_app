# Generated by Django 4.2.5 on 2023-10-17 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='estimated_hours',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
