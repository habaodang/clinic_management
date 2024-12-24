  document.addEventListener('DOMContentLoaded', function () {
        const roleSelect = document.getElementById('role');
        const departmentContainer = document.getElementById('department-container');

        roleSelect.addEventListener('change', function () {
            if (roleSelect.value === 'doctor' || roleSelect.value === 'nurse') {
                departmentContainer.hidden = false; // Hiện select cho khoa
            } else {
                departmentContainer.hidden = true; // Ẩn select cho khoa
                document.getElementById('department').value = ''; // Reset giá trị đã chọn
            }
        });
    });