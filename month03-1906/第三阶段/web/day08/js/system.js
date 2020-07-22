//编写一个指范围和位数的函数
function getRandByParm(max, len, blnZ, blnT) {
    //定义一个数组，保存生成的随机数
    var _arr = [];
    while (_arr.length < len) {
        if (!blnT) {
            var n = Math.floor(Math.random() * max);
        }
        else {
            var n = Math.ceil(Math.random() * max);
        }
        //如果值小于10，则前加上0
        if (n < 10 && blnZ)
            n = "0" + n;
        //定义一个正则表达式
        var reg = new RegExp(n, 'g');
        //验证是否在数组中存在,如果不存，则追加
        if (!reg.test(_arr.toString()))
            //追加到数组中
            _arr.push(n);
    }
    return _arr;
}