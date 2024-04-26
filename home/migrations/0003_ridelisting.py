# Generated by Django 4.2.5 on 2023-10-19 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_ride'),
    ]

    operations = [
        migrations.CreateModel(
            name='RideListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ride')),
            ],
        ),
    ]
