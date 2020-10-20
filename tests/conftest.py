import os
import pytest
from findcrashedcodedeveloper.githubapi import GithubAPI
from findcrashedcodedeveloper.sentryapi import SentryAPI
from findcrashedcodedeveloper.githubapi.models.repository import GithubRepository


@pytest.fixture
def github_api():
    GITHUB_API_TOKEN = os.environ.get('TEST_GITHUB_API_KEY')
    message = 'Please set environment variable TEST_GITHUB_API_KEY to make api calls to github'
    assert GITHUB_API_TOKEN, message
    return GithubAPI(GITHUB_API_TOKEN)


@pytest.fixture
def sentry_api():
    SENTRY_API_TOKEN = os.environ.get('TEST_SENTRY_API_KEY')
    message = 'Please set environment variable TEST_SENTRY_API_KEY to make api calls to sentry'
    assert SENTRY_API_TOKEN, message
    return SentryAPI(SENTRY_API_TOKEN)


@pytest.fixture
def dummy_repository():
    return GithubRepository('karambir252', 'findcrashedcodedeveloper')
