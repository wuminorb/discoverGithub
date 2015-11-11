function refresh(url) {
    $.get(url, function (data, status) {
        location.reload();
    });
}
