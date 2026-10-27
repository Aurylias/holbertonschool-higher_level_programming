const header = document.querySelector('header');
const updateHeader = document.querySelector('#update_header');

updateHeader.onclick = function () {
  header.textContent = 'New Header !!!';
};
