# BÀI TẬP LỚN GIỮA KỲ MÔN HỆ THỐNG PHÂN TÁN

## Đề tài

Tìm hiểu và thực nghiệm hệ thống xử lý luồng phân tán sử dụng Faust Streaming và Apache Kafka.

## Giới thiệu

Trong các hệ thống hiện đại, dữ liệu được sinh ra liên tục từ nhiều nguồn khác nhau như giao dịch thương mại điện tử, mạng xã hội, thiết bị IoT,... Việc xử lý dữ liệu theo thời gian thực là một yêu cầu quan trọng nhằm đáp ứng nhu cầu giám sát, phân tích và ra quyết định nhanh chóng.

Dự án này sử dụng Faust Streaming kết hợp với Apache Kafka để xây dựng một hệ thống xử lý dữ liệu dạng luồng (stream processing). Hệ thống cho phép gửi dữ liệu vào Kafka và thực hiện xử lý dữ liệu theo thời gian thực thông qua các worker của Faust.

## Mục tiêu

* Tìm hiểu kiến trúc của Faust Streaming.
* Tìm hiểu cơ chế hoạt động của Apache Kafka.
* Cài đặt và thực nghiệm hệ thống xử lý luồng.
* Mô phỏng môi trường xử lý phân tán với nhiều worker.
* Nghiên cứu và phát triển thêm các tính năng mới liên quan đến hệ thống phân tán.

## Công nghệ sử dụng

* Python
* Faust Streaming
* Apache Kafka
* Apache Zookeeper
* Docker Desktop
* Git và Github
* Visual Studio Code

## Cấu trúc thư mục

```text
CK-faust/
│
├── app/
│   ├── __init__.py
│   ├── producer.py
│   └── worker.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

## Cài đặt môi trường

### Khởi động Kafka và Zookeeper

```bash
docker compose up -d
```

### Kiểm tra trạng thái container

```bash
docker ps
```

### Cài đặt thư viện Python

```bash
pip install -r requirements.txt
```

## Chức năng hiện tại

* Khởi tạo Kafka Broker.
* Khởi tạo Zookeeper.
* Gửi dữ liệu vào Kafka thông qua Producer.
* Nhận và xử lý dữ liệu bằng Faust Worker.

## Hướng phát triển

### Tính năng 1

Mô phỏng nhiều worker xử lý song song nhằm tăng khả năng mở rộng của hệ thống.

### Tính năng 2

Xây dựng cơ chế Retry và Fault Tolerance khi xảy ra lỗi trong quá trình xử lý dữ liệu.


## Github

Repository được sử dụng để quản lý mã nguồn, theo dõi lịch sử phát triển và lưu trữ toàn bộ quá trình thực hiện dự án.
