import hashlib

# Define the string
string = "stringToCheck"

# Encode the string to bytes
encoded_string = string.encode()

# Create a SHA1 hash object
sha1_hash = hashlib.sha1()

# Update the hash object with the encoded string
sha1_hash.update(encoded_string)

# Get the hexadecimal representation of the hash
hash_hex = sha1_hash.hexdigest()

print("SHA1 hash:", hash_hex)
