// Khi trang tải, đảm bảo tab đầu tiên là "Thông tin bác sĩ"
document.addEventListener('DOMContentLoaded', function () {
    const tabs = new bootstrap.Tab(document.querySelector('#doctor-info-tab'));
    tabs.show();
});


document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".form-group");
    let fileInput = document.getElementById("profile-picture"); // Sử dụng let để gán lại input
    const avatarPreview = document.getElementById("avatar-preview");
    const uploadLabel = document.getElementById("upload-label");
    const changeAvatarBtn = document.getElementById("change-avatar-btn");

    // Hàm xử lý khi file được chọn
    function handleFileChange(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                avatarPreview.src = e.target.result; // Gắn ảnh vào thẻ img
                avatarPreview.style.display = "block"; // Hiển thị ảnh preview
                changeAvatarBtn.style.display = "block"; // Hiển thị nút "Thay đổi ảnh"
                uploadLabel.style.display = "none"; // Ẩn nhãn "Upload your photo"
            };

            reader.readAsDataURL(file); // Đọc file
        }
    }

    // Gắn sự kiện change cho input ban đầu
    fileInput.addEventListener("change", handleFileChange);

    // Hàm xử lý khi nhấn "Thay đổi ảnh"
    changeAvatarBtn.addEventListener("click", () => {
        // Tạo một input file mới
        const newFileInput = document.createElement("input");
        newFileInput.type = "file";
        newFileInput.id = "profile-picture";
        newFileInput.name = "profile-picture";
        newFileInput.accept = "image/*";
        newFileInput.style.display = "none";

        // Thay thế input cũ bằng input mới
        container.replaceChild(newFileInput, fileInput);

        // Gán input mới vào biến fileInput
        fileInput = newFileInput;

        // Gắn lại sự kiện change cho input mới
        fileInput.addEventListener("change", handleFileChange);

        // Reset giao diện
        avatarPreview.style.display = "none"; // Ẩn ảnh
        changeAvatarBtn.style.display = "none"; // Ẩn nút "Thay đổi ảnh"
        uploadLabel.style.display = "block"; // Hiển thị lại nhãn
    });
});

 function showDetails(title, time, nurse, reason) {
            document.getElementById('nurseName').value = nurse;
            document.getElementById('appointmentDate').value = time;
            document.getElementById('appointmentReason').value = reason;
            document.getElementById('detailsModal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('detailsModal').style.display = 'none';
        }