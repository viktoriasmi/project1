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
    menuList.style.display = menuList.style.display === 'none' ? 'block' : 'none';
  });

  infoButton.addEventListener('click', () => {
    infoList.style.display = infoList.style.display === 'none' ? 'block' : 'none';
  });

  profileButton.addEventListener('click', () => {
    profileList.style.display = profileList.style.display === 'none' ? 'block' : 'none';
  });

  filterButton.addEventListener('click', () => {
    filterList.style.display = filterList.style.display === 'none' ? 'block' : 'none';
  });
});



