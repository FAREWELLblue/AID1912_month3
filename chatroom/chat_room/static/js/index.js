var data_obj=null
$(document).ready(get_room_list());
var num=0;
var content_list=[];
var room_list=[];
var username=null;
function get_room_list() {
    $.ajax({
        url:'/room?req=room_list',
        type:'get',
        dataType:'json',
        success:function(data){
            console.log(data);
            // console.log(JSON.parse( data['data']));
            if(data['code']==0){
                alert(data['data'])
            }else if(data['code']==1){
                data_obj=JSON.parse( data['data']);
                username=data['user'];
                $("#uname").html(username);
                $.each(data_obj,function(i,e){
                    var room=$("<div class='room'><span id='room_name'>"+e[1]+"</span><br>"+
                        "<div class='owner'>" +
                        "<span id='own'>聊天室管理员:</span>" +
                        "<span id='owner_id'>"+e[3]+"</span>" +
                        "</div></div>");
                    room_list.push(room);
                    $("#left").append(room);
                    var content=$("<div id='content'><div id='introduce_name'>" +
                            "<div id='irn'>" + e[1] +
                            "</div><p id='room_id' style='display:none;'>"+e[0]+"</p>" +
                            "<div id='iro'>" +
                            "聊天室管理员：" +
                            "</div>" +"<div id='iron'>" +e[3]+
                            "</div>"+
                            "</div>" +
                            "<div id='introduce'>" +
                            "<div id='in'>聊天室简介</div>" +
                            "<div id='ic'>"+e[2]+"</div>" +
                            "</div></div>"+"<button id='in_btn' class='btn btn-block' onclick='in_room()'>进入聊天室</button>")
                    content_list.push(content);
                   
                })
                
                $(".room").click(function() {
                    for (var i=0;i<room_list.length;i++){
                        if(this==room_list[i][0]){
                            console.log(i);
                            num=i;
                            
                            console.log(num);
                        }
                    }
                    $("#right").html(content_list[num]);
                })

            }else if(data['code']=='404'){
                console.log(data['data']);
            }
        }
    })

    
}

$("#logout").click(function(){
    $.get('/logout',function(res){
        if(res['code']=='1'){
            location.reload();
        }
    },'json');
})
$("#new_room").hide()
$("#btn_new").click(function(){
    $("#new_room").fadeIn(100)
    $("#main").fadeOut(100)
})
$("#n_btn").click(function(){
    r_name=$("#r_name")
    r_intr=$("#r_intro")
    $.ajax({
        url:'/room',
        type:'post',
        dataType:'json',
        contentType:"application/json",
        data:JSON.stringify({r_name:r_name.val(),r_intro:r_intr.val()}),
        success:function(res){
            if (res.code=='1'){
                location.reload();
            }else if (res.code=='0'){
                alert('聊天室名称不可重复');
                location.reload();
            }
        }
    })
    
    
})

function in_room(){
    rname=$("#irn").html()
    // console.log($("#room_id").html());
    window.location.href='/chat_room?rname='+rname
}