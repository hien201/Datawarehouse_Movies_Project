# Datawarehouse_Movies_Project
## 1. Mô tả Project:
### 1.1 Mục đích:  
- Dựa trên dữ liệu nguồn xây dựng DW movies từ đó xây dựng hệ thống giới thiệu/ đề xuất phim và phân tích các yếu tố ảnh hưởng đến doanh thu.
### 1.2. Phân tích yêu cầu:
Từ DW này phải trả lời được các câu hỏi kinh doanh sau:
- Phim nào đc xem nhiều nhất
- Thể loại phim nào được yêu thích nhất 
- Xu hướng phòng vé - việc phát hành một bộ phim nào đó vào một thời điểm nào đó có ảnh hưởng gì đến doanh thu hay không
- Thể loại nào có doanh thu cao nhất mọi thời đại, tính theo chỉ số giá tiêu dùng. 
## 2. Đọc dữ liệu:
- movies_metadata: dữ liệu chính chứa thông tin về 45.000 phim. Bao gồm các columns sau: posters, backdrops, budget, revenue, release dates, languages, production countries, companies. 
→ đây là bảng dim 

- Rating: chứa thông tin về việc đánh giá các bộ phim của người dùng, bao gồm các column sau: movie_id, user_id, rating
→ đây là  bảng fact

- CPI: chứa thông tin về chỉ số giá tiêu dùng theo từng ngày, bắt đầu từ năm 2000 đến nay. 
→ bảng fact

## 3. Xây dựng Data Warehouse:
- lựa chọn mô hình dữ liệu galaxy
Data Model:

![image](https://user-images.githubusercontent.com/90466915/226553184-e7b60a99-3aa9-4bec-a18f-7ca38766b059.png)

## Ý tưởng thực hiện :
- Download bộ dataset từ Kaggle và Fred xuống local
- Sử dụng Google Cloud Platform để xây dựng ETL
- Từ local thực hiện ETL dữ liệu lên bảng tạm trên BIGQUERY
- Từ các bảng tạm sẽ merge data vào bảng chính theo các điều kiện nhất định.

## 5. Architecture:
- Dựa trên phân tích và ý tưởng trên, lựa chọn kiến trúc như sau:

![image](https://user-images.githubusercontent.com/90466915/226554013-2e34633a-326e-4e40-9cf7-7910d3f98177.png)

## 6. Project Structure:
- upload_to_GCS và main_upload_to_GCS.py: upload file movie_meta.csv, rating.csv, cpi.csv từ local lên GCS
- create_table và main_create_table: tạo các bảng tạm và bảng chính trên Goggle Bigquery
- upload_BIGQUERY.py  và main_upload_BIGQUERY.py: upload data từ 3 file csv trên GCS vào các bảng tạm trên BIGQUERY
- upsert_target_table.py: merget dữ liệu từ các bảng tạm vào bảng chính tùy theo điều kiện. 
- parameter.py & sql_create_table.py: chứa biến để chạy các module trên

## 7. Chạy ETL:
main_create_table → main_upload_GCS → main_upload_BIGQUERY → upsert_target_table → check data on BIGQUERY

## 8. Cải thiện:
- Tiến tới sử dụng Airflow để chạy ETL: quản lý và điều phối tác vụ. 






 
