$(function(){
    $("#newPoem").load("./tpotd/index.html .poem:first");
    if ('12345'.indexOf(new Date().getDay()) != -1) {
        $('#words').hide();
    }
});
