# 🩴 Dép Store — Kafka Streaming Demo

Hệ thống xử lý đơn hàng thời gian thực sử dụng Apache Kafka.  
Bài tập lớn môn Ứng dụng Phân tán.

---

## Kiến trúc

```
Producer
   ↓
Kafka
   ↓
Worker-1   Worker-2   (Load Balancing)
   ↓
Retry Worker           (Fault Tolerance)
```

---

## Tính năng

**1. Multi-Worker Load Balancing**  
Nhiều worker cùng tham gia một consumer group. Kafka tự động chia đơn hàng cho từng worker — không worker nào xử lý trùng đơn.

**2. Retry Failed Orders**  
Đơn hàng lỗi (amount < 0) được gửi sang retry topic và xử lý lại sau 3 giây.

---

## Cài đặt

**Yêu cầu:** Python 3.11+, Docker Desktop

```bash
# 1. Clone repo
git clone https://github.com/<username>/dep-store-kafka.git
cd dep-store-kafka

# 2. Tạo virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Cài thư viện
pip install -r requirements.txt

# 4. Chạy Kafka
docker-compose up -d
```

---

## Chạy demo

Mở 4 terminal, chạy theo thứ tự:

```bash
# Terminal 1
cd app && python retry_worker.py

# Terminal 2
cd app && python worker.py    # nhập: Worker-1

# Terminal 3
cd app && python worker.py    # nhập: Worker-2

# Terminal 4 — chạy sau cùng
cd app && python producer.py
```

Mở dashboard: [http://localhost:5000](http://localhost:5000)

```bash
python server.py
```

---

## Cấu trúc thư mục

```
dep-store-kafka/
├── app/
│   ├── config.py         # cấu hình Kafka
│   ├── producer.py       # gửi đơn hàng
│   ├── worker.py         # xử lý đơn hàng
│   └── retry_worker.py   # xử lý đơn lỗi
├── docker-compose.yml    # Kafka + Zookeeper
├── server.py             # Flask serve dashboard
├── index.html            # giao diện web
├── requirements.txt
└── README.md
```

---

## Thư viện sử dụng

```
kafka-python
flask
flask-cors
```