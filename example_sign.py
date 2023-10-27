import secrets
from sha3 import keccak_256
from ecpy.curves import Curve

cv = Curve.get_curve('secp256k1')
n = cv.order

def compute_s(message, private_key):
    # Get curve and generator point
    public_key = private_key * cv.generator

    # Hash the message using keccak_256
    h = int(keccak_256(message.encode("utf-8")).digest().hex(), 16)

    # Generate a nonce `k`--used once for signing, then thrown away
    k = n
    while k >= n:
        k = int("0x" + secrets.token_hex(32), 16)

    # Compute R
    R = k * cv.generator
    r = R.x
    assert r > 0

    # Compute k's modular inverse
    k_inv = pow(k, -1, n)
    assert k * k_inv % n == 1

    # Compute s
    s = (k_inv * (h + r * private_key)) % n

    return r, s, public_key

if __name__ == "__main__":
    ## Generate a private key
    #private_key = n
    #while private_key >= n:
    #    private_key = int("0x" + secrets.token_hex(32), 16)

    private_key = 1454344372246026460200508591395882747343986357555964651916223348442022100776
    message = "Hello World!"
    r, s, public_key = compute_s(message, private_key)
    
    print(f"Private key: {private_key}")
    print(f"r: {r}")
    print(f"s: {s}")

