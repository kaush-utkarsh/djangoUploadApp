function showForm(item)
{
    if($(item).attr('id')=='SignUp')
    {
        $('.signInForm').attr('style','display:none;')
        $('.signUpForm').attr('style','display:block;')
    }
    else
    {
        $('.signUpForm').attr('style','display:none;')
        $('.signInForm').attr('style','display:block;')
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function makeAjax(payload,url)
{
    var csrftoken = getCookie('csrftoken');
    if(payload != ""){
    var datum = $.ajax(
                    {
                        url: url,
                        type: "POST",
                        data: payload,
                        async: false,
                        beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", csrftoken);},
                        success: function (data) {
                            return data
                    }
                });
    return datum;
    }
    else{
    var datum = $.ajax(
                    {
                        url: url,
                        type: "POST",
                        async: false,
                        beforeSend: function(xhr){xhr.setRequestHeader("X-CSRFToken", csrftoken);},
                        success: function (data) {
                            return data
                    }
                });
    
    return datum;
    }
}

function logMeOut()
{
    var aj = makeAjax("","/signOut/")
    window.location.href='/'
}

jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("static/img/backgrounds/1.jpg");
    
    
    /*
        Form validation
    */
    $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    $('.login-form').on('submit', function(e) {
    	e.preventDefault();
        var cnt = 0;
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function(){
    		if( $(this).val() == "" ) {
    			$(this).addClass('input-error');
                cnt++;
                return false;
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
        if(cnt==0 && $(this).attr('id')=='signInForm')
        {
            // console.log($(this).serialize())
            var resultset = makeAjax($(this).serialize(),"/signIn/")
            if (resultset.responseText == "false")
            {
                $('#passwordError').attr('style','display:block;')
                return false;
            }
            else
                window.location.href='/dashboard/'
            // console.log(resultset.responseText)

        }
        else if(cnt==0 && $(this).attr('id')=='signUpForm')
        {
            console.log($(this).serialize())
            
            if($('#form-password').val().length<6)
            {
                $('#form-password').addClass('input-error')
                $('#pwdlengthError').attr('style','display:block;')
                return false;   
            }
            if($('#form-password').val()!==$('#form-password-confirm').val())
            {
                $('#form-password-confirm').addClass('input-error')
                $('#wrongpwdError').attr('style','display:block;')
                return false;   
            }
            var resultset = makeAjax($(this).serialize(),"/signUp/")
            if (resultset.responseText == "false")
            {
                $('#usernameError').attr('style','display:block;')
                return false;
            }
            else
                window.location.href='/dashboard/'
            
            // console.log(resultset.responseText)
        }

    });
    
    
});


