$(function(){
    $("#display").click(function(){
        $("#newPoem").load("./demo.txt", function(){
            alert('done');
            alert($('#newPoem').html())
        });
    });
});
