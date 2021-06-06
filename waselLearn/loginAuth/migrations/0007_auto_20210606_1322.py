# Generated by Django 3.2.3 on 2021-06-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginAuth', '0006_user_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='planePassword',
            field=models.CharField(default='oldpassesforall', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.CharField(choices=[('physics', 'physics'), ('chemistry', 'chemistry'), ('english', 'english'), ('mathematics', 'mathematics'), ('arabic', 'arabic'), ('biology', 'biology'), ('art', 'art'), ('music', 'music'), ('history', 'history')], max_length=25, null=True),
        ),
    ]
