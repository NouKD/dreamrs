# Generated by Django 3.0.7 on 2020-06-21 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag_Article', to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='categoriearticle',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='UserP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo/UserP')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserP',
                'verbose_name_plural': 'UserPs',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auteur_Article', to='blog.UserP'),
        ),
    ]
