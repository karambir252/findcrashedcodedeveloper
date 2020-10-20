def test_get_issues(sentry_api):
    issues = sentry_api.issues.get_list(
        'karambir2522', 'karambir2522'
    )

    issues_titles = set(
        issue.title for issue in issues
    )

    assert "AttributeError: 'NoneType' object has no attribute 'value'" in issues_titles
    assert 'ZeroDivisionError: division by zero' in issues_titles