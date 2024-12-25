document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".form-group");
    let fileInput = document.getElementById("profile-picture"); // Sử dụng let để gán lại input
    const avatarPreview = document.getElementById("avatar-preview");
    const uploadLabel = document.getElementById("upload-label");
    const changeAvatarBtn = document.getElementById("change-avatar-btn");

    // Hàm xử lý khi file được chọn
    function handleFileChange(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                avatarPreview.src = e.target.result; // Gắn ảnh vào thẻ img
                avatarPreview.style.display = "block"; // Hiển thị ảnh preview
                changeAvatarBtn.style.display = "block"; // Hiển thị nút "Thay đổi ảnh"
                uploadLabel.style.display = "none"; // Ẩn nhãn "Upload your photo"
            };

            reader.readAsDataURL(file); // Đọc file
        }
    }

    // Gắn sự kiện change cho input ban đầu
    fileInput.addEventListener("change", handleFileChange);

    // Hàm xử lý khi nhấn "Thay đổi ảnh"
    changeAvatarBtn.addEventListener("click", () => {
        // Tạo một input file mới
        const newFileInput = document.createElement("input");
        newFileInput.type = "file";
        newFileInput.id = "profile-picture";
        newFileInput.name = "profile-picture";
        newFileInput.accept = "image/*";
        newFileInput.style.display = "none";

        // Thay thế input cũ bằng input mới
        container.replaceChild(newFileInput, fileInput);

        // Gán input mới vào biến fileInput
        fileInput = newFileInput;

        // Gắn lại sự kiện change cho input mới
        fileInput.addEventListener("change", handleFileChange);

        // Reset giao diện
        avatarPreview.style.display = "none"; // Ẩn ảnh
        changeAvatarBtn.style.display = "none"; // Ẩn nút "Thay đổi ảnh"
        uploadLabel.style.display = "block"; // Hiển thị lại nhãn
    });
});

 function showDetails(title, time, nurse, reason) {
            document.getElementById('nurseName').value = nurse;
            document.getElementById('appointmentDate').value = time;
            document.getElementById('appointmentReason').value = reason;
            document.getElementById('detailsModal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('detailsModal').style.display = 'none';
        }

function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("collapsed");
}

// SIDEBAR
const menuItems = document.querySelectorAll('.menu-item');

// THEME
const theme = document.querySelector('#theme');
const themeModal = document.querySelector('.customize-theme');
const fontSizes = document.querySelectorAll('.choose-size span');
const root = document.querySelector(':root');
const colorPalette = document.querySelectorAll('.choose-color span');
const Bg1 = document.querySelector('.bg-1');
const Bg2 = document.querySelector('.bg-2');
const Bg3 = document.querySelector('.bg-3');

// SIDEBAR
// Remove active class from all menu items
document.addEventListener('DOMContentLoaded', () => {
    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            menuItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
        });
    });

    // Apply saved font size
    const savedFontSize = localStorage.getItem('fontSize');
    if (savedFontSize) {
        document.querySelector('html').style.fontSize = savedFontSize;
    }

    // Apply saved primary color
    const savedPrimaryHue = localStorage.getItem('primaryHue');
    if (savedPrimaryHue) {
        root.style.setProperty('--primary-color-hue', savedPrimaryHue);
    }

    // Apply saved background
    const savedBackground = localStorage.getItem('background');
    if (savedBackground === 'bg1') {
        Bg1.classList.add('active');
    } else if (savedBackground === 'bg2') {
        Bg2.classList.add('active');
        root.style.setProperty('--dark-color-lightness', localStorage.getItem('darkColorLightness'));
        root.style.setProperty('--white-color-lightness', localStorage.getItem('whiteColorLightness'));
        root.style.setProperty('--light-color-lightness', localStorage.getItem('lightColorLightness'));
    } else if (savedBackground === 'bg3') {
        Bg3.classList.add('active');
        root.style.setProperty('--dark-color-lightness', localStorage.getItem('darkColorLightness'));
        root.style.setProperty('--white-color-lightness', localStorage.getItem('whiteColorLightness'));
        root.style.setProperty('--light-color-lightness', localStorage.getItem('lightColorLightness'));
    }
});

