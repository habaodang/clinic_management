document.addEventListener('DOMContentLoaded', function() {
    // Get the elements
    const submitButton = document.getElementById('btn-book'); // "Đặt Lịch Khám" button
    const successNotification = document.getElementById('success-notification'); // Success notification div

    // Hide success notification by default
    successNotification.style.display = 'none';

    // Handle the "Đặt Lịch Khám" button click
    submitButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent form submission

        // Show the success notification
        successNotification.style.display = 'block';
    });

    // Handle the close button (X) click in the success notification
    document.getElementById('close-notification').addEventListener('click', function() {
        // Hide the success notification when closed
        successNotification.style.display = 'none';
    });

    // Handle the "Chấp nhận" button click in the success notification
    document.getElementById('accept-notification').addEventListener('click', function() {
        // Hide the success notification after accepting
        successNotification.style.display = 'none';
    });
});
