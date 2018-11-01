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

function changeFontSize(that) {
  if (that.value == 16)
  {
    document.getElementById("base").style.fontSize = "16px";
  }
  else if(that.value == 18)
  {
    document.getElementById("base").style.fontSize = "18px";
  }
}
