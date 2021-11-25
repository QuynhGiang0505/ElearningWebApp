# Generated by Django 3.2.8 on 2021-11-25 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GTEAMS_APP', '0002_typecourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='cost',
        ),
        migrations.AddField(
            model_name='courses',
            name='Type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GTEAMS_APP.typecourse'),
            preserve_default=False,
        ),
    ]
