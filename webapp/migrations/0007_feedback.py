# Generated by Django 3.1.3 on 2023-03-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_userrequests'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=1000)),
            ],
        ),
    ]