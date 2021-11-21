# Generated by Django 3.2.8 on 2021-11-02 02:18

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('meta_tags', models.CharField(blank=True, max_length=2000)),
                ('meta_desc', models.TextField(blank=True, max_length=2000)),
                ('image_alt_name', models.CharField(blank=True, max_length=200)),
                ('youtube', models.URLField(default='', max_length=500)),
                ('author', models.CharField(default='admin', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Practice_title',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title_Content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('linkVideo', embed_video.fields.EmbedVideoField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('MieuTa', models.TextField()),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('contentA', models.CharField(max_length=500)),
                ('contentB', models.CharField(max_length=500)),
                ('contentC', models.CharField(max_length=500)),
                ('contentD', models.CharField(max_length=500)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GTEAMS_APP.practice_title')),
            ],
        ),
    ]
