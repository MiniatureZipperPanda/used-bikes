from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, TemplateView, ListView, DetailView, DeleteView, UpdateView
from seller.models import Bikes
from seller.forms import SellerForm
from seller.forms import SignUpForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class SellerHomeView(TemplateView):
    template_name = "sl-home.html"


# sign up
class SignUpView(CreateView):
    model = Bikes
    form_class = SignUpForm
    template_name = "user-signup.html"
    success_url = reverse_lazy("list-bikes")


# sign in
class SignInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("user_name")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request, user)

                return redirect("list-bikes")
            else:
                return render(request, "login.html", {"form": form})


# ////////////  SIGN OUT  \\\\\\\\
def sign_out_view(request, *args, **kwargs):
    logout(request)
    return redirect("sign-in")


class AddBikeView(CreateView):
    model = Bikes
    form_class = SellerForm
    template_name = "add-bike.html"
    success_url = reverse_lazy("list-bikes")


class ListBikeView(ListView):
    model = Bikes
    context_object_name = "bikes"
    template_name = "list-bike.html"


class DetailBikeView(DetailView):
    model = Bikes
    context_object_name = "bike"
    template_name = "details-bike.html"
    pk_url_kwarg = "id"


class EditBikeView(UpdateView):
    model = Bikes
    form_class = SellerForm
    template_name = "edit-bike.html"
    success_url = reverse_lazy("list-bikes")
    pk_url_kwarg = "id"


class DeleteBikeView(DeleteView):
    model = Bikes
    template_name = "delete-bike.html"
    success_url = reverse_lazy("list-bikes")
    pk_url_kwarg = "id"


class ChangePassword(TemplateView):
    template_name = "change-password.html"

    def post(self, request, *args, **kwargs):
        pwd = request.POST.get("pwd")
        uname = request.user
        user = authenticate(request, username=uname, password=pwd)
        if user:
            return redirect("password-reset")
        else:
            return render(request, self.template_name)


class PasswordReset(TemplateView):
    template_name = "password-reset.html"

    def post(self, request, *args, **kwargs):
        password1 = request.POST.get("pwd1")
        password2 = request.POST.get("pwd1")
        if password1 != password2:
            return render(request, self.template_name, {"msg": "Password Mismatch"})
        else:
            u = User.objects.get(username=request.user)
            u.set_password(password2)
            u.save()
            return redirect("sign-in")
