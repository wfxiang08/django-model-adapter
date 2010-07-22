#!/usr/bin/env python
import os.path
import sys

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE="sqlite3",
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "model_adapter",
            "tests.test_app_one",
            "tests.test_app_two",
        ]
    )

from django.test.simple import run_tests

def runtests(*test_args):
    if not test_args:
        test_args = ["tests"]
    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])
