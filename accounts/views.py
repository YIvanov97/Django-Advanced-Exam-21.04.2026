from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import RegisterForm, ProfileEditForm
from accounts.models import Profile


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/edit-profile.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )