 function showDetails(title, time, nurse, reason) {
            document.getElementById('nurseName').value = nurse;
            document.getElementById('appointmentMoney').value = time;
            document.getElementById('appointmentReason').value = reason;
            document.getElementById('detailsModal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('detailsModal').style.display = 'none';
        }

        const closeButtons = document.querySelectorAll('.close-btn');
        closeButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                e.target.closest('.appointment-card').remove();
            });
        });