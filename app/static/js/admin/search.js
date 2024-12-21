
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
    const sampleData = {
    benhnhan: [
        {
            id: 'MS19',
            name: 'nguyễn Thị Ánh Hồng',
            dob: '01/09/2004',
            gender: 'Nữ',
            cmnd: '00000000000',
            address: 'Xã Xuân Bắc, huyện Xuân Lộc, tỉnh Đồng Nai',
            phone: '032000000',
            job: 'Sinh Viên'
        }
    ]
};

document.getElementById('searchButton').addEventListener('click', function () {
    const searchType = document.getElementById('searchType').value;
    const searchInput = document.getElementById('searchInput').value.trim();
    const resultsContainer = document.getElementById('searchResults');
    let html = '';

    if (searchInput === '') {
        html = '<p class="text-danger text-center">Vui lòng nhập từ khóa tìm kiếm!</p>';
    } else if (searchType === 'benhnhan') {
        const patient = sampleData.benhnhan.find(p => p.name.toLowerCase().includes(searchInput.toLowerCase()));

        if (patient) {
            html += `
                <div class="card text-start border-info p-3 mt-3">
                    <h5 class="bg-primary text-white py-2 rounded-left p-3 border d-inline-block">Thông Tin Bệnh Nhân</h5>
                    <p><strong>Mã Bệnh Nhân:</strong> ${patient.id}</p>
                    <p><strong>Họ và tên:</strong> ${patient.name}</p>
                    <p><strong>Ngày sinh:</strong> ${patient.dob} <strong>Giới tính:</strong> ${patient.gender}</p>
                    <p><strong>Số CMND/CCCD:</strong> ${patient.cmnd}</p>
                    <p><strong>Địa chỉ:</strong> ${patient.address}</p>
                    <p><strong>Số điện thoại:</strong> ${patient.phone}</p>
                    <p><strong>Nghề nghiệp:</strong> ${patient.job}</p>
                    <button class="btn btn-dark text-end" onclick="showMedicalHistory()">Xem Lịch Sử Bệnh Án</button>
                </div>
            `;
        } else {
            html = '<p class="text-warning text-center">Không tìm thấy bệnh nhân!</p>';
        }
    }

    resultsContainer.innerHTML = html;
});
// Hàm hiển thị lịch sử bệnh án
function showMedicalHistory() {
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = `
        <div class="card border-secondary p-3 mt-3">
            <h5 class=" bg-secondary text-end text-white py-2 rounded-left">Lịch Sử Bệnh Án</h5>
            <ul>
                <li>20/01/2024: Khám tổng quát - Kết quả bình thường</li>
                <li>15/03/2024: Khám sốt siêu vi - Đã điều trị khỏi</li>
                <li>10/05/2024: Khám đau đầu - Kết luận: Thiếu ngủ</li>
            </ul>
            <button class="btn btn-primary mt-2 text-end" onclick="showPatientInfo()">Quay Lại</button>
        </div>
    `;
}

// Hàm quay lại thông tin bệnh nhân
function showPatientInfo() {
    document.getElementById('searchButton').click();
}
