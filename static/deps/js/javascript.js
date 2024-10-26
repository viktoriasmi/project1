document.addEventListener('DOMContentLoaded', function() {
  const menuButton = document.getElementById('menuButton');
  const menuList = document.getElementById('menuList');
  const infoButton = document.getElementById('infoButton');
  const infoList = document.getElementById('infoList');
  const profileButton = document.getElementById('profileButton');
  const profileList = document.getElementById('profileList');
  const filterButton = document.getElementById('filterButton');
  const filterList = document.querySelector('.dropdown-content-filter'); 

  // Обработка меню
  if (menuButton && menuList) {
    menuButton.addEventListener('click', () => {
      if (menuList.style.display === 'block') {
        menuList.style.display = 'none';
      } else {
        closeAllMenus();
        menuList.style.display = 'block';
      }
    });
  }

  // Обработка информации
  if (infoButton && infoList) {
    infoButton.addEventListener('click', () => {
      if (infoList.style.display === 'block') {
        infoList.style.display = 'none';
      } else {
        closeAllMenus();
        infoList.style.display = 'block';
      }
    });
  }

  // Обработка профиля
  if (profileButton && profileList) {
    profileButton.addEventListener('click', () => {
      if (profileList.style.display === 'block') {
        profileList.style.display = 'none';
      } else {
        closeAllMenus();
        profileList.style.display = 'block';
      }
    });
  }

  // Обработка фильтра
  if (filterButton && filterList) {
    filterButton.addEventListener('click', () => {
      if (filterList.style.display === 'block') {
        filterList.style.display = 'none';
      } else {
        closeAllMenus();
        filterList.style.display = 'block';
      }
    });
  }

  function closeAllMenus() {
    if (menuList) menuList.style.display = 'none';
    if (infoList) infoList.style.display = 'none';
    if (profileList) profileList.style.display = 'none';
    if (filterList) filterList.style.display = 'none';
  }
});
