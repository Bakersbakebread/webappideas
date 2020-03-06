# Generated by Django 3.0.2 on 2020-01-16 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_auto_20200116_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_to', models.CharField(max_length=250)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.Idea')),
            ],
        ),
    ]
