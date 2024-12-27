


// Mở form tìm kiếm thuốc
function openForm() {
  document.getElementById("overlay").style.display = "flex"; // Mở overlay
  document.getElementById("medicineTable-test").style.display = "table";  // Hiển thị bảng thuốc tìm kiếm (bao gồm tiêu đề)
  document.getElementById("infoContainer").style.display = "none";  // Ẩn thông tin chi tiết
  document.getElementById("medicineCode").value = "";  // Xóa mã thuốc đã nhập
}
// Đóng form tìm kiếm
function closeForm() {
  document.getElementById("overlay").style.display = "none";  // Ẩn overlay
  document.getElementById("medicineTable-test").style.display = "none";  // Ẩn bảng thuốc tìm kiếm (bao gồm tiêu đề và dữ liệu)
}


// Tìm kiếm thuốc và hiển thị trong bảng tạm thời
function searchMedicine() {
  const inputCode = document.getElementById("medicineCode").value.trim().toUpperCase();
  const codePrefix = inputCode.slice(0, 2); // Lấy phần đầu mã (ví dụ: "PA" từ "PA01")

  const table = document.getElementById("medicineTable-test-body");
  table.innerHTML = ""; // Xóa các kết quả tìm kiếm trước đó

  let found = false;

  // Duyệt qua tất cả thuốc và tìm mã có cùng tiền tố
  for (const [code, medicine] of Object.entries(medicineData)) {
    if (code.startsWith(codePrefix)) {
      found = true;
      const row = table.insertRow();
      const stt = table.rows.length;

      row.innerHTML =
        `<td>${stt}</td>
         <td>${code}</td>
         <td>${medicine.name}</td>
         <td>${medicine.unit}</td>
         <td><button onclick="selectMedicine('${code}')">Xác Nhận</button></td>`;
    }
  }

  if (!found) {
    alert("Không tìm thấy thuốc!");
  }
}

// Chọn thuốc từ bảng tạm thời và hiển thị thông tin chi tiết
function selectMedicine(code) {
  const medicine = medicineData[code];
  if (medicine) {
    document.getElementById("medicineName").value = medicine.name;
    document.getElementById("medicineUnit").value = medicine.unit;
    document.getElementById("medicineCode").value = code;
    document.getElementById("infoContainer").style.display = "block";  // Hiển thị thông tin thuốc
    document.getElementById("medicineTable-test").style.display = "none";  // Ẩn bảng thuốc tạm thời
  }
}

/// Thêm thuốc vào bảng chính và đóng form tìm kiếm
function addMedicine() {
  const code = document.getElementById("medicineCode").value.toUpperCase();
  const name = document.getElementById("medicineName").value;
  const unit = document.getElementById("medicineUnit").value;
  const quantity = document.getElementById("medicineQuantity").value;
  const effect = medicineData[code].effect;
  const usage = medicineData[code].usage;

  const table = document.getElementById("medicineTable");
  const row = table.insertRow();
  const stt = table.rows.length;

  row.innerHTML =
    `<td>${stt}</td>
     <td>${code}</td>
     <td>${name}</td>
     <td>${unit}</td>
     <td>${quantity}</td>
     <td>${effect}</td>
     <td>${usage}</td>
     <td><button class="update-btn" onclick="showUpdateConfirmation(this)">Cập Nhật</button></td>`;

  // Đóng form tìm kiếm sau khi xác nhận
  closeForm();  // Ẩn overlay và bảng tìm kiếm
}
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
// Đóng modal cập nhật và đảm bảo nút "Cập Nhật" và "Xóa Tất Cả" không bị vô hiệu hóa
function closeUpdateConfirmation() {
  document.getElementById("updateConfirmation").style.display = "none";  // Ẩn modal cập nhật
  document.getElementById("overlay").style.display = "none"; // Đảm bảo overlay không ảnh hưởng đến các phần tử khác
}

