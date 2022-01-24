window.addEventListener('DOMContentLoaded',()=>{
    const menu = document.querySelector('#menu');
    const close = document.querySelector('#close');
    const navbar = document.querySelector('.list');
    const nav_items = document.querySelectorAll('.list a');

    menu.addEventListener('click',()=>{
        menu.style.display = 'none';
        close.classList.toggle('active');
        navbar.classList.toggle('active');
    });
    close.addEventListener('click',()=>{
        menu.style.display = 'block';
        close.classList.remove('active');
        navbar.classList.remove('active');
    });
    nav_items.forEach(item=>{
        item.addEventListener('click',()=>{
            menu.style.display = 'block';
            close.classList.remove('active');
            navbar.classList.remove('active');
        })
    })

});