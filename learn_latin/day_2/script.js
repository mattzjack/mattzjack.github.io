$(function(){
    alert("Hello, I am Vibius Vibidius Zosimus.");
    alert("pls don't check this box below because I am an innocuous script...");
    var a = prompt("enter your Latin full name:\nif you have forgotten, enter EXACTLY \"igpay atinlay\".");
    if (a == "igpay atinlay") {
      alert("remember your name!\nand pig latin is one thing that you are not going to learn about here..");
      $("#hidden").html("<h2>prologue</h2><h6>the magic of javascript</h6><p>Hopefully you didn't keep refreshing and flirt with my script a lot...</p>");
    } else if (a == null | a == "") {
      alert("at least enter something there.. whatever..");
      $("#hidden").html("<h2>prologue</h2><h6>the magic of javascript</h6><p>Hopefully you didn't keep refreshing and flirt with my script a lot...</p>");
    } else {
      alert("welcome back, " + a + ".. what a name..");
      $("#hidden").html("<h2>prologue</h2><h6>the magic of javascript</h6><p>Hopefully you didn't keep refreshing and flirt with my script a lot...</p>");
    }
});
