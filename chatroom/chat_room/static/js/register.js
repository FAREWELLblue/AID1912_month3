var $uname=$("#username")
var $pwd=$("#password")
var $rpwd=$("#re_password")
var $email=$("#email")
var $msg=$("#uname_msg")
var $rpmsg=$("#rpwd_msg")
var $pmsg=$("#pwd_msg")
var result=false;
function check_uname(){
    $.ajax({
        url:'/register',
        type:'post',
        async:false,
        contentType:'application/json',
        data:JSON.stringify({"dur":0,'uname':$uname.val()}),
        dataType:'json',
        success:function(res){
            console.log(res);
            $msg.html(res['msg']);
            if(res['code']==0){
                $msg.css("color","red");
                result = false;
            }else{
                $msg.css("color","green");
                result = true;
            }
        }
    })
}
$uname.blur(function(){
    if($uname.val()!=''){
        check_uname();
    }else{
        $msg.css("color","red");
        $msg.html('请输入用户名')
    }
})

$("#btn_register").click(function(){
    if($uname.val()==''){
        $msg.html('用户名不可为空').css('color','red');
        if($pwd.val()==''){
            $pmsg.html('密码不可为空').css('color','red');
        }
        if($rpwd.val()==''){
            $rpmsg.html('请再输入一次密码').css('color','red');
        }
    }
    else if(!result){
        alert('请重新输入用户名');
        $msg.html('请重新输入用户名').css('color','red');
        $uname.val('');
    }
    else{
        console.log(result)
        $.ajax({
            url:'/register',
            type:'post',
            data:JSON.stringify({"dur":1,'uname':$uname.val(),'password':$pwd.val(),'email':$email.val()}),
            dataType:'json',
            contentType:'application/json',
            async:true,
            success:function(res){
                alert(res['msg']);
                $(location).attr('href','/index');
            }
        })

    }
})

$rpwd.blur(function (){
    if($pwd.val()!=''&&$rpwd.val()!=''){
        if($pwd.val()==$rpwd.val()){
            $rpmsg.css('color','green')
            $rpmsg.html('两次密码输入一致')
        }else{
            $rpmsg.css('color','red')
            $rpmsg.html('两次密码输入不一致')
        }
    }
})
$pwd.blur(function(){
    if($pwd.val()!=''&&$rpwd.val()!=''){
        if($pwd.val()==$rpwd.val()){
            $rpmsg.css('color','green')
            $rpmsg.html('两次密码输入一致')
        }else{
            $rpmsg.css('color','red')
            $rpmsg.html('两次密码输入不一致')
        }
    }
})
