# Generated by Django 4.2.16 on 2024-11-13 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_name', models.CharField(max_length=100, verbose_name='想去的地方')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('start_date', models.DateField(verbose_name='开始日期')),
                ('end_date', models.DateField(verbose_name='结束日期')),
            ],
            options={
                'verbose_name': '行程信息',
                'verbose_name_plural': '行程信息',
            },
        ),
        migrations.CreateModel(
            name='TripPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField(verbose_name='第几天')),
                ('trip_description', models.CharField(max_length=200, verbose_name='目的地')),
                ('trip_order', models.IntegerField(verbose_name='游玩顺序')),
                ('description', models.TextField(blank=True, null=True, verbose_name='目的地简介')),
                ('trip_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_plans', to='trip.tripinformation', verbose_name='行程ID')),
            ],
            options={
                'verbose_name': '行程内容',
                'verbose_name_plural': '行程内容',
                'ordering': ['days', 'trip_order'],
            },
        ),
    ]
