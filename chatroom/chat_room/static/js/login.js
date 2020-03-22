$uname=$("#username");
$pwd=$("#password");
$("#btn_login").click(
function (){
    $.ajax({
        url:'/login',
        type:'post',
        data:JSON.stringify({"username":$uname.val(),"password":$pwd.val()}),
        dataType:'json',
        contentType:'application/json',
        success:function(res){
            $("#btn").removeAttr('disabled')
            console.log(res);
            if(res['code']==1){
                $(location).attr('href','/login')
            }else if(res['code']==0){
                alert(res['msg']);
                location.reload();
            }
        },
        beforeSend:function(){
            $("#btn_login").attr('disabled','disabled')
        }
    })

    
})