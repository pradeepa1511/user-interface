# Generated by Django 2.2.14 on 2020-07-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentsaccceptorreject', models.CharField(default='accept', max_length=10)),
            ],
        ),
    ]