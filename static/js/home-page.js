const categoryList = document.getElementById("category-list");
const leftButton = document.getElementById("category-scroll-left");
const rightButton = document.getElementById("category-scroll-right");

if (categoryList && leftButton && rightButton) {
    const scrollAmount = 420; // adjust based on card width + gap

    leftButton.addEventListener("click", () => {
        categoryList.scrollBy({
            left: -scrollAmount,
            behavior: "smooth",
        });
    });

    rightButton.addEventListener("click", () => {
        categoryList.scrollBy({
            left: scrollAmount,
            behavior: "smooth",
        });
    });
}