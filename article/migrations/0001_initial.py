# Generated by Django 2.1.3 on 2018-11-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('article_body', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
