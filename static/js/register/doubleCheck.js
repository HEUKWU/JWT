function doubleCheck() {
    $('#loginId').change(function () {
        $('#id_check_sucess').hide();
        $('#doubleCheck').show();
        $('#loginId').attr("check_result", "fail")

    })

    let id = $('#loginId').val()
    let idReg = /^[a-zA-Z]+[a-z0-9A-Z]{3,19}$/g;
    if (id === '') {
        alert("아이디를 입력해주세요.");
    } else if (!idReg.test(id)) {
        alert("아이디는 영소문자로 시작하는 4~20자 영문자 또는 숫자이어야 합니다.");
    } else {
        $.ajax({
            type: "GET",
            url: "/api/double",
            data: {},
            success: function (response) {
                let user = response["user"];
                if (user.length === 0) {
                    alert('사용가능한 아이디입니다.');
                    $('#id_check_sucess').show();
                    $('#doubleCheck').hide();
                    $('#loginId').attr("check_result", "success")
                } else {
                    for (let i = 0; i < user.length; i++) {
                        let dbId = user[i]['id']
                        if (dbId === id) {
                            check = 1;
                            break;
                        } else {
                            check = 0
                        }
                    }
                    if (check === 1) {
                        alert("이미 사용중인 아이디입니다.");
                    } else {
                        alert("사용 가능한 아이디입니다.")
                        $('#id_check_sucess').show();
                        $('#doubleCheck').hide();
                        $('#loginId').attr("check_result", "success")
                    }
                }

            }
        });
    }
}