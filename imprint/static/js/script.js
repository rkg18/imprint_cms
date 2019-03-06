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