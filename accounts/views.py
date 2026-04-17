from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import RegisterForm, ProfileEditForm, UserDeleteForm, ProfileDeleteForm, LoginForm
from accounts.models import Profile, AppUser
from cart.utils import merge_session_cart_into_user_cart


class AppLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        merge_session_cart_into_user_cart(self.request, self.request.user)
        return response

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        users_group, _ = Group.objects.get_or_create(name="Users")
        self.object.groups.add(users_group)
        return response

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-page.html'

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/edit-profile-page.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        return reverse(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )

class RemoveProfilePictureView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.pk == self.kwargs["pk"]

    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=self.kwargs["pk"])

        if profile.profile_picture:
            profile.profile_picture.delete(save=False)
            profile.profile_picture = None
            profile.save()

        return redirect("edit-profile", pk=profile.pk)

class DeleteUserView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AppUser
    form_class = UserDeleteForm
    template_name = 'accounts/delete-profile-page.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_form = self.form_class(instance=self.object)
        context['user_form'] = user_form
        context['profile_form'] = ProfileDeleteForm(instance=self.object.profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        logout(request)
        self.object.delete()
        return redirect('home-page')