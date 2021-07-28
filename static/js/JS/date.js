const date = (new Date()).getFullYear();

let footerDATE = document.querySelector('#footer-date');

footerDATE.innerHTML = date;

// console.log(date);

// Header

// When the user scrolls down 50px from the top of the document, resize the header's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("scroll-head").classList.add("scroll-header")
  } else {
    document.getElementById("scroll-head").classList.remove("scroll-header")
  }
}