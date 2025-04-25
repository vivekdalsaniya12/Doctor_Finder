function validateForm() {
    let isValid = true;

    // Input values
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document.getElementById("confirm_password").value.trim();

    // Error spans
    const nameError = document.getElementById("nameError");
    const emailError = document.getElementById("emailError");
    const phoneError = document.getElementById("phoneError");
    const passwordError = document.getElementById("passwordError");
    const confirmPasswordError = document.getElementById("confirmPasswordError");

    // Reset errors
    nameError.innerHTML = "";
    emailError.innerHTML = "";
    phoneError.innerHTML = "";
    passwordError.innerHTML = "";
    confirmPasswordError.innerHTML = "";

    // Name validation
    if (name === "") {
        nameError.innerHTML = "Name is required";
        isValid = false;
    }

    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email === "") {
        emailError.innerHTML = "Email is required";
        isValid = false;
    } else if (!emailPattern.test(email)) {
        emailError.innerHTML = "Invalid email format";
        isValid = false;
    }

    // Phone validation (10 digits)
    const phonePattern = /^[0-9]{10}$/;
    if (phone === "") {
        phoneError.innerHTML = "Phone number is required";
        isValid = false;
    } else if (!phonePattern.test(phone)) {
        phoneError.innerHTML = "Phone number must be 10 digits";
        isValid = false;
    }

    // Password validation
    if (password.length < 6) {
        passwordError.innerHTML = "Password must be at least 6 characters";
        isValid = false;
    }

    // Confirm Password validation
    if (confirmPassword !== password) {
        confirmPasswordError.innerHTML = "Passwords do not match";
        isValid = false;
    }

    return isValid;
}
