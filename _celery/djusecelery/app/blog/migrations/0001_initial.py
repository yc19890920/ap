# Generated by Django 2.0.7 on 2018-07-11 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='标题')),
            ],
            options={
                'verbose_name': '文章',
                'db_table': 'blog',
            },
        ),
    ]
