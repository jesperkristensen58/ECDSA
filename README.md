# ECDSA Signature with secp256k1 & Keccak-256
This repository contains a simple Python implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) using the secp256k1 curve and keccak_256 as the hashing function.

## About
The code computes the s parameter of the ECDSA signature for a given message and private key. The signature consists of two parameters: r and s. The public key, corresponding to the given private key, is also computed using the elliptic curve.

The ECDSA algorithm is widely used in the crypto community, especially in Ethereum for generating signatures.

You can verify the signature as well with the provided code.

## Dependencies
secrets: For generating a random nonce.
sha3: Provides the keccak_256 hashing function.
ecpy: A Python library to work with elliptic curves.
Usage
To get the r and s values of the ECDSA signature for a message:

```python Copy code
message = "Your Message Here!"
private_key = Your_Private_Key_Here
r, s, public_key = compute_s(message, private_key)
print(f"r: {r}")
print(f"s: {s}")
```

By default, the private key in the main block is hardcoded. You can uncomment the lines in the main block to generate a random private key.

## License
This project is licensed under the MIT License.

## Author
Jesper Kristensen

*Note: Always exercise caution and avoid sharing your private key. This implementation is meant for educational purposes and may not be suited for production use.*
