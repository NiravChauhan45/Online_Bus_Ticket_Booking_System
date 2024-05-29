const formContainer = document.querySelector(".modal-body"),
  
  forgot_pwBtn = document.querySelector("#forgot_pw");


forgot_pwBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.add("active");
});
