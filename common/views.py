from django.shortcuts import render

from datetime import datetime
from django.views import View
from django.http import HttpResponse


class CurrentDateView(View):
    def get(self, request):
        # now = datetime.now()
        # html = f"{now.time()}"
        html = f"{datetime.now()}"
        return HttpResponse(html)


class HelloWorld(View):
    def get(self, request):
        html = f"<h1>Hello, World</h1>"
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')
