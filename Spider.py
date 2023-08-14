from bs4 import BeautifulSoup


# 源代码
html_source1='''<span>治理结构</span>
     
</div>
        </div>
        <div class="mechanism clearfix">
            <div class="mechanism-wp" style="width:100%"><UL>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70455)" style="display: initial;">中共同济大学委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70454)" style="display: initial;">中共同济大学纪律检查委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70462)" style="display: initial;">同济大学校务委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70456)" style="display: initial;">同济大学学术委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70457)" style="display: initial;">同济大学教务委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70461)" style="display: initial;">同济大学学位评定委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70460)" style="display: initial;">同济大学专业技术职务聘任工作委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70459)" style="display: initial;">同济大学教职工代表大会执行委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70458)" style="display: initial;">同济大学工会委员会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70463)" style="display: initial;">同济大学学生代表大会</a></h4>
                    </li>
                    <li>
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70464)" style="display: initial;">同济大学研究生代表大会</a></h4>
                    </li>
</UL></div>
        </div>
    </div>
</div>
<!-- 内容部分end -->'''
html_source2 = """
<span>院部设置</span>
     
</div>
        </div>
       <div style="width: 267px;float:right;text-align: right;"><div style="width: 37%;float: left;"><a href="ybsz.htm" style="color: #4d4d4d;">A-Z</a></div></div>
        <div class="mechanism clearfix"><div class="mechanism-wp" style="width: 100%;padding-left: 10px;"><UL>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://sem.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70471)" style="display: initial;">经济与管理学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://caup.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70495)" style="display: initial;">建筑与城市规划学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://civileng.tongji.edu.cn" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70480)" style="display: initial;">土木工程学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://mefaculty.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70489)" style="display: initial;">机械与能源工程学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://sese.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70468)" style="display: initial;">环境科学与工程学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://life.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70484)" style="display: initial;">生命科学与技术学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://smse.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70469)" style="display: initial;">材料科学与工程学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://see.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70483)" style="display: initial;">电子与信息工程学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://sfl.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70470)" style="display: initial;">外国语学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://med.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70482)" style="display: initial;">医学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://kouqiang.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70466)" style="display: initial;">口腔医学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://railway.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70490)" style="display: initial;">铁道与城市轨道交通研究院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://sse.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70465)" style="display: initial;">软件学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://auto.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70491)" style="display: initial;">汽车学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://mgg.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70479)" style="display: initial;">海洋与地球科学学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://tjjt.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70487)" style="display: initial;">交通运输工程学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70472)" style="display: initial;">医学与生命科学部</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://aero-mech.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70486)" style="display: initial;">航空航天与力学学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://sal.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70473)" style="display: initial;">人文学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://my.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70492)" style="display: initial;">马克思主义学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://law.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70474)" style="display: initial;">法学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://spsir.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70496)" style="display: initial;">政治与国际关系学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://tjdi.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70475)" style="display: initial;">设计创意学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://celiang.tongji.edu.cn/chinese/sy.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70485)" style="display: initial;">测绘与地理信息学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://physics.tongji.edu.cn" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70476)" style="display: initial;">物理科学与工程学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://am.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70497)" style="display: initial;">艺术与传媒学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://chemweb.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70481)" style="display: initial;">化学科学与工程学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://math.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70493)" style="display: initial;">数学科学学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://sicip.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70467)" style="display: initial;">上海国际知识产权学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://sports.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70494)" style="display: initial;">体育教学部</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://football.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70477)" style="display: initial;">国际足球学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://xsy.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70488)" style="display: initial;">新生院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70478)" style="display: initial;">国豪书院</a></h4>
                    </li>
</UL></div>
           
        </div>
         <div class="mechanism clearfix">
            <div class="mechanism-wp" style="width: 100%;padding-left: 20px;"><UL>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://cdh.tongji.edu.cn/cdhChinese/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70501)" style="display: initial;">中德学部</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://cdhk.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70508)" style="display: initial;">中德学院</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://cdhaw.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70502)" style="display: initial;">中德工程学院</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://cdibb.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70511)" style="display: initial;">职业技术教育学院</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://dk.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70509)" style="display: initial;">出国培训学院、留德预备部</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://is.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70507)" style="display: initial;">国际文化交流学院</a></h4>
                    </li>
                    <li style="width:63%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://unep-iesd.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70503)" style="display: initial;">联合国环境规划署-同济大学环境与可持续发展学院</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70663)" style="display: initial;">卓越工程师学院/国际工程师学院</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://ifcim.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70504)" style="display: initial;">中法工程和管理学院</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://tjsic.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70506)" style="display: initial;">中意学院</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://sfc.tongji.edu.cn/chinese/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70505)" style="display: initial;">中芬中心</a></h4>
                    </li>
                    <li style="width:30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://ssc.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70510)" style="display: initial;">中西学院</a></h4>
                    </li>
</UL></div>
           
        </div>
         <div class="mechanism clearfix">
            <div class="mechanism-wp" style="width: 100%;padding-left: 20px;"><UL>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://tjee.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70498)" style="display: initial;">继续教育学院、网络教育学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://nzxy.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70500)" style="display: initial;">女子学院</a></h4>
                    </li>
                    <li style="width: 30%;float: left;margin-right: 30px;">
                        <h4><span><img src="../../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://sie.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70499)" style="display: initial;">创新创业学院</a></h4>
                    </li>
</UL></div>
           
        </div>
        </div>
    </div>
</div>
<!-- 内容部分end -->
"""
html_source3='''<span>党政部门</span>
     
</div>
        </div>
        <div class="department">
           
            <ul class="clearfix" style="padding: 0 16px;">

              
<li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://dangban.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70559)" style="display: initial;">党委办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://jw.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70564)" style="display: initial;">纪检监察机构</a>

<i></i>
</h4>

<div class="dropdown">

<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70560)">办公室</a>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70561)">第一纪检监察室</a>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70562)">第二纪检监察室</a>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70563)">综合业务室</a>

</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70565)" style="display: initial;">党委巡视工作办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://tjzzb.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70566)" style="display: initial;">党委组织部、党校</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://news.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70567)" style="display: initial;">党委宣传部（宣传处）</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://tzb.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70568)" style="display: initial;">党委统战部</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li style="    float: left;    width: 64.7%;    height: 48px;    position: relative;    margin: 0 20px 10px 0">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://student.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70570)" style="display: initial;">党委学生工作部（学生处）、党委研究生工作部</a>

<i></i>
</h4>

<div class="dropdown">

<a href="https://tj91.tongji.edu.cn/index.jsp" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70569)">就业指导中心</a>

</div>
</li>


                
                <li style="    float: left;    width: 30%;    height: 48px;    position: relative;">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>


<a href="https://jsgzb.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70571)" style="display: initial;">党委教师工作部</a>

</h4>

<div class="dropdown">


</div>
</li>


    <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://baowei.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70572)" style="display: initial;">党委保卫部（保卫处）、</a><a href="https://wzb.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70572)" style="display: initial;">武装部</a>

</h4>

<div class="dropdown">


</div>
</li>


    
    
    
    
                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://jgdw.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70573)" style="display: initial;">机关党委</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://ltb.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70574)" style="display: initial;">离退休干部党工委、离退休工作办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                
                
                </ul></div>
                 <div class="department">
                <ul class="clearfix" style="padding: 0 16px;">
                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://deanoffi.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70580)" style="display: initial;">校长办公室、对外联络与发展办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://fzgh.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70592)" style="display: initial;">发展规划与学科建设部</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://jwc.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70581)" style="display: initial;">本科生院</a>

</h4>

<div class="dropdown">


</div>
</li>


                
                
                
                
                
                
                
                
                
                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://gs.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70583)" style="display: initial;">研究生院</a>

<i></i>
</h4>

<div class="dropdown">

<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70582)">学位评定委员会办公室</a>

</div>
</li>






                
                
                
                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://qa.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70584)" style="display: initial;">教学质量管理办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://kgb.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70585)" style="display: initial;">科研管理部</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://xjy.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70586)" style="display: initial;">先进技术研究院</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://wkb.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70587)" style="display: initial;">文科办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://hr.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70588)" style="display: initial;">人事处</a>

<i></i>
</h4>

<div class="dropdown">

<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70591)">人才工作领导小组...</a>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70589)">博士后管理办公室</a>
<a href="https://rczx.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70590)">人才中心</a>

</div>
</li>


                
                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://fao.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70593)" style="display: initial;">外事办公室</a>

<i></i>
</h4>

<div class="dropdown">

<a href="https://fao.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70594)">港澳台事务办公室</a>
<a href="http://study.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70595)">留学生办公室</a>

</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://tjcwc.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70597)" style="display: initial;">财务处</a>

<i></i>
</h4>

<div class="dropdown">

<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70596)">国有资产管理委员会办公室</a>

</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://sjc.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70598)" style="display: initial;">审计处</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://jjc.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70599)" style="display: initial;">基建处</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://zcsys.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70602)" style="display: initial;">资产与实验室管理处</a>

<i></i>
</h4>

<div class="dropdown">

<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70601)">实验室安全管理办公室</a>
<a href="http://nyglzx.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70600)">能源管理中心</a>

</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70603)" style="display: initial;">医院管理处</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://nic.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70605)" style="display: initial;">信息化办公室</a>

<i></i>
</h4>

<div class="dropdown">

<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70604)">教育技术与计算中心</a>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70606)">网络管理中心</a>

</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70607)" style="display: initial;">基础教育合作办学管理委员会办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                
                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://hqc.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70608)" style="display: initial;">后勤管理与保障处</a>

</h4>

<div class="dropdown">


</div>
</li>


                
                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://jiading.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70609)" style="display: initial;">嘉定校区管理委员会办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                
                
                
                
                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://hx.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70610)" style="display: initial;">沪西校区管理委员会办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                
                 <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://hb.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70611)" style="display: initial;">沪北校区管理办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                
               
                
                
                
                
                
                
                
            </ul>
        </div>
        
         <div class="department">
                <ul class="clearfix" style="padding: 0 16px;">
        
        
        <li style="margin: 0 20px 10px 0;">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70575)" style="display: initial;">嘉定校区党工委</a>

</h4>

<div class="dropdown">


</div>
</li>


                
               
                
                
                
                <li style="    margin-right: 70px;">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>

<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70576)" style="display: initial;">医学与生命科学联合党工委</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li style="    margin-right: 20px;">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://gonghui.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70577)" style="display: initial;">工会</a>

</h4>

<div class="dropdown">


</div>
</li>


        <li style="margin: 0 20px 10px 0;">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://youth.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70578)" style="display: initial;">团委</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li style="margin: 0 20px 10px 0;">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://women.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70579)" style="display: initial;">妇委</a>

</h4>

<div class="dropdown">


</div>
</li>


                
                 
        
         </ul>
        </div>
         <div class="department">
                <ul class="clearfix" style="padding: 0 16px;">
        <li style="width: 299px">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://ggw.tongji.edu.cn/index.php?classid=1100" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70645)" style="display: initial;">关心下一代工作委员会</a>

</h4>

<div class="dropdown">


</div>
</li>

</ul>
        </div>
    </div>
</div>
<!-- 内容部分end -->'''
html_source4='''<span>直属单位</span>
     
</div>
        </div>
        <div class="department">
            
            <ul class="clearfix" style="padding: 0 16px;">

              
<li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://www.lib.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70612)" style="display: initial;">图书馆</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://dafw.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70614)" style="display: initial;">档案馆</a>

<i></i>
</h4>

<div class="dropdown">

<a href="http://gtjuh.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70613)">校史馆</a>

</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://czb.tongji.edu.cn/sggl/cgw/index.jsp" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70615)" style="display: initial;">采购与招标管理办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://agri.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70616)" style="display: initial;">新农村发展研究院</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://nmtc.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70619)" style="display: initial;">磁浮交通工程技术研究中心</a>

</h4>

<div class="dropdown">


</div>
</li>


                <li>
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70617)" style="display: initial;">国家海底科学观测系统项目办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


               <li style="width: 613px;">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="https://srias.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70618)" style="display: initial;">上海自主智能无人系统科学中心建设领导小组办公室</a>

</h4>

<div class="dropdown">


</div>
</li>


                
                <li style="width: 281px;">
<h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span>
<a href="http://shtjh.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70620)" style="display: initial;">同济大学附属同济医院分院</a>

</h4>

<div class="dropdown">


</div>
</li>


    
    
    
    
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
                
                
                
                
                
                
                
                
                
                
                
                
                




                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            </ul>
        </div>
    </div>
</div>
<!-- 内容部分end -->'''
html_source5='''<span>附属单位及直管企业</span>
     
</div>
        </div>
       
        <div class="mechanism clearfix"><div class="mechanism-wp" style="width: 100%;padding-left: 10px;"><UL>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://www.tongjihospital.com.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70628)" style="display: initial;">同济大学附属同济医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://kouqiang.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70629)" style="display: initial;">同济大学附属口腔医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://www.shdsyy.com.cn/web/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70622)" style="display: initial;">同济大学附属第十人民医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://www.easthospital.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70623)" style="display: initial;">同济大学附属东方医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://www.shsfkyy.com/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70625)" style="display: initial;">同济大学附属上海市肺科医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://www.51mch.com/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70631)" style="display: initial;">同济大学附属第一妇婴保健院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://www.shypzx.com/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70621)" style="display: initial;">同济大学附属杨浦医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://www.shygkf.org.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70630)" style="display: initial;">同济大学附属养志康复医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://www.shskin.com/index.php?classid=3841" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70626)" style="display: initial;">同济大学附属皮肤病医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://www.sh4th.com/index.html" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70627)" style="display: initial;">同济大学附属上海市第四人民医院</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70624)" style="display: initial;">同济大学附属精神卫生中心</a></h4>
                    </li>
                    <li style="width: 32%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70653)" style="display: initial;">同济大学附属普陀人民医院</a></h4>
                    </li>
</UL></div>
           
        </div>
         <div class="mechanism clearfix">
            <div class="mechanism-wp" style="width: 100%;padding-left: 10px;"><UL>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://tjyfz.tongji.edu.cn/main.htm" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70632)" style="display: initial;">同济大学第一附属中学</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://www.hstjef.pte.sh.cn" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70636)" style="display: initial;">同济大学第二附属中学</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://www.71school.edu.sh.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70633)" style="display: initial;">同济大学附属七一中学</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70637)" style="display: initial;">同济大学附属实验中学（同济大学附属嘉定实验中学）</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70634)" style="display: initial;">同济大学附属实验小学（同济大学附属嘉定实验小学）</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70638)" style="display: initial;">同济大学附属嘉定实验幼儿园</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="#" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70639)" style="display: initial;">同济大学附属新江湾城实验学校</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://www.qd37.qdedu.net/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70635)" style="display: initial;">同济大学附属青岛礼贤初级中学</a></h4>
                    </li>
</UL></div>
           
        </div>
         <div class="mechanism clearfix">
            <div class="mechanism-wp" style="width: 100%;padding-left: 10px;"><UL>
                    <li style="width: 48%;float: left;margin-right: 28px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://tjkg.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70642)" style="display: initial;">同济创新创业控股有限公司</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://tjhq.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70644)" style="display: initial;">上海同济后勤产业发展有限公司</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://www.tjad.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70640)" style="display: initial;">同济大学建筑设计研究院（集团）有限公司</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="https://press.tongji.edu.cn/" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70643)" style="display: initial;">同济大学出版社有限公司</a></h4>
                    </li>
                    <li style="width: 48%;float: left;margin-right: 12px;">
                        <h4><span><img src="../images/jiaotou1110.png" style="width: 13px;"></span><a href="http://www.tjupdi.com/new" title="" onclick="_addDynClicks(&#34;wburl&#34;, 1454720253, 70641)" style="display: initial;">上海同济城市规划设计研究院有限公司</a></h4>
                    </li>
</UL></div>
           
        </div>
        </div>
    </div>
</div>
<!-- 内容部分end -->'''

