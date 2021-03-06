# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 08:48
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=512, null=True)),
                ('source', models.CharField(max_length=256, null=True)),
                ('author', models.CharField(max_length=64, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('number_problem', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('directory', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), size=None)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_relations', to='rest_api.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('introduction', models.TextField()),
                ('allow_all', models.BooleanField(default=False)),
                ('number_category', models.IntegerField(default=0)),
                ('number_problem', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientCategory',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_relation', to='rest_api.Category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_relation', to='rest_api.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=512, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True)),
                ('number_problem', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('judge_id', models.CharField(max_length=16, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('number_problem', models.IntegerField(default=0)),
                ('number_limit', models.IntegerField(default=0)),
                ('number_judge', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvalidWord',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('info', models.TextField(null=True)),
                ('last_update', models.DateTimeField(null=True)),
                ('cmd_queue', models.CharField(max_length=64)),
                ('environment', models.ManyToManyField(related_name='judge', to='rest_api.Environment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('env_name', models.CharField(max_length=128)),
                ('time_limit', models.IntegerField(default=-1)),
                ('memory_limit', models.IntegerField(default=-1)),
                ('length_limit', models.IntegerField(default=-1)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='limits', to='rest_api.Environment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetaProblem',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=512, null=True)),
                ('source', models.CharField(max_length=256, null=True)),
                ('author', models.CharField(max_length=64, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('number_description', models.IntegerField(default=0)),
                ('number_sample', models.IntegerField(default=0)),
                ('number_test_data', models.IntegerField(default=0)),
                ('number_problem', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=512, null=True)),
                ('source', models.CharField(max_length=256, null=True)),
                ('author', models.CharField(max_length=64, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_special_judge', models.BooleanField(default=False)),
                ('number_test_data', models.IntegerField(default=0)),
                ('number_limit', models.IntegerField(default=0)),
                ('number_category', models.IntegerField(default=0)),
                ('number_node', models.IntegerField(default=0)),
                ('number_invalid_word', models.IntegerField(default=0)),
                ('description', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='rest_api.Description')),
                ('environments', models.ManyToManyField(related_name='problems', through='rest_api.Limit', to='rest_api.Environment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProblemLimitJudge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_l_relation', to='rest_api.Judge')),
                ('limit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.Limit')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='ProblemTestData',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_data_rel', to='rest_api.Problem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=512, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True)),
                ('number_problem', models.IntegerField(default=0)),
                ('meta_problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='rest_api.MetaProblem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecialJudge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=512, null=True)),
                ('code', models.BinaryField()),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_judge', to='rest_api.Environment')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_judge', to='rest_api.Problem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.IntegerField(default=-1)),
                ('memory', models.IntegerField(default=-1)),
                ('length', models.IntegerField(default=-1)),
                ('user', models.CharField(max_length=150, null=True)),
                ('contest', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[('PD', 'Pending'), ('PDR', 'Pending Rejudge'), ('CP', 'Compiling'), ('CE', 'Compile Error'), ('CD', 'Compile Done'), ('RJ', 'Running & Judging'), ('RN', 'Running'), ('RE', 'Runtime Error'), ('TLE', 'Time Limit Exceed'), ('MLE', 'Memory Limit Exceed'), ('OLE', 'Output Limit Exceed'), ('RD', 'Running Done'), ('JD', 'Judging'), ('WA', 'Wrong Answer'), ('PE', 'Presentation Error'), ('AC', 'Accepted')], default='PD', max_length=4)),
                ('finished', models.BooleanField(default=False)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('creator', models.CharField(max_length=150, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('updater', models.CharField(max_length=150, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=512, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('in_size', models.IntegerField()),
                ('out_size', models.IntegerField()),
                ('test_in', models.BinaryField(null=True)),
                ('test_out', models.BinaryField(null=True)),
                ('number_problem', models.IntegerField(default=0)),
                ('meta_problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_data', to='rest_api.MetaProblem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompileInfo',
            fields=[
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='compile_info', serialize=False, to='rest_api.Submission')),
                ('info', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionCode',
            fields=[
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='code', serialize=False, to='rest_api.Submission')),
                ('code', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='TestDataStatus',
            fields=[
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='test_data_status', serialize=False, to='rest_api.Submission')),
                ('status', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submissions', to='rest_api.Client'),
        ),
        migrations.AddField(
            model_name='submission',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='rest_api.Environment'),
        ),
        migrations.AddField(
            model_name='submission',
            name='judge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='rest_api.Judge'),
        ),
        migrations.AddField(
            model_name='submission',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='rest_api.Problem'),
        ),
        migrations.AddField(
            model_name='problemtestdata',
            name='test_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems_rel', to='rest_api.TestData'),
        ),
        migrations.AddField(
            model_name='problem',
            name='judge',
            field=models.ManyToManyField(related_name='problem', through='rest_api.ProblemLimitJudge', to='rest_api.Judge'),
        ),
        migrations.AddField(
            model_name='problem',
            name='meta_problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='rest_api.MetaProblem'),
        ),
        migrations.AddField(
            model_name='problem',
            name='sample',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='rest_api.Sample'),
        ),
        migrations.AddField(
            model_name='problem',
            name='test_data',
            field=models.ManyToManyField(related_name='problems', through='rest_api.ProblemTestData', to='rest_api.TestData'),
        ),
        migrations.AddField(
            model_name='limit',
            name='judge',
            field=models.ManyToManyField(related_name='limit', through='rest_api.ProblemLimitJudge', to='rest_api.Judge'),
        ),
        migrations.AddField(
            model_name='limit',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='limits', to='rest_api.Problem'),
        ),
        migrations.AddField(
            model_name='invalidword',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invalid_words', to='rest_api.Problem'),
        ),
        migrations.AddField(
            model_name='description',
            name='meta_problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='rest_api.MetaProblem'),
        ),
        migrations.AddField(
            model_name='client',
            name='categories',
            field=models.ManyToManyField(related_name='clients', through='rest_api.ClientCategory', to='rest_api.Category'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categoryproblem',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_relations', to='rest_api.Problem'),
        ),
        migrations.AddField(
            model_name='category',
            name='problems',
            field=models.ManyToManyField(related_name='categories', through='rest_api.CategoryProblem', to='rest_api.Problem'),
        ),
    ]
