document.addEventListener("DOMContentLoaded", function () {
    const categorySelect = document.getElementById("id_category");

    function hideAllGroups() {
        document.querySelectorAll(".details-form").forEach(group => {
            group.style.display = "none";

            group.querySelectorAll("input, select, textarea").forEach(field => {
                field.disabled = true;
                field.required = false;
            });
        });
    }

    function toggleGroups() {
        hideAllGroups();

        const selected = categorySelect.value;
        const visibleGroup = document.querySelector("." + selected + "-fields");

        if (visibleGroup) {
            visibleGroup.style.display = "block";

            visibleGroup.querySelectorAll("input, select, textarea").forEach(field => {
                field.disabled = false;

                if (field.dataset.required === "true") {
                    field.required = true;
                }
            });
        }
    }

    categorySelect.addEventListener("change", toggleGroups);
    toggleGroups();
});