# Generated by Django 3.0.6 on 2020-09-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0016_auto_20200423_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_intent',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]