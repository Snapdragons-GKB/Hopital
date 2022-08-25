# Generated by Django 4.1 on 2022-08-25 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_patient', models.BooleanField(default=False)),
                ('is_scheduler', models.BooleanField(default=False)),
                ('is_provider', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedulerProfile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_personal_blurb', models.CharField(max_length=200)),
                ('provider_specialization', models.CharField(choices=[('0', 'None'), ('1', 'Cardiology'), ('2', 'Neurology'), ('3', 'Pediatrics'), ('4', 'Surgery'), ('5', 'Dental'), ('6', 'General Medicine'), ('7', 'Psychiatry'), ('8', 'Radiology'), ('9', 'Surgical'), ('10', 'Other')], default='0', max_length=20)),
                ('provider_insurances_taken', models.CharField(choices=[('0', 'Without Insurance'), ('1', 'Medicaid'), ('2', 'Medicare'), ('3', 'Private')], default='0', max_length=20)),
                ('day1', models.BooleanField(default=False)),
                ('day2', models.BooleanField(default=False)),
                ('day3', models.BooleanField(default=False)),
                ('day4', models.BooleanField(default=False)),
                ('day5', models.BooleanField(default=False)),
                ('day6', models.BooleanField(default=False)),
                ('day7', models.BooleanField(default=False)),
                ('providerProfile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PatientRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', models.CharField(choices=[('0', 'Awating Response'), ('1', 'Accepted'), ('2', 'Rejected'), ('3', 'Completed')], default='0', max_length=20)),
                ('request_ailment_category', models.CharField(choices=[('0', 'None'), ('1', 'Cardiology'), ('2', 'Neurology'), ('3', 'Pediatrics'), ('4', 'Surgery'), ('5', 'Dental'), ('6', 'General Medicine'), ('7', 'Psychiatry'), ('8', 'Radiology'), ('9', 'Surgical'), ('10', 'Other')], default='0', max_length=20)),
                ('request_ailment_description', models.CharField(max_length=80)),
                ('request_preferred_date_range', models.DateField()),
                ('request_procedure_date', models.DateField()),
                ('request_scheduling_comment', models.TextField()),
                ('request_doctor_comment_on_operation', models.TextField()),
                ('request_doctor_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctorofrequest', to='main_app.profile')),
                ('request_patient_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patientofrequest', to='main_app.profile')),
                ('request_scheduler_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedulerofrequest', to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_age', models.IntegerField()),
                ('patient_insurance_type', models.CharField(choices=[('0', 'Without Insurance'), ('1', 'Medicaid'), ('2', 'Medicare'), ('3', 'Private')], default='0', max_length=20)),
                ('patient_preexisting_conditions', models.TextField(max_length=80)),
                ('patient_current_medications', models.TextField(max_length=80)),
                ('patientProfile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
    ]
