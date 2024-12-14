document.addEventListener("DOMContentLoaded", function () {
    // Bắt sự kiện khi thay đổi phương thức
    const methodSelect = document.getElementById("verificationMethod");
    const manualForm = document.getElementById("manualForm");
    const imageForm = document.getElementById("imageForm");

    methodSelect.addEventListener("change", function () {
        if (this.value === "manual") {
            manualForm.style.display = "block";
            imageForm.style.display = "none";
        } else if (this.value === "image") {
            manualForm.style.display = "none";
            imageForm.style.display = "block";
        }
    });

    // Mở modal khi bấm nút "Xác Thực"
    const verifyButton = document.querySelector(".btn-primary.btn-lg");
    verifyButton.addEventListener("click", function () {
        const modal = new bootstrap.Modal(document.getElementById("verificationModal"));
        modal.show();
    });
});


document.querySelectorAll('.menu-item').forEach(item => {
    item.addEventListener('click', function () {
        document.querySelectorAll('.menu-item').forEach(menuItem => menuItem.classList.remove('active'));
        item.classList.add('active');
    });
});
