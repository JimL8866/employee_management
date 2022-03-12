# Generated by Django 4.0.3 on 2022-03-12 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='title of Dep')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=25, verbose_name='first name')),
                ('l_name', models.CharField(max_length=25, verbose_name='last name')),
                ('password', models.CharField(max_length=30, verbose_name='password used')),
                ('age', models.IntegerField(verbose_name='age of employee')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='salary balance')),
                ('create_time', models.DateTimeField(verbose_name='time for account created')),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], verbose_name='gender')),
                ('dep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.department')),
            ],
        ),
    ]