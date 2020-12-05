from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserMixin(UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_authenticated and self.request.user.is_superuser


class IsOwnerOrReadOnly(BasePermission):
	message = 'permission denied, you\'re not the owner'

	def has_permission(self, request, view):
		return request.user.is_authenticated and request.user

	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		return obj.user == request.user
