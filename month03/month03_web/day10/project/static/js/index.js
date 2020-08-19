// 外部ＪＳ文件
$(function(){
    // 当页面元素加载完成之后执行的ｊｓ代码
    // alert("外部ｊｓ文件加载完成");
    // console.log(blogData);
    // console.log(faderData)


    // 使用faderData在页面加载所有的轮播图


    // 声明本地图片路径
    // 图片路径通常随着项目的位置发生变化　　对于路径而言尽量不要写死图片路径，通常
    // 采用地址＋图片名的方式拼接路径　　这样项目位置发生改变只需要改变图片地址即可
    var BASE_URL = "../static/images/"

    var html = "";

    // 遍历faderData  生成三个ｌｉ标签拼接到字符串ｈｔｍｌ中
    // 打印字符串
    // <li class="slide">
    //     <a href="#">
    //         <img src="../static/images/banner01.jpg" alt="banner1">
    //         <span class="imginfo">
    //             爬虫微课5小时 Python 学习路线!
    //         </span>
    //     </a>
    // </li>

    $.each(faderData,function(i,o){
        html += '<li class="slide">';
        html += ' <a href="#">'
        html+= `<img src="${BASE_URL+o.img_url}" alt="banner1">`
        html +='<span class="imginfo">'
        html += o.img_info
        html += '</span></a></li>'
       
    })

    // 将拼接好的字符串作为兄弟元素添加到fader_controls前
    $(".fader_controls").before(html);

    // jquery-->easyfader-->index.js
    // 调用jQuery.easyfader.min.js提供的函数 实现轮播功能
    $('.fader').easyFader();



    // 加载页面中的博客
    // 当页面加载时　显示前三条数据　　每次滚动时如果滚动条快要到底了　　再加载５条数据　直到没有数据为止

    function add_blogs(data){
        var html = "";
        $.each(data,function(i,o){
            var blog = `
            <div class="blogs">
                <h3 class="blogtitle">
                    <a href="#">
                        ${o.blogtitle}
                    </a>
                </h3>
                <div class="blogpic">
                    <a href="#">
                        <img src="${BASE_URL+o.blogpic}" alt="">
                    </a>
                </div>
                <p class="blogtext">
                    ${o.blogtext}
                </p>
                <ul>
                    <li class="author">
                        <a href="#">${o.bloginfo.author}</a>
                    </li>
                    <li class="lmname">
                        <a href="#">${o.bloginfo.lmname}</a>
                    </li>
                    <li class="timer">
                        <a href="#">${o.bloginfo.timer}</a>
                    </li>
                    <li class="view">
                        <a href="#">${o.bloginfo.view}</a>
                    </li>
                    <li class="like">
                        <a href="#">${o.bloginfo.like}</a>
                    </li>
                </ul>
            </div>`
            html += blog
        })
        $(".blogsbox").append(html)
    }

    //当页面加载时 显示blogData前3条数据
    add_blogs(blogData.slice(0,3));


    var canLoad = true;
    $(document).scroll(function(){
        // 滚动条滚动事件
        // console.log("我滚啦")
        // 获取滚动条相对顶端的距离（蓝色）
        var scrollTop = $(document).scrollTop()
        // 获取可视范围高度（黄色）
        var windowHeight = $(window).height()
        // 获取完整文档高度（红色）
        var documentHeight = $(document).height()
        // if(scrollTop+windowHeight==documentHeight){
        //     console.log("到底啦")
        // }

        if(documentHeight-scrollTop -windowHeight <=200){
            console.log("快到底了")
            // 获取后面５条数据
            // 页面中３条　slice(3,8)
            // 页面中８条开始　slice(８,13)
            var size = $('.blogs').length;
            if(canLoad){
                var data = blogData.slice(size,size+5);
                if(data.length>0){
                    add_blogs(data);
                }else{
                    alert("没数据了")
                    canLoad = false  //没有数据就禁止加载
                }
                
            }
            
        }
    })


})







