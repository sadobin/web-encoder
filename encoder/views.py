from django.shortcuts import render
from encoder.src.Encoder import Encoder

# Create your views here.

DATA = {
    'title': 'Encoder',
}

def homepage(request):

    return render(request, 'homepage.html', DATA)


def result(request):

    if request.method == "GET":
        return render(request, 'homepage.html', DATA)

    else:
        string = request.POST["string"]
        chars = request.POST["chars"]

        all_chars = False
        desired_chars = ""

        if chars == "all_chars":
            all_chars = True
        elif chars == "desired_chars":
            desired_chars = request.POST["desired_chars"]
        else:
            return render(request, 'homepage.html', DATA)


        encoder = Encoder(string, desired_chars, all_chars)
        result = encoder.get_result()

        DATA['string'] = string
        DATA['bin'] = result[string]['bin']
        DATA['hex'] = result[string]['hex']
        DATA['url'] = result[string]['url']
        DATA['unicode'] = result[string]['unicode']
        DATA['html_dec'] = result[string]['html_dec']
        DATA['html_hex'] = result[string]['html_hex']
        DATA['base64'] = result[string]['base64']


    return render(request, 'result.html', DATA)