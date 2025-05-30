# Generated by Django 5.1.7 on 2025-04-16 13:46

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('desc', models.CharField(blank=True, max_length=2000)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time of creation of this ledger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Ledger creator and owner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('desc', models.CharField(blank=True, max_length=2000)),
                ('entry_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time of this entry')),
                ('payment_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time of payment')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total cost of the payment')),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.ledger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Payment creator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.payment')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.person')),
            ],
        ),
        migrations.CreateModel(
            name='UserPlaceholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='placeholder',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to='main.userplaceholder'),
        ),
    ]
