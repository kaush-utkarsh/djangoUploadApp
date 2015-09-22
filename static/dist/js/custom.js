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

function updatelocalVideos()
{
    $('#localUploadVideos').html('')
    $.each(video_filesList, function(k, vid)
    {
        $.each(vid, function(key, value)
        {
          var img = "<div class='col-sm-2 col-md-2'><div class='thumbnail'><i class='glyphicon glyphicon-facetime-video'></i><div class='caption localVideoFiles'><h3 style='font-size:15px;'>"+value.name+"</h3><input type='checkbox' checked class='vid' name='"+value.lastModified+"' alt='"+value.name+"'></div></div></div>"
         $('#localUploadVideos').append(img)
          // console.log(value)
        });
    });
}
function updatelocalAudios()
{
    $('#localUploadAudios').html('')
    $.each(audio_filesList, function(k, vid)
    {
        $.each(vid, function(key, value)
        {
          var img = "<div class='col-sm-2 col-md-2'><div class='thumbnail'><i class='glyphicon glyphicon-music'></i><div class='caption localVideoFiles'><h3 style='font-size:15px;'>"+value.name+"</h3><input type='checkbox' checked class='aud' name='"+value.lastModified+"' alt='"+value.name+"'></div></div></div>"
         $('#localUploadAudios').append(img)
          // console.log(value)
        });
    });
}

var options =   {
                    // Required. Called when a user selects an item in the Chooser.
                    success: function(files) {
                        // dropBoxFiles = files
                        console.log(files)
                    },

                    // Optional. Called when the user closes the dialog without selecting a file
                    // and does not include any parameters.
                    cancel: function() {

                    },

                    // Optional. "preview" (default) is a preview link to the document for sharing,
                    // "direct" is an expiring link to download the contents of the file. For more
                    // information about link types, see Link types below.
                    linkType: "direct", // or "direct"

                    // Optional. A value of false (default) limits selection to a single file, while
                    // true enables multiple file selection.
                    multiselect: true, // or false

                    // Optional. This is a list of file extensions. If specified, the user will
                    // only be able to select files with these extensions. You may also specify
                    // file types, such as "video" or "images" in the list. For more information,
                    // see File types below. By default, all extensions are allowed.
                    extensions: ['.pdf', '.doc', '.docx','.bmp', '.cr2', '.gif', '.ico', '.ithmb', '.jpeg', '.jpg', '.nef', '.png', '.raw', '.svg', '.tif', '.tiff', '.wbmp', '.webp', '.3g2', '.3gp', '.3gpp', '.3gpp2', '.asf', '.avi', '.dv', '.dvi', '.flv', '.m2t', '.m4v', '.mkv', '.mov', '.mp4', '.mpeg', '.mpg', '.mts', '.ogv', '.ogx', '.rm', '.rmvb', '.ts', '.vob', '.webm', '.wmv', '.aac', '.aif', '.aifc', '.aiff', '.au', '.flac', '.m4a', '.m4b', '.m4p', '.m4r', '.mid', '.mp3', '.oga', '.ogg', '.opus', '.ra', '.ram', '.spx', '.wav', '.wma'],
                };

function uploadManual(item)
{
    $(item).next().click();
}

