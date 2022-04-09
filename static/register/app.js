const sign_in_btn = document.querySelector('#sign-in-btn');
const sign_up_btn_user = document.querySelector('#sign-up-btn-user');
const sign_up_btn_company = document.querySelector('#sign-up-btn-company');
const container = document.querySelector('.container');

sign_up_btn_user.addEventListener('click', () => {
  container.classList.add('sign-up-mode');
});

sign_up_btn_company.addEventListener('click', () => {
  container.classList.add('sign-up-mode');
});

sign_in_btn.addEventListener('click', () => {
  container.classList.remove('sign-up-mode');
});



document.getElementById("sign-up-btn-user").onclick = function() {
  
  document.getElementById("company").style.display = "none";
  document.getElementById("user").style.display = "block";

}

document.getElementById("sign-up-btn-company").onclick = function() {
  
  document.getElementById("user").style.display = "none";
  document.getElementById("company").style.display = "block";

}