function refresh(url) {
    $.ajax({
        url: url,
        success: function (data) {
            location.reload();
        },
        timeout:3600000
    });
}
