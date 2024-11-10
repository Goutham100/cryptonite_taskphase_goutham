# vault door

flag: `c0nv3rt1ng_fr0m_ba5e_64_0b957c4f`

my approach to the problem:
- in the script provided the password is URL-encoded [this means each byte is % followed by a hexadecimal chars]
- 1st ill have to decode the expected strings from base64
- the decoded strings should be URL-encoded version of the password
- after that finally reverse th eURL encoding for the original password
- ```
    import base64
    import urllib.parse
    
    expected = (
    "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
    "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
    "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2"
    )
    
    decoded_url_encoded = base64.b64decode(expected).decode('utf-8')
    password = urllib.parse.unquote(decoded_url_encoded)
    
    print("The password is:", password)

  ```
- the following python code will help us find the password
