
 document.getElementById('searchButton').addEventListener('click', function () {
        const searchType = document.getElementById('searchType').value;
        const searchInput = document.getElementById('searchInput').value.trim();
        const resultsContainer = document.getElementById('searchResults');

        // Dữ liệu mẫu giả lập
        const sampleData = {
            thuoc: [
                { id: 'MT01', name: 'Thuốc 1', unit: 'Vỉ', quantity: 1, usage: 'Uống Trước Khi Ăn' },
                { id: 'MT02', name: 'Paradol', unit: 'Viên', quantity: 2, usage: 'Uống Trước Khi Ăn' },
                { id: 'MT03', name: 'Paradol', unit: 'Hộp', quantity: 2, usage: 'Uống sau Khi Ăn' },
                { id: 'MT04', name: 'Paradol', unit: 'Vỉ', quantity: 2, usage: 'Uống Trước Khi Ăn' },
                { id: 'MT05', name: 'Paradol', unit: 'Viên', quantity: 2, usage: 'Uống Trước Khi Ăn' },
            ],
            benhnhan: [
                { id: 'BN01', name: 'Nguyễn Văn A', age: 30, address: 'Hà Nội' },
                { id: 'BN02', name: 'Trần Thị B', age: 25, address: 'Hồ Chí Minh' }
            ]
        };

        let html = '';
        if (searchInput === '') {
            html = '<p class="text-danger text-center">Vui lòng nhập từ khóa tìm kiếm!</p>';
        } else {
            const data = sampleData[searchType].filter(item =>
                Object.values(item).some(val => val.toString().toLowerCase().includes(searchInput.toLowerCase()))
            );

            if (data.length > 0) {
                html = '<table class="table table-striped table-hover">';
                html += '<thead class="table-light"><tr>';

                // Tiêu đề bảng
                if (searchType === 'thuoc') {
                    html += '<th>Mã Thuốc</th><th>Tên Thuốc</th><th>Đơn Vị</th><th>Số Lượng</th><th>Cách Dùng</th>';
                } else {
                    html += '<th>Mã Bệnh Nhân</th><th>Tên Bệnh Nhân</th><th>Tuổi</th><th>Địa Chỉ</th>';
                }
                html += '</tr></thead><tbody>';

                // Nội dung bảng
                data.forEach(item => {
                    if (searchType === 'thuoc') {
                        html += `<tr>
                                    <td>${item.id}</td>
                                    <td>${item.name}</td>
                                    <td>${item.unit}</td>
                                    <td>${item.quantity}</td>
                                    <td>${item.usage}</td>
                                 </tr>`;
                    } else {
                        html += `<tr>
                                    <td>${item.id}</td>
                                    <td>${item.name}</td>
                                    <td>${item.age}</td>
                                    <td>${item.address}</td>
                                 </tr>`;
                    }
                });
                html += '</tbody></table>';
            } else {
                html = '<p class="text-center text-warning">Không có kết quả phù hợp!</p>';
            }
        }

        resultsContainer.innerHTML = html;
    });
