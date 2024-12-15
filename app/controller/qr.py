import cv2

def scan_qr():
    # Khởi tạo đối tượng QRCodeDetector
    qrc = cv2.QRCodeDetector()

    # Mở camera (nên thử với chỉ số 0 nếu không mở được camera)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Không thể mở camera.")
        exit()

    while True:
        ret, frame = cap.read()
        if ret:
            # Phát hiện và giải mã mã QR
            r = qrc.detectAndDecodeMulti(frame)
            if r[0]:  # Kiểm tra xem có mã QR nào được phát hiện không
                for value, point in zip(r[1], r[2]):
                    print(value)
                break

            # Hiển thị frame với cameraq
            cv2.imshow('QR Code Detection', frame)

        # Thoát bằng phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên
    cap.release()
    cv2.destroyAllWindows()

