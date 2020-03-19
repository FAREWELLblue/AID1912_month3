$uname=$("#username");
$pwd=$("#password");
$("#btn_login").click(
function (){
    var xhr = new XMLHttpRequest();
    xhr.open('post','/login',true)
    xhr.onreadystatechange=function(){
        if(xhr.readyState==4&&xhr.status==200){
            console.log(xhr.responseText);
            if(JSON.parse(xhr.responseText)['code']==1){
                $(location).attr('href','/login')
            }else if(JSON.parse(xhr.responseText)['code']==0){
                alert(JSON.parse(xhr.responseText)['msg']);
                location.reload();
            }
        }
    }
    data=JSON.stringify({"username":$uname.val(),"password":$pwd.val()})
    xhr.setRequestHeader('Content-Type','application/json')
    console.log(data);
    xhr.send(data);
})