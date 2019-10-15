# Generated by Django 2.2.6 on 2019-10-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('role', models.CharField(max_length=225)),
                ('gender', models.CharField(default='Male', max_length=6)),
                ('age', models.IntegerField()),
            ],
        ),
    ]