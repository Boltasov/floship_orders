# Generated by Django 4.2.3 on 2023-07-05 04:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('order_number', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'In Progress'), (3, 'Stored'), (4, 'Send')], default=1)),
            ],
        ),
    ]
