

// function switchTabs(e, tabName){
//   let i, tabcontent, tablinks;
//   tabcontent = document.getElementsByClassName("tabcontent");
//   for(i=0; i<tabcontent.length; i++){
//     tabcontent[i].style.display = "none";
//   }
//   tablinks = document.getElementsByClassName("tablinks");
//   for(i=0; i<tablinks.length; i++){
//     tablinks[i].className = tablinks[i].className.replace(" active", "");
//   }
//   document.getElementById(tabName).style.display = "block";
//   e.currentTarget.className += " active";
// }

<<<<<<< HEAD
console.log(2+5);
=======
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
>>>>>>> 04183062be212b961a77e0a18bf935b279a71f1f
