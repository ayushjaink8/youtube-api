from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from backend.serializers import UserSerializer, GroupSerializer, YoutubeDataSerializer
from backend.models import YoutubeData
from backend.services.fetch_youtube import getnewposts

from rest_framework.pagination import PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]

# Hit this function to fetch the data. This will trigger getnewposts() to fetch
# and store data asynchronously.
def fetch_data_from_youtube(request):
    try:
        getnewposts()
        return HttpResponse("New videos fetched successfully!")
    except:
        return HttpResponse("Some error occurred.")


class YoutubeDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that fetched data from youtube based on a
    pre-defined query.
    """
    queryset = YoutubeData.objects.all().order_by('-published_datetime')
    serializer_class = YoutubeDataSerializer
    pagination_class = PageNumberPagination
