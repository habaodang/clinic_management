 function addRow() {
      const table = document.getElementById("medicineTable").getElementsByTagName("tbody")[0];
      const newRow = table.insertRow();

      const data = [
        "MT0" + (table.rows.length + 1),
        `Thuốc ${table.rows.length + 1}`,
        "Viên",
        1,
        "Uống Trước Khi Ăn"
      ];

      for (let i = 0; i < data.length; i++) {
        const cell = newRow.insertCell(i);
        cell.textContent = data[i];
      }
    }

    function deleteRow() {
      const table = document.getElementById("medicineTable").getElementsByTagName("tbody")[0];
      if (table.rows.length > 0) {
        table.deleteRow(table.rows.length - 1);
      } else {
        alert("Không còn hàng nào để xóa!");
      }
    }