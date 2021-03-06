# Generated by Django 2.2.11 on 2020-03-23 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pretixbase', '0146_giftcardtransaction_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('hex_address', models.CharField(max_length=42, unique=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pretixbase.Event')),  # noqa: E501
                ('order_payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pretixbase.OrderPayment')),  # noqa: E501
            ],
        ),
    ]
