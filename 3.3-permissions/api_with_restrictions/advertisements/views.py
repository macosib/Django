from rest_framework import status
from rest_framework.response import Response
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
    def add_to_favorites(self, request, pk=None):
        if request.data.get('creator') is not None and self.request.user.id == request.data.get('creator').get('id'):
            return Response({'Автор не может добавить свою статью в избранное'})
        if len(AdvertisementFavorites.objects.filter(user=request.user, advertisement=pk)) == 0:
            favorite = AdvertisementFavorites.objects.create(user=request.user, advertisement=self.get_object())
            serializer = AdvertisementFavoritesSerializer(favorite)
            return Response(serializer.data)
        else:
            return Response({'Уже есть в избранном'})

    def get_permissions(self):
        if self.request.user.is_staff:
            return [IsAdminUser()]
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy", "add_to_favorites"]:
            return [IsOwnerOrReadOnlyPermission()]
        return []


class AdvertisementFavoritesViewSet(ModelViewSet):
    queryset = AdvertisementFavorites.objects.all()
    serializer_class = AdvertisementFavoritesSerializer