// THEME CUSTOMIZATION
// Opens modal
function openThemeModal() {
    themeModal.style.display = 'grid';
}

// Close modal
const closeThemeModal = (e) => {
    if (e.target.classList.contains('customize-theme')) {
        themeModal.style.display = 'none';
    }
};

themeModal.addEventListener('click', closeThemeModal);
theme.addEventListener('click', openThemeModal);

// --------FONTS-----------
// Remove active class from span or font size selectors
const removeSizeSelector = () => {
    fontSizes.forEach(size => {
        size.classList.remove('active');
    });
};

fontSizes.forEach(size => {
    size.addEventListener('click', () => {
        removeSizeSelector();
        let fontSize;
        size.classList.add('active');
        if (size.classList.contains('font-size-1')) {
            fontSize = '10px';
        } else if (size.classList.contains('font-size-2')) {
            fontSize = '13px';
        } else if (size.classList.contains('font-size-3')) {
            fontSize = '16px';
        } else if (size.classList.contains('font-size-4')) {
            fontSize = '19px';
        } else if (size.classList.contains('font-size-5')) {
            fontSize = '22px';
        }
        document.querySelector('html').style.fontSize = fontSize;
        localStorage.setItem('fontSize', fontSize); // Save to localStorage
    });
});

// -------------COLOR---------------
// Remove active class from colors
const changeActiveColorClass = () => {
    colorPalette.forEach(colorPicker => {
        colorPicker.classList.remove('active');
    });
};

// Changes colors
colorPalette.forEach(color => {
    color.addEventListener('click', () => {
        let primaryHue;
        changeActiveColorClass();
        if (color.classList.contains('color-1')) {
            primaryHue = 252;
        } else if (color.classList.contains('color-2')) {
            primaryHue = 52;
        } else if (color.classList.contains('color-3')) {
            primaryHue = 352;
        } else if (color.classList.contains('color-4')) {
            primaryHue = 152;
        } else if (color.classList.contains('color-5')) {
            primaryHue = 202;
        }
        color.classList.add('active');
        root.style.setProperty('--primary-color-hue', primaryHue);
        localStorage.setItem('primaryHue', primaryHue); // Save to localStorage
    });
});

// ----------------BACKGROUND----------------
let lightColorLightness;
let whiteColorLightness;
let darkColorLightness;

// Change background color
const changeBG = () => {
    root.style.setProperty('--light-color-lightness', lightColorLightness);
    root.style.setProperty('--white-color-lightness', whiteColorLightness);
    root.style.setProperty('--dark-color-lightness', darkColorLightness);
};

Bg1.addEventListener('click', () => {
    Bg1.classList.add('active');
    Bg2.classList.remove('active');
    Bg3.classList.remove('active');
    localStorage.setItem('background', 'bg1');
    window.location.reload();
});

Bg2.addEventListener('click', () => {
    darkColorLightness = '95%';
    whiteColorLightness = '20%';
    lightColorLightness = '15%';
    Bg2.classList.add('active');
    Bg1.classList.remove('active');
    Bg3.classList.remove('active');
    localStorage.setItem('background', 'bg2');
    localStorage.setItem('darkColorLightness', darkColorLightness);
    localStorage.setItem('whiteColorLightness', whiteColorLightness);
    localStorage.setItem('lightColorLightness', lightColorLightness);
    changeBG();
});

Bg3.addEventListener('click', () => {
    darkColorLightness = '95%';
    whiteColorLightness = '10%';
    lightColorLightness = '0%';
    Bg3.classList.add('active');
    Bg1.classList.remove('active');
    Bg2.classList.remove('active');
    localStorage.setItem('background', 'bg3');
    localStorage.setItem('darkColorLightness', darkColorLightness);
    localStorage.setItem('whiteColorLightness', whiteColorLightness);
    localStorage.setItem('lightColorLightness', lightColorLightness);
    changeBG();
});
