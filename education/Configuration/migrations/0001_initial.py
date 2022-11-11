# Generated by Django 3.1.8 on 2022-11-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('age', models.IntegerField(null=True, verbose_name='Age')),
                ('phone', models.CharField(max_length=10, null=True, verbose_name='Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('registration_date', models.DateField(verbose_name='Registration Date')),
                ('qualification', models.CharField(max_length=200, verbose_name='Qualification')),
                ('introduction_brief', models.CharField(max_length=200, verbose_name='Introduction brief')),
                ('image', models.ImageField(blank=True, null=True, upload_to='picture')),
                ('num_of_published_course', models.IntegerField(null=True, verbose_name='Published course')),
                ('num_of_enrolled_student', models.IntegerField(null=True, verbose_name='Enrolled student')),
                ('average_review_rating', models.IntegerField(blank=True, null=True, verbose_name='Rating')),
                ('num_of_reviews', models.IntegerField(blank=True, null=True, verbose_name='Reviews')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('age', models.IntegerField(null=True, verbose_name='Age')),
                ('phone', models.CharField(max_length=10, null=True, verbose_name='Phone')),
                ('qualification', models.CharField(max_length=200, verbose_name='Qualification')),
                ('specialized', models.CharField(max_length=50, verbose_name='Specialized')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('parent_phone_no', models.CharField(max_length=10, null=True, verbose_name='Parent Phone')),
                ('registration_date', models.DateField(verbose_name='Registration Date')),
                ('num_of_courses_enrolled', models.IntegerField(null=True, verbose_name='enrolled course')),
                ('num_of_courses_complete', models.IntegerField(null=True, verbose_name='complete course')),
            ],
        ),
    ]
