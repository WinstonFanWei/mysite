from django.shortcuts import redirect
from django.urls import reverse
import re

class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        path = request.path
        urllist = ['/myadmin/myadmin_login', '/myadmin/myadmin_dologin', '/myadmin/myadmin_logout']
        if re.match(r'^/myadmin', path) and (path not in urllist):
            if 'adminuser' not in request.session:
                return redirect(reverse("myadmin_login"))
        response = self.get_response(request)
        return response