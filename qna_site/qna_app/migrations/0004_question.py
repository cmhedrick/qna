# Generated by Django 2.1.7 on 2019-04-06 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0003_auto_20190327_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='qna_app.Organization')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='qna_app.Staff')),
            ],
        ),
    ]
