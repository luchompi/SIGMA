from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Home(LoginRequiredMixin,TemplateView):
    login_url='/auth/login'
    template_name = "Home/index.html"

class error(LoginRequiredMixin,TemplateView):
    template_name="base/404.html"

class Error500(TemplateView):
    template_name="base/500.html"
    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view
