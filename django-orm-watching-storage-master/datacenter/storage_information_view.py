from datacenter.models import Visit
from django.shortcuts import render
from datacenter.time_visits_api import get_duration, format_duration


def storage_information_view(request):
    incomplete_visits = Visit.objects.filter(entered_at__isnull=False,
                                             leaved_at__isnull=True)
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
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
