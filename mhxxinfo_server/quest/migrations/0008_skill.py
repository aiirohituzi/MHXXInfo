# Generated by Django 2.0.2 on 2018-02-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0007_auto_20180203_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillType', models.CharField(max_length=30)),
                ('skillName', models.CharField(max_length=200)),
                ('point', models.CharField(max_length=25)),
                ('effect', models.CharField(max_length=500)),
            ],
        ),
    ]