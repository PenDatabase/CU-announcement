from django.shortcuts import render
from django.http import Http404
from .utils import announcement_search
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




def search_announcements_view(request, page):
    search_phrase = request.GET.get("search_phrase").strip()
    announcements = announcement_search(search_phrase, page)
    if page == "official":
        return render(request, "announcements/official.html", {"announcements": announcements})
    # elif page == "event":
    #     return render(request, )
    else:
        return Http404("This is a wrong url")