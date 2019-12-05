from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from initiative.models import Initiative
from initiative.forms import InitiativeForm
from django.utils import timezone


class InitiativeView(LoginRequiredMixin, views.View):
    def get(self, request):
        initiatives = Initiative.objects.all()
        return render(
            request,
            "initiative.html",
            {"initiatives": initiatives, "form": InitiativeForm()},
        )

    def post(self, request):
        form = InitiativeForm(request.POST)
        initiatives = Initiative.objects.all()
        if form.is_valid():
            Initiative.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                # visual=form.cleaned_data["visual"],
                team_leader=request.user,
                date=timezone.now(),
            )
            return redirect("initiatives:create")
        else:
            return render(
                request, "initiative.html", {"initiatives": initiatives, "form": form}
            )

