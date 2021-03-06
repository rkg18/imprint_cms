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

    // Creates Label
    var lblHeading = document.createElement("h3");
    lblHeading.innerHTML = "Heading";
    document.getElementById("isJumbotron").appendChild(lblHeading);

    // Heading
    var newHeading = document.createElement("input");
    newHeading.setAttribute("name","heading");
    newHeading.setAttribute("class","form-control");
    newHeading.setAttribute("id", "heading");
    newHeading.setAttribute("type","text");
    newHeading.setAttribute("placeholder","Enter Heading");
    newHeading.required = true;
    document.getElementById("isJumbotron").appendChild(newHeading);

    // Sub-heading
    var newSubheading = document.createElement("input");
    newSubheading.setAttribute("name","subheading");
    newSubheading.setAttribute("class","form-control");
    newSubheading.setAttribute("id", "subheading");
    newSubheading.setAttribute("type","text");
    newSubheading.setAttribute("placeholder","Enter Sub-Heading");
    newSubheading.required = true;
    document.getElementById("isJumbotron").appendChild(newSubheading);

    // Button Text
    var newButton = document.createElement("input");
    newButton.setAttribute("name","button-text");
    newButton.setAttribute("class","form-control");
    newButton.setAttribute("id", "button-text");
    newButton.setAttribute("type","text");
    newButton.setAttribute("placeholder","Enter Button Text");
    newButton.required = true;
    document.getElementById("isJumbotron").appendChild(newButton);

    // Button URL
    var newUrl = document.createElement("input");
    newUrl.setAttribute("name","button-url");
    newUrl.setAttribute("class","form-control");
    newUrl.setAttribute("id", "button-url");
    newUrl.setAttribute("type","text");
    newUrl.setAttribute("placeholder","Enter Button URL");
    document.getElementById("isJumbotron").appendChild(newUrl);

    // Seperator
    var sep = document.createElement("hr");
    document.getElementById("isJumbotron").appendChild(sep);
  }

}

function addSignup()
{
  var isSignup = document.getElementById('isSignup');

  if(isSignup != null)
  {
    alert("You can only have 1 email signup");
  }
  else
  {
    // Creates span element
    var newSignup = document.createElement("span");
    newSignup.setAttribute("id","isSignup");
    document.getElementById("landing-page-display").appendChild(newSignup);

    // Creates Label
    var lblSignup = document.createElement("h3");
    lblSignup.innerHTML = "Email Sign-Up";
    document.getElementById("isSignup").appendChild(lblSignup);

    // Email
    var newSignup = document.createElement("input");
    newSignup.setAttribute("name","signup");
    newSignup.setAttribute("class","form-control");
    newSignup.setAttribute("id", "signup");
    newSignup.setAttribute("type","text");
    newSignup.setAttribute("placeholder","Enter E-Mail Call-to-Action");
    newSignup.required = true;
    document.getElementById("isSignup").appendChild(newSignup);

    // Seperator
    var sep = document.createElement("hr");
    document.getElementById("isSignup").appendChild(sep);
  }

}

/**************************** JQuery Move Up and Down ********************************* */
$(".moveup").on("click", function() {
  var elem = $(this).closest("div");
  elem.prev().before(elem);
});

$(".movedown").on("click", function() {
  var elem = $(this).closest("div");
  elem.next().after(elem);
});

function addInfoBlock()
{
  var isInfo = document.getElementById('isInfo');

  if(isInfo != null)
  {
    alert("You can only have 1 Info Block");
  }
  else
  {
    // Creates span element
    var newInfo = document.createElement("span");
    newInfo.setAttribute("id","isInfo");
    document.getElementById("landing-page-display").appendChild(newInfo);

    // Creates Label
    var lblInfo = document.createElement("h3");
    lblInfo.innerHTML = "Information Block";
    document.getElementById("isInfo").appendChild(lblInfo);

    // Info Block
    var newInfoHeader = document.createElement("input");
    newInfoHeader.setAttribute("name","info-header");
    newInfoHeader.setAttribute("class","form-control");
    newInfoHeader.setAttribute("id", "info-header");
    newInfoHeader.setAttribute("type","text");
    newInfoHeader.setAttribute("placeholder","Enter Information Header");
    newInfoHeader.required = true;
    document.getElementById("isInfo").appendChild(newInfoHeader);

    // Info Block
    var newInfoBlock = document.createElement("input");
    newInfoBlock.setAttribute("name","info-block");
    newInfoBlock.setAttribute("class","form-control");
    newInfoBlock.setAttribute("id", "info-block");
    newInfoBlock.setAttribute("type","text");
    newInfoBlock.setAttribute("placeholder","Enter Information Block");
    newInfoBlock.required = true;
    document.getElementById("isInfo").appendChild(newInfoBlock);

    // Seperator
    var sep = document.createElement("hr");
    document.getElementById("isInfo").appendChild(sep);
  }
}

/**************************** THEMES ******************************** */
function setActiveStyleSheet(title) {
  var i, a, main;
  for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
    if(a.getAttribute("rel").indexOf("style") != -1 && a.getAttribute("title")) {
      a.disabled = true;
      if(a.getAttribute("title") == title) a.disabled = false;
    }
  }
}

function getActiveStyleSheet() {
  var i, a;
  for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
    if(a.getAttribute("rel").indexOf("style") != -1 && a.getAttribute("title") && !a.disabled) return a.getAttribute("title");
  }
  return null;
}

function getPreferredStyleSheet() {
  var i, a;
  for(i=0; (a = document.getElementsByTagName("link")[i]); i++) {
    if(a.getAttribute("rel").indexOf("style") != -1
       && a.getAttribute("rel").indexOf("alt") == -1
       && a.getAttribute("title")
       ) return a.getAttribute("title");
  }
  return null;
}

function createCookie(name,value,days) {
  if (days) {
    var date = new Date();
    date.setTime(date.getTime()+(days*24*60*60*1000));
    var expires = "; expires="+date.toGMTString();
  }
  else expires = "";
  document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for(var i=0;i < ca.length;i++) {
    var c = ca[i];
    while (c.charAt(0)==' ') c = c.substring(1,c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
  }
  return null;
}

window.onload = function(e) {
  var cookie = readCookie("style");
  var title = cookie ? cookie : getPreferredStyleSheet();
  setActiveStyleSheet(title);
}

window.onunload = function(e) {
  var title = getActiveStyleSheet();
  createCookie("style", title, 365);
}

var cookie = readCookie("style");
var title = cookie ? cookie : getPreferredStyleSheet();
setActiveStyleSheet(title);