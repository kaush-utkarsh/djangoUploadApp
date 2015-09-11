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

function makeAjax(payload,url)
{
    if(payload != ""){
    var datum = $.ajax(
                    {
                        url: url,
                        type: "POST",
                        data: payload,
                        async: false,
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
            console.log($(this).serialize())
            var resultset = makeAjax($(this).serialize(),"/signIn/")
            window.location.href='/'
            console.log(resultset.responseText)

        }
        else if(cnt==0 && $(this).attr('id')=='signUpForm')
        {
            console.log($(this).serialize())
            var resultset = makeAjax($(this).serialize(),"/signUp/")
            window.location.href='/'
            console.log(resultset.responseText)
        }

    });
    
    
});
