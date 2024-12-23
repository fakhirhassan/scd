# Generated by Django 5.0.4 on 2024-05-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('player_1_id', models.CharField(max_length=100)),
                ('player_1_name', models.CharField(max_length=100)),
                ('player_2_id', models.CharField(max_length=100)),
                ('player_2_name', models.CharField(max_length=100)),
                ('player_3_id', models.CharField(max_length=100)),
                ('player_3_name', models.CharField(max_length=100)),
                ('player_4_id', models.CharField(max_length=100)),
                ('player_4_name', models.CharField(max_length=100)),
                ('substitute_id', models.CharField(max_length=100)),
                ('substitute_name', models.CharField(max_length=100)),
                ('tournament', models.CharField(max_length=100)),
            ],
        ),
    ]
