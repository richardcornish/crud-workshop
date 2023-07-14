from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from django.urls import reverse_lazy


from .forms import PollForm
from .models import Poll


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm


class PollDeleteView(DeleteView):
    model = Poll
    success_url = reverse_lazy("poll_list")


class PollUpdateView(UpdateView):
    model = Poll
    form_class = PollForm


class PollDetailView(DetailView):
    model = Poll


class PollListView(ListView):
    model = Poll
