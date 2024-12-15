// Giả sử danh sách thông báo
const notifications = [
  'Đã cập nhật thông tin thành công',
  'Đã thay đổi mật khẩu',
  'Đã kê đơn #111'
];

// Cập nhật số lượng thông báo chưa đọc
const notificationCount = document.querySelector('.notification-count');
notificationCount.textContent = notifications.length;

// Hiển thị danh sách thông báo khi click vào nút dropdown
const dropdownMenu = document.querySelector('.dropdown-menu');

dropdownMenu.addEventListener('show.bs.dropdown', () => {
  // Xóa tất cả các phần tử con của dropdown-menu (trừ các phần tử chia ngăn)
  while (dropdownMenu.firstChild && dropdownMenu.firstChild !== dropdownMenu.lastChild) {
    dropdownMenu.removeChild(dropdownMenu.firstChild);
  }

  // Thêm các thông báo vào dropdown menu
  notifications.forEach(notification => {
    const listItem = document.createElement('li');
    const link = document.createElement('a');
    link.classList.add('dropdown-item');
    link.textContent = notification;
    listItem.appendChild(link);
    dropdownMenu.insertBefore(listItem, dropdownMenu.lastChild);
  });
});