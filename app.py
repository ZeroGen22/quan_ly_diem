import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Tạo DataFrame chứa thông tin 10 sinh viên
data = {'Ho_va_ten': ['Lê Quốc Nguyên', 'Phạm Phương Thảo', 'Phan Gia Huy', 'Lưu Ngọc Hà', 'Trần Đức Hiếu', 'Tôn Nhật Chi', 'Hồ Đăng Khoa', 'Thái Trà My', 'Cao Thanh Trí', 'Bùi Hồng Nhung'],
    'Chuyên_cần': [10.0, 10.0, 9.0, 9.5, 8.5, 8.0, 8.0, 7.5, 6.5, 5.0],
    'Giữa_kỳ':    [9.0,  9.5,  8.0, 9.0, 8.2, 7.5, 7.8, 7.0, 6.0, 4.5],
    'Cuối_kỳ':    [9.5, 10.0,  8.2, 9.2, 8.5, 7.8, 8.0, 6.8, 5.5, 4.0]}
df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df['Tong_ket'] = (0.2 * df['Chuyên_cần'] + 0.3 * df['Giữa_kỳ'] + 0.5 * df['Cuối_kỳ']).round(2)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# Hiển thị bảng điểm 10 sinh viên
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df, use_container_width=True)

# 4. Thống kê
diem_tb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_dat = (df['Tong_ket'] >= 5.0).sum()

st.subheader("Thống kê chung")
st.write(f"- Điểm trung bình của lớp: {diem_tb_lop:.2f}")
st.write(f"- Sinh viên có điểm cao nhất: {sv_max['Ho_va_ten']} ({sv_max['Tong_ket']})")
st.write(f"- Sinh viên có điểm thấp nhất: {sv_min['Ho_va_ten']} ({sv_min['Tong_ket']})")
st.write(f"- Số sinh viên đạt (>= 5.0): {so_dat}/10")

# 5. Danh sách xổ xuống chọn sinh viên và hiển thị chi tiết
st.subheader("Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn một sinh viên:", df['Ho_va_ten'])

student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]
st.write(f"**Họ và tên:** {student_info['Ho_va_ten']}")
st.write(f"**Điểm chuyên cần:** {student_info['Chuyên_cần']}")
st.write(f"**Điểm giữa kỳ:** {student_info['Giữa_kỳ']}")
st.write(f"**Điểm cuối kỳ:** {student_info['Cuối_kỳ']}")
st.write(f"**Điểm tổng kết:** {student_info['Tong_ket']}")
st.write(f"**Xếp loại:** {student_info['Xep_loai']}")

# 6. Trực quan hóa biểu đồ cột điểm tổng kết
st.subheader("Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df['Ho_va_ten'], df['Tong_ket'], color='skyblue', edgecolor='black')
ax.set_xlabel('Họ và tên')
ax.set_ylabel('Điểm tổng kết')
ax.set_title('Biểu đồ điểm tổng kết')
plt.xticks(rotation=30, ha='right')
ax.set_ylim(0, 10)
st.pyplot(fig)

# 7. Thông tin người tạo ở cuối trang với kích thước chữ nhỏ
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: small;'>Họ tên: Gen - MSSV: [Nhập MSSV]</p>", unsafe_allow_html=True)
