# Generated by Django 2.2.5 on 2019-09-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='important_thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ersteller', models.CharField(max_length=30)),
                ('Datum', models.DateField(verbose_name='Datum')),
                ('body', models.TextField()),
            ],
        ),
    ]