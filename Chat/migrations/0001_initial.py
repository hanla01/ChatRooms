# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Roomname', models.CharField(max_length=30)),
                ('Max', models.PositiveSmallIntegerField(null=True, default=50)),
                ('Current', models.PositiveSmallIntegerField(null=True, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Content', models.TextField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('ChatRooms', models.ForeignKey(to='Chat.ChatRooms')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=30)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Password', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='Username',
            field=models.ForeignKey(to='Chat.User'),
            preserve_default=True,
        ),
    ]
