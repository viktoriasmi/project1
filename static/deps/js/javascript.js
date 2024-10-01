document.addEventListener('DOMContentLoaded', function() {
  const menuButton = document.getElementById('menuButton');
  const menuList = document.getElementById('menuList');
  const infoButton = document.getElementById('infoButton');
  const infoList = document.getElementById('infoList');
  const profileButton = document.getElementById('profileButton');
  const profileList = document.getElementById('profileList');
  const filterButton = document.getElementById('filterButton');
  const filterList = document.querySelector('.dropdown-content-filter'); 

  menuButton.addEventListener('click', () => {
    if (menuList.style.display === 'block') {
      menuList.style.display = 'none';
    } else {
      closeAllMenus();
      menuList.style.display = 'block';
    }
  });

  infoButton.addEventListener('click', () => {
    if (infoList.style.display === 'block') {
      infoList.style.display = 'none';
    } else {
      closeAllMenus();
      infoList.style.display = 'block';
    }
  });

  profileButton.addEventListener('click', () => {
    if (profileList.style.display === 'block') {
      profileList.style.display = 'none';
    } else {
      closeAllMenus();
      profileList.style.display = 'block';
    }
  });

  filterButton.addEventListener('click', () => {
    if (filterList.style.display === 'block') {
      filterList.style.display = 'none';
    } else {
      closeAllMenus();
      filterList.style.display = 'block';
    }
  });

  function closeAllMenus() {
    menuList.style.display = 'none';
    infoList.style.display = 'none';
    profileList.style.display = 'none';
    if (filterList) {
      filterList.style.display = 'none';
    }
  }
});
