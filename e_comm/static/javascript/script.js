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



