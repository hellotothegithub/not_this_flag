import hashlib
import os
import sys

def crack_hash(target, wordlist_path, hash_type="sha256", salt=""):
    """
    Attempts to crack a hash by iterating through a dictionary file.
    """
    if not os.path.exists(wordlist_path):
        print(f"[!] Error: File '{wordlist_path}' not found.")
        return None

    print(f"[*] Target Hash: {target}")
    print(f"[*] Using Salt: '{salt}'")
    print(f"[*] Algorithm: {hash_type.upper()}")
    print("-" * 50)

    count = 0
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                # Clean the word from the dictionary
                word = line.strip()
                # Combine salt with word if present
                salted_word = salt + word
                
                # Create the hash object dynamically
                h = hashlib.new(hash_type)
                h.update(salted_word.encode('utf-8'))
                guess = h.hexdigest()
                
                count += 1
                # Optional: Print progress every 1000 attempts
                if count % 1000 == 0:
                    print(f"[*] Checked {count} passwords...", end='\r')

                if guess == target:
                    print(f"\n\n[+] MATCH FOUND!")
                    print(f"[+] Raw Password: {word}")
                    print(f"[+] Total Attempts: {count}")
                    return word
                    
    except KeyboardInterrupt:
        print("\n[!] User interrupted the process.")
        sys.exit()

    print(f"\n[-] Failure: No match found after {count} attempts.")
    return None

# --- Configuration ---
# Example: SHA-256 of salt "secret_" + password "123456"
demo_hash = "679f2913e003780360a0f443b0922e379058b8f2d5778a4878a7c2957908b8b7"
dictionary_file = "passwords.txt" # You would create this file locally
applied_salt = "FLAG{salt_pass_key}"

# To run this, you would uncomment the line below:
# crack_hash(demo_hash, dictionary_file, salt=applied_salt)
