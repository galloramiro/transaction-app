# Generated by Django 3.0.5 on 2020-04-11 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on wich the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on wich the object was last modified.', verbose_name='modified_at')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on wich the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on wich the object was last modified.', verbose_name='modified_at')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_operations', to='accounts.Account')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on wich the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on wich the object was last modified.', verbose_name='modified_at')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_operations', to='accounts.Account')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]