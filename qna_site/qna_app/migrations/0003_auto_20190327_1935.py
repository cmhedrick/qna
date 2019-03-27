# Generated by Django 2.1.7 on 2019-03-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0002_auto_20190327_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='role', max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='organization',
            name='user',
        ),
        migrations.AddField(
            model_name='staff',
            name='org',
            field=models.ManyToManyField(to='qna_app.Organization'),
        ),
        migrations.AddField(
            model_name='staff',
            name='role',
            field=models.ManyToManyField(to='qna_app.Role'),
        ),
    ]