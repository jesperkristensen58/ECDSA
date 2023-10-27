from ecpy.curves import Curve
from sha3 import keccak_256
cv = Curve.get_curve('secp256k1')
n = cv.order

def verify_signature(message, public_key, r, s):
    # Constants for secp256k1 curve

    # Hash the message
    h = int(keccak_256(message.encode("utf-8")).digest().hex(), 16)

    # Step 1: Calculate w == s^(-1)
    w = pow(s, -1, n)
    assert s * w % n == 1

    # Step 2: Calculate terms for C
    u = (h * w) % n
    v = (r * w) % n

    # Step 3: Calculate point C
    C = u * cv.generator + v * public_key

    # Step 4: Validate the signature
    return r == C.x % n

if __name__ == "__main__":
    # Constants for the curve
    G = cv.generator

    private_key = 1454344372246026460200508591395882747343986357555964651916223348442022100776
    public_key = private_key * G

    # Assuming r and s are already computed, let's mock them here for simplicity
    # (you should replace these values with the ones you've computed earlier)
    message = "Hello World!"
    r = 55746467792705440031515636631680548494405608855639968652694738645984582077297
    s = 82660667060023805117012427294827515888260657670991295911160834048118385163815

    # Verify the signature
    is_valid = verify_signature(message, public_key, r, s)
    print(f"Signature is {'valid' if is_valid else 'invalid'}")

