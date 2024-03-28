from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timedelta
from django.shortcuts import get_object_or_404


def get_duration(visit):
    if visit.leaved_at is None:
        visit_duration = localtime() - visit.entered_at
    else:
        visit_duration = visit.leaved_at - visit.entered_at
    return visit_duration


def format_duration(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return f"{hours}:{minutes}:{seconds}"


def is_visit_long(visit, minutes=60):
    one_hour_ago = localtime() - timedelta(hours=1)

    if visit.leaved_at is None and visit.entered_at < one_hour_ago:
        return True

    if visit.leaved_at is not None:
        visit_duration = visit.leaved_at - visit.entered_at
        duration_in_minutes = visit_duration.total_seconds() / 60
        if duration_in_minutes > minutes:
            return True
    return False


def passcard_info_view(request, passcode):
    # passcard = Passcard.objects.all()[0]
    # Программируем здесь
    owner_passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=owner_passcard)
    this_passcard_visits = []
    for visit in passcard_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': formatted_duration,
                'is_strange': is_visit_long(visit)
            },
        )
    context = {
        'passcard': owner_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
