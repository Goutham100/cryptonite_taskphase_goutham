import base64
import urllib.parse

expected = (
    "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
    "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
    "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2"
)

decoded_url_encoded = base64.b64decode(expected).decode('utf-8')
password = urllib.parse.unquote(decoded_url_encoded)

print(password)
