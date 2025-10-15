from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name="dispatch")
class DashboardView(View):
    template_name = "app/dashboard.html"

    def get(self, request):
        context = {
            "title": "Dashboard",
        }

        return render(
            request=request, template_name=self.template_name, context=context
        )
