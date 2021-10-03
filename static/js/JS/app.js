let DropDowns = document.querySelectorAll(".child-main");
let CloseDiv = document.querySelector(".close-drop");

function toggleDrop(e) {
  console.log(e);

  let Menu = e.target.parentElement.querySelector(".child-drop");
  closeAllDrops(Menu);
  if (Menu.classList.contains("show-drop")) {
    Menu.classList.remove("show-drop");
    CloseDiv.classList.remove("show-drop");
  } else {
    Menu.classList.add("show-drop");
    CloseDiv.classList.add("show-drop");
  }
}

function closeAllDrops(Menu) {
  let DS = document.querySelectorAll(".child-drop");

  if (!(Menu instanceof HTMLElement)) {
    DS.forEach((D) => D.classList.remove("show-drop"));
    CloseDiv.classList.remove('show-drop');
    return 
  }
  let contain = Menu.classList.contains("show-drop");
  DS.forEach((D) => D.classList.remove("show-drop"));
  if (contain) {
    Menu.classList.add("show-drop");
    CloseDiv.classList.add("show-drop");
  }
}

DropDowns.forEach((DropDown) => {
  DropDown.addEventListener("click", toggleDrop);
});
CloseDiv.addEventListener("click", closeAllDrops);

console.log(5+6)