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

/************* Product Page  **************/
function addBulletpoint()
{
  bulletcount = document.getElementById("bulletCount").innerHTML;
  out = parseInt(bulletcount) + 1;

  if(out < 6)
  {
    var y = document.createElement("input");
    y.setAttribute("type","text");
    y.setAttribute("placeholder","Bulletpoint #" + out);
    y.setAttribute("class","form-control");
    y.required = true;
    
    document.getElementById("bulletCount").innerHTML = out;
    y.setAttribute("id", "bulletpoint" + out);
    y.setAttribute("name", "bulletpoint" + out);
    document.getElementById("newBulletpoint").appendChild(y);
  }
  else
  {
    alert("Maximum of 5 bullet points is allowed");
  }
}

function removeBulletpoint()
{
  bulletcount = document.getElementById("bulletCount").innerHTML;
  out = parseInt(bulletcount);
  if(out > 1)
  {
    var ele = document.getElementById("bulletpoint" + out);
    ele.parentNode.removeChild(ele);
    document.getElementById("bulletCount").innerHTML = out-1;
  }
  else
  {
    alert("You must have at least 1 bullet");
  }
}

/****************** Landing Page ***********************/
function addJumbotron()
{
  var isJumbotron = document.getElementById('isJumbotron');

  if(isJumbotron != null)
  {
    alert("You can only have 1 Jumbotron element!!!");
    print(isJumbotron);
  }
  else
  {
    // Creates Span Id
    var newJumbotron = document.createElement("span");
    newJumbotron.setAttribute("id","isJumbotron");
    document.getElementById("landing-page-display").appendChild(newJumbotron);

    // Heading
    var newHeading = document.createElement("input");
    newHeading.setAttribute("name","heading");
    newHeading.setAttribute("class","form-control");
    newHeading.setAttribute("id", "heading");
    newHeading.setAttribute("type","text");
    newHeading.required = true;
    document.getElementById("isJumbotron").appendChild(newHeading);

    // Sub-heading

    // Button Text

    // Button URL
  }

}