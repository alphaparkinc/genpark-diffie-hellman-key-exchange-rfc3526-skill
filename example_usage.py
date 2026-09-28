from client import DiffieHellmanKeyExchange

def main():
    a_priv, a_pub = DiffieHellmanKeyExchange.generate_keypair()
    b_priv, b_pub = DiffieHellmanKeyExchange.generate_keypair()
    k1 = DiffieHellmanKeyExchange.compute_shared_secret(a_priv, b_pub)
    k2 = DiffieHellmanKeyExchange.compute_shared_secret(b_priv, a_pub)
    print("Shared AES-256 Key Derived:", k1.hex())
    assert k1 == k2

if __name__ == "__main__":
    main()
