document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".edit-review-button").forEach(btn => {
        btn.addEventListener("click", () => {
            const reviewId = btn.dataset.reviewId;
            const reviewContent = document.getElementById(`review-content-${reviewId}`);
            const reviewForm = document.getElementById(`edit-review-form-${reviewId}`);

            const isReviewFormHidden = getComputedStyle(reviewForm).display === "none";

            reviewForm.style.display = isReviewFormHidden ? "flex" : "none";
            reviewContent.style.display = isReviewFormHidden ? "none" : "block";
        });
    });

    document.querySelectorAll(".cancel-edit-review-button").forEach(btn => {
        btn.addEventListener("click", () => {
            const reviewId = btn.dataset.reviewId;
            const reviewContent = document.getElementById(`review-content-${reviewId}`);
            const reviewForm = document.getElementById(`edit-review-form-${reviewId}`);

            reviewForm.style.display = "none";
            reviewContent.style.display = "block";
        });
    });
})