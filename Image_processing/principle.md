### 1. Principle Component Analysis (PCA)
- Trích xuất đặc trưng => ứng dụng cho bài toán nhận dạng mặt người
> Có một cơ sở dữ liệu nhân viên, trong đó mỗi nhân viên đề có k ảnh
1. step1: Compute the average face image

2. Find eigenvectors and eigenvalues

- tù ảnh người (N) -> (PCA) ra được ảnh là đại diện của người đó với độ phân giải thấp hơn rất nhiều
nhưng lại có thể bao quát hết được các đặc trừng ảnh đó (N2)
- Từ N2 so sánh với với cơ sở dữ liệu (khoảng cách eculer)