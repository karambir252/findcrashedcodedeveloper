"""Script to send a dummy crash to sentry

- Install sentry_sdk - pip install sentry_sdk
- Set SENTRY_DSN environment variable from sentry project

How to use?
- python dummmycrash.py
- python dummycrash.py none
"""

import os
import sys
import sentry_sdk

sentry_sdk.init(dsn=os.environ['SENTRY_DSN'])


def divide(a, b):
    return a / b


def zero_division_crash():
    a = 0
    b = 100
    c = divide(b, a)


def get_value(a):
    return a.value


def aggregate_value(a):
    return get_value(a)


def none_type_crash():
    a = None
    return aggregate_value(a)


def main():
    if len(sys.argv) > 1:
        crash_type = sys.argv[1]
    else:
        crash_type = None

    if crash_type == 'none':
        none_type_crash()
    else:
        zero_division_crash()


if __name__ == '__main__':
    main()
