# Generated by Django 3.0.6 on 2020-09-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0049_auto_20200903_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamticket',
            name='expires',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
