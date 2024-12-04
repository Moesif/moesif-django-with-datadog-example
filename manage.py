#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from ddtrace import patch_all, tracer
from custom_writer import ConsoleWriter

patch_all()
# Set the custom writer to log traces to the console for easier debugging
# but you can use any writer you want after verify writing to console works.
tracer.configure(writer=ConsoleWriter())


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jandog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
