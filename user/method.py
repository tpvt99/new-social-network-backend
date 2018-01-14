from user.models import User

def get_user(request):
    user_pk = request.COOKIES.get('a')
    if user_pk:
        user_pk = int(user_pk)
    user_id = request.COOKIES.get('user')
    try:
        user = User.objects.get(pk = user_pk, user_id = user_id)
        return user
    except User.DoesNotExist:
        return False
