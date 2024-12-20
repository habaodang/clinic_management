// Wait for DOM content to load
document.addEventListener("DOMContentLoaded", () => {
    // Tab functionality
    const tabs = document.querySelectorAll(".filter-btn");
    const cards = document.querySelectorAll(".card");

    // Function to filter cards based on tab selection
    function filterCards(filter) {
        cards.forEach((card) => {
            if (filter === "all") {
                card.style.display = "block";
            } else if (card.classList.contains(filter)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    }

    // Add click event listener for each tab
    tabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            // Remove active class from all tabs
            tabs.forEach((btn) => btn.classList.remove("active"));
            tab.classList.add("active");

            // Filter cards based on data-filter
            const filter = tab.getAttribute("data-filter");
            filterCards(filter);
        });
    });


});
