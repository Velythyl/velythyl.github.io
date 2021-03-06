(function(document) {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar');
  var checkbox = document.querySelector('#sidebar-checkbox');

  function resize(e) {
    if(screen.width >= 769) {
      checkbox.checked = true;
      toggle.style.display = "none";
      document.querySelectorAll('.container').forEach(x => x.style.margin = 0);
      document.querySelector('.wrap').style.width = Math.floor(0.75*(screen.width-sidebar.getBoundingClientRect().width))+"px";
    } else {
      checkbox.checked = false;
      toggle.style.display = null;
      document.querySelector('.wrap').style.width = null;
      document.querySelectorAll('.container').forEach(x => x.style.margin = null);
      document.addEventListener('click', function(e) {
        var target = e.target;

        if(!checkbox.checked ||
          sidebar.contains(target) ||
          (target === checkbox || target === toggle)) return;

        checkbox.checked = false;
      }, false);
    }
  }

  resize();

  window.addEventListener("resize", resize, false);
  
})(document);
