let updateRowIndex = -1; // Chỉ số hàng cần cập nhật

// Dữ liệu mẫu của thuốc
const medicineData = {
  "MT01": { name: "Thuốc 1", unit: "Vỉ", effect: "Giảm đau", usage: "Uống Trước Khi Ăn" },
  "MT02": { name: "Thuốc 2", unit: "Viên", effect: "Hạ sốt", usage: "Uống Sau Khi Ăn" },
  "MT03": { name: "Thuốc 3", unit: "Chai", effect: "Kháng viêm", usage: "Uống Trước Khi Ăn" }
};

// Mở form thêm thuốc
function openForm() {
  document.getElementById("overlay").style.display = "flex";
  document.getElementById("infoContainer").style.display = "none";
  document.getElementById("medicineCode").value = "";
}

// Đóng form
function closeForm() {
  document.getElementById("overlay").style.display = "none";
}

// Tìm kiếm thuốc
function searchMedicine() {
  const code = document.getElementById("medicineCode").value.trim().toUpperCase();
  const medicine = medicineData[code];

  if (medicine) {
    document.getElementById("medicineName").value = medicine.name;
    document.getElementById("medicineUnit").value = medicine.unit;
    document.getElementById("medicineEffect").value = medicine.effect;
    document.getElementById("medicineUsage").value = medicine.usage;
    document.getElementById("infoContainer").style.display = "block";
  } else {
    alert("Không tìm thấy thuốc!");
    document.getElementById("infoContainer").style.display = "none";
  }
}

// Thêm thuốc vào bảng
function addMedicine() {
  const code = document.getElementById("medicineCode").value.toUpperCase();
  const name = document.getElementById("medicineName").value;
  const unit = document.getElementById("medicineUnit").value;
  const quantity = document.getElementById("medicineQuantity").value;
  const effect = document.getElementById("medicineEffect").value;
  const usage = document.getElementById("medicineUsage").value;

  const table = document.getElementById("medicineTable");
  const row = table.insertRow();
  const stt = table.rows.length; // Tính số thứ tự

  row.innerHTML = `
    <td>${stt}</td> <!-- Thêm STT -->
    <td>${code}</td>
    <td>${name}</td>
    <td>${unit}</td>
    <td>${quantity}</td>
    <td>${effect}</td>
    <td>${usage}</td>
    <td><button class="update-btn" onclick="showUpdateConfirmation(this)">Cập Nhật</button></td>
  `;

  closeForm();
}

// Hiển thị modal xác nhận cập nhật hoặc xóa
function showUpdateConfirmation(button) {
  // Lưu chỉ số hàng cần cập nhật
  updateRowIndex = button.closest('tr').rowIndex;
  const row = document.getElementById('medicineTable').rows[updateRowIndex - 1]; // Chú ý cần trừ 1 vì bảng bắt đầu từ 0

  // Điền thông tin vào form cập nhật
  document.getElementById("medicineCode").value = row.cells[1].textContent; // Cột Mã Thuốc
  document.getElementById("medicineName").value = row.cells[2].textContent; // Cột Tên Thuốc
  document.getElementById("medicineUnit").value = row.cells[3].textContent; // Cột Đơn Vị
  document.getElementById("medicineQuantity").value = row.cells[4].textContent; // Cột Số Lượng
  document.getElementById("medicineEffect").value = row.cells[5].textContent; // Cột Tác Dụng
  document.getElementById("medicineUsage").value = row.cells[6].textContent; // Cột Cách Dùng

  document.getElementById("overlay").style.display = "flex"; // Hiển thị form cập nhật
  document.getElementById("infoContainer").style.display = "block"; // Hiển thị thông tin thuốc
  document.getElementById("updateConfirmation").style.display = "flex"; // Hiển thị modal cập nhật
}

// Modal Xác nhận Cập Nhật hoặc Xóa
function confirmUpdate(action) {
  const table = document.getElementById("medicineTable");

  if (action === 'update') {
    // Cập nhật lại dữ liệu của hàng trong bảng
    const code = document.getElementById("medicineCode").value.toUpperCase();
    const name = document.getElementById("medicineName").value;
    const unit = document.getElementById("medicineUnit").value;
    const quantity = document.getElementById("medicineQuantity").value;
    const effect = document.getElementById("medicineEffect").value;
    const usage = document.getElementById("medicineUsage").value;

    const row = table.rows[updateRowIndex - 1]; // Trừ 1 vì bảng bắt đầu từ 0
    row.cells[1].textContent = code;  // Cập nhật Mã Thuốc
    row.cells[2].textContent = name;  // Cập nhật Tên Thuốc
    row.cells[3].textContent = unit;  // Cập nhật Đơn Vị
    row.cells[4].textContent = quantity; // Cập nhật Số Lượng
    row.cells[5].textContent = effect;  // Cập nhật Tác Dụng
    row.cells[6].textContent = usage;  // Cập nhật Cách Dùng

  } else if (action === 'delete') {
    // Xóa thuốc khỏi bảng
    table.deleteRow(updateRowIndex - 1); // Trừ 1 vì bảng bắt đầu từ 0
  }

  closeForm(); // Đóng form
  closeUpdateConfirmation(); // Đóng modal cập nhật
}

// Đóng modal cập nhật
function closeUpdateConfirmation() {
  document.getElementById("updateConfirmation").style.display = "none"; // Ẩn modal cập nhật
}

// Xóa tất cả thuốc
function clearTable() {
  const table = document.getElementById("medicineTable");
  table.innerHTML = ""; // Xóa toàn bộ các dòng trong bảng
}
// Hàm quay lại trang trước
function goBack() {
    window.history.back();
}

function openUpdateForm() {
    // Ẩn form tìm kiếm thuốc
    document.getElementById('overlay').style.display = 'none';

    // Hiển thị form cập nhật thuốc
    document.getElementById('updateFormOverlay').style.display = 'block';

    const row = document.getElementById('medicineTable').rows[updateRowIndex - 1]; // Trừ 1 vì bảng bắt đầu từ 0

    // Điền thông tin vào form cập nhật
    document.getElementById("medicineCode").value = row.cells[1].textContent; // Mã Thuốc
    document.getElementById("medicineName").value = row.cells[2].textContent; // Tên Thuốc
    document.getElementById("medicineUnit").value = row.cells[3].textContent; // Đơn Vị
    document.getElementById("medicineQuantity").value = row.cells[4].textContent; // Số Lượng
    document.getElementById("medicineEffect").value = row.cells[5].textContent; // Tác Dụng
    document.getElementById("medicineUsage").value = row.cells[6].textContent; // Cách Dùng
}

function openForm() {
  // Hiển thị overlay form tìm kiếm thuốc
  document.getElementById('overlay').style.display = 'flex';
  document.getElementById('updateFormOverlay').style.display = 'none'; // Ẩn form cập nhật
}

function closeForm() {
  // Ẩn tất cả form
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('updateFormOverlay').style.display = 'none';
  document.getElementById('updateConfirmation').style.display = 'none';
}


function closeUpdateConfirmation() {
    // Ẩn form xác nhận cập nhật
    document.getElementById('updateConfirmation').style.display = 'none';
}
