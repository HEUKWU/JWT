$(document).ready(function () {
    alert("왔다.")
    show_list()
})

function show_list() {
    alert("show_list")
    $.ajax({
        type: "GET",
        url: "/api/post",
        data: {},
        success: function (response) {
            let rows = response["list"]
            for(let i=0; i<rows.length; i++){
                let group_name = rows[i]["group_name"]
                let image = rows[i]["image"]
                let desc = rows[i]["desc"]
                let like = rows[i]["like"]

                temp_html = `<div class="card mb-3">
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
                                        <div class="card-footer">
                                            <small class="text-muted">🤍${like}</small>
                                        </div>
                                    </div>
                                </div>
                            </div>`
                $('#cards').append(temp_html)
            }
        }
    })
}