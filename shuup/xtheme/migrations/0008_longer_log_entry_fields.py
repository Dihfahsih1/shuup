# Generated by Django 2.2.17 on 2021-01-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_xtheme', '0007_add_modified_on_for_view_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='snippet_type',
            field=models.CharField(choices=[('inline_js', 'Inline JavaScript'), ('inline_css', 'Inline CSS'), ('inline_html', 'Inline HTML'), ('inline_jinja_html', 'Inline Jinja HTML')], max_length=20, verbose_name='snippet type'),
        ),
    ]