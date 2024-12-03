import qrcode

# Dữ liệu để mã hóa trong mã QR
data = "hello"

# Tạo đối tượng QRCode
qr = qrcode.QRCode(
    version=1,  # Độ lớn của mã QR (1 là nhỏ nhất, 40 là lớn nhất)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Độ chính xác của mã QR
    box_size=10,  # Kích thước mỗi ô vuông trong mã QR
    border=4,  # Độ dày biên của mã QR
)

# Thêm dữ liệu vào QRCode
qr.add_data(data)
qr.make(fit=True)

# Tạo hình ảnh mã QR
img = qr.make_image(fill='black', back_color='white')

# Lưu hình ảnh vào file
img.save("hello_qr.png")

# Hiển thị mã QR (tuỳ chọn)
img.show()
