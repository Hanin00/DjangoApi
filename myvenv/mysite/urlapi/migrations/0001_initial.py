# Generated by Django 3.2.6 on 2021-09-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('cat_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('locate', models.TextField()),
                ('character', models.TextField()),
                ('preferences', models.TextField()),
            ],
        ),
    ]
