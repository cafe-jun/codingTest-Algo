
import base64
import urllib.parse


def convert_unicode():
    u = "%ED%85%8C%EC%8A%A4%ED%8A%B83"
    decodeStr = urllib.parse.unquote(u)
    print(decodeStr)


convert_unicode()
