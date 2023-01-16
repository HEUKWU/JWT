function like_up(num) {
    $.ajax({
        type: "POST",
        url: "/api/like",
        data: {num_give: num},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    })
}

function like_down(num) {
    $.ajax({
        type: "POST",
        url: "/api/like/cancel",
        data: {num_give: num},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    })
}