# Generated by Django 2.1.12 on 2022-07-18 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('bc_id', models.IntegerField(blank=True, null=True)),
                ('role', models.SmallIntegerField(choices=[(0, 'ADMIN'), (1, 'SENIOR_BUYER'), (2, 'JUNIOR_BUYER'), (3, 'SUPER_ADMIN')])),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_users', to='companies.Companies')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
