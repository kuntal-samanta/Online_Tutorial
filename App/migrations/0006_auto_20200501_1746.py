# Generated by Django 2.2 on 2020-05-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_aboutcms_basecms_comments_contactus_coursecms_courses_coverphoto_homecms_portfolio_screenshots_subsc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]