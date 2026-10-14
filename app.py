import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# 1. Tạo DataFrame chứa thông tin 10 sinh viên
data = {
    "Họ và tên": [
        "An",
        "Bình",
        "Chi",
        "Dũng",
        "Hà",
        "Lan",
        "Minh",
        "Nam",
        "Phúc",
        "Trang",
    ],
    "Chuyên cần": [8.0, 9.0, 7.0, 8.5, 7.5, 6.0, 9.0, 7.0, 8.0, 9.5],
    "Giữa kỳ": [7.0, 8.0, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    "Cuối kỳ": [7.5, 8.5, 7.0, 9.5, 7.5, 6.5, 8.5, 7.0, 7.5, 9.5],
}
df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"] + 0.3 * df["Giữa kỳ"] + 0.5 * df["Cuối kỳ"]
)


# 3. Xếp loại sinh viên
def xep_loai(dtk):
  if dtk >= 8.5:
    return "Giỏi"
  elif dtk >= 7.0:
    return "Khá"
  elif dtk >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"


df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 4. Thống kê cơ bản
diem_tb_lop = df["Tổng kết"].mean()
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = (df["Tổng kết"] >= 5.0).sum()

# ==================== THIẾT KẾ WEB APP BẰNG STREAMLIT ====================

# Hiển thị tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Hiển thị bảng điểm
st.subheader("Bảng điểm chi tiết của sinh viên")
st.dataframe(df)

# Hiển thị thông tin thống kê
st.subheader("Thống kê chung")
st.write(f"- **Điểm tổng kết trung bình của lớp:** {diem_tb_lop:.2f}")
st.write(
    f"- **Sinh viên có điểm cao nhất:** {sv_cao_nhat['Họ và tên']} ({sv_cao_nhat['Tổng kết']:.2f})"
)
st.write(
    f"- **Sinh viên có điểm thấp nhất:** {sv_thap_nhat['Họ và tên']} ({sv_thap_nhat['Tổng kết']:.2f})"
)
st.write(f"- **Số sinh viên đạt (≥ 5.0):** {so_sv_dat} sinh viên")

# Tạo danh sách xổ xuống (Selectbox) để chọn sinh viên
st.subheader("Tra cứu thông tin cá nhân sinh viên")
selected_student = st.selectbox(
    "Chọn tên sinh viên cần xem:", df["Họ and tên"] if "Họ and tên" in df else df["Họ và tên"]
)

# Lọc thông tin sinh viên được chọn
student_info = df[df["Họ và tên"] == selected_student].iloc[0]
st.write(f"Thông tin chi tiết của **{selected_student}**:")
st.json(student_info.to_dict())

# Hiển thị biểu đồ cột điểm tổng kết
st.subheader("Biểu đồ điểm tổng kết của lớp")
fig, ax = plt.subplots()
ax.bar(df["Họ và tên"], df["Tổng kết"], color="skyblue")
ax.set_xlabel("Họ và tên")
ax.set_ylabel("Điểm tổng kết")
ax.set_title("Biểu đồ điểm tổng kết 10 sinh viên")
plt.xticks(rotation=45)
st.pyplot(fig)

# Hiển thị họ tên và MSSV ở cuối trang với kích thước chữ nhỏ
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: small;'>Người tạo ứng dụng: [Nguyễn Ngọc Hải Sơn] - MSSV: [030208007962]</p>",
    unsafe_allow_html=True,
)