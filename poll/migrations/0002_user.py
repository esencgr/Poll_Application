# Generated by Django 3.0.3 on 2021-05-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]
