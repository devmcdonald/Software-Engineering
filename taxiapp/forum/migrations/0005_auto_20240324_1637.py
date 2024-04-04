# Generated by Django 5.0.2 on 2024-03-24 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def add_category_data(apps, schema_editor):
    Category = apps.get_model("forum", "Category")
    categories = ["Experience", "Question", "Concern", "News", "Other"]
    for cat in categories:
        Category.objects.create(name=cat)


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0004_category_alter_post_content_alter_post_title_and_more"),
    ]

    operations = [
        migrations.RunPython(add_category_data),
    ]
