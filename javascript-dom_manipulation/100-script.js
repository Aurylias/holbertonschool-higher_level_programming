document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const myList = document.querySelector('.my_list');

  addItem.onclick = function () {
    const newLi = document.createElement('li');
    const liText = document.createTextNode('Item');
    newLi.appendChild(liText);
    myList.appendChild(newLi);
  };

  removeItem.onclick = function () {
    const liList = document.querySelectorAll('li');
    const liListLength = liList.length - 1;
    liList[liListLength].remove();
  };

  clearList.onclick = function () {
    const liList = document.querySelectorAll('li');
    liList.forEach(element => {
      element.remove();
    });
  };
});
