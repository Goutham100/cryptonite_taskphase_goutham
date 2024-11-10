# Scrambling RSA

Unsuccessful Methods I have tried:
- RSA (Rivest–Shamir–Adleman) is one of the first and most widely used public-key cryptosystems for secure data transmission.
- it has 2 keys The public key is (e,n) and the private key is (d,n)(d,n). where e is encrypted text d is decrypted text and n is p+q where p and q are prime numbers
- my approach was to find p and q so that i can find the private key using a decoder online
- so I used this
 ```
        n = 130802315821960193603939240623379006738906985021585692098063702720089709228180178839930929895948198817441905689815097585158321423011719683310659938758030593320823678893867375733797431546081969504909062355893631690605401059602402466302563317494088761130193280123171916485191930178704913584198513194852004613993

        a = isqrt(n) +1
        
        while True:
            b2 = a^2 - n
            if is_square(b2):
                b = sqrt(b2)
                break
                break
            a = a+1
        p = a+b
        q = a-b
 ```
- this code will iterate till b is a square
- but this requires lots of computation and i have yet to find the value for b

refernces: 
- https://www.youtube.com/watch?v=-ShwJqAalOk&t=603s&pp=ygUqYnJlYWtpbmcgcnNhIHVzaW5nIGNob3NlbiBwbGFpbnRleHQgYXR0YWNr