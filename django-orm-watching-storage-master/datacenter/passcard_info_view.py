from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.time_visits_functions import (get_duration, format_duration,
                                              is_visit_long)


def passcard_info_view(request, passcode):
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
