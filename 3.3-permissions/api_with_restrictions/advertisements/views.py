from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permission import IsOwnerOrReadOnlyPermission
from advertisements.serializers import AdvertisementSerializer
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.request.user.is_staff:
            return [IsAdminUser()]
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnlyPermission()]
        return []
