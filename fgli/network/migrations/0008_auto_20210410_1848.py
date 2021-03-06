# Generated by Django 3.2 on 2021-04-10 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0007_auto_20210410_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='userroles',
            name='a1',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='userroles',
            name='a2',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='userroles',
            name='employer',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userroles',
            name='fgli',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userroles',
            name='linkedin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userroles',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='MentorApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField(auto_now=True)),
                ('employer', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('a1', models.CharField(max_length=1000)),
                ('a2', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
