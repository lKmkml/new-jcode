from django.http import JsonResponse
from django.views import View
from video.models import Video

class VideoAutocompleteView(View):
    def get(self, request):
        query = request.GET.get('query')
        videos = Video.objects.filter(name__icontains=query)
        data = []
        for video in videos:
            item = {'id': video.id, 'name': video.name, 'price': video.price}
            data.append(item)
        return JsonResponse(data, safe=False)