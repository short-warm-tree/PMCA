# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-05 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=5, verbose_name='姓名')),
                ('grade', models.CharField(default='', max_length=5, verbose_name='年级')),
                ('stunum', models.CharField(default='', max_length=13, verbose_name='学号')),
                ('college', models.CharField(choices=[('1', '计算机学院'), ('2', '软件学院'), ('3', '电子信息学院'), ('4', '电气信息学院'), ('5', '数学学院'), ('6', '经济学院'), ('7', '空天科学与工程学院'), ('8', '高分子科学与工程学院'), ('9', '材料科学与工程学院'), ('10', '制造科学与工程学院'), ('11', '建筑与环境学院'), ('12', '水利水电学院'), ('13', '化学工程学院'), ('14', '轻纺与食品学院'), ('15', '法学院'), ('16', '艺术学院'), ('17', '文学与新闻学院'), ('18', '外国语学院'), ('19', '马克思主义学院（政治学院）'), ('20', '物理科学与技术学院（核科学与工程技术学院）'), ('21', '化学学院'), ('22', '生命科学学院'), ('23', '灾后重建与管理学院'), ('24', '公共管理学院'), ('25', '商学院'), ('26', '华西基础医学与法医学院'), ('27', '华西临床医学院'), ('28', '华西口腔医学院'), ('29', '华西公共卫生学院'), ('30', '华西药学院'), ('31', '吴玉章学院'), ('32', '体育学院'), ('33', '网络空间安全学院'), ('33', '研究生院'), ('34', '其他')], default='27', max_length=2, verbose_name='学院')),
                ('major', models.CharField(default='', max_length=10, verbose_name='专业')),
                ('gender', models.CharField(choices=[('1', '男'), ('0', '女')], default='1', max_length=1, verbose_name='性别')),
                ('skill', models.TextField(default='', max_length=200, verbose_name='技能')),
                ('prove', models.TextField(default='', max_length=255, verbose_name='技能证明材料')),
                ('done', models.TextField(default='', max_length=500, verbose_name='协会贡献')),
            ],
        ),
    ]
