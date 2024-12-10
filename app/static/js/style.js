 window.addEventListener('scroll', function () {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
 document.querySelector('.dropdown-menu').addEventListener('wheel', function(event) {
      event.preventDefault();
      this.scrollBy({
        top: event.deltaY,
        behavior: 'smooth'
      });
    });

// Lắng nghe sự kiện khi dropdown được mở hoặc đóng
var dropdownMenus = document.querySelectorAll('.dropdown-toggle');
dropdownMenus.forEach(function(dropdownMenu) {
  dropdownMenu.addEventListener('click', function() {
    var dropdownIcon = this.querySelector('i');
    var isExpanded = this.getAttribute('aria-expanded') === 'true';

    // Thay đổi icon khi dropdown mở hoặc đóng
    if (isExpanded) {
      dropdownIcon.classList.remove('bi-chevron-down');
      dropdownIcon.classList.add('bi-chevron-up'); // Mũi tên lên khi mở
    } else {
      dropdownIcon.classList.remove('bi-chevron-up');
      dropdownIcon.classList.add('bi-chevron-down'); // Mũi tên xuống khi đóng
    }
  });
});
document.getElementById("playVideoBtn").addEventListener("click", function() {
        // Hiển thị video
        document.getElementById("videoContainer").style.display = "block";
    });

document.querySelectorAll(".toggle-form").forEach((btn) => {
  btn.addEventListener("click", (e) => {
    e.preventDefault();
    document.querySelector(".form-login").classList.toggle("active");
    document.querySelector(".form-signup").classList.toggle("active");
  });
});



document.getElementById('scrollButton').addEventListener('click', function () {
            document.getElementById('section2').scrollIntoView({ behavior: 'smooth' });
        });

document.getElementById('homeButton').addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Cuộn mượt
        });
    });