# Generated by Django 4.1.5 on 2024-01-15 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_options_remove_project_vote_ratio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-created_at',)},
        ),
    ]