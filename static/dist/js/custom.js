$('.panel').on('hidden.bs.collapse', function (e) {
    // console.log($(this).html())
})

$('.panel').on('show.bs.collapse', function (e) {
    // console.log($(this).html())
    window.abc = $(this)
})
var projectName = ""
var projectDetailsDump;

function ajaxRequest(payload,url)
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


function createProject(item)
{
	projectName = ($(item).parent().find('input[type="text"]').val()).trim()
	console.log(projectName)
	if(projectName=="")
	{
		$(item).parent().find('input[type="text"]').addClass('input-error').focus()
		return false;
	}
	else
	{


		$('label[id="projectName"]').html(projectName)
		$(item).parent().attr('style','display:none;')
		projectDetailsDump = $('#projectDetails').clone()
		$('#projectDetails').attr('style','display:block;')
		$(item).parent().parent().find('#newProject').attr('style','display:block;')
	}
}

function renameProject(item)
{
	console.log(item)
}

function deleteProject(item)
{
	console.log(item)
}

function modifyProject(item)
{
	console.log(item)
	$('#newProject').attr('style','display:none;')
	$('#editProject').attr('style','display:block;')
}
