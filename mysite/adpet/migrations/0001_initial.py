# Generated by Django 3.0.2 on 2021-02-09 22:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')])),
                ('specie', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog')], max_length=50, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Big', 'Big')], max_length=50, null=True)),
                ('vaccinated', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('sterilized', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('breed', models.CharField(max_length=30, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('age', models.IntegerField(null=True)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('picture', models.BinaryField(editable=True, null=True)),
                ('content_type', models.CharField(help_text='The MIMEType of the file', max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(validators=[django.core.validators.MinLengthValidator(3, 'Comment must be greater than 3 characters')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adpet.Ad')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_petowned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='comments',
            field=models.ManyToManyField(related_name='adpet_commented', through='adpet.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_petowned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adpet.Ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('ad', 'user')},
            },
        ),
    ]
