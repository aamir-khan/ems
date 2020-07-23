# Generated by Django 2.0.13 on 2020-07-23 10:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_pic', models.FileField(upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'permissions': (('CAN_VIEW_UserProfile', 'Can View UserProfile'),),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalLedger',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('type', models.CharField(choices=[('EXPENSE_ADVANCE', 'Expense_or_advance'), ('SALARY', 'Salary')], max_length=50)),
                ('expense_date', models.DateField()),
                ('amount', models.FloatField()),
                ('notes', models.TextField(null=True)),
                ('hours', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('hourly_rate', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('trade', models.CharField(blank=True, max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ledger',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('EXPENSE_ADVANCE', 'Expense_or_advance'), ('SALARY', 'Salary')], max_length=50)),
                ('expense_date', models.DateField()),
                ('amount', models.FloatField()),
                ('notes', models.TextField(null=True)),
                ('hours', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('hourly_rate', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('trade', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ('-expense_date', 'user', 'type'),
                'permissions': (('CAN_VIEW_Ledger', 'Can View Ledger'),),
            },
        ),
        migrations.CreateModel(
            name='TimeSheetMonthlyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('work_month', models.DateField()),
                ('time_sheet_file', models.FileField(upload_to='')),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'permissions': (('CAN_VIEW_TimeSheetMonthlyRecord', 'Can View TimeSheetMonthlyRecord'),),
            },
        ),
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('document_type', models.CharField(choices=[('Passport', 'PASSPORT'), ('Visa', 'VISA'), ('Labour card', 'LABOUR_CARD'), ('Emirates ID', 'EMIRATES_ID'), ('Home country ID', 'HOME_COUNTRY_ID')], max_length=550)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=512)),
                ('issued_by', models.CharField(blank=True, max_length=256)),
                ('issued_date', models.DateField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('image', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('CAN_VIEW_UserDocument', 'Can View UserDocument'),),
            },
        ),
        migrations.CreateModel(
            name='WorkSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=550)),
                ('location', models.CharField(max_length=550)),
            ],
            options={
                'permissions': (('CAN_VIEW_WorkSite', 'Can View WorkSite'),),
            },
        ),
        migrations.AddField(
            model_name='timesheetmonthlyrecord',
            name='work_site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.WorkSite'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='time_sheet_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.TimeSheetMonthlyRecord'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledgers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalledger',
            name='time_sheet_record',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='users.TimeSheetMonthlyRecord'),
        ),
        migrations.AddField(
            model_name='historicalledger',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
