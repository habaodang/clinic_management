 function showDetails(title, time, nurse, id) {
            document.getElementById('nurseName').value = nurse;
            document.getElementById('appointmentMoney').value = time;
            document.getElementById('appointmentID').value = id;
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