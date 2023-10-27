# ECDSA Signature with secp256k1 & Keccak-256

This repository contains a simple Python implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) using the `secp256k1` curve and `keccak_256` as the hashing function. It provides functionality for both generating and verifying ECDSA signatures.

## About

- **Signature Generation**: Computes the `r` and `s` parameters of the ECDSA signature for a given message and private key. The signature consists of two parameters: `r` and `s`. The public key, corresponding to the given private key, is also computed using the elliptic curve.

- **Signature Verification**: Validates the signature by checking whether the provided `r` and `s` values match the given message and public key.

The ECDSA algorithm is widely used in the crypto community, especially in Ethereum for generating and verifying signatures.

## Dependencies

- `secrets`: For generating a random nonce (used in signature generation).
- `sha3`: Provides the `keccak_256` hashing function.
- `ecpy`: A Python library to work with elliptic curves.

## Usage

### Generating a Signature
To get the `r` and `s` values of the ECDSA signature for a message:

```python Copy code
message = "Your Message Here!"
private_key = Your_Private_Key_Here
r, s, public_key = compute_s(message, private_key)
print(f"r: {r}")
print(f"s: {s}")
```

### Verifying a Signature

To validate an ECDSA signature for a message:

```python Copy code
message = "Your Message Here!"
public_key = Your_Public_Key_Here
r = Your_R_Value_Here
s = Your_S_Value_Here

is_valid = verify_signature(message, public_key, r, s)
print(f"Signature is {'valid' if is_valid else 'invalid'}")
```

By default, the private key in the main blocks of both files is hardcoded. You can uncomment the lines in the main block of the signature generation file to generate a random private key.

## License
This project is licensed under the MIT License.

## Author
Jesper Kristensen

*Note: Always exercise caution and avoid sharing your private key. This implementation is meant for educational purposes and may not be suited for production use.*
