# Generated by Django 4.1.3 on 2022-12-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=15, verbose_name='lastname')),
                ('firstname', models.CharField(max_length=15, verbose_name='firstname')),
                ('thirdname', models.CharField(max_length=15, verbose_name='thirdname')),
                ('job', models.TextField(verbose_name='job')),
                ('placejob', models.TextField(verbose_name='placejob')),
                ('theme', models.TextField(verbose_name='theme')),
                ('header', models.TextField(verbose_name='header')),
                ('full_text', models.TextField(verbose_name='full_text')),
            ],
        ),
    ]