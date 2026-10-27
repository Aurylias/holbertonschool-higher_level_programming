const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItem.onclick = function () {
  const newLi = document.createElement('li');
  const liText = document.createTextNode('Item');
  newLi.appendChild(liText);
  myList.appendChild(newLi);
};
