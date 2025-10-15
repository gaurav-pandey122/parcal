from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView

from app.forms.store import StoreForm
from app.models import Store


@method_decorator(login_required, name="dispatch")
class StoreListView(View):
    template_name = "app/store/list.html"

    def get(self, request):
        stores = Store.objects.for_user(request.user)

        context = {
            "stores": stores,
        }
        return render(request, self.template_name, context=context)


@method_decorator(login_required, name="dispatch")
class StoreCreateView(CreateView):
    model = Store
    form_class = StoreForm
    template_name = "app/store/form.html"
    success_url = reverse_lazy("stores")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


@method_decorator(login_required, name="dispatch")
class StoreUpdateView(UpdateView):
    model = Store
    form_class = StoreForm
    template_name = "app/store/form.html"
    success_url = reverse_lazy("stores")

    def get_queryset(self):
        return Store.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


@method_decorator(login_required, name="dispatch")
class StoreDeleteView(View):
    def post(self, request, pk):
        try:
            store = Store.objects.get(id=pk)

            store.delete()

            return JsonResponse({"success": True})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
