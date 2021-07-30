from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Experience, ExperienceDescription
from .forms import ExperienceForms, ExperienceDescriptionFormSet, ExperienceFormSet
from resumes.models import Resume
from django.contrib import messages


class ExperienceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'experience_form.html'
    success_message = "Experience was created successfully"

    def get(self, *args, **kwargs):
        form = ExperienceForms()
        formset = ExperienceDescriptionFormSet(queryset=ExperienceDescription.objects.none())
        return self.render_to_response({'form': form, 'formsets': formset})

    def post(self, *args, **kwargs):
        form = ExperienceForms(data=self.request.POST)
        formset = ExperienceDescriptionFormSet(data=self.request.POST)
        if form.is_valid() and formset.is_valid():
            instance = form.save(commit=False)
            resume_id = self.kwargs['pk']
            instance.resume = Resume.objects.get(id=resume_id)
            instance.save()
            description_instances = formset.save(commit=False)
            for description_instance in description_instances:
                resume_id = self.kwargs['pk']
                description_instance.experience = Experience.objects.get(resume_id=resume_id)
                description_instance.save()
            form.save()
            formset.save()
            return redirect(reverse_lazy('skills:create_skill', kwargs={'pk': self.kwargs['pk']}))
        return self.render_to_response({'form': form, 'formsets': formset})


class ExperienceUpdateView(LoginRequiredMixin, UpdateView):
    model = Experience
    template_name = 'experience_update.html'
    success_url = reverse_lazy('resumes:resumes',)
    success_message = "Experience was updated successfully"

    def get(self, *args, **kwargs):
        formset = ExperienceFormSet(queryset=Experience.objects.filter(resume_id=self.kwargs['pk']))
        return self.render_to_response({'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = ExperienceFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            messages.success(self.request, self.success_message)
            return redirect(reverse_lazy('resumes:resumes'))
        return self.render_to_response({'formset': formset})


class ExperienceListView(LoginRequiredMixin, ListView):
    model = Experience
    template_name = 'experience_list.html'