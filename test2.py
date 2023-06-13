from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.keys import HDKey

# Generate a random BIP39 mnemonic phrase
mnemonic_phrase = Mnemonic().generate()

# Derivation path according to BIP44 specification
derivation_path = "m/44'/0'/0'/0/0"

# Generate the master seed from the mnemonic phrase
master_seed = Mnemonic().to_seed(mnemonic_phrase)

# Create the master key and chain code from the master seed
master_key, chain_code = HDKey(master_seed)

# Convert the seed, master key, and chain code to hexadecimal format
seed_hex = master_seed.hex()
master_key_hex = master_key.export_to_base58()
chain_code_hex = chain_code.hex()

print("Mnemonic Phrase:", mnemonic_phrase)
print("Seed (Hex):", seed_hex)
print("Master Key:", master_key_hex)
print("Chain Code:", chain_code_hex)
