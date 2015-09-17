$('.panel').on('hidden.bs.collapse', function (e) {
    // console.log($(this).html())
})

$('.panel').on('show.bs.collapse', function (e) {
    // console.log($(this).html())
    window.abc = $(this)
})