from django.shortcuts import render

# Create your views here.


def home(request):
    import requests
    import json

    # grab crypto prices
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,USD")
    # convert api request into json object, easy to work with
    price_api = json.loads(price_request.content)

    # grab crypto news
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    # convert api request into json object, easy to work with
    api = json.loads(api_request.content)
    # render request and pass to home.html page, also can pass in further arguments, returning json object
    return render(request, 'home.html', {'api': api, 'price_api': price_api})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = "Enter a crypto currency symbol into the form above..."
        return render(request, 'prices.html', {'notfound': notfound})
