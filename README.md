# Cloud DataWarehouse Project
## 1. Mô tả Project:


MovieLens là một hệ thống đề xuất phim phi thương mại trên nền tảng web. Nó được tạo ra vào năm 1997 và vận hành bởi GroupLens, một phòng nghiên cứu tại Đại học Minnesota, nhằm thu thập dữ liệu đánh giá phim phục vụ mục đích nghiên cứu.

Với vai trò là một kỹ sư dữ liệu, tôi muốn xây dựng một mô hình dữ liệu để người dùng cuối cùng có thể khai thác được dữ liệu liên quan đến các bộ phim trong tập dữ liệu Movielens và dữ liệu vể chỉ số giá tiêu dùng để trả lời các câu hỏi kinh doanh:
* Phim nào được xem nhiều nhất mọi thời đại?
* Thể loại phim nào được yêu thích nhất
* Xu hướng phòng vé - việc phát hành một bộ phim thuộc thể loại nào đó vào thàng/quý nhất định có ảnh hưởng gì đến doanh thu không?
* Thể loại phim nào có thu nhập cao nhất mọi thời đại theo chỉ số giá tiêu dùng?

Để làm được điều đó, trong Project này tôi sẽ tập chung vào 2 phần chính:
* Phân tích yêu cầu và phân tích dữ liệu nguồn --> xây dựng DW phù hợp
* Xây dựng ETL pipeline để trích xuất, chuyển đổi- xử lý và tải dữ vào DW đã thiết kế.
  
## 2. Phân tích yêu cầu và scop dự án:

**Về mặt nghiệp vụ:**
* DW phải đáp ứng được yêu cầu là trả lời được các câu hỏi kinh doanh tôi đã đề cập ở mục "Giới thiệu"

**Về mặt dữ liệu:**
* Dữ liệu phải đảm bảo toàn vẹn
* Các vấn đề của dữ liệu phải được dọn dẹp, xử lý trước khi tải vào DW
* Dữ liệu trong DW không được trùng lặp

**Về mặt công nghệ:**
* Phải xây dựng DW trên nền tảng đám mây (Bigquery)
* ETL phải đảm bảo được khả năng vận hành khi lượng dữ liệu tăng lên nhanh chóng.

## 3. Thu thập và khai phá dữ liệu:

**movies_metadata**:
  *  Dữ liệu chứa 26 triệu đánh giá người dùng của hơn 270.000 người dùng trên bộ sưu tập hơn 45.000 phim.
  *  Bao gồm các columns sau: posters, backdrops, budget, revenue, release dates, languages, production countries, companies.
  *  Nguồn: https://www.kaggle.com/rounakbanik/the-movies-dataset

 **Rating**: 
 * Chứa thông tin về việc đánh giá các bộ phim của người dùng
 * Bao gồm các column sau: movie_id, user_id, rating
 * Nguồn: https://www.kaggle.com/rounakbanik/the-movies-dataset
 
**CPI:**
* Chứa thông tin về chỉ số giá tiêu dùng theo từng ngày, bắt đầu từ năm 2000 đến nay.
* Dữ liệu này giúp đánh giá/tính toán doanh thu phòng vé so với lạm phát các năm
* Nguồn: https://fred.stlouisfed.org/series/CUSR0000SS62031

## 4. Xác định các bảng trong DW:
Cần phải xác định được DW sẽ được tổ chức như thế nào? gồm những bảng nào?
Trong dự án này, tôi xác định DW sẽ có:
* 2 vùng: Staging và Mart
* 2 loại bảng: Dim và Fact
* Tổng cộng 9 bảng
![image](https://github.com/hien201/Google_Bigquery_DataWarehouse/assets/90466915/5bc0309b-8011-4ad4-b291-fcd86c3e55dd)

-------------------------------
## 3. Mô hình dũ liệu:

- lựa chọn mô hình dữ liệu galaxy
- Data Model:

![image](https://user-images.githubusercontent.com/90466915/226553184-e7b60a99-3aa9-4bec-a18f-7ca38766b059.png)

## 4. Ý tưởng thực hiện :
---
- Download bộ dataset từ Kaggle và Fred xuống local
- Sử dụng Google Cloud Platform để xây dựng ETL
- Từ local thực hiện ETL dữ liệu lên bảng tạm trên BIGQUERY
- Từ các bảng tạm sẽ merge data vào bảng chính theo các điều kiện nhất định.

## 5. Architecture:
---
- Dựa trên phân tích và ý tưởng trên, lựa chọn kiến trúc như sau:

![image](https://user-images.githubusercontent.com/90466915/226554013-2e34633a-326e-4e40-9cf7-7910d3f98177.png)

## 6. Project Structure:
---
- upload_to_GCS và main_upload_to_GCS.py: upload file movie_meta.csv, rating.csv, cpi.csv từ local lên GCS
- create_table và main_create_table: tạo các bảng tạm và bảng chính trên Goggle Bigquery
- upload_BIGQUERY.py  và main_upload_BIGQUERY.py: upload data từ 3 file csv trên GCS vào các bảng tạm trên BIGQUERY
- upsert_target_table.py: merget dữ liệu từ các bảng tạm vào bảng chính tùy theo điều kiện. 
- parameter.py & sql_create_table.py: chứa biến để chạy các module trên

## 7. Chạy ETL:
---
main_create_table → main_upload_GCS → main_upload_BIGQUERY → upsert_target_table → check data on BIGQUERY 

## 8. Cải thiện:
---
- Tiến tới sử dụng Airflow để chạy ETL: quản lý và điều phối tác vụ. 






 
