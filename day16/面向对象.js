/**
 * Created by 武伟 on 2017-07-10.
 */

function Foo(n){
    this.name = n;
    this.sayName = function () {
        console.log(this.name)
    }
}

var obj1 = new Foo('Ivor');
