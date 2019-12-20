from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from apiChug.serializers import WalletSerializer
from wallet.models import Wallet
from cryptos import Bitcoin, sha256, entropy_to_words
import qr_code

def wallet(request):
    return render(request, 'wallet.html')

@csrf_exempt
def wallet_list(request):
    """
    List all wallets, or create a new wallet.
    """
    if request.method == 'GET':
        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WalletSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def wallet_detail(request, pk):
    """
    Retrieve, update or delete a code wallet.
    """
    try:
        wallet = Wallet.objects.get(pk=pk)
    except wallet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WalletSerializer(wallet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WalletSerializer(wallet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        wallet.delete()
        return HttpResponse(status=204)


#blockcypher block explorer
def qr_addr(addr):
    data = "https://live.blockcypher.com/btc-testnet/address/"+ addr
    return data

#queries user's privkey to return public key and generate QR to explorer
def address(request):
    context = {}
    query = list(Wallet.objects.filter(user_id = getattr(request.user, "pk")).values_list("privkey"))
    priv = [key[0] for key in query]
    c = Bitcoin(testnet=True)
    addr = c.pubtoaddr(c.privtopub(priv[0]))
    qr = qr_addr(addr)
    context['qr'] = qr
    context['address'] = addr
    return render(request, "wallet.html", context)
