# Generated by Django 4.0.5 on 2022-09-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('repassword', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('salary', models.FloatField()),
                ('hired_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('sale_end', models.DateTimeField(blank=True, default=None, null=True)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='products')),
            ],
        ),
    ]