import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView

from app.forms.order import OrderForm
from app.models import Order
from app.utils.order import order_stage, state_status


@method_decorator(login_required, name="dispatch")
class OrderView(View):
    template_name = "app/order/order.html"

    def get(self, request, state):
        context = {
            "state": order_stage(state),
            "status": state_status(state),
        }

        return render(
            request=request, template_name=self.template_name, context=context
        )


@method_decorator(login_required, name="dispatch")
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "app/order/form.html"
    success_url = reverse_lazy("delivery", args=["all"])


@method_decorator(login_required, name="dispatch")
class OrderAPIView(View):
    def post(self, request):
        print(request.POST)
        post_data = request.POST.dict()
        print(json.dumps(post_data, indent=4))

        status = request.POST.get("status")
        state = request.POST.get("state")
        draw = int(request.POST.get("draw"))
        start = int(request.POST.get("start"))
        length = request.POST.get("length")
        search = request.POST.get("search[value]")
        order_column = request.POST.get("order[0][column]")
        order_by = request.POST.get("order[0][dir]")

        column = request.POST.get(f"columns[{order_column}][data]")

        print(
            status, state, draw, start, length, search, order_column, order_by, column
        )

        return JsonResponse({"status": "success"})
