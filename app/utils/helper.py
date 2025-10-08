from app.models import Store


def has_complete_register(request):
    user = request.user
    if not user.is_authenticated:
        return False

    stores = Store.objects.filter(user=user)

    if not stores.exists():
        return False

    return True
