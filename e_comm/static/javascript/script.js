// JavaScript to automatically move focus to the next box after entering a digit
document.querySelectorAll('.otp-box').forEach((box, index, boxes) => {
    box.addEventListener('input', () => {
        if (box.value.length === 1 && index < boxes.length - 1) {
            boxes[index + 1].focus();
        }
    });

    // Optionally allow the user to delete a digit by pressing backspace
    box.addEventListener('keydown', (e) => {
        if (e.key === 'Backspace' && box.value.length === 0 && index > 0) {
            boxes[index - 1].focus();
        }
    });
});

document.getElementById('confirm_password').addEventListener('input', function() {
    const password = document.getElementById('password').value;
    const confirm_pass = document.getElementById('confirm_password').value;
    const span = document.getElementById('password_match');
    console.log(password,confirm_pass)
    if (password !== confirm_pass) {
        span.style.display = 'block';
        span.innerText = "Password and confirm password do not match"
        span.style.color = 'red';
    } else {
        span.style.display = 'block';
        span.innerText = "Password and confirm password match";
        span.style.color = 'green';
    }

})

