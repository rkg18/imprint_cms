/********* Changes Font Size and Family **********/
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