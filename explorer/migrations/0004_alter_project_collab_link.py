# Generated by Django 4.0.4 on 2022-05-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0003_project_collab_project_collab_link_project_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='collab_link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
