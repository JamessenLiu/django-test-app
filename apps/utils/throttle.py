from rest_framework.throttling import UserRateThrottle


class UserThrottle(UserRateThrottle):

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.username
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }