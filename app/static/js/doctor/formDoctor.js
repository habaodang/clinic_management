document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.card');

    // Hàm hiển thị thẻ theo filter
    const filterCards = (filter) => {
        cards.forEach(card => {
            // Corrected: Use `card` instead of `article`
            const status = card.getAttribute('data-status');

            if (filter === 'all' ||
                (filter === 'started' && status === true) ||
                (filter === 'finished' && status === false)) {
                card.classList.add('active'); // Hiển thị thẻ
            } else {
                card.classList.remove('active'); // Ẩn thẻ
            }
        });
    };

    // Hiển thị mặc định tab "All" khi trang được tải
    filterCards('all');

    // Lắng nghe sự kiện nhấn nút tab
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Xóa class active khỏi tất cả các nút
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            // Lấy trạng thái cần lọc từ data-filter
            const filter = button.getAttribute('data-filter');
            filterCards(filter);
        });
    });
});
