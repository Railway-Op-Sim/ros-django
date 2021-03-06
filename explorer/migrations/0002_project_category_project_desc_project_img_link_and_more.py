# Generated by Django 4.0.4 on 2022-05-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='UNKNOWN', max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.CharField(default='UNKNOWN', max_length=25565),
        ),
        migrations.AddField(
            model_name='project',
            name='img_link',
            field=models.CharField(default='UNKNOWN', max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='short_desc',
            field=models.CharField(default='UNKNOWN', max_length=1000),
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.CharField(default='UNKNOWN', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='UNKNOWN', max_length=200),
        ),
    ]
