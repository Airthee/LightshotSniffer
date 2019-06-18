# *-* coding: utf8
import urllib.request
import re
import requests
import sys

# from PIL import Image
# from io import BytesIO


class Downloader:
    def __init__(self):
        pass

    @classmethod
    def downloadById(static, id):
        url = "https://prnt.sc/{}".format(id)
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"
            },
        )
        httpResponse = urllib.request.urlopen(request)
        if httpResponse.getcode() == 200:
            responseBody = httpResponse.read()
            resultSearch = re.search(
                b"src=[\"']([:\.\w\/]+\.(?:png|jpe?g|bmp))[\"']", responseBody
            )
            if resultSearch:
                urlImage = resultSearch.group(1)
                print("Image trouvée : {}".format(urlImage.decode("utf-8")))
                return urlImage
