document.addEventListener("DOMContentLoaded", function() {
    let searchInput = document.getElementById("search-input");
    let searchButton = document.getElementById("search-button");

    searchButton.addEventListener("click", function(event) {
        if (searchInput.value.trim().length < 4) {
            event.preventDefault();
            alert("Enter a keyword of length greater than or equal to 4 before searching.");
        }
    });
});
