const profileIcon = document.getElementById('profile')
const profileDialog = document.getElementById('profile-dialog')

profileIcon.addEventListener('click', (e) => {
    e.stopPropagation()

    if (profileDialog.style.display === 'none') {
         profileDialog.style.display = 'flex'
     } else {
         profileDialog.style.display = 'none'
     }
})

document.addEventListener('click', (e) => {
    if (
        !profileDialog.contains(e.target) &&
        !profileIcon.contains(e.target)
    ) {
        profileDialog.style.display = 'none'
    }
})