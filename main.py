import os
import sys
import argparse
import hashlib
import hmac
import base64
from typing import Optional

def generate_keypair() -> tuple[str, str]:
    private_key = os.urandom(32)
    public_key = hashlib.sha256(private_key).hexdigest()
    return base64.b64encode(private_key).decode('utf-8'), public_key

def sign_challenge(private_key: str, challenge: str) -> str:
    private_key_bytes = base64.b64decode(private_key)
    challenge_bytes = bytes.fromhex(challenge)
    signature = hmac.new(private_key_bytes, challenge_bytes, hashlib.sha256).digest()
    return base64.b64encode(signature).decode('utf-8')

def main() -> None:
    parser = argparse.ArgumentParser(description='Tesla keygen tool')
    parser.add_argument('--private-key', type=str, help='Private key (base64 encoded)')
    parser.add_argument('--public-key', type=str, help='Public key (hex encoded)')
    parser.add_argument('--challenge', type=str, help='Challenge to sign (hex encoded)')
    args = parser.parse_args()

    if args.challenge:
        if not args.private_key:
            print("Error: --private-key is required when using --challenge")
            sys.exit(1)
        signature = sign_challenge(args.private_key, args.challenge)
        print(signature)
    else:
        private_key, public_key = generate_keypair()
        print(f"Private key: {private_key}")
        print(f"Public key: {public_key}")

if __name__ == "__main__":
    main()
