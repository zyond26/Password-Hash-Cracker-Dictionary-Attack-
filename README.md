# 🔑 Password Hash Cracker (Python)

Một công cụ nhỏ viết bằng Python để **crack mật khẩu từ các hash (MD5, SHA1, SHA256)** bằng 2 phương pháp:
- **Dictionary Attack**: thử mật khẩu từ một wordlist có sẵn.
- **Brute-force Attack**: thử tất cả chuỗi ký tự theo độ dài giới hạn.

---

## 📌 Mục tiêu dự án
- Minh họa **rủi ro bảo mật** khi người dùng đặt mật khẩu yếu hoặc bị lộ dữ liệu.
- Hiểu rõ hơn về:
  - Cơ chế hash (MD5, SHA1, SHA256).
  - Dictionary attack & brute-force attack.
  - Quản lý mật khẩu an toàn trong thực tế.

---

## ⚙️ Cài đặt & Chuẩn bị
Yêu cầu:
- Python 3 (>=3.8).
- Không cần cài thêm thư viện ngoài `hashlib`.

🚀 Cách sử dụng
Dictionary Attack

Ví dụ crack MD5 của "hello" (5d41402abc4b2a76b9719d911017c592):

python hash_cracker.py --hash 5d41402abc4b2a76b9719d911017c592 --algo md5 --wordlist passwords.txt

===> kết quả là : [+] FOUND (dictionary): hello

