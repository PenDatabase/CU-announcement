from django.db.models import Q, Case, When, Value, IntegerField, F
from django.contrib.contenttypes.models import ContentType
from announcements.models import Announcement
from user.models import Organization, Staff


def announcement_search(keyword, announcment_type: str):
    filters = Q()

    # Base filters for search

    filters |= Q(title__icontains=keyword)
    filters |= Q(content__icontains=keyword)

    # Base cases for rank score
    cases = [
                Case(When(title__icontains=keyword, then=Value(3)), output_field=IntegerField()),
                Case(When(content__icontains=keyword, then=Value(1)),  output_field=IntegerField())
            ]


    if announcment_type == "official":
        StaffContentType = ContentType.objects.get_for_model(Staff)
        filtered_ids = Staff.objects.filter(office__icontains=keyword).values_list("id", flat=True)
        filters |= Q(announcer_type=StaffContentType) & Q(announcer_id__in=filtered_ids)
        cases.append(
            Case(
                    When(announcer_type=StaffContentType, 
                        announcer_id__in=filtered_ids, 
                        then=Value(3)), 
                    output_field=IntegerField()
                )
            )



    elif announcment_type == "event":
        OrganizationContentType = ContentType.objects.get_for_model(Organization)
        filtered_ids = Organization.objects.filter(name__icontains=keyword).values_list("id", flat=True)
        filters |= Q(announcer_type=OrganizationContentType) & Q(announcer_id__in=filtered_ids)
        cases.append(
            Case(
                    When(announcer_type=OrganizationContentType, 
                        announcer_id__in=filtered_ids, 
                        then=Value(3)), 
                    output_field=IntegerField()
                )
            )



    return Announcement.objects.filter(filters).annotate(
        rank_score = sum(cases)
    ).order_by("-rank_score")

