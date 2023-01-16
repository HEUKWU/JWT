// $(document).ready(function () {
//     deep_post()
//
// })
//
//
// function deep_post() {
//     $('#cards_box').empty()
//     alert(JSON.parse($('#idol_list').val()))
//     let rows = JSON.parse($('#idol_list').val())
//     for (let i = 0; i < rows.length; i++) {
//         let idol_nickname = rows[i]["nickname"]
//         let idol_image = rows[i]["image"]
//         let idol_name = rows[i]["name"]
//         let idol_birth = rows[i]["birth"]
//         let idol_nation = rows[i]["nation"]
//         let idol_position = rows[i]["position"]
//
//         let temp_html = `<div class="col">
//                         <div class="card">
//                             <img src="${idol_image}" class="card-img-top"
//                                  alt="...">
//                             <div class="card-body">
//                                 <h5 class="card-title">${idol_nickname}</h5>
//                                 <hr>
//                                 <p class="card-text">본명 : ${idol_name}</p>
//                                 <hr>
//                                 <p class="card-text">출생연도 : ${idol_birth}</p>
//                                 <hr>
//                                 <p class="card-text">국적 : ${idol_nation}</p>
//                                 <hr>
//                                 <p>포지션 : ${idol_position}</p>
//                             </div>
//                         </div>
//                     </div>`
//         $('#cards_box').append(temp_html)
//     }
// }