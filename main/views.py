from django.views.generic import TemplateView
from django.views.generic import DetailView
from main.utils import get_random_choice
from main.models import Epos, Manaschi, Researchers


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        context_data['epos_list'] = Epos.objects.all()
        context_data['manaschi_list'] = Manaschi.objects.all()
        context_data['researchers_list'] = Researchers.objects.all()

        return context_data

class EposDetailView(DetailView):
    model = Epos
    template_name = "main/epos_detail.html"
    context_object_name = "epos"

class ManaschiDetailView(DetailView):
    model = Manaschi
    template_name = "main/manaschi_detail.html"
    context_object_name = "manaschi"

class ResearchersDetailView(DetailView):
    model = Researchers
    template_name = "main/researchers_detail.html"
    context_object_name = "researchers"

class MuxtarView(TemplateView):
    template_name = "main/muxtar.html"

