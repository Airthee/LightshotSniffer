#*-* coding: utf8

import sys
import generator
import urllib.request
import re
import requests
from PIL import Image         
from io import BytesIO     

def main():
    letters = "0123456789abcdefghijklmnopqrstuvwxyz"

    # Get arguments values
    startVal = getArgumentValue("--start", "zzzzzz")
    endVal = getArgumentValue("--end", "000000")

    # For each value
    # Get url and ask to keep or not the image
    gen = generator.Generator(startVal, endVal)
    while True:
        value = gen.value()
        url = "https://prnt.sc/{}".format(value)
        print("Testing {}...".format(url))
        request = urllib.request.Request(url, headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"
        })
        httpResponse = urllib.request.urlopen(request)
        if httpResponse.getcode() == 200:
            responseBody = httpResponse.read()
            resultSearch = re.search(b"src=[\"']([:\.\w\/]+\.(?:png|jpe?g|bmp))[\"']", responseBody)
            if resultSearch:
                urlImage = resultSearch.group(1)
                print("Image trouvée : {}".format(urlImage.decode('utf-8')))

        # If we finished, break the loop
        if not gen.next():
            break

def getArgumentValue(argName, defaultValue = None):
    try:
        argIndex = sys.argv.index(argName)
        return sys.argv[argIndex + 1]
    except ValueError:
        return

if __name__ == "__main__":
    main()