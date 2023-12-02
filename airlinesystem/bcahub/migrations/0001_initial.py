# Generated by Django 4.2.5 on 2023-12-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operating_date', models.DateTimeField()),
                ('airline', models.CharField(max_length=20)),
                ('airline_name', models.CharField(max_length=20)),
                ('airline_NO', models.IntegerField(verbose_name=10)),
                ('depature_Port', models.CharField(max_length=10)),
                ('depature_date_time', models.DateTimeField()),
                ('arrival_date_time', models.DateField()),
                ('flight_status', models.CharField(max_length=10)),
                ('delay_issue', models.CharField(max_length=10)),
                ('remarks', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=20)),
                ('service_status', models.CharField(max_length=10)),
                ('depature_port', models.CharField(max_length=10)),
                ('arrival_port', models.CharField(max_length=10)),
                ('depature_date_time', models.DateTimeField()),
                ('arrival_date_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Journeysearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name=5)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.IntegerField(verbose_name=10)),
                ('father', models.CharField(max_length=20)),
                ('passport', models.IntegerField(verbose_name=10)),
                ('gender', models.CharField(max_length=10)),
                ('flightName', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=10)),
                ('depature_date_time', models.DateTimeField()),
                ('arrival_date_time', models.DateField()),
                ('risk_satus', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Riskaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name=5)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.IntegerField(verbose_name=10)),
                ('father', models.CharField(max_length=20)),
                ('passport', models.IntegerField(verbose_name=10)),
                ('gender', models.CharField(max_length=10)),
                ('nrc', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Traveller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=20)),
                ('timeFrame', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.IntegerField(verbose_name=10)),
                ('nrc', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('depature_port', models.CharField(max_length=10)),
                ('depature_date_time', models.DateTimeField()),
                ('arrival_port', models.CharField(max_length=10)),
                ('arrival_date_time', models.DateField()),
            ],
        ),
    ]
