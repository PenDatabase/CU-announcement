from django.shortcuts import redirect, render
# from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .models import Announcement

# Create your views here.


def home(request):
    official_annoucement = Announcement.objects.select_related("announcer_type").filter(category="Official").first()
    event_announcement = Announcement.objects.select_related("announcer_type").filter(category="Events").first()
    context = {
        "official": official_annoucement,
        "event": event_announcement
    }
    return render(request, "announcements/home.html", context)




def official(request):
    official_announcement = Announcement.objects.filter(category="Official").all().select_related("announcer_type")
    return render(request, "announcements/official.html", {"announcements": official_announcement})




def official_search(request):
    pass
    # keyphrase = request.GET.get("search_phrase")
    # results = Announcement.objects.none()
    # if keyphrase:
    #     vector = (
    #         SearchVector('title', weight="A") +
    #         SearchVector('announcer__office', weight="A") +
    #         SearchVector('content', weight="B")
    #         )
    #     search_query = SearchQuery(keyphrase)

    #     results = Announcement.objects.annotate(
    #         rank=SearchRank(vector, search_query)
    #     ).filter(rank__gte=0.1).order_by('-rank')
    #     return render(request,
    #                   "announcements/official.html", 
    #                   {"announcements": results,
    #                    "result_count": results.count()}
    #                    )
    
    # return render(request,
    #                   "announcements/official.html", 
    #                   {"announcements": results,
    #                    "result_count": results.count()}
    #                    )
