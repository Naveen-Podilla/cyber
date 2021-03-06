# Generated by Django 3.0.2 on 2021-02-16 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserAdd_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('records', models.CharField(max_length=1000)),
                ('organizationtype', models.CharField(max_length=1000)),
                ('method', models.CharField(max_length=100)),
                ('adddata', models.CharField(max_length=500)),
                ('attackresult', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=100)),
                ('uregid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserRegister_Model')),
            ],
        ),
    ]
