/**
 * Created by 武伟 on 2017-06-27.
 */

function f1() {
    //根据ID获取指定标签的内容，定于局部变量接受
    var tag = document.getElementsById('id');
    //获取标签内部的内容
    var content = tag.innerText;
    var f = content.charAt(0);
    var l = content.substring(1,content.length);
    var new_content = l + f;
    tag.innerText = new_content;
}