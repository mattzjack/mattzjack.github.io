$(function() {
    var iframeElement   = document.querySelector('iframe');
    var iframeElementID = iframeElement.id;
    var widget          = SC.Widget(iframeElement);
    var x = 1;

    $("#togglePlay").click(function() {
        console.log("toggle clicked");
        widget.toggle();
    });
});