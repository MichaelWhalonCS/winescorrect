# Generated by Django 3.0.8 on 2020-07-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wine_name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=10)),
                ('varietal', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
