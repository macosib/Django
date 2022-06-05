from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, AdvertisementFavorites
from advertisements.permission import IsOwnerOrReadOnlyPermission
from advertisements.serializers import AdvertisementSerializer, AdvertisementFavoritesSerializer
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    @action(detail=True, methods=['post'])
    def recent_users(self, request, pk=None):
        print(self)
        recent_users = Advertisement.objects.filter(id=request)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(recent_users, many=True)
        # return Response(serializer.data)
        page = self.paginate_queryset(recent_users)




    # def get_permissions(self):
    #     if self.request.user.is_staff:
    #         return [IsAdminUser()]
    #     if self.action == "create":
    #         return [IsAuthenticated()]
    #     if self.action in ["update", "partial_update", "destroy"]:
    #         return [IsOwnerOrReadOnlyPermission()]
    #     return []


class AdvertisementFavoritesViewSet(ModelViewSet):
    queryset = AdvertisementFavorites.objects.all()
    serializer_class = AdvertisementFavoritesSerializer

    # def get_permissions(self):
    #     if self.request.user.is_staff:
    #         return [IsAdminUser()]
    #     if self.action == "create":
    #         return [IsAuthenticated()]
    #     if self.action in ["update", "partial_update", "destroy"]:
    #         return [IsOwnerOrReadOnlyPermission()]
    #     return []