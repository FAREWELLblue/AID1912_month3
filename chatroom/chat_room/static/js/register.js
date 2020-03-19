var $uname=$("#username")
var $pwd=$("#password")
var $rpwd=$("#re_password")
var $email=$("#email")
var $msg=$("#uname_msg")
var $rpmsg=$("#rpwd_msg")
var $pmsg=$("#pwd_msg")
var result=false;
$uname.blur(function check_uname(){
    if($uname.val()!=''){
        var xhr = new XMLHttpRequest();
        xhr.open('post','/register',false);
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4&&xhr.status==200){
                console.log(JSON.parse(xhr.responseText)['msg']);
                $msg.html(JSON.parse(xhr.responseText)["msg"])
                $msg.css({
                   "float":"left",
                   "border":"1px solid #000"
                })
                console.log($msg);
                $uname.after($msg);
                if(JSON.parse(xhr.responseText)['code']==0){
                    $msg.css("color","red");
                    result = false;
                }else{
                    $msg.css("color","green");
                    result = true;
                }
            }
        }
        data=JSON.stringify({"dur":0,'uname':$uname.val()})
        xhr.setRequestHeader('Content-Type','application/json')
        xhr.send(data)
        return result
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
        var xhr = new XMLHttpRequest();
        xhr.open('post','/register',true);
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4&&xhr.status==200){
                if(JSON.parse(xhr.responseText)['code']=='200'){
                    alert(JSON.parse(xhr.responseText)['msg']);
                    $(location).attr('href','/index');
                }
            }
        }
        data=JSON.stringify({"dur":1,'uname':$uname.val(),'password':$pwd.val(),'email':$email.val()})
        console.log(data)
        xhr.setRequestHeader('Content-Type','application/json')
        xhr.send(data)
    }
})

$("#re_password").change(function(){
    if($pwd.val()==$rpwd.val()){
        $rpmsg.css('color','green')
        $rpmsg.html('两次密码输入一致')
    }else{
        $rpmsg.css('color','red')
        $rpmsg.html('两次密码输入不一致')
    }
})