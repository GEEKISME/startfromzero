import hmac
message = b'hello,world!'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
temp = h.hexdigest()
print(temp)