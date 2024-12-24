// Danh sách bác sĩ mẫu
const doctors = [
    "Bác sĩ Nguyễn Văn A",
    "Bác sĩ Trần Thị B",
    "Bác sĩ Lê Văn C",
    "Bác sĩ Phạm Thị D",
    "Bác sĩ Hoàng Văn E"
];

const searchIconBtn = document.getElementById('search-icon-btn');
const searchContainer = document.getElementById('search-container');
const searchInput = document.getElementById('search-doctor');
const searchResults = document.getElementById('search-results');
const editableDate = document.getElementById('editable-date');

// Hiển thị/ẩn khối tìm kiếm khi nhấn vào biểu tượng tìm kiếm
searchIconBtn.addEventListener('click', () => {
    searchContainer.classList.toggle('d-none'); // Hiện/ẩn khối tìm kiếm
    searchInput.focus(); // Tự động focus vào ô tìm kiếm khi mở
});

// Xử lý tìm kiếm bác sĩ
searchInput.addEventListener('input', () => {
    const query = searchInput.value.toLowerCase();
    if (query.trim() === "") {
        searchResults.classList.add('d-none');
        return;
    }

    // Lọc danh sách bác sĩ theo từ khóa
    const filteredDoctors = doctors.filter(doctor =>
        doctor.toLowerCase().includes(query)
    );

    // Hiển thị kết quả
    if (filteredDoctors.length > 0) {
        searchResults.classList.remove('d-none');
        searchResults.innerHTML = filteredDoctors
            .map(doctor => `<div>${doctor}</div>`)
            .join('');
    } else {
        searchResults.innerHTML = `<div>Không tìm thấy bác sĩ</div>`;
    }
});

// Chọn bác sĩ từ danh sách kết quả tìm kiếm
searchResults.addEventListener('click', (event) => {
    if (event.target.tagName === 'DIV') {
        editableDate.textContent = event.target.textContent;
        searchInput.value = '';
        searchResults.classList.add('d-none');
        searchContainer.classList.add('d-none'); // Ẩn khối tìm kiếm sau khi chọn
    }
});

// Ẩn kết quả khi click ra ngoài
document.addEventListener('click', (event) => {
    if (!event.target.closest('.form-group')) {
        searchResults.classList.add('d-none');
        searchContainer.classList.add('d-none'); // Ẩn khối tìm kiếm khi click ngoài
    }
});
function goBack() {
    window.history.back();
}