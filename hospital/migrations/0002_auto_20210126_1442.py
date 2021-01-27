# Generated by Django 3.1.4 on 2021-01-26 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okb2', '0001_initial'),
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='napr',
            name='napr_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='b_diag',
            name='diag_tip',
            field=models.CharField(blank=True, choices=[('1', 'Гистологический признак'), ('2', 'Маркёр (ИГХ)')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='b_prot',
            name='prot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.n001'),
        ),
        migrations.AlterField(
            model_name='cons',
            name='pr_cons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.n019'),
        ),
        migrations.AlterField(
            model_name='ksg_kpg',
            name='ksg_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.v023'),
        ),
        migrations.AlterField(
            model_name='napr',
            name='napr_issl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.v029'),
        ),
        migrations.AlterField(
            model_name='napr',
            name='napr_mo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.f003'),
        ),
        migrations.AlterField(
            model_name='napr',
            name='napr_usl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.v001'),
        ),
        migrations.AlterField(
            model_name='napr',
            name='napr_v',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.v028'),
        ),
        migrations.AlterField(
            model_name='onk_usl',
            name='hir_tip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.n014'),
        ),
        migrations.AlterField(
            model_name='onk_usl',
            name='usl_tip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='okb2.n013'),
        ),
    ]
