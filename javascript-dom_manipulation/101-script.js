document.addEventListener('DOMContentLoaded', () => {
  const btnTranslate = document.querySelector('#btn_translate');
  const hello = document.querySelector('#hello');

  btnTranslate.onclick = function () {
    const languague = document.querySelector('#language_code').value;
    
    fetch(`https://hellosalut.stefanbohacek.com/?lang=${languague}`)
      .then((response) => response.json())
      .then((data) => {
        hello.textContent = data.hello;
      });
  };
});
