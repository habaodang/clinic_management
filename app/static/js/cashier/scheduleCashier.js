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
                    document.querySelectorAll('.date').forEach(d => d.classList.remove('active'));
                    dateDiv.classList.add('active');
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