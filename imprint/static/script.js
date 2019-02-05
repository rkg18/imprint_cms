function checkPageType(that) {
  if (that.value == 'landing-page')
  {
    document.getElementById("landing-page-display").style.display = "block";
    document.getElementById("product-page-display").style.display = "none";
  }
  else if(that.value == 'product-page')
  {
    document.getElementById("landing-page-display").style.display = "none";
    document.getElementById("product-page-display").style.display = "block";
  }
}

// Function changes for 'Settings'
function changeFontSize()
  {
    var e = document.getElementById("fontSize");
    var fontValue = e.options[e.selectedIndex].value;

    document.getElementById("output").style.fontSize= fontValue;
    document.getElementById("post").style.fontSize= fontValue;
  }

  function changeFontFamily()
  {
    var e = document.getElementById("fontFamily");
    var fontFamily = e.options[e.selectedIndex].value;

    document.getElementById("output").style.fontFamily= fontFamily;
  }

  function changeFontColor()
  {
    
  }