alert("Hello, I am Vibius Vibidius Zosimus.");
alert("pls don't check this box below because I am an innocuous script...");
var a;
var b = true;
while(b)
{
  a = prompt("enter your Latin full name:\nif you have forgotten, enter EXACTLY \"I'm a pig\".");
  if (a == "I'm a pig")
  {
    alert("remember your name!");
    b = false;
  }
  else if (a == null | a == "")
  {
    alert("at least enter something here...");
  }
  else
  {
    alert("welcome back, " + a + "... what a name...");
    b = false;
  }
}
if (!b)
{
  document.getElementById("hidden").innerHTML = "<h2>prologue</h2><h6>the magic of javascript</h6><p>Hopefully you didn't keep refreshing and flirt with my script a lot...</p>";
}