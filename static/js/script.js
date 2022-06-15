// Flash messages //
var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
  close[i].onclick = function () {
    var div = this.parentElement;
    div.style.opacity = "0";
    setTimeout(function () {
      div.style.display = "none";
    }, 600);
  };
}

// Accordian for FAQ page //
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");

    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

// Form validation for add and edit recipes //
function validate() {
  var obj1 = document.getElementById('direction_1');
  if (trimTextarea(obj1.value) == '') {
    return false;
  }
}

function trimTextarea(str) {
  return str.replace(/^\s+|\s+$/g, '');
}