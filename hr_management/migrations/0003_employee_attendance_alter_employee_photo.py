# Generated by Django 4.0.5 on 2022-09-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management', '0002_remove_employee_repassword_remove_employee_sale_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='attendance',
            field=models.CharField(choices=[('absent', 'Absent'), ('attended', 'Attended')], default='absent', max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='Employee'),
        ),
    ]
