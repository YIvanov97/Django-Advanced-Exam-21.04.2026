document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById('profile-picture')
    const preview = document.getElementById('profile-picture-preview')
    const placeholder = document.getElementById('profile-picture-placeholder')
    const clearButton = document.getElementById('clear-profile-picture')

    function updateElements(hasImage) {
        clearButton.style.display = hasImage ? "block" : "none";
        preview.style.display = hasImage ? "block" : "none";
        placeholder.style.display = hasImage ? "none" : "block";
    }

    const hasProfileImage = preview.getAttribute("src") && preview.getAttribute("src").trim() !== "";
    updateElements(hasProfileImage)

    input.addEventListener('change', function () {
        const file = input.files[0]

        if (!file) return;

        preview.src = URL.createObjectURL(file)
        updateElements(true)
    });

    clearButton.addEventListener('click', function () {
        input.value = ""
        preview.removeAttribute("src")
        updateElements(false)
    });
});