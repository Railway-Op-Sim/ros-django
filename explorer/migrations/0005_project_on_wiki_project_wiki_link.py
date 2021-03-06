# Generated by Django 4.0.4 on 2022-05-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0004_alter_project_collab_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='on_wiki',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='wiki_link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
