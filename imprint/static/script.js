function checkPageType(that) {
  if (that.value == 'landing-page')
  {
    document.getElementById("landing-page-display").style.display = "block";
  }
  else if(that.value == 'product-page')
  {
    document.getElementById("landing-page-display").style.display = "none";
  }
}
