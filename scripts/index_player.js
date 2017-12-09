$(function() {
    var iframeElement   = document.querySelector('iframe');
    var iframeElementID = iframeElement.id;
    var widget          = SC.Widget(iframeElement);

    $("#togglePlay").click(function() {
        widget.toggle();
    });
});