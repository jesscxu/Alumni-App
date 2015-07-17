# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_text', models.CharField(max_length=200)),
                ('address_text', models.CharField(max_length=200)),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
            ],
        ),
    ]
