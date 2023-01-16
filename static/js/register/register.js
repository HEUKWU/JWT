function register() {
    let id = $('#loginId').val();
    let pw = $('#loginPw').val()
    pw_check = $('#register-password-check').val();

    let idReg = /^[a-zA-Z]+[a-z0-9A-Z]{3,19}$/g;
    let pwReg = /^(?!((?:[A-Za-z]+)|(?:[~!@#$%^&*()_+=]+)|(?=[0-9]+))$)[A-Za-z\d~?!@#$%^&*()_+=]{8,}$/;
    if (id === "") {
        alert('아이디를 입력해주세요')
    } else if ($('#loginId').attr("check_result") === "fail") {
        alert("아이디 중복체크를 해주세요.");
    } else if (pw === "") {
        alert('비밀번호를 입력해주세요');
    } else if (!idReg.test(id)) {
        alert("아이디는 영소문자로 시작하는 4~20자 영문자 또는 숫자이어야 합니다.");
        return;
    } else if (!pwReg.test(pw)) {
        alert("비밀번호는 영문, 숫자, 특수문자 중 2가지 이상 조합하여 8자리 이내로 입력해주세요.");
        return;
    } else if (pw !== pw_check) {
        alert('동일한 비밀번호를 입력해주세요.');
    } else {
        $.ajax({
            type: "POST",
            url: "/api/register",
            data: {id_give: id, pw_give: pw},
            success: function (response) {
                if (response['check'] === 1) {
                    alert('회원가입 성공!')
                    window.location.replace("/login")
                } else if (response['check'] === 0) {
                    alert('이미 가입한 회원입니다.')
                }
            }
        });
    }

}
