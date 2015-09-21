$('.panel').on('hidden.bs.collapse', function (e) {
    // console.log($(this).html())
})

$('.panel').on('show.bs.collapse', function (e) {
    // console.log($(this).html())
    window.abc = $(this)
})
var projectName = ""
var projectDetailsDump;

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

function ajaxRequest(payload,url)
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

function create_project()
{
var uploadedFiles = []
$('.dropBoxVideoFiles').each(function(i,item){
	var videoFile= {name:$(item).find('#fileName').val(), link:$(item).find('#fileLink').val(), thumbnail:$(item).find('#fileThumbnail').val(), type:"video", source:"dropbox"}
	uploadedFiles.push(videoFile)
})
// var audioFiles =[]
$('.dropBoxMusicFiles').each(function(i,item){
	var videoFile= {name:$(item).find('#fileName').val(), link:$(item).find('#fileLink').val(), thumbnail:$(item).find('#fileThumbnail').val(), type:"audio", source:"dropbox"}
	uploadedFiles.push(videoFile)
})

var projectTitle = $('#projectTitle').html()
var instructions = $('#instructions').val()
var payload = {projectTitle:projectTitle, instructions:instructions, files: JSON.stringify(uploadedFiles)}
var url = "/create-project/"
var projectId = ajaxRequest(payload,url)
console.log(projectId)
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


function logOut()
{
    var aj = ajaxRequest("","/signOut/")
    window.location.href='/'
}

function updateStats()
{
	var vidCount = $('.dropBoxVideoFiles').length
	var musCount = $('.dropBoxMusicFiles').length
	var sum = 0
	$('.dropBoxVideoFiles').each(function(i,item){
		sum = sum+parseInt(parseInt($(item).find('#fileSize').val())/1000000)
		
	})
	// var audioFiles =[]
	$('.dropBoxMusicFiles').each(function(i,item){
		sum = sum+parseInt(parseInt($(item).find('#fileSize').val())/1000000)

	})

	$('#MusCount').html("Music "+musCount)
	$('#VidCount').html("Videos "+vidCount)
	$('#priceCount').html("Total: <b>$ "+sum+"</b>")
}
