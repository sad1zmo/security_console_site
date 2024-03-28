from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


incomplete_visits = Visit.objects.filter(entered_at__isnull=False,
                                         leaved_at__isnull=True)


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


def storage_information_view(request):
    non_closed_visits = []
    for incomplete_visit in incomplete_visits:
        duration = get_duration(incomplete_visit)
        formatted_duration = format_duration(duration)

        non_closed_visits.append(
            {
                'who_entered': incomplete_visit.passcard.owner_name,
                'entered_at': incomplete_visit.entered_at,
                'duration': formatted_duration,
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
