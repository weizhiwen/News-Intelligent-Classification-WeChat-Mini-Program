# 公用工具类

from bs4 import BeautifulSoup

# 转换新闻内容，将html标签转换为wxml标签
def html2wxml_news_content(news_content):
    pass

if __name__ == "__main__":
    news_content = """
    <div class="left_zw" style="position:relative">  
<p>　　近日，有网友在微博上提起，全国各个省市的人力资源和社会保障局官方网站上列有许多补贴职业培训项目，推荐一些符合条件的网友报名参加，充实自我。很多课程全部由通过政府认证许可的职业学校或就业中心负责具体培训。符合享受政府培训费用补贴的对象，参加课程并考核合格后，不仅可以获得技能登记证书，还能享受高达50%-100%的培训费用补贴。</p>

<p>　　“过来人”分享体会：花费不多 收获颇丰</p>

<p>　　评论区出现了不少“过来人”，分享了许多自己参加课程的有趣经历。</p>

<p>　　无论是暗自蓄力重新出发的失业人员、还是退休后上课打发时间的大叔大妈、抑或是刚毕业还需继续充电的学生党们，都在这些花费不大的技能课程中收获颇丰。</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/1736260037.png" /><img src="http://www.chinanews.com/cr/2019/0330/3525953723.png" /><img src="http://www.chinanews.com/cr/2019/0330/4244548533.png" /><img src="http://www.chinanews.com/cr/2019/0330/2383282182.png" /><img src="http://www.chinanews.com/cr/2019/0330/478750541.png" />

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/2390654632.png" /></p>
</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/2570514240.png" /></p>

<p>　　课程种类丰富 专业老师指导</p>

<p>　　除了电工、钳工这类特种技能对一些技术人员来说是刚需，非常热门以外，像插花、烹饪、茶艺这类日常生活都能用到的技能也广受大众欢迎。</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/3458061744.png" /><img src="http://www.chinanews.com/cr/2019/0330/300190990.png" /><img src="http://www.chinanews.com/cr/2019/0330/2168006367.png" />

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/1427003489.png" /></p>
</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/265139664.png" /></p>

<p>　　△网友晒出的课程成果</p>

<p>　　很多人还提到，在许多负责认真的专业老师指导下，充分利用闲暇时光习得一门技能不是难事。</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/3422112185.png" />

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/307954894.png" /></p>
</p>

<p>　　考核严格 通过则可获得国家认可的证书</p>

<p>　　与某些社会组织“光学就完事”的技能兴趣班不同，这些课程都必须通过正规严厉的最终考核，才能获得国家认可的技能证书持证上岗。</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/2191376820.png" />

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/3496522813.png" /></p>
</p>

<p>　　各地职业培训和具体政策不相同</p>

<p>　　细看各个省市政府补贴的职业培训项目中，除了常见常用技能，一些省市的项目名单中还出现了一些“新奇玩意”。</p>

<p>　　在上海职业培训指导服务网站上，有网友发现职业资格项目中有一个名叫“白山羊饲养”的课程，课程介绍称这是一门有关白山羊饲养管理，羊病的预防和简易治疗，以及羊舍建设等技术。</p>

<p>　　同样在广州的职业培训名录上，也有像婚姻家庭咨询师、手语翻译员、芳香保健师、小儿推拿师等其他省市少见的技能培训。</p>

<p>　　职业培训服务更加人性化</p>

<p>　　为了方便学员能够更方便地查询相关培训信息，各地政府除了在人力资源官网上公布内容，还有些地方开始探索网络新工具——开发运营职业培训的APP和小程序。</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/561000170.png" /></p>

<p>　　今年1月底，“广州职业培训地图(线上版)”就正式上线运行，这个小程序能够帮助广州全市职业培训学员仅仅通过微信，就可以简单便捷地选择职业培训机构以及课程内容。</p>

<p>　　所有培训机构的管理和展示集成到一个平台，清晰展示了培训课程与机构的简介信息、场地图片、许可培训项目、联系方式等内容，在地图功能的协助下还能够提供定位导航服务。</p>

<p>　　较为贴心的是，广州这款小程序还引入VR实景功能，学员在报名前足不出户，只要用手机就能了解培训机构的现场实景，这个功能在全国实属创新一步。</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/574470060.gif" /></p>

<p>　　△某职业培训指导中心家政护理实训室</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/849623132.gif" /></p>

<p>　　△某职业培训指导中心中式烹饪实训室</p>

<p>　　培训有条件 不是所有人都可以随意参加</p>

<p>　　根据2017年财政部、人力资源社会保障部印发的《就业补助资金管理办法》通知。其中明确规定，能够享受这类职业培训补贴的人员范围只有“五类人员”和部分符合条件的企业职工。</p>

<p>　　“五类人员”包括贫困家庭子女、毕业年度高校毕业生(含技师学院高级工班、预备技师班和特殊教育院校职业教育类毕业生)、城乡未继续升学的应届初高中毕业生、农村转移就业劳动者、城镇登记失业人员工。</p>

<p>　　各地具体办法实施也会在此基础上进行更详细的要求划分。以上海为例，补贴对象的大类主要以“是否为该市户籍”划分，并且将具备该市户籍的退役士兵和残疾人等经认定者也列入可享受补贴名单。</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/3818101938.png" /></p>

<p>　　而各类人群具体可享受的补贴比例也有明确规定，在培训安排互不冲突的情况下如果同时参加不同培训，一年只能享受一个项目的补贴优惠。</p>

<p>　　<img src="http://www.chinanews.com/cr/2019/0330/1403117411.png" /></p>

<p>　　▌本文来源：观察者网</p><table border=0 cellspacing=0 cellpadding=0 align=left style="padding-right:10px;"><tr><td><div id=adhzh name=hzh>

<script>
(function() {
    var s = "_" + Math.random().toString(36).slice(2);
    document.write('<div id="' + s + '"></div>');
    (window.slotbydup=window.slotbydup || []).push({
        id: '2473874',
        container: s,
        size: '300,250',
        display: 'inlay-fix'
    });
})();
</script>
<script src="http://dup.baidustatic.com/js/os.js"></script>

</div>

</td></tr></table><div id="function_code_page"></div>  

      </div>
    """
    # print(news_content)
    htmlsoup = BeautifulSoup(news_content, "lxml")
    new_tag = htmlsoup.new_tag("text")
    # 去除所有的script标签
    [s.extract() for s in htmlsoup("script")]
    # 
    [s.wrap(new_tag) for s in htmlsoup("p")]
    print(htmlsoup)
    # wxmlsoup = BeautifulSoup("<view></view>", "lxml")
    # print('测试：' + str(htmlsoup.p))
    # for p in htmlsoup.find_all('p'):
    #     wxmlsoup.insert(1, p)
    # print(wxmlsoup)