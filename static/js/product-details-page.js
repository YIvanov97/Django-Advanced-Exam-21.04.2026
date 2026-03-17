document.addEventListener("DOMContentLoaded", function() {
    const mainImage = document.getElementById('main-image');
    const thumbnails = document.querySelectorAll(".product-details__thumbnail");
    const indicator = document.getElementById("thumbnail-indicator");
    const thumbnailsGap = 20 * 2

    function moveIndicator(target) {
        indicator.style.width = `${target.offsetWidth}px`;
        indicator.style.height = `${target.offsetHeight}px`;
        indicator.style.transform = `translate(${target.offsetLeft - thumbnailsGap}px)`;
    }

    thumbnails.forEach(el => {
        el.addEventListener("click", () => {
            mainImage.src = el.src;

            thumbnails.forEach((thumb) => thumb.classList.remove("thumbnail-active"));
            el.classList.add("thumbnail-active");

            moveIndicator(el);
        });
    });

    thumbnails[0].classList.add("thumbnail-active")
    moveIndicator(thumbnails[0]);
});