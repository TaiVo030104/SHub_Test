const carousel = document.getElementById('carousel');
const items = document.querySelectorAll('.carousel-item');
let index = 0;
const itemsToShow = 6;
const totalItems = items.length;

document.getElementById('next').addEventListener('click', () => {
    index = (index + 1) % totalItems;
    carousel.appendChild(carousel.firstElementChild); 
});

document.getElementById('prev').addEventListener('click', () => {
    index = (index - 1 + totalItems) % totalItems;
    carousel.prepend(carousel.lastElementChild); 
});
