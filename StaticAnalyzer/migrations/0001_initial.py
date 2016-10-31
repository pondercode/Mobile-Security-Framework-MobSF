# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticAnalyzerAndroid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TITLE', models.TextField()),
                ('APP_NAME', models.TextField()),
                ('SIZE', models.CharField(max_length=50)),
                ('MD5', models.CharField(max_length=30)),
                ('SHA1', models.TextField()),
                ('SHA256', models.TextField()),
                ('PACKAGENAME', models.TextField()),
                ('MAINACTIVITY', models.TextField()),
                ('TARGET_SDK', models.CharField(max_length=50)),
                ('MAX_SDK', models.CharField(max_length=50)),
                ('MIN_SDK', models.CharField(max_length=50)),
                ('ANDROVERNAME', models.CharField(max_length=100)),
                ('ANDROVER', models.CharField(max_length=50)),
                ('MANIFEST_ANAL', models.TextField()),
                ('PERMISSIONS', models.TextField()),
# Esteve 21.08.2016 - begin - Permission Analysis with Androguard
                ('ANDROPERMS', models.TextField()),
# Esteve 21.08.2016 - END - Permission Analysis with Androguard
                ('FILES', models.TextField()),
                ('CERTZ', models.TextField()),
                ('ACTIVITIES', models.TextField()),
                ('RECEIVERS', models.TextField()),
                ('PROVIDERS', models.TextField()),
                ('SERVICES', models.TextField()),
                ('LIBRARIES', models.TextField()),
                ('CNT_ACT', models.CharField(max_length=50)),
                ('CNT_PRO', models.CharField(max_length=50)),
                ('CNT_SER', models.CharField(max_length=50)),
                ('CNT_BRO', models.CharField(max_length=50)),
                ('CERT_INFO', models.TextField()),
                ('ISSUED', models.CharField(max_length=10)),
                ('NATIVE', models.CharField(max_length=50)),
                ('DYNAMIC', models.CharField(max_length=50)),
                ('REFLECT', models.CharField(max_length=50)),
                ('CRYPTO', models.CharField(max_length=50)),
                ('OBFUS', models.CharField(max_length=50)),
                ('API', models.TextField()),
                ('DANG', models.TextField()),
                ('URLS', models.TextField()),
                ('DOMAINS', models.TextField()),
                ('EMAILS', models.TextField()),
                ('STRINGS', models.TextField()),
# Esteve 14.08.2016 - begin - Pirated and Malicious App Detection with APKiD
                ('APKID', models.TextField()),
# Esteve 14.08.2016 - end - Pirated and Malicious App Detection with APKiD
                ('ZIPPED', models.TextField()),
                ('MANI', models.TextField()),
                ('EXPORTED_ACT', models.TextField()),
                ('E_ACT', models.CharField(max_length=50)),
                ('E_SER', models.CharField(max_length=50)),
                ('E_BRO', models.CharField(max_length=50)),
                ('E_CNT', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StaticAnalyzerIOSZIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TITLE', models.TextField()),
                ('APPNAMEX', models.TextField()),
                ('SIZE', models.CharField(max_length=50)),
                ('MD5', models.CharField(max_length=50)),
                ('SHA1', models.TextField()),
                ('SHA256', models.TextField()),
                ('INFOPLIST', models.TextField()),
                ('BINNAME', models.TextField()),
                ('IDF', models.TextField()),
                ('VERSION', models.CharField(max_length=50)),
                ('SDK', models.TextField()),
                ('PLTFM', models.TextField()),
                ('MINX', models.TextField()),
                ('BIN_ANAL', models.TextField()),
                ('LIBS', models.TextField()),
                ('FILES', models.TextField()),
                ('SFILESX', models.TextField()),
                ('HTML', models.TextField()),
                ('CODEANAL', models.TextField()),
                ('URLnFile', models.TextField()),
                ('DOMAINS', models.TextField()),
                ('EmailnFile', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StaticAnalyzerIPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TITLE', models.TextField()),
                ('APPNAMEX', models.TextField()),
                ('SIZE', models.CharField(max_length=50)),
                ('MD5', models.CharField(max_length=50)),
                ('SHA1', models.TextField()),
                ('SHA256', models.TextField()),
                ('INFOPLIST', models.TextField()),
                ('BINNAME', models.TextField()),
                ('IDF', models.TextField()),
                ('VERSION', models.CharField(max_length=50)),
                ('SDK', models.TextField()),
                ('PLTFM', models.TextField()),
                ('MINX', models.TextField()),
                ('BIN_ANAL', models.TextField()),
                ('LIBS', models.TextField()),
                ('FILES', models.TextField()),
                ('SFILESX', models.TextField()),
                ('STRINGS', models.TextField()),
            ],
        ),
    ]
