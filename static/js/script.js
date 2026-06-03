document.addEventListener("DOMContentLoaded", () => {
    // 1. Form Validation Logic
    const form = document.getElementById("bookingForm");

    if(form) {
        const nameInput = document.getElementById("fullName");
        const passportInput = document.getElementById("passport");
        const submitButton = document.getElementById("submitButton");

        // Real-time Validation Listeners
        if(nameInput) nameInput.addEventListener("input", () => { validateName(); updateButton(); });
        if(passportInput) passportInput.addEventListener("input", () => { validatePassport(); updateButton(); });

        function setError(inputId, message) {
            const error = document.getElementById(`err-${inputId}`);
            if (error) error.textContent = message;
        }

        function clearError(inputId) {
            const error = document.getElementById(`err-${inputId}`);
            if (error) error.textContent = "";
        }

        function validateName() {
            const value = nameInput.value.trim();
            if (value === "") {
                setError("fullName", "Full name is required.");
                return false;
            }
            clearError("fullName");
            return true;
        }

        function validatePassport() {
            const value = passportInput.value.trim();
            const pattern = /^[A-Z0-9]{6,9}$/; // 6-9 AlphaNumeric characters

            if (value === "") {
                setError("passport", "Passport number is required.");
                return false;
            }
            if (!pattern.test(value)) {
                setError("passport", "Invalid passport (6-9 alphanumeric chars).");
                return false;
            }
            clearError("passport");
            return true;
        }

        function updateButton() {
            const isNameValid = validateName();
            const isPassportValid = validatePassport();

            // Only enable button if all fields are valid
            if (isNameValid && isPassportValid) {
                submitButton.disabled = false;
            } else {
                submitButton.disabled = true;
            }
        }
    }

    // 2. Extra Website Feature (Dynamic Promo Message)
    // This runs on any page with a main title or specific ID
    const headerTitle = document.querySelector('.header-right h1');
    if(headerTitle) {
        const promos = [" - Fly High!", " - Best Prices", " - Book Now"];
        let index = 0;

        setInterval(() => {
            const baseText = "SkyTravel";
            headerTitle.textContent = baseText + promos[index];
            index = (index + 1) % promos.length;
        }, 3000); // Changes every 3 seconds
    }
});