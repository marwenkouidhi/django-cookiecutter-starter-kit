from django.urls import include, path

urlpatterns = [
    path(
        "auth/",
        include(
            ("{{cookiecutter.project_slug}}.authentication.urls", "authentication")
        ),
    ),
    path("users/", include(("{{cookiecutter.project_slug}}.users.urls", "users"))),
    path("errors/", include(("{{cookiecutter.project_slug}}.errors.urls", "errors"))),
    path("files/", include(("{{cookiecutter.project_slug}}.files.urls", "files"))),
]
