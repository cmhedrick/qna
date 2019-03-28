from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.views import generic

from qna_app import models, forms

class RedirectView(generic.RedirectView):
    permanent = False


class IndexPageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        return context
