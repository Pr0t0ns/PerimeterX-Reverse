import json
from urllib.parse import quote, unquote
import re
import base64
import math

# For Padding (Pretty sure it's a static value globally)
character_list = list("G^S}DNK8DNa>D`K}GK77")

# First Collector POST Request Payload UnEncrypted/Decoded
payload_unencrypted = [{
    "t": "PX12095", 
    "d": {
        "PX11645": "https://www.ssense.com/en-ca", # Endpoint/Host
        "PX12207": 0, # To Be Determined (Probably False Value)
        "PX12458": "Win32", # OS
        "PX11902": 0, # To Be Determined (Probably False Value)
        "PX11560": 756, # Browser Width (Not 100% Sure) 
        "PX12248": 3600, # Browser Height (Not 100% Sure)
        "PX11385": 1713737306091, # Unix Runtime (Start Time)
        "PX12280": 1713737306096, # Unix Runtime (End Time)
        "PX11496": "ad2e4860-002b-11ef-bc61-1b44c38fe285", # UUID (this is important for reverse) 
        "PX12564": None,
        "PX12565": -1, # TO BE DETERMINED (probably False Value or Undefined)
        "PX11379": True # TO BE DETERMINED (Probably True Value)
    }
}]

def Sl(t,e,n,r,a) -> int:
    return math.floor((t - e) / (n - e) * (a - r) + r)

def encode(payload: str, e:int=50) -> str:
    output = ''
    for i in range(len(payload)):
        output += chr(ord(payload[i]) ^ e)
    return output

def encrypt(payload: str) -> str:
    encoded_str = quote(payload)
    decoded_str = unquote(re.sub(r'%([0-9A-F]{2})', lambda m: chr(int(m.group(1), 16)), encoded_str))
    return base64.b64encode(decoded_str.encode()).decode()

def get_offset(t, e, n) -> list:
    g = encode(base64.b64encode(str(n).encode()).decode(), 10)
    p = []
    w = -1

    for A in range(len(t)):
        m = math.floor(A / len(g) + 1)
        y = A if A >= len(g) else A % len(g)
        G = ord(g[y]) * ord(g[m])
        if G > w:
            w = G
    for V in range(len(t)):
        b = math.floor(V / len(g)) + 1
        Q = V % len(g)
        T = ord(g[Q]) * ord(g[b])
        
        if T >= e:
            T = Sl(T, 0, w, 0, e - 1)
        
        while T in p:
            T += 1
        
        p.append(T)
    return sorted(p)

def add_padding(payload: str, PX_UID: str) -> str:
    n = get_offset(character_list, 368, PX_UID)
    i = 0; o = ""; c = character_list
    for u in range(20):
        o += payload[i:n[u] - u - 1] + c[u]
        i = n[u] - u - 1
    return o + payload[i:]


# Generate the Encrypted "Payload" value.
PXUID = payload_unencrypted[0]['d']['PX11496']
payload_unencrypted = json.dumps(payload_unencrypted).replace(" ", "")
encrypted_payload = (encrypt(encode(payload_unencrypted)))
finished_payload = (add_padding(encrypted_payload, PXUID))
print(finished_payload)
