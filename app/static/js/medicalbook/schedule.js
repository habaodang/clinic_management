 function showDetails(title, time, nurse, reason) {

            document.getElementById('appointmentDate').value = time;
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
         document.getElementById("profile-picture").addEventListener("change", function(event) {
        const fileInput = event.target;
        const fileName = fileInput.files[0] ? fileInput.files[0].name : "No file selected";
        document.getElementById("file-name").textContent = fileName;
    });