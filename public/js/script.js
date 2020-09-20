(function(document) {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar');
  var checkbox = document.querySelector('#sidebar-checkbox');
  
  if(screen.width >= 769) {
    checkbox.checked = true;
    checkbox.style.display = "none";
    toggle.style.display = "none";
    document.querySelector('.container').style.margin = 0;
  } else {

    document.addEventListener('click', function(e) {
      var target = e.target;

      if(!checkbox.checked ||
         sidebar.contains(target) ||
         (target === checkbox || target === toggle)) return;

      checkbox.checked = false;
    }, false);
  }
})(document);
