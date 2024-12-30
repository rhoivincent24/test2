from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Event,Resource
from django.urls import reverse_lazy
from .forms import ResourceForm
from django.views.generic import ListView
from .models import Resource
from django.contrib import messages


class ResourceListView(ListView):
    model = Resource
    template_name = 'app/content.html'  # Use 'content.html' for listing videos
    context_object_name = 'resources'


# Detail View to display a single resource
class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'app/resource_detail.html'
    context_object_name = 'resource'

class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'app/resource_form.html'
    success_url = reverse_lazy('resource_list')  # Redirect to /resources/ after creation

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Resource "{self.object.name}" was created successfully!')
        return response
# Update View to edit an existing resource
class ResourceUpdateView(UpdateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'app/resource_form.html'
    success_url = reverse_lazy('resource_list')  # Redirect after updating a resource

# Delete View to delete a resource
class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = 'app/resource_confirm_delete.html'
    success_url = reverse_lazy('resource_list')  # Redirect after deleting a resource

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContentPageView(TemplateView):
    template_name = 'app/content.html'

class ResourcesPageView(TemplateView):
    template_name = 'app/resources.html'

class CommunityPageView(TemplateView):
    template_name = 'app/community.html'

class EventsPageView(TemplateView):
    template_name = 'app/events.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

class LoginPageView(TemplateView):
    template_name = 'app/login.html'
