# Generated by Django 3.0.6 on 2020-09-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0050_auto_20200904_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_jwt_iat',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]