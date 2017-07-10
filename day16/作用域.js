/**
 * Created by 武伟 on 2017-07-10.
 */
// 3.
x = 'Ivor';
function func1() {
    var x = 'alex';
    function f2() {
        console.log(x)

    }
    return f2;
}
ret = func1();
ret();
// 》》》alex

x = 'Ivor';
function f1() {
    var y = 'alex';
    function f2() {
        console.log(y)

    }
    var y = 'jack';
    return f2;
}
ret = f1();
ret();
// 》》》jack

// 4.
     function func2(){
          console.log(xxoo);
          var xxoo = 'alex'
     }
     func2();
// 》》》undefined；


     function func3(){
          console.log(xxoo);
          var xxoo = 'alex';
     }
     func3();
// 》》》报错

