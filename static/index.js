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

const controls = document.querySelectorAll(".control");
let currentItem = 0;
const items = document.querySelectorAll(".item");
const maxItems = items.length;

controls.forEach((control) => {
  control.addEventListener("click", (e) => {
    isLeft = e.target.classList.contains("arrow-left");


    if (isLeft) {
      currentItem -= 1;
    } else {
      currentItem += 1;
    }

    if (currentItem >= maxItems) {
      currentItem = 0;
    }

    if (currentItem < 0) {
      currentItem = maxItems - 1;
    }

    items[currentItem].scrollIntoView({
      behavior: "smooth",
      inline: "center"
    });
  });
});

