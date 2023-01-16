$(document).ready(function () {
    show_list()
})

function show_list() {
    $('#cards').empty()
    $.ajax({
        type: "GET",
        url: "/api/post",
        data: {},
        success: function (response) {
            let rows = response["group_list"]
            let like_list = response["like_list"]

            for (let i = 0; i < rows.length; i++) {
                let group_name = rows[i]["group_name"]
                let image = rows[i]["image"]
                let desc = rows[i]["desc"]
                let like = rows[i]["like"]
                let group_num = rows[i]["group_num"]

                let like_id = ""
                let like_text = ""
                if (like_list == null || !like_list["group_num"].includes(group_num)) {
                    like_text = "❤ " + like
                    like_id = "like_up(" + group_num + ")"
                } else {
                    like_text = "💖 " + like
                    like_id = "like_down(" + group_num + ")"
                }
                let temp_html = `<a href="/api/deep?num=${group_num}">
                            <div class="card mb-3">
                                <div class="row g-0">
                                    <div class="col-md-4">
                                        <img src=${image}
                                             class="card-img-top" alt="..." style="height: 100%"/>
                                    </div>
                                    <div class="col-md-8">
                                        <div class="card-body">
                                            <h5 class="card-title">${group_name}</h5>
                                            <p class="card-text">${desc}</p>
                                        </div>
                                        <button onclick=${like_id} class="card-footer">
                                            <small class="text-muted">${like_text}</small>
                                        </button>
                                    </div>
                                </div>
                            </div>
                            </a>`
                $('#cards').append(temp_html)
            }
        }
    })
}
