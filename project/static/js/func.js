$(function()
{
    $(".meun-item").click(function() 
    {
        $(".meun-item").removeClass("meun-item-active");
        $(this).addClass("meun-item-active");
        var itmeObj = $(".meun-item").find("img");
        itmeObj.each(function() 
        {
            var items = $(this).attr("src");
            items = items.replace("_grey.png", ".png");
            items = items.replace(".png", "_grey.png");
            $(this).attr("src", items);
        });
        var attrObj = $(this).find("img").attr("src");
        attrObj = attrObj.replace("_grey.png", ".png");
        $(this).find("img").attr("src", attrObj);
    });
    $(".toggle-btn").click(function() 
    {
        $("#leftMeun").toggleClass("show");
        $("#rightContent").toggleClass("pd0px");
    });
});

$(function() 
{
    $(".hovertable").hide();
});

$(document).ready(function()
{
    $("#show").click(function () 
    {
        $(".hovertable").show();
    });
    $("#download").click(function () 
    {
        window.open("http://127.0.0.1:8000/download");
    });
    $("#update").click(function () 
    {
        
    });
});


