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
