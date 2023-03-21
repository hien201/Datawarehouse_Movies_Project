# Datawarehouse_Movies_Project
# 1. DESCRIPTION:
## 1.1 MỤC ĐÍCH:  
- Dựa trên dữ liệu nguồn xây dựng DW movies từ đó xây dựng hệ thống giới thiệu/ đề xuất phim và phân tích các yếu tố ảnh hưởng đến doanh thu.
## 2. Phân tích yêu cầu:
Từ DW này phải trả lời được các câu hỏi kinh doanh sau:
- Phim nào đc xem nhiều nhất
- Thể loại phim nào được yêu thích nhất 
- Xu hướng phòng vé - việc phát hành một bộ phim nào đó vào một thời điểm nào đó có ảnh hưởng gì đến doanh thu hay không
- Thể loại nào có doanh thu cao nhất mọi thời đại, tính theo chỉ số giá tiêu dùng. 
# 2. ĐỌC - HIỂU DỮ LIỆU:
movies_metadata: dữ liệu chính chứa thông tin về 45.000 phim. Bao gồm các columns sau: posters, backdrops, budget, revenue, release dates, languages, production countries, companies. 
→ đây là bảng dim 

Rating: chứa thông tin về việc đánh giá các bộ phim của người dùng, bao gồm các column sau: movie_id, user_id, rating
→ đây là  bảng fact

CPI: chứa thông tin về chỉ số giá tiêu dùng theo từng ngày, bắt đầu từ năm 2000 đến nay. 
→ bảng fact


 
