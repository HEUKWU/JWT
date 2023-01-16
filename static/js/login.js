function loginClick() {
    let username_receive = $('#loginId').val()
    let password_receive = $('#loginPw').val()

    if (username_receive === '') {
        alert('아이디를 입력해주세요.')
    } else if (password_receive === '') {
        alert('비밀번호를 입력해주세요.')
    } else {
        $.ajax({
            type: "POST",
            url: "/api/login",
            data: {id_give: username_receive, pw_give: password_receive},
            success: function (response) {
                if (response['result'] === 'success') {
                    $.cookie('mytoken', response['token']);
                    alert('로그인이 완료되었습니다!')
                    window.location.href = '/'
                } else {
                    alert(response['msg'])
                }
            }
        })
    }

}