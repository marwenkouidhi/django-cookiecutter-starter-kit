from django.apps import AppConfig


class TestingExamplesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.project_slug}}.testing_examples"
