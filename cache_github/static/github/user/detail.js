function refresh(url) {
    $.ajax({
        url: url,
        success: function (data) {
            alert(data);
            location.reload();
        },
        timeout:3600000
    });
}