function fetchDropBox(item,fileType)
{
    if(fileType=="vids")
    {
        options.extensions = ['.bmp', '.cr2', '.gif', '.ico', '.ithmb', '.jpeg', '.jpg', '.nef', '.png', '.raw', '.svg', '.tif', '.tiff', '.wbmp', '.webp', '.3g2', '.3gp', '.3gpp', '.3gpp2', '.asf', '.avi', '.dv', '.dvi', '.flv', '.m2t', '.m4v', '.mkv', '.mov', '.mp4', '.mpeg', '.mpg', '.mts', '.ogv', '.ogx', '.rm', '.rmvb', '.ts', '.vob', '.webm', '.wmv']
    
        options.success = function(files)
        {
            
            $.each(files,function(i,item){
                if(item.thumbnailLink == undefined)
                    var thumbnail="<div class='col-sm-2 col-md-2'><div class='thumbnail'><i class='glyphicon glyphicon-music'></i><div class='caption dropBoxVideoFiles'><h3 style='font-size:15px;'>"+item.name+"</h3><input type='hidden' id='fileName' value='"+item.name+"'><input type='hidden' id='fileLink' value='"+item.link+"'><input type='hidden' id='fileSize' value='"+item.bytes+"'><input type='hidden' id='fileThumbnail' value=''></div></div></div>";
                else
                    var thumbnail="<div class='col-sm-2 col-md-2'><div class='thumbnail'><img data-src='holder.js/100%x200' alt='100%x200' style='width: 150px; display: block;' src='"+item.thumbnailLink+"' data-holder-rendered='true'><div class='caption dropBoxVideoFiles'><h3 style='font-size:15px;'>"+item.name+"</h3><input type='hidden' id='fileName' value='"+item.name+"'><input type='hidden' id='fileLink' value='"+item.link+"'><input type='hidden' id='fileSize' value='"+item.bytes+"'><input type='hidden' id='fileThumbnail' value='"+item.thumbnailLink+"'></div></div></div>";

                $('#dropboxVideos').append(thumbnail)
            })

            updateStats()
        }

    }
    else
    {
        options.extensions = ['.aac', '.aif', '.aifc', '.aiff', '.au', '.flac', '.m4a', '.m4b', '.m4p', '.m4r', '.mid', '.mp3', '.oga', '.ogg', '.opus', '.ra', '.ram', '.spx', '.wav', '.wma']
        
        options.success = function(files)
        {

            $.each(files,function(i,item){
                if(item.thumbnailLink == undefined)
                    var thumbnail="<div class='col-sm-2 col-md-2'><div class='thumbnail'><i class='glyphicon glyphicon-music'></i><div class='caption dropBoxMusicFiles'><h3 style='font-size:15px;'>"+item.name+"</h3><input type='hidden' id='fileName' value='"+item.name+"'><input type='hidden' id='fileLink' value='"+item.link+"'><input type='hidden' id='fileSize' value='"+item.bytes+"'><input type='hidden' id='fileThumbnail' value=''></div></div></div>";
                else
                    var thumbnail="<div class='col-sm-2 col-md-2'><div class='thumbnail'><img data-src='holder.js/100%x200' alt='100%x200' style='width: 150px; display: block;' src='"+item.thumbnailLink+"' data-holder-rendered='true'><div class='caption dropBoxMusicFiles'><h3 style='font-size:15px;'>"+item.name+"</h3><input type='hidden' id='fileName' value='"+item.name+"'><input type='hidden' id='fileLink' value='"+item.link+"'><input type='hidden' id='fileSize' value='"+item.bytes+"'><input type='hidden' id='fileThumbnail' value='"+item.thumbnailLink+"'></div></div></div>";


                $('#dropboxMusic').append(thumbnail)
            })

            updateStats()
        }
    }
    Dropbox.choose(options);
}

function setProjectTitle(item)
{
    if(($(item).val()).trim()!="")
        $('#projectTitle').html($(item).val())
    else
        $('#projectTitle').html("Project Title")
    // console.log($(item).val())
}

function uploadLocalFiles(projectId)
{
    var checkedVids = []
    $('input[class="vid"]').each(function(i,item){
      if(item.checked)
        checkedVids.push($(item).attr("name"))
    })
    var checkedAuds = []
    $('input[class="aud"]').each(function(i,item){
      if(item.checked)
        checkedAuds.push($(item).attr("name"))
    })

    var data = new FormData();
    $.each(video_filesList, function(k, vid)
    {
        $.each(vid, function(key, value)
        {
            if($.inArray(""+value.lastModified.toString(), checkedVids))
                data.append("my_file", value);
        });
    });
    // console.log(data);
    $.ajax({
        url: "/upload-video-file/",
        type: "POST",
        data: data,
        cache: false,
        async: false,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function(data, textStatus, jqXHR){
            // alert("in succcess block");
        },
        error: function(jqXHR, textStatus, errorThrown){
            // alert("error");
        }
    });

    data = new FormData();
    $.each(audio_filesList, function(k, aud)
    {
        $.each(aud, function(key, value)
        {
            if($.inArray(""+value.lastModified.toString(), checkedAuds))
                data.append("my_file", value);
        });
    });
    // console.log(data);
    $.ajax({
        url: "/upload-audio-file/",
        type: "POST",
        data: data,
        cache: false,
        async: false,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function(data, textStatus, jqXHR){
            // alert("in succcess block");
        },
        error: function(jqXHR, textStatus, errorThrown){
            // alert("error");
        }
    });    



    window.location.href = "/checkout/"
}



function create_project()
{
    $('#loading').show()
    $("body").prepend("<div class=\"overlay\"></div>");

    $(".overlay").css({
        "position": "absolute", 
        "width": $(document).width(), 
        "height": $(document).height(),
        "z-index": 99999, 
    }).fadeTo(0, 0.8);

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
    var resultset = ajaxRequest(payload,url)
    resultset = JSON.parse(resultset.responseText)
    var projectId = resultset.project_id
    console.log(projectId)
    uploadLocalFiles(projectId)
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