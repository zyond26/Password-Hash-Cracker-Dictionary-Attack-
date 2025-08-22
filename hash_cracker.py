import hashlib
import itertools
import string
import argparse

# Các thuật toán hỗ trợ
SUPPORTED = {"md5": hashlib.md5, "sha1": hashlib.sha1, "sha256": hashlib.sha256}

def hash_word(word: str, algo: str) -> str:
    """Tính hash của một mật khẩu bằng thuật toán cho trước"""
    return SUPPORTED[algo](word.encode()).hexdigest()

def crack_dictionary(target_hash: str, algo: str, wordlist: str):
    """Dictionary attack: duyệt qua wordlist và so sánh"""
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for word in f:
            word = word.strip()
            if not word:
                continue
            if hash_word(word, algo) == target_hash:
                print(f"[+] FOUND (dictionary): {word}")
                return
    print("[-] Not found in dictionary.")

def crack_bruteforce(target_hash: str, algo: str, max_length: int):
    """Brute-force attack: thử tất cả chuỗi với độ dài từ 1 đến max_length"""
    chars = string.ascii_lowercase + string.digits  # bảng ký tự: a-z, 0-9
    for length in range(1, max_length + 1):
        for candidate in itertools.product(chars, repeat=length):
            word = "".join(candidate)
            if hash_word(word, algo) == target_hash:
                print(f"[+] FOUND (bruteforce): {word}")
                return
    print("[-] Not found in brute-force search.")

def main():
    parser = argparse.ArgumentParser(description="Password Hash Cracker (Dictionary + Brute-force)")
    parser.add_argument("--hash", required=True, help="Hash mục tiêu cần crack")
    parser.add_argument("--algo", required=True, choices=SUPPORTED.keys(), help="Thuật toán: md5, sha1, sha256")
    parser.add_argument("--wordlist", help="Đường dẫn wordlist (dictionary attack)")
    parser.add_argument("--bruteforce", type=int, help="Dùng brute-force (tối đa độ dài n)")
    args = parser.parse_args()

    target_hash = args.hash.lower()
    algo = args.algo.lower()

    if args.wordlist:
        crack_dictionary(target_hash, algo, args.wordlist)

    if args.bruteforce:
        crack_bruteforce(target_hash, algo, args.bruteforce)

if __name__ == "__main__":
    main()
