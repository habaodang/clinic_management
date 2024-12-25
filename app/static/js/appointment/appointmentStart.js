document.addEventListener('DOMContentLoaded', function() {
    // Get the cookie consent element, CAPTCHA checkbox, and the form's submit button
    const cookieConsent = document.getElementById('cookie-consent');
    const captchaCheckbox = document.getElementById('captcha');
    const successNotification = document.getElementById('success-notification');
    const submitButton = document.querySelector('button[type="submit"]');  // "Đặt Lịch Khám" button

    // Initially hide the cookie consent pop-up
    cookieConsent.style.display = 'none';

    // Ensure the CAPTCHA checkbox is unchecked by default (reset on each page load)
    captchaCheckbox.checked = false;

    // Check if the CAPTCHA was already accepted in localStorage and set the checkbox state accordingly
    if (localStorage.getItem('captchaAccepted') === 'true') {
        // Set checkbox to checked if 'captchaAccepted' is found in localStorage
        captchaCheckbox.checked = false;
    }

    // Listen to changes in the CAPTCHA checkbox to update localStorage
    captchaCheckbox.addEventListener('change', function() {
        if (this.checked) {
            // Save the state in localStorage when checkbox is checked
            localStorage.setItem('captchaAccepted', 'true');
        } else {
            // Remove the state from localStorage when checkbox is unchecked
            localStorage.removeItem('captchaAccepted');
        }
    });

    // Handle the "Đặt Lịch Khám" button click (submit event)
    submitButton.addEventListener('click', function(event) {
        // Check if the CAPTCHA is not checked
        if (!captchaCheckbox.checked) {
            // Prevent form submission
            event.preventDefault();

            // Show the cookie consent pop-up if CAPTCHA is unchecked
            cookieConsent.style.display = 'block';
        }
    });



    // Handle the "Chấp nhận" button click
    document.getElementById('accept-cookie').addEventListener('click', function() {
        console.log("User accepted cookies");
        // Check the CAPTCHA checkbox and set it as accepted
        captchaCheckbox.checked = true;

        // Save the state in localStorage
        localStorage.setItem('captchaAccepted', 'true');

        // Hide the cookie consent pop-up
        cookieConsent.style.display = 'none';
    });

    // Handle the close button (X) click
    document.getElementById('close-cookie').addEventListener('click', function() {
        console.log("User closed cookie consent");
        // Hide the cookie consent pop-up without changing CAPTCHA state
        cookieConsent.style.display = 'none';
    });

        // Handle the "Đặt Lịch Khám" button click (submit event)
    submitButton.addEventListener('click', function(event) {
        // Check if the CAPTCHA is not checked
        if (!captchaCheckbox.checked) {
            // Prevent form submission
            event.preventDefault();

            // Show the cookie consent pop-up if CAPTCHA is unchecked
            cookieConsent.style.display = 'block';
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Get the elements
    const submitButton = document.querySelector('button[type="submit"]'); // "Đặt Lịch Khám" button
    const successNotification = document.getElementById('success-notification'); // Success notification div

    // Hide success notification by default
    successNotification.style.display = 'none';

    // Handle the "Đặt Lịch Khám" button click
    submitButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent form submission (optional)

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

document.addEventListener('DOMContentLoaded', () => {
  // Restrict date input to one day from today
  const dateInput = document.getElementById('appointment-date');
  const today = new Date();
  const tomorrow = new Date(today);
  tomorrow.setDate(today.getDate());
  dateInput.min = tomorrow.toISOString().split('T')[0];

  // Form validation
  const form = document.querySelector('form');
  form.addEventListener('submit', (event) => {
    const date = dateInput.value;
    const time = document.getElementById('appointment-time').value;
    const location = document.getElementById('clinic-room').value;
    const package = document.getElementById('doctor').value;
    const captcha = document.getElementById('captcha').checked;
  });
});
