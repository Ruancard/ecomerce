const menu_button = document.querySelector('.header_menu')
const menu = document.querySelector('.lateral_menu')
const menu_button2 = document.querySelector('.header_liked')
const menu2 = document.querySelector('.liked_menu')

menu_button.addEventListener('click', () => {
    menu.classList.toggle('lateral_menu--active')
})

menu_button2.addEventListener('click', () => {
    menu2.classList.toggle('liked_menu--active')
})
