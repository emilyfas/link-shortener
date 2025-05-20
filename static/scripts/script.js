document.querySelector('#ano-footer').textContent = new Date().getFullYear();

document.getElementById('toggle-theme').addEventListener('click', () => {
  const html = document.documentElement;
  html.classList.toggle('dark');

  const isDark = html.classList.contains('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
});



document.addEventListener('DOMContentLoaded', () => {
  const menuButton = document.getElementById('menu-button');
  const mobileMenu = document.getElementById('mobile-menu');
  const openIcon = document.getElementById('menu-open-icon');
  const closeIcon = document.getElementById('menu-close-icon');

  menuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
    openIcon.classList.toggle('hidden');
    closeIcon.classList.toggle('hidden');
  });
});
