# Generated by Django 3.2.8 on 2021-11-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTEAMS_APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]