html_dict={"院部设置":html_source2,"治理结构":html_source1,"党政部门":html_source3,"直属单位":html_source4,"附属单位及直管企业":html_source5}
dep_dict={"治理结构":None,"院部设置":None,"党政部门":None,"直属单位":None,"附属单位及直管企业":None}

for key in html_dict.keys():
    soup = BeautifulSoup(html_dict[key], 'html.parser')

    # 查找"党政部门"所在的<span>标签
    span_element = soup.find('span', string=key)

    # 初始化部门字典
    departments = {}

    # 找到<ul>标签下的所有<li>标签
    if span_element:
        ul_element = span_element.find_next('ul')
        if ul_element:
            li_elements = ul_element.find_all('li')
            current_department = None  # 当前正在处理的部门
            for li in li_elements:
                h4_element = li.find('h4')
                if h4_element:
                    a_element = h4_element.find('a')
                    if a_element:
                        department_name = a_element.get_text().strip()
                        departments[department_name] = []
                        current_department = departments[department_name]

                        # 检查是否有下级部门
                        dropdown_div = li.find('div', class_='dropdown')
                        if dropdown_div:
                            sub_departments = dropdown_div.find_all('a')
                            for sub_department in sub_departments:
                                sub_name = sub_department.get_text().strip()
                                current_department.append(sub_name)
    dep_dict[key]=departments
print(dep_dict)
