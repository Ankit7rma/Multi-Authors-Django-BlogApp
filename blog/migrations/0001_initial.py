# Generated by Django 3.1.5 on 2021-04-24 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0003_author_author_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Catagory',
            },
        ),
        migrations.CreateModel(
            name='EmailSignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'verbose_name_plural': ' User Emails',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('detail', models.TextField(max_length=2000, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/media')),
                ('status', models.CharField(choices=[('active', 'active'), ('pending', 'pending')], default='pending', max_length=20)),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.author')),
                ('catagories', models.ManyToManyField(to='blog.Catagory')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
