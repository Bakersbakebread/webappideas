from django.http import HttpResponseRedirect
from .models import Idea, Submission
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import NewIdeaSubmissionForm
from django.db.models import Count

class IdeasList(ListView):
    model = Idea
    queryset = Idea.objects.annotate(number_of_submissions=Count('submissions'))

class IdeaDetail(DetailView):
    model = Idea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submissions'] = Submission.objects.filter(
            idea__pk=self.object.id).all()
        return context


class SubmissionCreate(CreateView):
    template_name = 'ideas/submission_form.html'
    form_class = NewIdeaSubmissionForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        idea = Idea.objects.get(slug=self.kwargs.get('slug'))
        self.object.idea = idea
        self.object.save()
        return HttpResponseRedirect(
            reverse_lazy('idea-detail',args=[self.object.idea.slug]))

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs['idea'] = Idea.objects.get(slug=self.kwargs.get('slug'))
        kwargs['author'] = self.request.user
        print('kwargs::', kwargs)
        return kwargs