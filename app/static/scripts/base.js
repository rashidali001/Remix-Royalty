/* register html script */
$(document).ready(function(){

    $("#email").focus(function(){
        $("#email-error").hide();
    })

    $("#password").focus(function(){
        $("#error").hide();

    })

    $("#password").keyup(function(){
        let password = $("#password").val();
        let repeat_password = $("#repeat-password").val();
        
        if (password){
            if (repeat_password){
                if (password != repeat_password){
                    $("#error").show();
                }else{
                    $("#error").hide();
                }
            }
        }
    })

    $("#repeat-password").focus(function(){
        let email = $("#email").val();
        let password = $("#password").val();
        let repeat_password = $("#repeat-password").val();
        if (password != repeat_password){
            $("#error").show();
        }
    })

    $("#repeat-password").keyup(function(){
        let email = $("#email").val();
        let password = $("#password").val();
        let repeat_password = $("#repeat-password").val();
        if (password != repeat_password){
            $("#error").show();
        }else{
            $("#error").hide();
        }
    })

    $("#register").submit(function(e){
        e.preventDefault();

        let username = $("#name").val();
        let email = $("#email").val();
        let password = $("#password").val();
        let repeat_password = $("#repeat-password").val();

        if (password != repeat_password){
            $("#error").show();
        }else{
            $.ajax({
                url:"/check_email",
                method:"post",
                data:{
                    email:email,
                    password:password,
                    repeat_password:repeat_password
                },
                success:function(){
                    $.ajax({
                        url:"/register",
                        method:"post",
                        contentType:"application/json",
                        dataType:"json",
                        data: JSON.stringify({
                            username:username,
                            email:email,
                            password:password,
                        }),
                        success: function(response){
                            window.location.href = response.redirect;

                        }
                    })
                },
                error:function(){
                    $("#email-error").show();
                }
                
            })
        }


    })

})