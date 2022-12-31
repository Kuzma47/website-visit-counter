def parse_platform(headers):
    if 'iPhone' in headers:
        return 'iOS'
    if 'Android' in headers:
        return 'Android'
    if 'Windows NT' in headers:
        return 'Windows'
    if 'Macintosh' in headers:
        return 'Macintosh'
    return 'Linux'


def parse_browser(headers):
    if 'OPR' in headers or 'Opera' in headers:
        return 'Opera'
    if 'Edg' in headers:
        return 'Edge'
    if 'Firefox' in headers:
        return 'Firefox'
    if 'Safari' in headers and 'Chrome' not in headers:
        return 'Safari'
    return 'Chrome'
