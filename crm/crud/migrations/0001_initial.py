# Generated by Django 5.0.6 on 2024-07-08 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=122)),
                ('emp_code', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=12)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.position')),
            ],
        ),
    ]
