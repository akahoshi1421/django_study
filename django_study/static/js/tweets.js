function search_js(event)
{
    let user = event.currentTarget.value;
    $.ajax({
        url: window.location.origin + "/study/api/user",
        type: "POST",
        data: {"user": user},
        dataType:"json",
        success:function(data){
            let user_result = document.getElementById("user_result");
            user_result.innerHTML = "検索予想";
            for(let user of data.users){
                user_result.innerHTML += ("<li>" + user + "</li>")
            }
        }
    })
}

window.addEventListener('load', init);

function init()
{
    let user = document.getElementById("search_user");
    user.addEventListener("input", search_js);
}
