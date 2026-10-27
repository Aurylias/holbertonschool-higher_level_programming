const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

redHeader.onclick = function () {
  header.classList.add('red');
};
