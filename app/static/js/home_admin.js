const homeButton = document.getElementById('homeButton');
const contactButton = document.getElementById('contactButton');

const calendar = document.getElementById('calendar');
const monthYear = document.getElementById('monthYear');
const prevMonth = document.getElementById('prev-month');
const nextMonth = document.getElementById('next-month');

let today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();

const months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
];

function renderCalendar(month, year) {
    calendar.innerHTML = '';

    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    monthYear.textContent = `${months[month]} ${year}`;

    // Days of the week
    const days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    days.forEach(day => {
        const dayDiv = document.createElement('div');
        dayDiv.textContent = day;
        dayDiv.classList.add('day');
        calendar.appendChild(dayDiv);
    });

    // Blank spaces for days before the start of the month
    for (let i = 0; i < firstDay; i++) {
        const blankDiv = document.createElement('div');
        calendar.appendChild(blankDiv);
    }

    // Dates of the month
    for (let date = 1; date <= daysInMonth; date++) {
        const dateDiv = document.createElement('div');
        dateDiv.textContent = date;
        dateDiv.classList.add('date');

        if (
            date === today.getDate() &&
            month === today.getMonth() &&
            year === today.getFullYear()
        ) {
            dateDiv.classList.add('active');
        }

        dateDiv.addEventListener('click', () => {
            // Deselect all other dates
            document.querySelectorAll('.date').forEach(d => d.classList.remove('active'));

            // Mark the clicked date as active
            dateDiv.classList.add('active');

            // Save the selected date in the hidden div with id "selected-day"
            const selectedDate = `${year}-${month + 1}-${date}`;
            document.getElementById('selected-day').textContent = selectedDate;

            // Optionally, log it or perform further actions
            console.log("Ngày đã chọn:", selectedDate);
        });

        calendar.appendChild(dateDiv);
    }
}

prevMonth.addEventListener('click', () => {
    currentMonth--;
    if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
    }
    renderCalendar(currentMonth, currentYear);
});

nextMonth.addEventListener('click', () => {
    currentMonth++;
    if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
    }
    renderCalendar(currentMonth, currentYear);
});

renderCalendar(currentMonth, currentYear);

// Scroll smooth for dropdown
document.querySelector('.dropdown-menu').addEventListener('wheel', function(event) {
    event.preventDefault();
    this.scrollBy({
        top: event.deltaY,
        behavior: 'smooth'
    });
});

// Toggle dropdown icon
var dropdownMenus = document.querySelectorAll('.dropdown-toggle');
dropdownMenus.forEach(function(dropdownMenu) {
    dropdownMenu.addEventListener('click', function() {
        var dropdownIcon = this.querySelector('i');
        var isExpanded = this.getAttribute('aria-expanded') === 'true';

        if (isExpanded) {
            dropdownIcon.classList.remove('bi-chevron-down');
            dropdownIcon.classList.add('bi-chevron-up');
        } else {
            dropdownIcon.classList.remove('bi-chevron-up');
            dropdownIcon.classList.add('bi-chevron-down');
        }
    });
});

// Toggle form between login and signup
document.querySelectorAll(".toggle-form").forEach((btn) => {
    btn.addEventListener("click", (e) => {
        e.preventDefault();
        document.querySelector(".form-login").classList.toggle("active");
        document.querySelector(".form-signup").classList.toggle("active");
    });
});

// Scroll effect for header
window.addEventListener('scroll', function () {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});
