from .utils.order import ORDER_STAGE
from .utils.profile import has_complete_register


def app_setting(request):
    return {
        "app_setting": {
            "name": "SmartParcel",
            "logo_lg": "assets/images/logo-dark.png",
            "logo_sm": "assets/images/logo-sm.png",
            "favicon": "assets/images/favicon.png",
        },
        "delivery_status": ORDER_STAGE,
        "has_complete_register": has_complete_register(request),
    }
