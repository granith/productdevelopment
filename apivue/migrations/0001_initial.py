# Generated by Django 2.1.1 on 2018-09-22 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=30, verbose_name='Field Name')),
                ('type', models.CharField(choices=[('Text', 'text'), ('Number', 'number'), ('Date', 'date'), ('enum', 'enum')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RiskFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_types', models.ManyToManyField(to='apivue.FieldTypes')),
            ],
        ),
        migrations.CreateModel(
            name='RiskTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.AddField(
            model_name='riskfields',
            name='risks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apivue.RiskTypes'),
        ),
    ]
