# from django.shortcuts import render
from fundraiser_app.models import FMItem
from fundraiser_app.forms import FMItemForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class FMItemListView(ListView):
    # if no template name is said here. The default one is fmitem_list.html. It is just
    # the first and second words lower cased and with an underscore
    model = FMItem

    # Define how I want to grab this list
    def get_queryset(self):
        # This allow us to deal with django ORMs (Object-related models)
        return FMItem.objects.order_by('name')

class FMItemDetailView(DetailView):
    model = FMItem

class FMItemCreateView(CreateView):
    model = FMItem
    form_class = FMItemForm
    redirect_field_name = 'fundraiser_app/fmitem_detail.html'

class FMItemUpdateView(UpdateView):
    model = FMItem
    form_class = FMItemForm
    redirect_field_name = 'fundraiser_app/fmitem_detail.html'

class FMItemDeleteView(LoginRequiredMixin, DeleteView):
    model = FMItem
    success_url = reverse_lazy('fmitem_list')
