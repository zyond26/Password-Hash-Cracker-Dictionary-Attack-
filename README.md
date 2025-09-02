# 🔐 Password Hash Cracker (Educational Demo)

## 📌 Giới thiệu
Dự án này là một **demo học tập** nhằm minh họa:
- Cách hoạt động của hash function (MD5, SHA1, SHA256).
- Cơ chế tấn công mật khẩu yếu bằng **dictionary attack** và **brute force**.
- Vì sao mật khẩu yếu hoặc sử dụng thuật toán hash nhanh là **không an toàn**.

⚠️ **Lưu ý:** Dự án chỉ mang tính **giáo dục** và minh họa. Không sử dụng cho mục đích tấn công thực tế.

---

## 🚀 Tính năng
- Hash mật khẩu với MD5, SHA1, SHA256.
- Thử crack hash bằng:
  - **Dictionary attack** (dùng wordlist mật khẩu phổ biến).
  - **Brute force** (tạo chuỗi ký tự theo độ dài cho trước).
- Demo với mật khẩu ngắn/yếu.

---

## 🛠️ Cài đặt & chạy
### Yêu cầu
- Python 3.8+
- Không cần thư viện ngoài (chỉ dùng `hashlib`, `itertools`).

### Cách chạy
```bash
git clone https://github.com/zyond26/Password-Hash-Cracker-Dictionary-Attack-.git
cd Password-Hash-Cracker-Dictionary-Attack-

+) Run in terminal :

python hash_cracker.py

+) Run in web  

- Cài đặt flask = lệnh pip install flask
-Cài xong tthì chạy : python app.py 