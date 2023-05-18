import hmac
import base64


def sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body



if __name__ == '__main__':
    signStr = sign(pre_hash('1659927638003', 'POST', '/api/mix/v1/order/placeOrder', str('{"symbol":"TRXUSDT_SPBL","side":"open_long","orderType":"limit","force":"normal","price":"0.046317","quantity":"1212"}')), '')
    print(signStr)