# Generated by Django 3.0.2 on 2021-02-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adpet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (None, 'Male or Female')], null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='seize',
            field=models.IntegerField(choices=[(0, 'Small'), (1, 'Medium'), (2, 'Big'), (None, 'Small, Medium or big')], null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='sterilized',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (None, 'Yes or No')], null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='vaccinated',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (None, 'Yes or No')], null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='specie',
            field=models.CharField(choices=[('CT', 'Cat'), ('DG', 'Dog'), (None, 'Dog or cat')], max_length=200),
        ),
    ]
