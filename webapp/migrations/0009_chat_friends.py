# Generated by Django 3.1.3 on 2023-03-24 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_missing'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('chatbw', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.CharField(max_length=149)),
                ('frnd_e', models.CharField(max_length=149)),
                ('frnd_n', models.CharField(max_length=149)),
            ],
        ),
    ]