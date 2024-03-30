from django.utils.timezone import localtime

SECONDS_IN_THE_HOUR = 3600
HOURS_IN_THE_DAY = 24
SECONDS_IN_THE_MINUTE = 60


def get_duration(visit):
    if visit.leaved_at:
        visit_duration = visit.leaved_at - visit.entered_at
    else:
        visit_duration = localtime() - visit.entered_at
    return visit_duration


def format_duration(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * HOURS_IN_THE_DAY + seconds // SECONDS_IN_THE_HOUR
    minutes = (seconds % SECONDS_IN_THE_HOUR) // SECONDS_IN_THE_MINUTE
    seconds = (seconds % SECONDS_IN_THE_MINUTE)
    return f"{hours}:{minutes}:{seconds}"


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit).total_seconds()
    suspicious_time = minutes * 60

    return duration > suspicious_time
