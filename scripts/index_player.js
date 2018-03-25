$(function() {
    var iframeElement    = document.querySelector('#song1');
    var iframeElement2   = document.querySelector('#song2');
    var iframeElementID  = iframeElement.id;
    var iframeElementID2 = iframeElement2.id;
    var widget           = SC.Widget(iframeElement);
    var widget2          = SC.Widget(iframeElement2);

    $("#togglePlay").click(function() {
        widget.toggle();
    });

    $("#togglePlay2").click(function() {
        widget2.toggle();
    });
});
