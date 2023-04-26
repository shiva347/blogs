from rest_framework import viewsets
from . import constants


class BaseViewSet(viewsets.ModelViewSet):
    filterset_class = None
    dynamic_serializers = {}

    def get_serializer_class(self):
        serializer_dict = self.dynamic_serializers

        if not serializer_dict:
            return self.serializer_class

        request_action = self.action

        if request_action in [constants.Action.CREATE, constants.Action.UPDATE]:
            return serializer_dict[request_action]
        else:
            return serializer_dict[constants.Action.LIST]

