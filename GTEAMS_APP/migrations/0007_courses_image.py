# Generated by Django 3.2.8 on 2021-11-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTEAMS_APP', '0006_remove_practice_title_tui'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
