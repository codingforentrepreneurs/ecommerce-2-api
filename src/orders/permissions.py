from rest_framework.permissions import BasePermission



class IsOwnerAndAuth(BasePermission):
	def has_object_permission(self, request, view, obj):
		try:
			return obj.user.user == request.user
		except:
			return False


	def has_permission(self, request, view):
		if request.user and request.user.is_authenticated():
			return True
		return False