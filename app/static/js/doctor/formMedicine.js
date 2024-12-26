// Chọn thuốc từ bảng tạm thời và hiển thị thông tin chi tiết
function selectMedicine(code) {
  // Find the medicine object in the medicines array based on the selected code
  const medicine = medicines.find(m => m.id == code);  // Assuming medicines is available globally

  if (medicine) {
    document.getElementById("medicineName").value = medicine.name;
    document.getElementById("medicineUnit").value = medicine.unit;
    document.getElementById("medicineCode").value = code;
    document.getElementById("medicineEffect").value = medicine.effect;
    document.getElementById("medicineUsage").value = medicine.usage;
    document.getElementById("infoContainer").style.display = "block";  // Hiển thị thông tin thuốc
    document.getElementById("medicineTable-test").style.display = "none";  // Ẩn bảng thuốc tạm thời
  }
}
