# Generated by Django 2.0.2 on 2018-03-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0008_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='effect',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='point',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skillName',
            field=models.TextField(),
        ),
    ]