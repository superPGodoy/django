# Generated by Django 2.0.9 on 2018-11-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]