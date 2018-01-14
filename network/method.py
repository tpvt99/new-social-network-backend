from network.models import NetworkAccount

def get_network_account(request):
    nu = request.COOKIES.get('nu')
    if nu:
        try:
            network_account = NetworkAccount.objects.get(network_id = nu)
            return network_account
        except NetworkAccount.DoesNotExist:
            return False

