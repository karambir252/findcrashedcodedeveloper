def test_get_latest_event(sentry_api):
    issues = sentry_api.issues.get_list(
        'karambir2522', 'karambir2522'
    )

    crashed_line_code = {
        'ZeroDivisionError: division by zero': '    return a / b',
        "AttributeError: 'NoneType' object has no attribute 'value'": '    return a.value'
    }

    for issue in issues:
        if issue.title not in crashed_line_code:
            continue
        event = sentry_api.events.get_latest_event(issue.id)
        assert event.get_crashed_line_code() == crashed_line_code[issue.title]
