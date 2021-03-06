# Generated by Django 3.0.6 on 2020-07-28 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0046_auto_20200602_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_id', models.CharField(blank=True, max_length=256)),
                ('type', models.CharField(blank=True, max_length=256)),
                ('team_id', models.CharField(blank=True, max_length=256)),
                ('league_id', models.CharField(blank=True, max_length=256)),
                ('expires', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('expires',),
            },
        ),
        migrations.AddField(
            model_name='user',
            name='stream_tickets',
            field=models.ManyToManyField(blank=True, related_name='user_stream_tickets', to='account.StreamTicket'),
        ),
    ]
