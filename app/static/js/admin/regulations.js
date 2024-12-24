const drugList = [
    {
        name: "Paracetamol",
        code: "P123",
        type: "Thuốc giảm đau",
        unit: "Viên",
        quantity: 100,
        usage: "Uống 1 viên mỗi 4-6 giờ",
    },
    {
        name: "Ibuprofen",
        code: "I456",
        type: "Thuốc chống viêm",
        unit: "Viên",
        quantity: 50,
        usage: "Uống 1 viên mỗi 8 giờ",
    },
    {
        name: "Amoxicillin",
        code: "A789",
        type: "Kháng sinh",
        unit: "Viên",
        quantity: 200,
        usage: "Uống 1 viên mỗi 6 giờ",
    }
];

// Xử lý sự kiện khi người dùng bấm nút Tìm kiếm
document.getElementById('searchButton').addEventListener('click', function() {
    const searchTerm = document.getElementById('searchInput').value.trim().toLowerCase();
    const resultContainer = document.getElementById('searchResults');
    const resultTableBody = resultContainer.querySelector('tbody');
    const noResultsMessage = document.getElementById('noResultsMessage');

    if (searchTerm) {
        const results = drugList.filter(drug =>
            drug.name.toLowerCase().includes(searchTerm) || drug.code.toLowerCase().includes(searchTerm)
        );

        resultTableBody.innerHTML = ''; // Xóa kết quả cũ

        if (results.length > 0) {
            resultContainer.style.display = 'block'; // Hiển thị bảng kết quả tìm kiếm
            noResultsMessage.style.display = 'none'; // Ẩn thông báo "Vui lòng nhập..."

            results.forEach(drug => {
                const row = document.createElement('tr');

                row.innerHTML = `
                    <td>${drug.name}</td>
                    <td>${drug.code}</td>
                    <td>${drug.type}</td>
                    <td>${drug.usage}</td>
                    <td>${drug.unit}</td>
                    <td>
                        <button class="btn btn-warning btn-edit" data-id="${drug.code}">Sửa</button>
                        <button class="btn btn-danger btn-delete" data-id="${drug.code}">Xóa</button>
                        <button class="btn btn-success btn-confirm" data-id="${drug.code}">Xác nhận</button>
                    </td>
                `;

                resultTableBody.appendChild(row);
            });
        } else {
            resultContainer.style.display = 'none'; // Ẩn bảng nếu không có kết quả
            noResultsMessage.style.display = 'block'; // Hiển thị lại thông báo "Vui lòng nhập..."
             noResultsMessage.innerHTML = '<p class="text-center text-danger font-weight-bold">Không có loại thuốc phù hợp</p>';
        }
    } else {
         resultContainer.style.display = 'block';
        noResultsMessage.style.display = 'none';
    }
});

// Sửa lại đoạn xử lý sự kiện nút "Sửa"
document.getElementById('searchResults').addEventListener('click', function(event) {
    if (event.target && event.target.classList.contains('btn-edit')) {
        const drugCode = event.target.getAttribute('data-id');
        const drug = drugList.find(d => d.code === drugCode);

        if (drug) {
            // Điền thông tin thuốc vào form
            document.getElementById('drugName').value = drug.name;
            document.getElementById('drugCode').value = drug.code;
            document.getElementById('drugType').value = drug.type;
            document.getElementById('drugUsage').value = drug.usage;
            document.getElementById('drugUnit').value = drug.unit;

            // Hiển thị modal và lớp phủ mờ
            document.getElementById('drugDetailsBlock').style.display = 'block'; // Mở modal
            document.querySelector('.modal-overlay').style.display = 'block'; // Mở lớp phủ mờ
        }
    }
});

// Đóng modal khi nhấn nút "Hủy" hoặc ngoài modal
document.getElementById('cancelButton').addEventListener('click', function() {
    closeModal();
});

// Đóng modal khi nhấn nút "Lưu"
document.getElementById('saveButton').addEventListener('click', function() {
    closeModal();
});

// Đóng modal và ẩn lớp phủ mờ
function closeModal() {
    document.getElementById('drugDetailsBlock').style.display = 'none'; // Ẩn modal đúng
    document.querySelector('.modal-overlay').style.display = 'none'; // Ẩn lớp phủ mờ
}
// Xử lý sự kiện khi bấm nút "Xóa"
document.getElementById('searchResults').addEventListener('click', function(event) {
    if (event.target && event.target.classList.contains('btn-delete')) {
        const drugCode = event.target.getAttribute('data-id');

        // Tìm thuốc trong drugList và xóa nó
        const drugIndex = drugList.findIndex(d => d.code === drugCode);

        if (drugIndex !== -1) {
            // Xóa thuốc khỏi drugList
            drugList.splice(drugIndex, 1);

            // Cập nhật lại bảng kết quả sau khi xóa
            updateSearchResults();
        }
    }
});

// Hàm cập nhật lại kết quả tìm kiếm sau khi xóa thuốc
function updateSearchResults() {
    const searchTerm = document.getElementById('searchInput').value.trim().toLowerCase();
    const resultContainer = document.getElementById('searchResults');
    const resultTableBody = resultContainer.querySelector('tbody');
    const noResultsMessage = document.getElementById('noResultsMessage');

    if (searchTerm) {
        const results = drugList.filter(drug =>
            drug.name.toLowerCase().includes(searchTerm) || drug.code.toLowerCase().includes(searchTerm)
        );

        resultTableBody.innerHTML = ''; // Xóa kết quả cũ

        if (results.length > 0) {
            resultContainer.style.display = 'block'; // Hiển thị bảng kết quả tìm kiếm
            noResultsMessage.style.display = 'none'; // Ẩn thông báo không có kết quả

            results.forEach(drug => {
                const row = document.createElement('tr');

                row.innerHTML = `
                    <td>${drug.name}</td>
                    <td>${drug.code}</td>
                    <td>${drug.type}</td>
                    <td>${drug.usage}</td>
                    <td>${drug.unit}</td>
                    <td>
                        <button class="btn btn-warning btn-edit" data-id="${drug.code}">Sửa</button>
                        <button class="btn btn-danger btn-delete" data-id="${drug.code}">Xóa</button>
                        <button class="btn btn-success btn-confirm" data-id="${drug.code}">Xác nhận</button>
                    </td>
                `;

                resultTableBody.appendChild(row);
            });
        } else {
            resultContainer.style.display = 'none'; // Ẩn bảng nếu không có kết quả
            noResultsMessage.style.display = 'block'; // Hiển thị lại thông báo không có kết quả
        }
    } else {
        resultContainer.style.display = 'none'; // Ẩn bảng nếu từ khóa tìm kiếm rỗng
        noResultsMessage.style.display = 'block'; // Hiển thị lại thông báo không có kết quả
    }
}


