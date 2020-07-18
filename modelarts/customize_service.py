<!DOCTYPE html>
<html lang='zh-CN'>
<head>
<title>official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py · ModelArts/ModelArts-Lab - 码云 Gitee.com</title>
<link href="https://assets.gitee.com/assets/favicon-9007bd527d8a7851c8330e783151df58.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
<meta content='gitee.com/ModelArts/ModelArts-Lab git https://gitee.com/ModelArts/ModelArts-Lab.git' name='go-import'>
<meta charset='utf-8'>
<meta content='always' name='referrer'>
<meta content='码云' property='og:site_name'>
<meta content='Object' property='og:type'>
<meta content='http://gitee.com/ModelArts/ModelArts-Lab/blob/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py' property='og:url'>
<meta content='https://gitee.com/static/images/logo_themecolor.png' itemprop='image' property='og:image'>
<meta content='official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py · ModelArts/ModelArts-Lab - 码云 Gitee.com' itemprop='name' property='og:title'>
<meta content='ModelArts-Lab是基于华为云ModelArts平台的示例代码库(内容与github一致)' property='og:description'>
<meta content='码云,代码托管,git,Git@OSC,gitee.com,开源,内源,项目管理,版本控制,开源代码,代码分享,项目协作,开源项目托管,免费代码托管,Git代码托管,Git托管服务' name='Keywords'>
<meta content='ModelArts-Lab是基于华为云ModelArts平台的示例代码库(内容与github一致)' itemprop='description' name='Description'>

<meta content="IE=edge" http-equiv="X-UA-Compatible" />
<meta content="authenticity_token" name="csrf-param" />
<meta content="zcj+uvjq/HNuidbOrVb6HDZy2HFUeNM7S5mmnmOjb80=" name="csrf-token" />

<link href="https://assets.gitee.com/assets/application-855de085bf19856c55ec7345cdd97e55.css" media="all" rel="stylesheet" />
<script>
//<![CDATA[
window.gon = {};gon.locale="zh-CN";gon.sentry_dsn=null;gon.baidu_register_hm_push=null;gon.info={"controller_path":"blob","action_name":"show","current_user":false};gon.tour_env={"current_user":null,"action_name":"show","original_url":"http://gitee.com/ModelArts/ModelArts-Lab/blob/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py","controller_path":"blob"};gon.http_clone="https://gitee.com/ModelArts/ModelArts-Lab.git";gon.user_project="ModelArts/ModelArts-Lab";gon.manage_branch="管理分支";gon.manage_tag="管理标签";gon.enterprise_id=0;gon.create_reaction_path="/ModelArts/ModelArts-Lab/reactions";gon.ref="master";
//]]>
</script>
<script src="https://assets.gitee.com/assets/static/sentry-5.1.0-109ee3d8895a239331efcf947ba7f5d8.js"></script>
<script src="https://assets.gitee.com/assets/application-a450ef00c4c922bb8d66b150e782139a.js"></script>
<script src="https://assets.gitee.com/assets/lib/jquery.timeago.zh-CN-9c36ca7c4899a28168320613879d208a.js"></script>

<link href="https://assets.gitee.com/assets/projects/application-c4d2b90e83d054a150b44a0e5a32f7c5.css" media="all" rel="stylesheet" />
<script src="https://assets.gitee.com/assets/projects/app-6de13fd09a69ffee57a5387ad0f751a5.js"></script>

<script src="//res.wx.qq.com/open/js/jweixin-1.2.0.js"></script>
<script>
  var title = document.title.replace(/( - Gitee| - 码云)$/, '')
      imgUrl = '';
  
  document.addEventListener('DOMContentLoaded', function(event) {
    var imgUrlEl = document.querySelector('.readme-box .markdown-body > img, .readme-box .markdown-body :not(a) > img');
    imgUrl = imgUrlEl && imgUrlEl.getAttribute('src');
  
    if (!imgUrl) {
      imgUrlEl = document.querySelector('meta[itemprop=image]');
      imgUrl = imgUrlEl && imgUrlEl.getAttribute('content'); 
      imgUrl = imgUrl || "https://gitee.com/static/images/logo_themecolor.png";
    }
  
    wx.config({
      debug: false,
      appId: "wxff219d611a159737",
      timestamp: "1595056581",
      nonceStr: "04a608222fe1e3c52983feee6cd722af",
      signature: "ab9ad0862fd00aa5620e13f95a71d565f6e1e9e2",
      jsApiList: [
        'onMenuShareTimeline',
        'onMenuShareAppMessage'
      ]
    });
  
    wx.ready(function () {
      wx.onMenuShareTimeline({
        title: title, // 分享标题
        link: "https://gitee.com/ModelArts/ModelArts-Lab/blob/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py", // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
        imgUrl: imgUrl // 分享图标
      });
      wx.onMenuShareAppMessage({
        title: title, // 分享标题
        link: "https://gitee.com/ModelArts/ModelArts-Lab/blob/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py", // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
        desc: document.querySelector('meta[name=Description]').getAttribute('content'),
        imgUrl: imgUrl // 分享图标
      });
    });
    wx.error(function(res){
      console.error('err', res)
    });
  })
</script>

<script type='text/x-mathjax-config'>
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    displayMath: [["$$","$$"],["\\[","\\]"]],
    processEscapes: true,
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    ignoreClass: "container|files",
    processClass: "markdown-body"
  }
});
</script>
<script src="https://assets.gitee.com/uploads/resources/MathJax-2.7.2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<script>
  (function () {
    var messages = {
      'zh-CN': {
        addResult: '增加 <b>{term}</b>',
        count: '已选择 {count}',
        maxSelections: '最多 {maxCount} 个选择',
        noResults: '未找到结果',
        serverError: '连接服务器时发生错误'
      },
      'zh-TW': {
        addResult: '增加 <b>{term}</b>',
        count: '已選擇 {count}',
        maxSelections: '最多 {maxCount} 個選擇',
        noResults: '未找到結果',
        serverError: '連接服務器時發生錯誤'
      }
    }
  
    if (messages[gon.locale]) {
      $.fn.dropdown.settings.message = messages[gon.locale]
    }
  }());
</script>

<script>
  var userAgent = navigator.userAgent;
  var isLessIE11 = userAgent.indexOf('compatible') > -1 && userAgent.indexOf('MSIE') > -1;
  if(isLessIE11){
    var can_access = ""
    if (can_access != "true"){
      window.location.href = "/incompatible.html";
    }
  }
</script>
</head>

<body class='git-project lang-zh-CN'>
<header class='common-header fixed noborder' id='git-header-nav'>
<div class='ui container'>
<div class='ui menu header-menu'>
<div class='git-nav-expand-bar'>
<i class='iconfont icon-mode-table'></i>
</div>
<div class='gitee-nav__sidebar'>
<div class='gitee-nav__sidebar-container'>
<div class='gitee-nav__sidebar-top'>
<div class='gitee-nav__avatar-box'></div>
<div class='gitee-nav__buttons-box'>
<a class="ui button small fluid orange" href="/login">登录</a>
<a class="ui button small fluid basic is-register" href="/signup">注册</a>
</div>
</div>
<div class='gitee-nav__sidebar-middle'>
<div class='gitee-nav__sidebar-list'>
<ul>
<li class='gitee-nav__sidebar-item'>
<a href="/explore"><i class='iconfont icon-ic-discover'></i>
<span class='gitee-nav__sidebar-name'>开源软件</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/enterprises"><i class='iconfont icon-ic-enterprise'></i>
<span class='gitee-nav__sidebar-name'>企业版</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/education"><i class='iconfont icon-ic-education'></i>
<span class='gitee-nav__sidebar-name'>高校版</span>
</a></li>
<li class='gitee-nav__sidebar-item split-line'></li>
<li class='gitee-nav__sidebar-item'>
<a href="/search"><i class='iconfont icon-ic-search'></i>
<span class='gitee-nav__sidebar-name'>搜索</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/help"><i class='iconfont icon-help-circle'></i>
<span class='gitee-nav__sidebar-name'>帮助中心</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/terms"><i class='iconfont icon-file'></i>
<span class='gitee-nav__sidebar-name'>使用条款</span>
</a></li>
<li class='gitee-nav__sidebar-item'>
<a href="/about_us"><i class='iconfont icon-issuepx'></i>
<span class='gitee-nav__sidebar-name'>关于我们</span>
</a></li>
</ul>
</div>
</div>
<div class='gitee-nav__sidebar-bottom'>
<div class='gitee-nav__sidebar-close-button'>
<i class='fa fa-angle-double-left'></i>
</div>
</div>
</div>
</div>

<div class='item gitosc-logo'>
<a href="/"><img alt='码云 Gitee — 基于 Git 的代码托管和研发协作平台' class='ui inline image' height='28' src='/static/images/logo.svg?t=158106664' title='码云 Gitee — 基于 Git 的代码托管和研发协作平台' width='95'>
<img alt='码云 Gitee — 基于 Git 的代码托管和研发协作平台' class='ui inline black image' height='28' src='/static/images/logo-black.svg?t=158106664' title='码云 Gitee — 基于 Git 的代码托管和研发协作平台' width='95'>
</a></div>
<a class="item " href="/explore" title="开源软件">开源软件
</a><a class="item " href="/enterprises" title="企业版">企业版
<sup class='ui red label'>
特惠
</sup>
</a><a class="item " href="/education" title="高校版">高校版
</a><a class="item" href="https://blog.gitee.com/" id="gitee-blog" target="_blank" title="博客">博客
</a><div class='center responsive-logo'>
<a href="/"><img alt='码云 Gitee — 基于 Git 的代码托管和研发协作平台' class='ui inline image' height='24' src='/static/images/logo.svg?t=158106664' title='码云 Gitee — 基于 Git 的代码托管和研发协作平台' width='85'>
<img alt='码云 Gitee — 基于 Git 的代码托管和研发协作平台' class='ui inline black image' height='24' src='/static/images/logo-black.svg?t=158106664' title='码云 Gitee — 基于 Git 的代码托管和研发协作平台' width='85'>
</a></div>
<div class='right menu userbar' id='git-nav-user-bar'>
<form accept-charset="UTF-8" action="/search" class="ui item" data-text-filter="搜索格式不正确" data-text-require="搜索关键字不能少于1个" id="navbar-search-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<input id="navbar-search-type" name="type" type="hidden" />
<input id="fork_filter" name="fork_filter" type="hidden" value="on" />
<div class='ui search'>
<input class="prompt" id="navbar-search-input" name="q" placeholder="搜索项目" type="text" value="" />
</div>
</form>

<script>
  var can_search_in_repo = 1,
      repo = "VDBSSk0wMVVaek5PUjBVelRtcE9iV0UzTmpObWE3NjNm",
      reponame = "ModelArts/ModelArts-Lab";
  
  $(function() {
    var $search = $('#navbar-search-form .ui.search');
    $search.search({
      apiSettings: {
        url: '/search/relative_project?q={query}',
        onResponse: function (res) {
          if (res && res.status === 200 && res.data) {
            var query = htmlSafe($search.search('get value'));
  
            res.data.map(function (item) {
              item.path_ns = '/' + item.path_ns;
              item.icon = 'iconfont icon-project-public';
            });
            res.data.unshift({
              name_ns: "在全站搜索 <b class='hl'>" + query +"</b> 相关项目",
              path_ns: '/search?fork_filter=on&q=' + query,
              icon: 'iconfont icon-search'
            });
            if(can_search_in_repo == 1) {
              res.data.unshift({
                name_ns: "在当前仓库搜索 <b class='hl'>" + query +"</b> 相关代码",
                path_ns: '/search?type=code&q=' + query + '&repo=' + repo + '&reponame=' + reponame,
                icon: 'iconfont icon-search'
              });
            }
            return res;
          } else {
            return { data: [] };
          }
        }
      },
      fields: {
        results: 'data',
        description: 'name_ns',
        url: 'path_ns',
        icon: 'icon'
      },
      minCharacters: 1,
      maxResults: 10,
      searchDelay: 250,
      showNoResults: false,
      transition: 'fade'
    });
  });
</script>

<a class="item git-nav-user__login-item" href="/login">登录
</a><a class="item git-nav-user__register-item" href="/signup">注册
</a><script>
  $('.destroy-user-session').on('click', function() {
    $.cookie('access_token', null, { path: '/' });
  })
</script>

</div>
</div>
</div>
</header>
<script>
  Gitee.initNavbar()
  Gitee.initRepoRemoteWay()
</script>

<script>
  var userAgent = navigator.userAgent;
  var isLessIE11 = userAgent.indexOf('compatible') > -1 && userAgent.indexOf('MSIE') > -1;
  if(isLessIE11){
    var can_access = ""
    if (can_access != "true"){
      window.location.href = "/incompatible.html";
    }
  }
</script>

<div class='fixed-notice-infos'>
<div class='all-messages'>
</div>
<div class='ui container'>
<div class='flash-messages' id='messages-container'></div>
</div>
<script>
  (function() {
    $(function() {
      var $error_box, alertTip, notify_content, notify_options, template;
      template = '<div data-notify="container" class="ui {0} message" role="alert">' + '<i data-notify="dismiss" class="close icon"></i>' + '<span data-notify="message">{2}</span>' + '</div>';
      notify_content = null;
      notify_options = {};
      alertTip = '';
      $error_box = $(".flash_error.flash_error_box");
      if (notify_options.type === 'error' && $error_box.length > 0 && !$.isEmptyObject(notify_content.message)) {
        if (notify_content.message === 'captcha_fail') {
          alertTip = "验证码不正确";
        } else if (notify_content.message === 'captcha_expired') {
          alertTip = "验证码已过期，请点击刷新";
        } else if (notify_content.message === 'not_found_in_database') {
          alertTip = "帐号或者密码错误";
        } else if (notify_content.message === 'not_found_and_show_captcha') {
          alertTip = "帐号或者密码错误";
        } else if (notify_content.message === 'phone_captcha_fail') {
          alertTip = "手机验证码不通过";
        } else {
          alertTip = notify_content.message;
        }
        return $error_box.html(alertTip).show();
      } else if (notify_content) {
        if ("show" === 'third_party_binding') {
          return $('#third_party_binding-message').html(notify_content.message).addClass('ui message red');
        }
        notify_options.delay = 3000;
        notify_options.template = template;
        notify_options.offset = {
          x: 10,
          y: 30
        };
        notify_options.element = '#messages-container';
        return $.notify(notify_content, notify_options);
      }
    });
  
  }).call(this);
</script>

</div>
<script>
  (function() {
    $(function() {
      var setCookie;
      setCookie = function(name, value) {
        $.cookie(name, value, {
          path: '/',
          expires: 365
        });
      };
      $('#remove-bulletin, #remove-bulletin-dashboard').on('click', function() {
        setCookie('remove_bulletin', "gitee-maintain-1594434874");
        $('#git-bulletin').hide();
      });
      $('#remove-member-bulletin').on('click', function() {
        setCookie('remove_member_bulletin', "gitee_member_bulletin");
        $(this).parent().hide();
      });
      return $('#remove-gift-bulletin').on('click', function() {
        setCookie('remove_gift_bulletin', "gitee-gift-bulletin");
        $(this).parent().hide();
      });
    });
  
  }).call(this);
</script>
<script>
  function closeMessageBanner(pthis, type, val) {
    var json = {}
  
    val = typeof val === 'undefined' ? null : val
    $(pthis).parent().remove()
    if (type === 'out_of_enterprise_member') {
      json = {type: type, data: val}
    } else if (type === 'enterprise_overdue') {
      json = {type: type, data: val}
    }
    $.post('/profile/close_flash_tip', json)
  }
</script>

<div class='site-content'>
<div class='git-project-header'>
<div class='fixed-notice-infos'>
<div class='ui info icon floating message green' id='fetch-ok' style='display: none'>
<div class='content'>
<div class='header status-title'>
<i class='info icon status-icon'></i>
代码拉取完成，页面将自动刷新
</div>
</div>
</div>
<div class='ui info icon floating message error' id='fetch-error' style='display: none'>
<div class='content'>
<div class='header status-title'>
<i class='info icon status-icon'></i>
<span class='error_msg'></span>
</div>
</div>
</div>
</div>
<div class='ui container'>
<div class='git-project-categories'>
<a href="/explore">开源项目</a>
<span class='symbol'>></span>
<a href="/explore/Artificial-Intelligence">人工智能</a>
<span class='symbol'>></span>
<a href="/explore/ai">AI-人工智能</a>
<span class='symbol and-symbol'>&</span>
</div>

<div class='git-project-header-details'>
<div class='git-project-header-container'>
<div class='git-project-header-actions'>
<span class='basic ui buttons pointing top left dropdown metrics-radar'>
<div class='ui button project-radar'>
<i class='iconfont icon-radar'></i>
指数
</div>
<div class='ui button action-social-count exponent-total-sorce'>
0
</div>
<div class='menu radar'>
<div class='item radar-menu'>
<div class='hide' data-url='/ModelArts/ModelArts-Lab/project_radars' id='metrics-radar'>
<div class='title'>
<div class='fisrt-title'>
<div class='project-name' title='ModelArts-Lab'>
ModelArts-Lab
</div>
<div class='gitee-exponent'>
<div class='text'></div>
<div class='exponent-score'></div>
</div>
</div>
<div class='total-percent'>
<div class='percent-header'></div>
<div class='percent-score'></div>
<div class='percent-end'></div>
</div>
</div>
<div class='wrap'></div>
<div class='project-radar-list'>
<div class='descript-contianer'>
<div class='descript-title'>
<p>代码活跃度</p>
<p>社区活跃度</p>
<p>团队健康</p>
<p>流行趋势</p>
<p>影响力</p>
</div>
<div class='descript'>
<p>：与代码提交频次相关</p>
<p>：与项目和用户的issue、pr互动相关</p>
<p>：与团队成员人数和稳定度相关</p>
<p>：与项目近期受关注度相关</p>
<p>：与项目的star、下载量等社交指标相关</p>
</div>
</div>
</div>
<div class='finaltime'></div>
</div>
<script src="https://assets.gitee.com/assets/skill_radar/rep_app-301ecccea9b1eac212beffa1823bf8c7.js"></script>

</div>
</div>
</span>
<div class='ui tiny modal project-donate-modal' id='project-donate-modal'>
<i class='iconfont icon-close close'></i>
<div class='header'>捐赠</div>
<div class='content'>
捐赠前请先登录
</div>
<div class='actions'>
<a class='ui blank button cancel'>取消</a>
<a class='ui orange ok button' href='/login'>前往登录</a>
</div>
</div>
<div class='ui small modal wepay-qrcode'>
<i class='iconfont icon-close close'></i>
<div class='header'>
扫描微信二维码支付
<span class='wepay-cash'></span>
</div>
<div class='content weqcode-center'>
<img id='wepay-qrcode' src=''>
</div>
<div class='actions'>
<div class='ui cancel blank button'>取消</div>
<div class='ui ok orange button'>
支付完成
</div>
</div>
</div>
<div class='ui mini modal' id='confirm-alipay-modal'>
<div class='header'>支付提示</div>
<div class='content'>
将跳转至支付宝完成支付
</div>
<div class='actions'>
<div class='ui approve orange button'>
确定
</div>
<div class='ui blank cancel button'>
取消
</div>
</div>
</div>

<span class='ui basic buttons watch-container'>
<a class="ui button watch" href="/login" title="你必须登录后才可以watch一个仓库"><i class='iconfont icon-watch'></i>
Watch
</a><a class="ui button action-social-count" href="/ModelArts/ModelArts-Lab/watchers" title="9">9
</a></span>
<span class='ui basic buttons star-container'>
<a class="ui button star" href="/login" title="你必须登录后才可以star一个仓库"><i class='iconfont icon-star'></i>
Star
</a><a class="ui button action-social-count" href="/ModelArts/ModelArts-Lab/stargazers" title="43">43
</a></span>
<span class='ui basic buttons fork-container' title='无权 Fork 此仓库'>
<a class="ui button fork" href="/login" title="你必须登录后才可以fork一个仓库"><i class='iconfont icon-fork'></i>
Fork
</a><a class="ui button action-social-count disabled-style" href="/ModelArts/ModelArts-Lab/members" title="26">26
</a></span>
</div>
<h2 class='git-project-title'>
<span class="project-title"><i class="project-icon iconfont icon-project-public" title="这是一个公开仓库"></i> <a class="author" href="/ModelArts" title="ModelArts">ModelArts</a> / <a class="repository" href="/ModelArts/ModelArts-Lab" style="padding-bottom: 0px" target="" title="ModelArts-Lab">ModelArts-Lab</a></span><span class="project-badges"><a class="ui small label proj-language" href="/explore/all?lang=Python" target="_blank" title="主要编程语言">Python</a><a class="ui small license label" href="/ModelArts/ModelArts-Lab/blob/master/LICENSE" title="开源许可协议">Apache-2.0</a><a class="git-project-recommend-badge" href="/explore" title="已被推荐"><i class='iconfont icon-recommended'></i>
</a><style>
  .gitee-modal {
    width: 500px !important; }
</style>
</span>
<input id="recomm_at" name="recomm_at" type="hidden" value="2020-06-03 19:58" />
<input id="project_title" name="project_title" type="hidden" value="ModelArts/ModelArts-Lab" />
</h2>
</div>
</div>
</div>
<div class='row' id='import-result-message' style='padding-top: 0px; display: none'>
<div class='sixteen wide column'>
<div class='ui icon yellow message status-color'>
<i class='info icon status-icon' style='width:60px;padding-right:12px;'></i>
<i class='close icon'></i>
<div class='header status-title'>
同步状态
</div>
<span class='status-message'></span>
</div>
</div>
</div>
<script>
  var title_import_url = "https://github.com/huaweicloud/ModelArts-Lab.git";
  var title_post_url = "/ModelArts/ModelArts-Lab/update_import";
  var title_fork_url = "/ModelArts/ModelArts-Lab/sync_fork";
  var title_project_path = "ModelArts-Lab";
  var title_p_name = "ModelArts-Lab";
  var title_p_id= "8271874";
  var title_description = "ModelArts-Lab是基于华为云ModelArts平台的示例代码库(内容与github一致)";
  var title_form_authenticity_token = "zcj+uvjq/HNuidbOrVb6HDZy2HFUeNM7S5mmnmOjb80=";
  var watch_type = "unwatch";
  
  $('.metrics-radar').dropdown({ action: 'nothing' });
  $('.js-project-watch').dropdown('set selected', watch_type);
  $('.checkbox.sync-wiki').checkbox();
</script>
<style>
  i.loading {
    -webkit-animation: icon-loading 1.2s linear infinite;
    animation: icon-loading 1.2s linear infinite;
  }
  .qrcode_cs {
    float: left;
  }
  .check-sync-wiki {
    float: left;
    height: 28px;
    line-height: 28px;
  }
  .sync-wiki-warn {
    color: #e28560;
  }
</style>

<div class='git-project-nav'>
<div class='ui container'>
<div class='ui secondary pointing menu'>
<a class="item active" href="/ModelArts/ModelArts-Lab"><i class='iconfont icon-code'></i>
代码
</a><a class="item " href="/ModelArts/ModelArts-Lab/issues"><i class='iconfont icon-task'></i>
Issues
<span class='ui mini circular label'>
3
</span>
</a><a class="item " href="/ModelArts/ModelArts-Lab/pulls"><i class='iconfont icon-pull-request'></i>
Pull Requests
<span class='ui mini circular label'>
0
</span>
</a><a class="item " href="/ModelArts/ModelArts-Lab/attach_files"><i class='iconfont icon-annex'></i>
附件
<span class='ui mini circular label'>0</span>
</a><a class="item " href="/ModelArts/ModelArts-Lab/wikis"><i class='iconfont icon-wiki'></i>
Wiki
<span class='ui mini circular label'>
10
</span>
</a><a class="item  " href="/ModelArts/ModelArts-Lab/graph/master"><i class='iconfont icon-statistics'></i>
统计
</a><div class='item project-devops-item'>
<div class='ui pointing top right dropdown project-devops-dropdown'>
<div class='text'>
<i class='iconfont icon-devops'></i>
DevOps
</div>
<i class='dropdown icon'></i>
<div class='menu' style='display:none'>
<a class="item" href="https://gitee.com/help/articles/4285" target="_blank"><img alt="Baidu efficiency cloud" src="https://assets.gitee.com/assets/baidu_efficiency_cloud-81a98c2eb67fac83b1453ca3d2feb326.svg" />
<div class='item-title'>
百度效率云
</div>
</a><a class="item" href="https://gitee.com/help/articles/4193" target="_blank"><img alt="Jenkins for gitee" src="https://assets.gitee.com/assets/jenkins_for_gitee-554ec65c490d0f1f18de632c48acc4e7.png" />
<div class='item-title'>
Jenkins for Gitee
</div>
</a></div>
</div>
</div>
<div class='item'>
<div class='ui pointing top right dropdown git-project-service'>
<div class='text'>
<i class='iconfont icon-service'></i>
服务
</div>
<i class='dropdown icon'></i>
<div class='menu' style='display:none'>
<a class="item" href="/ModelArts/ModelArts-Lab/pages"><img alt="Logo en" src="/static/images/logo-en.svg" />
<div class='item-title'>
Gitee Pages
</div>
</a><a class="item" href="/ModelArts/ModelArts-Lab/quality_analyses?platform=sonar_qube"><img alt="Sonar mini" src="https://assets.gitee.com/assets/sonar_mini-5e1b54bb9f6c951d97fb778ef623afea.png" />
<div class='item-title'>
质量分析
</div>
</a><a class="item" href="/ModelArts/ModelArts-Lab/quality_analyses?platform=codesafe"><img alt="Codesafe mini" src="https://assets.gitee.com/assets/codesafe_mini-accbe1e555e9864c552620240d10e4de.png" width="100%" />
<div class='item-title'>
奇安信代码卫士
</div>
</a><a class="item" href="/ModelArts/ModelArts-Lab/gitee_scans"><img alt="Giteescan" src="https://assets.gitee.com/assets/giteescan-cd9ab4076bd751faf7e30888eb10f782.png" />
<div class='item-title'>Gitee Scan</div>
</a><button class='ui orange basic button quit-button' id='quiting-button'>
我知道了，不再自动展开
</button>
</div>
</div>
</div>
<div class='item right mr-0 pr-0'>

</div>
</div>
</div>
</div>
<script>
  $('.git-project-nav .ui.dropdown').dropdown({ action: 'nothing' });
</script>
<style>
  .git-project-nav i.checkmark.icon {
    color: green;
  }
  #quiting-button {
    display: none;
  }
  
  .git-project-nav .dropdown .menu.hidden:after {
    visibility: hidden !important;
  }
</style>
<script>
  isSignIn = false
  isClickGuide = false
  $('#git-versions.dropdown').dropdown();
  $.ajax({
    url:"/ModelArts/ModelArts-Lab/access/add_access_log",
    type:"GET"
  });
  $('#quiting-button').on('click',function() {
    $('.git-project-service').click();
    if (isSignIn) {
      $.post("/projects/set_service_guide")
    }
    $.cookie("Serve_State", true, { expires: 3650, path: '/'})
    $('#quiting-button').hide();
  });
  if (!(isClickGuide || $.cookie("Serve_State") == 'true')) {
    $('.git-project-service').click()
    $('#quiting-button').show()
  }
</script>

</div>
<div class='ui container'>
<div class='register-guide'>
<div class='register-container'>
<div class='regist'>
加入 Gitee
</div>
<div class='description'>
与超过 500 万 开发者一起发现、参与优秀开源项目，私有仓库也完全免费 ：）
</div>
<a class="ui orange button free-registion" href="/signup?from=project-guide">免费加入</a>
<div class='login'>
已有帐号？
<a href="/login?from=project-guide">立即登录</a>
</div>
</div>
</div>

<div class='git-project-content-wrapper'>
<div class='git-project-content' id='git-project-content'>
<div class='row'>
<div class='git-project-desc-wrapper'>
<div class='git-project-desc'>
<div class='project-introduce'>
<span class='git-project-desc-text'>
ModelArts-Lab是基于华为云ModelArts平台的示例代码库(内容与github一致)
</span>
<a class='hide spread' href='javascript:void(0);'>
展开
<i class='caret down icon'></i>
</a>
<a class='retract hide' href='javascript:void(0);'>
收起
<i class='caret up icon'></i>
</a>
<p class='git-project-homepage'>
</p>
</div>
</div>
<div class='git-project-desc-edit flex'>
<div class='sixty-percent ui small input'>
<input name='project[description]' placeholder='描述' type='text' value='ModelArts-Lab是基于华为云ModelArts平台的示例代码库(内容与github一致)'>
</div>
<div class='twenty-percent ui small input'>
<input data-regex-value='(^$)|(^(http|https):\/\/(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).*)|(^(http|https):\/\/[a-zA-Z0-9]+([_\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,10}(:[0-9]{1,10})?(\/.*)?$)' name='project[homepage]' placeholder='主页(eg: https://gitee.com)' type='text' value=''>
</div>
<div class='zero-percent'>
<button class='ui orange button btn-save'>
保存更改
</button>
<button class='ui button btn-cancel-edit'>
取消
</button>
</div>
</div>
<script>
  $(function () {
    new ProjectInfoEditor({
      el: '.git-project-desc-wrapper',
      homepage: "",
      description: "ModelArts-Lab是基于华为云ModelArts平台的示例代码库(内容与github一致)",
      url: "/ModelArts/ModelArts-Lab/update_description",
      modalHelper: Gitee.modalHelper
    })
  })
  
  if (false) {
    gon.project_new_blob_path = "/ModelArts/ModelArts-Lab/new/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py"
    bindShowModal({
      el: $('.no-license .project-license__create'),
      complete: function(data, modal) {
        if (!data.haveNoChoice && !data.data) {
          Flash.show('请选择一项开源许可证')
        } else {
          location.href = gon.project_new_blob_path + '?license=' + data.data
        }
      },
      skip: function () {
        location.href = gon.project_new_blob_path + '?license'
      }
    })
  }
  
  $('i.help.circle.icon').popup({
    popup: '.no-license .ui.popup',
    position: 'right center'
  })
  
  $('#remove-no-license-message').on('click', function(){
    $.cookie("skip_repo_no_license_message_8271874", 'hide', { expires: 365 })
    $('#user-no-license-message').hide()
    return
  })
</script>
</div>

</div>
<div class='git-project-summary' id='git-project-summary'>
<div class='summary-viewer'>
<div class='viewer-wrapper'>
<ul>
<li>
<a href="/ModelArts/ModelArts-Lab/commits/master"><i class='iconfont icon-commit'></i>
<b>2305</b>
次提交
</a></li>
<li>
<a href="/ModelArts/ModelArts-Lab/branches"><i class='iconfont icon-branches'></i>
<b>12</b>
个分支
</a></li>
<li>
<a href="/ModelArts/ModelArts-Lab/tags"><i class='iconfont icon-tag'></i>
<b>0</b>
个标签
</a></li>
<li>
<a href="/ModelArts/ModelArts-Lab/releases"><i class='iconfont icon-release'></i>
<b>0</b>
个发行版
</a></li>
<li>
<a href="/ModelArts/ModelArts-Lab/contributors?ref=master"><i class='iconfont icon-collaborators'></i>
<b class='contributor-count' data-url='/ModelArts/ModelArts-Lab/contributors_count?ref=master'></b>
<span class='contributor-text'>
正在获取贡献者
</span>
</a></li>
</ul>
<ul>
<li>
<span class='ui circular label mini' style='background-color: #DA5B0B'></span>
<b>Jupyter Notebook</b>
<b class='percent'>98.8%</b>
</li>
<li>
<span class='ui circular label mini' style='background-color: #3572A5'></span>
<b>Python</b>
<b class='percent'>1.0%</b>
</li>
<li>
<span class='ui circular label mini' style='background-color: #e16737'></span>
<b>MATLAB</b>
<b class='percent'>0.1%</b>
</li>
<li>
<span class='ui circular label mini' style='background-color: #EDEDED'></span>
<b>Other</b>
<b class='percent'>0.1%</b>
</li>
</ul>
</div>
</div>
<div class='summary-languages' title='点击查看语言占比'>
<a class='language-color' style='width: 98.8%; background-color: #DA5B0B;'></a>
<a class='language-color' style='width: 1.0%; background-color: #3572A5;'></a>
<a class='language-color' style='width: 0.1%; background-color: #e16737;'></a>
<a class='language-color' style='width: 0.1%; background-color: #EDEDED;'></a>
</div>

</div>
<div class='git-project-bread' id='git-project-bread'>
<div class='git-project-right-actions float-right'>
<div class='d-inline-block' id='git-project-tree-actions'>
<script>
  $('.disabled-upload-readonly').popup({
    content: "只读目录不允许上传文件",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-create-folder').popup({
    content: "只读目录不允许创建目录",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-create-file').popup({
    content: "只读目录不允许创建文件",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-upload-readonly').click(() => {
    return false
  })
  $('.disabled-create-folder').click(() => {
    return false
  })
  $('.disabled-create-file').click(() => {
    return false
  })
</script>
<style>
  .disabled-upload-readonly, .disabled-create-file, .disabled-create-folder {
    background-color: #dcddde !important;
    color: rgba(0, 0, 0, 0.4) !important;
    opacity: 0.3 !important;
    background-image: none !important;
    -webkit-box-shadow: none !important;
            box-shadow: none !important; }
</style>

</div>
<div class='ui orange button' id='btn-dl-or-clone'>
克隆/下载
<i class='dropdown icon'></i>
<div class='git-project-download-panel for-project ui bottom right popup'>
<div class='ui small secondary pointing menu'>
<a class='item active' data-text='' data-type='http' data-url='https://gitee.com/ModelArts/ModelArts-Lab.git'>HTTPS</a>
<a class='item' data-text='' data-type='ssh' data-url='git@gitee.com:ModelArts/ModelArts-Lab.git'>SSH</a>
<a class='item' data-text="该仓库未启用SVN访问，请仓库管理员前往【&lt;a target='_blank' href=/ModelArts/ModelArts-Lab/settings&gt;仓库设置&lt;/a&gt;】开启。" data-type='svn' data-url=''>SVN</a>
<a class='item' data-text="该仓库未启用SVN访问，请仓库管理员前往【&lt;a target='_blank' href=/ModelArts/ModelArts-Lab/settings&gt;仓库设置&lt;/a&gt;】开启。" data-type='svn_ssh' data-url=''>SVN+SSH</a>
</div>
<div class='ui fluid right labeled small input download-url-panel'>
<input id="project_clone_url" name="project_clone_url" onclick="focus();select()" readonly="readonly" type="text" value="https://gitee.com/ModelArts/ModelArts-Lab.git" />
<div class='ui basic label'>
<div class='ui small basic orange button' data-clipboard-target='#project_clone_url' id='btn-copy-clone-url'>
复制
</div>
</div>
</div>
<div class='ui fluid right labeled warning-text forbid-warning-text'>

</div>
<hr>
<a class="ui fluid download link button" href="javascript:void(0);"><i class='icon download'></i>
下载ZIP
</a><div class='download_repository_zip form modal tiny ui' id='unlanding-complaint-modal'>
<i class='iconfont icon-close close'></i>
<div class='header'>
登录提示
</div>
<div class='container actions'>
<div class='content'>
该操作需登录码云帐号，请先登录后再操作。
</div>
<div class='ui orange icon large button ok'>
立即登录
</div>
<div class='ui button blank cancel'>
没有帐号，去注册
</div>
</div>
</div>
<script>
  var $elm = $('.download');
  
  $elm.on('click', function() {
    var modals = $("#unlanding-complaint-modal.download_repository_zip");
    if (modals.length > 1) {
      modals.eq(0).modal('show');
    } else {
      modals.modal('show');
    }
  })
  $("#unlanding-complaint-modal.download_repository_zip").modal({
    onDeny: function() {
      window.location.href = "/signup?from=download_repository_zip";
    },
    onApprove: function() {
      window.location.href = "/login?from=download_repository_zip";
    }
  })
</script>

<hr>
<div class='ent-poster mt-1 toschina-content__hidden'>
<h2>企业级软件开发协作工具</h2>
<p>代码托管 项目管理 文档协作 完备安全策略</p>
<a class="ui button orange" href="/enterprises?utm_source=g_download" target="_blank">了解更多</a>
</div>
</div>
<script>
  (function() {
    var $btnCopy, $input, $item, $panel, clipboard, dataUrl, remoteWay;
  
    $input = $('#project_clone_url');
  
    remoteWay = '';
  
    clipboard = new Clipboard('#btn-copy-clone-url');
  
    $panel = $('.git-project-download-panel');
  
    $btnCopy = $('#btn-copy-clone-url');
  
    $panel.find('.menu > .item').on('click', function() {
      var $item, dataUrl;
      $item = $(this).addClass('active');
      $item.siblings().removeClass('active');
      dataUrl = $item.attr('data-url');
      if (dataUrl) {
        $panel.find('.download-url-panel').show();
        $input.val(dataUrl);
        $panel.find('.forbid-warning-text').html('');
      } else {
        $panel.find('.download-url-panel').hide();
        $panel.find('.forbid-warning-text').html($item.attr('data-text') || '');
      }
      return $.cookie('remote_way', $item.attr('data-type'), {
        expires: 365,
        path: '/'
      });
    });
  
    $('body').on('click', '#btn-dl-or-clone', function(e) {
      e.stopImmediatePropagation();
      if ($(e.target)[0] === $panel[0] || $(e.target).closest($panel).length) {
        return;
      }
      return $panel.transition('fade up');
    });
  
    $('body').on('click', function() {
      if ($panel.transition('is visible')) {
        return $panel.transition('fade up');
      }
    });
  
    $item = $panel.find('.ui.menu .item').eq(0);
  
    $item.addClass('active').siblings().removeClass('active');
  
    dataUrl = $item.attr('data-url');
  
    if (dataUrl) {
      $panel.find('.download-url-panel').show();
      $input.val(dataUrl);
      $panel.find('.forbid-warning-text').html('');
    } else {
      $panel.find('.download-url-panel').hide();
      $panel.find('.forbid-warning-text').html($item.attr('data-text') || '');
    }
  
    clipboard.on('success', function() {
      $btnCopy.popup({
        content: '已复制',
        position: 'right center',
        onHidden: function() {
          return $btnCopy.popup('destroy');
        }
      });
      return $btnCopy.popup('show');
    });
  
    clipboard.on('error', function() {
      $btnCopy.popup({
        content: '复制失败，请手动复制',
        position: 'right center',
        onHidden: function() {
          return $btnCopy.popup('destroy');
        }
      });
      return $btnCopy.popup('show');
    });
  
  }).call(this);
</script>

</div>
</div>
<div class='ui horizontal list'>
<div class='item git-project-branch-item'>
<input id="path" name="path" type="hidden" value="official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py" />
<div class='ui top left pointing dropdown gradient button dropdown-has-tabs' id='git-project-branch'>
<input id="ref" name="ref" type="hidden" value="master" />
<div class='default text'>
master
</div>
<i class='dropdown icon'></i>
<div class='menu'>
<div class='ui left icon search input'>
<i class='iconfont icon-search'></i>
<input class='search-branch' placeholder='搜索分支' type='text'>
</div>
<div class='tab-menu'>
<div class='tab-menu-action' data-tab='branches'>
<a class="ui link button" href="/ModelArts/ModelArts-Lab/branches">管理</a>
</div>
<div class='tab-menu-action' data-tab='tags'>
<a class="ui link button" href="/ModelArts/ModelArts-Lab/tags">管理</a>
</div>
<div class='tab-menu-item' data-placeholder='搜索分支' data-tab='branches'>
分支 (12)
</div>
</div>
<div class='tab scrolling menu' data-tab='branches'>
<div class="item" data-value="master"><span>master</span></div>
<div class="item" data-value="revert-1522-revert-1505-patch-22"><span>revert-1522-revert-1505-patch-22</span></div>
<div class="item" data-value="revert-1505-patch-22"><span>revert-1505-patch-22</span></div>
<div class="item" data-value="revert-1374-patch-14"><span>revert-1374-patch-14</span></div>
<div class="item" data-value="revert-964-patch-2"><span>revert-964-patch-2</span></div>
<div class="item" data-value="revert-925-patch-1"><span>revert-925-patch-1</span></div>
<div class="item" data-value="revert-807-patch-1"><span>revert-807-patch-1</span></div>
<div class="item" data-value="revert-752-patch-1"><span>revert-752-patch-1</span></div>
<div class="item" data-value="revert-531-patch-1"><span>revert-531-patch-1</span></div>
<div class="item" data-value="legist-patch-1"><span>legist-patch-1</span></div>
<div class="item" data-value="images"><span>images</span></div>
<div class="item" data-value="face&amp;number"><span>face&amp;number</span></div>
</div>
</div>
</div>
<style>
  .iconfont.icon-shieldlock {
    color: #8c92a4;
  }
</style>

<script>
  $(function () {
    Gitee.initTabsInDropdown($('#git-project-branch').dropdown({
      fullTextSearch: true,
      selectOnKeydown: true,
      action: function (text,value,el) {
        var oItemOrInitObject = el[0] || el
        var isNotSelect = oItemOrInitObject.dataset.tab && oItemOrInitObject.dataset.tab === 'branches'
        if(isNotSelect){
          console.warn("You didn't choose a branch")
          return
        } 
        var path = $('#path').val();
        var href = ['/ModelArts/ModelArts-Lab/tree', encodeURIComponent(value), path].join('/');
        window.location.href = href;
        return true
      },
      onNoResults: function (searchTerm) {
        //未找到结果
        return true
      },
    }));
    $('.protected-branch-popup').popup()
  })
</script>

</div>
<div class='item' id='git-project-root-actions'>
<div class='repo-index repo-none-index' style='margin-left:0px;'>
<div class='ui horizontal list repo-action-list'>
<div class='item'>
<div class='ui pointing right top dropdown gradient button' id='git-project-file'>
<div class='text'>文件</div>
<i class='dropdown icon'></i>
<div class='menu'>
<a class="item repo-action" href="/ModelArts/ModelArts-Lab/new/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py" id="new_file_bread" title="新建文件">新建文件
</a><div class='disabled item'>上传文件</div>
<a class='item repo-action' id='search-files'>
搜索文件
</a>
</div>
</div>
</div>
<div class='item toschina-content__hidden'>
<a class="ui gradient button webide" href="/-/ide/project/ModelArts/ModelArts-Lab/edit/master" target="_blank">Web IDE</a>
</div>
<div class='item toschina-content__hidden'>
<a class="ui gradient button repo-action" href="/ModelArts/ModelArts-Lab/widget"><i class='iconfont icon-widget icon-orange'></i>
挂件
</a></div>
</div>
<script>
  $('#git-project-file').dropdown({ action: 'hide' });
</script>
</div>

</div>
<div class='item breadcrumb_path path-breadcrumb-contrainer' id='git-project-breadcrumb'>
<div class='ui breadcrumb path project-path-breadcrumb' id='path-breadcrumb'>
<a class="section repo-name" data-direction="back" href="/ModelArts/ModelArts-Lab/tree/master" style="font-weight: bold">ModelArts-Lab
</a><div class='divider'>
/
</div>
<strong>
<a class="section" data-direction="back" href="/ModelArts/ModelArts-Lab/tree/master/official_examples"><span class='cblue'>
official_examples
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
<a class="section" data-direction="back" href="/ModelArts/ModelArts-Lab/tree/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application"><span class='cblue'>
Using_MoXing_to_Create_a_MNIST_Datase...
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
<a class="section" data-direction="back" href="/ModelArts/ModelArts-Lab/tree/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes"><span class='cblue'>
codes
</span>
</a></strong>
<div class='divider'>
/
</div>
<strong>
customize_service.py
</strong>
</div>


</div>
</div>
</div>

<style>
  .ui.dropdown .menu > .header {
    text-transform: none; }
</style>
<script>
  $(document).ready(function () {
    var $gitProjectSummary = $('#git-project-summary');
    var $gitProjectLanguages = $gitProjectSummary.find('.summary-languages');
    var $statsSwitcherWrapper = $gitProjectSummary.find('.viewer-wrapper');
    var $contributorCount = $gitProjectSummary.find('.contributor-count');
    var $contributorText = $gitProjectSummary.find('.contributor-text');
    var contributorsCountUrl = $contributorCount.data('url');
  
    $gitProjectLanguages.on('click', function() {
      $statsSwitcherWrapper.toggleClass('js-lang');
    });
  
    $.ajax({
      url: contributorsCountUrl,
      method: 'GET',
      success: function(data) {
        if (data.status === 1) {
          $contributorCount.text(data.contributors_count);
          $contributorText.text('位贡献者')
        } else {
          $contributorText.text('获取失败')
        }
      }
    });
    var $tip = $('#apk-download-tip');
    if (!$tip.length) {
      return;
    }
    $tip.find('.btn-close').on('click', function () {
      $tip.slideUp();
    });
  });
  (function(){
    function pathAutoRender() {
      var $parent = $('#git-project-bread'),
          $child = $('#git-project-bread').children('.ui.horizontal.list'),
          mainWidth = 0;
      $child.each(function (i,item) {
        mainWidth += $(item).width()
        });
      $('.breadcrumb.path.fork-path').remove();
      if (mainWidth > 995) {
        $('#path-breadcrumb').hide();
        $parent.append('<div class="ui breadcrumb path fork-path">' + $('#path-breadcrumb').html() + '<div/>')
      } else {
        $('#path-breadcrumb').show();
      }
    }
    window.pathAutoRender = pathAutoRender;
    pathAutoRender();
  })();
</script>

<div class='row column tree-holder' id='tree-holder'>

<div class='tree-content-holder' id='tree-content-holder'>
<div class='file_holder'>
<div class='file_title'>
<div class='blob-header-title'>
<div class='blob-description'>
<i class="iconfont icon-file"></i>
<span class='file_name' title='customize_service.py'>
customize_service.py
</span>
<small>937 Bytes</small>
</div>
<div class='options'><div class='ui mini buttons basic'>
<textarea id="blob_raw" name="blob_raw" style="display:none;">
from PIL import Image&#x000A;import numpy as np&#x000A;from model_service.tfserving_model_service import TfServingBaseService&#x000A;&#x000A;&#x000A;class mnist_service(TfServingBaseService):&#x000A;  def _preprocess(self, data):&#x000A;    preprocessed_data = {}&#x000A;&#x000A;    for k, v in data.items():&#x000A;      for file_name, file_content in v.items():&#x000A;        image1 = Image.open(file_content)&#x000A;        image1 = np.array(image1, dtype=np.float32)&#x000A;        image1.resize((1, 784))&#x000A;        preprocessed_data[k] = image1&#x000A;&#x000A;    return preprocessed_data&#x000A;&#x000A;  def _postprocess(self, data):&#x000A;&#x000A;    outputs = {}&#x000A;    logits = data[&#39;logits&#39;][0]&#x000A;    label = logits.index(max(logits))&#x000A;    logits = [&#39;%.3f&#39; % logit for logit in logits]&#x000A;    outputs[&#39;predicted_label&#39;] = str(label)&#x000A;    label_list = [str(label) for label in list(range(10))]&#x000A;    scores = dict(zip(label_list, logits))&#x000A;    scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:5]&#x000A;    outputs[&#39;scores&#39;] = scores&#x000A;  &#x000A;    return outputs&#x000A;</textarea>
<a class="ui button" href="#" id="copy-text" style="border-left: none;">一键复制</a>
<a class="ui button edit-blob" href="/ModelArts/ModelArts-Lab/edit/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py" title="只有登陆后才可以编辑">编辑</a>
<a class="ui button web-ide" href="/-/ide/project/ModelArts/ModelArts-Lab/edit/master/-/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py" target="_blank">Web IDE</a>
<a class="ui button edit-raw" href="/ModelArts/ModelArts-Lab/raw/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py" target="_blank">原始数据</a>
<a class="ui button edit-blame" href="/ModelArts/ModelArts-Lab/blame/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py">按行查看</a>
<a class="ui button edit-history" href="/ModelArts/ModelArts-Lab/commits/master/official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py">历史</a>
</div>
<script>
  "use strict";
  try {
    if((gon.wait_fork!=undefined && gon.wait_fork==true) || (gon.wait_fetch!=undefined && gon.wait_fetch==true)){
      $('.edit-blob').popup({content:"当前仓库正在后台处理中,暂时无法编辑", on: 'hover', delay: { show: 200, hide: 200 }});
      $('.edit-blob').click(function(e){
        e.preventDefault();
      })
    }
  
    var setUrl = function() {
      var params = window.location.search
      if (params==undefined || $.trim(params).length==0) return;
      $('span.options').children('.basic').find('a').each(function(index,ele){
        var origin_href = $(ele).attr('href');
        if (origin_href!="#" && origin_href.indexOf('?') == -1){
          $(ele).attr('href',origin_href+params);
        }
      });
    }
  
    setUrl();
  
    var clipboard = null,
        $btncopy  = $("#copy-text");
  
    clipboard = new Clipboard("#copy-text", {
      text: function(trigger) {
        return $("#blob_raw").val();
      }
    })
  
    clipboard.on('success', function(e) {
      $btncopy.popup('hide');
      $btncopy.popup('destroy');
      $btncopy.popup({content: '已复制', position: 'bottom center'});
      $btncopy.popup('show');
    })
  
    clipboard.on('error', function(e) {
      var giteeModal = new GiteeModalHelper({okText: '确定'});
      giteeModal.alert("一键复制", '复制失败，请手动复制');
    })
  
    $(function() {
      $btncopy.popup({
        content: '点击复制',
        position: 'bottom center'
      })
    })
  
  } catch (error) {
    console.log('blob/action error:' + error);
  }
  
  $('.disabled-edit-readonly').popup({
    content: "只读文件不可编辑",
    className: {
      popup: 'ui popup',
    },
    position: 'bottom center',
  })
  $('.disabled-edit-readonly').click(() => {
    return false
  })
</script>
<style>
  .disabled-edit-readonly {
    background-color: #dcddde !important;
    color: rgba(0, 0, 0, 0.4) !important;
    opacity: 0.3 !important;
    background-image: none !important;
    -webkit-box-shadow: none !important;
            box-shadow: none !important; }
</style>
</div>
</div>
<div class='contributor-description'><span class='recent-commit' style='margin-top: 0.7rem'>
<a class="commit-author-link " href="mailto:33612283+CalvinXKY@users.noreply.github.com">CalvinXKY</a>
<span>提交于</span>
<span class='timeago commit-date' title='2019-09-05 19:10:57 +0800'>
2019-09-05 19:10
</span>
.
<a href="/ModelArts/ModelArts-Lab/commit/54cfbe9c02bd899f58b32ff34c9f7335bd085b18">Update customize_service.py (#920)</a>
</span>
</div>
</div>
<div class='clearfix'></div>
<div class='file_content code'>
<div class='lines white'>
<div class='line-numbers'><a href='#L1' id='L1'>1</a><a href='#L2' id='L2'>2</a><a href='#L3' id='L3'>3</a><a href='#L4' id='L4'>4</a><a href='#L5' id='L5'>5</a><a href='#L6' id='L6'>6</a><a href='#L7' id='L7'>7</a><a href='#L8' id='L8'>8</a><a href='#L9' id='L9'>9</a><a href='#L10' id='L10'>10</a><a href='#L11' id='L11'>11</a><a href='#L12' id='L12'>12</a><a href='#L13' id='L13'>13</a><a href='#L14' id='L14'>14</a><a href='#L15' id='L15'>15</a><a href='#L16' id='L16'>16</a><a href='#L17' id='L17'>17</a><a href='#L18' id='L18'>18</a><a href='#L19' id='L19'>19</a><a href='#L20' id='L20'>20</a><a href='#L21' id='L21'>21</a><a href='#L22' id='L22'>22</a><a href='#L23' id='L23'>23</a><a href='#L24' id='L24'>24</a><a href='#L25' id='L25'>25</a><a href='#L26' id='L26'>26</a><a href='#L27' id='L27'>27</a><a href='#L28' id='L28'>28</a><a href='#L29' id='L29'>29</a><a href='#L30' id='L30'>30</a><a href='#L31' id='L31'>31</a></div><div class="highlight"><pre class=""><div class='line' id='LC1'><span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>&#x000A;</div><div class='line' id='LC2'><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="n">np</span>&#x000A;</div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">model_service.tfserving_model_service</span> <span class="kn">import</span> <span class="n">TfServingBaseService</span>&#x000A;</div><div class='line' id='LC4'>&#x000A;</div><div class='line' id='LC5'>&#x000A;</div><div class='line' id='LC6'><span class="k">class</span> <span class="nc">mnist_service</span><span class="p">(</span><span class="n">TfServingBaseService</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC7'>  <span class="k">def</span> <span class="nf">_preprocess</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC8'>    <span class="n">preprocessed_data</span> <span class="o">=</span> <span class="p">{}</span>&#x000A;</div><div class='line' id='LC9'>&#x000A;</div><div class='line' id='LC10'>    <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">data</span><span class="p">.</span><span class="n">items</span><span class="p">():</span>&#x000A;</div><div class='line' id='LC11'>      <span class="k">for</span> <span class="n">file_name</span><span class="p">,</span> <span class="n">file_content</span> <span class="ow">in</span> <span class="n">v</span><span class="p">.</span><span class="n">items</span><span class="p">():</span>&#x000A;</div><div class='line' id='LC12'>        <span class="n">image1</span> <span class="o">=</span> <span class="n">Image</span><span class="p">.</span><span class="nb">open</span><span class="p">(</span><span class="n">file_content</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC13'>        <span class="n">image1</span> <span class="o">=</span> <span class="n">np</span><span class="p">.</span><span class="n">array</span><span class="p">(</span><span class="n">image1</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="n">np</span><span class="p">.</span><span class="n">float32</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC14'>        <span class="n">image1</span><span class="p">.</span><span class="n">resize</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span> <span class="mi">784</span><span class="p">))</span>&#x000A;</div><div class='line' id='LC15'>        <span class="n">preprocessed_data</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="n">image1</span>&#x000A;</div><div class='line' id='LC16'>&#x000A;</div><div class='line' id='LC17'>    <span class="k">return</span> <span class="n">preprocessed_data</span>&#x000A;</div><div class='line' id='LC18'>&#x000A;</div><div class='line' id='LC19'>  <span class="k">def</span> <span class="nf">_postprocess</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>&#x000A;</div><div class='line' id='LC20'>&#x000A;</div><div class='line' id='LC21'>    <span class="n">outputs</span> <span class="o">=</span> <span class="p">{}</span>&#x000A;</div><div class='line' id='LC22'>    <span class="n">logits</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s">'logits'</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>&#x000A;</div><div class='line' id='LC23'>    <span class="n">label</span> <span class="o">=</span> <span class="n">logits</span><span class="p">.</span><span class="n">index</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">logits</span><span class="p">))</span>&#x000A;</div><div class='line' id='LC24'>    <span class="n">logits</span> <span class="o">=</span> <span class="p">[</span><span class="s">'%.3f'</span> <span class="o">%</span> <span class="n">logit</span> <span class="k">for</span> <span class="n">logit</span> <span class="ow">in</span> <span class="n">logits</span><span class="p">]</span>&#x000A;</div><div class='line' id='LC25'>    <span class="n">outputs</span><span class="p">[</span><span class="s">'predicted_label'</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>&#x000A;</div><div class='line' id='LC26'>    <span class="n">label_list</span> <span class="o">=</span> <span class="p">[</span><span class="nb">str</span><span class="p">(</span><span class="n">label</span><span class="p">)</span> <span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))]</span>&#x000A;</div><div class='line' id='LC27'>    <span class="n">scores</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">label_list</span><span class="p">,</span> <span class="n">logits</span><span class="p">))</span>&#x000A;</div><div class='line' id='LC28'>    <span class="n">scores</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">scores</span><span class="p">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">item</span><span class="p">:</span> <span class="n">item</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">)[:</span><span class="mi">5</span><span class="p">]</span>&#x000A;</div><div class='line' id='LC29'>    <span class="n">outputs</span><span class="p">[</span><span class="s">'scores'</span><span class="p">]</span> <span class="o">=</span> <span class="n">scores</span>&#x000A;</div><div class='line' id='LC30'>  &#x000A;</div><div class='line' id='LC31'>    <span class="k">return</span> <span class="n">outputs</span>&#x000A;</div></pre></div></div>
</div>
<script>
  toMathMlCode('','markdown-body');
</script>

</div>
</div>
<div class='tree_progress'></div>
<div class='ui small modal' id='modal-linejump'>
<div class='ui custom form content'>
<div class='field'>
<div class='ui right action input'>
<input placeholder='跳转至某一行...' type='number'>
<div class='ui orange button'>
跳转
</div>
</div>
</div>
</div>
</div>

<div class='row column inner-comment' id='blob-comment'>
<input id="comment_path" name="comment_path" type="hidden" value="official_examples/Using_MoXing_to_Create_a_MNIST_Dataset_Recognition_Application/codes/customize_service.py" />
<div class='tree-comments'>
<h3 id='tree_comm_title'>
评论
(
<span class='comments-count'>
0
</span>
)
</h3>
<div class='ui threaded comments middle aligned' id='notes-list'></div>
<input id="ajax_add_note_id" name="ajax_add_note_id" type="hidden" />
<div class='text-center'>
<div class='tip-loading' style='display: none'>
<div class='ui active mini inline loader'></div>
正在加载...
</div>
</div>
</div>
<script>
  "use strict";
  $(function(){
    var page = 1
    var commentsCount = 0
    var $container = $('.tree-comments')
    var $comments = $container.find('.ui.comments')
    var $tipLoading = $container.find('.tip-loading')
    var $btnLoad = $container.find('.btn-load-more')
    var noteAnchor = new Gitee.NoteAnchor({ defaultAnchor: '#tree_comm_title' })
  
    if (commentsCount < 1) {
      return;
    }
  
    var path;
    if ($('#comment_path').val() === '') {
      path = '/';
    } else {
      path = $('#comment_path').val();
    }
  
    function loadComments () {
      $btnLoad.hide();
      $tipLoading.show();
      $.ajax({
        url: '/ModelArts/ModelArts-Lab/comment_list',
        data: {
          page: page,
          path: path
        },
        success: function(data) {
          var err;
          try {
            $tipLoading.hide();
            $btnLoad.show();
            if (data.status !== 0) {
              $btnLoad.text('无更多评论')
              return $btnLoad.prop('disabled', true).addClass('disabled');
            } else {
              TreeComment.CommentListHandler(data);
              page += 1;
              if (data.comments_count < 10) {
                $('#ajax_add_note_id').val('');
                $btnLoad.text('无更多评论')
                $btnLoad.prop('disabled', true).addClass('disabled');
              }
              // osctree can not load script
              $comments.find('.timeago').timeago();
              $comments.find('.commenter-role-label').popup();
              noteAnchor.locate();
              toMathMlCode('', 'comments');
              return $('.markdown-body pre code').each(function(i, block) {
                return hljs.highlightBlock(block);
              });
            }
          } catch (error) {
            err = error;
            return console.log('loadComments error:' + err);
          }
        }
      });
    };
  
  
    function checkLoad () {
      var listTop, top;
      top = $(window).scrollTop();
      listTop = $container.offset().top;
      if (listTop >= top && listTop < top + $(window).height()) {
        $(window).off('scroll', checkLoad);
        return loadComments();
      }
    };
  
    $btnLoad.on('click', loadComments);
    loadComments()
  })
</script>

</div>
<div class='inner-comment-box' id='comment-box'>
<p>
你可以在<a href="/login">登录</a>后，发表评论
</p>

</div>

<div class='complaint'>
<div class='ui modal small form' id='landing-comments-complaint-modal'>
<i class='iconfont icon-close close'></i>
<div class='header'>
举报
</div>
<div class='content'>
<div class='appeal-success-tip hide'>
<i class='iconfont icon-ic_msg_success'></i>
<div class='appeal-success-text'>
举报成功
</div>
<span>
我们将于2个工作日内通过站内信反馈结果给你！
</span>
</div>
<div class='appeal-tip'>
请认真填写举报原因，尽可能描述详细。
</div>
<div class='ui form appeal-form'>
<div class='inline field'>
<label class='left-part appeal-type-wrap'>
举报类型
</label>
<div class='ui dropdown selection' id='appeal-comments-types'>
<div class='text default'>
请选择举报类型
</div>
<i class='dropdown icon'></i>
<div class='menu'></div>
</div>
</div>
<div class='inline field'>
<label class='left-part'>
举报原因
</label>
<textarea class='appeal-reason' id='appeal-comment-reason' name='msg' placeholder='请说明举报原因' rows='3'></textarea>
</div>
<div class='ui message callback-msg hide'></div>
<div class='ui small error text message exceeded-size-tip'></div>
</div>
</div>
<div class='actions'>
<div class='ui button blank cancel'>
取消
</div>
<div class='ui orange icon button disabled ok' id='complaint-comment-confirm'>
发送
</div>
</div>
</div>
<script>
  var $complaintCommentsModal = $('#landing-comments-complaint-modal'),
      $complainCommentType = $complaintCommentsModal.find('#appeal-comments-types'),
      $complaintModalTip = $complaintCommentsModal.find('.callback-msg'),
      $complaintCommentsContent = $complaintCommentsModal.find('.appeal-reason'),
      $complaintCommentBtn = $complaintCommentsModal.find('#complaint-comment-confirm'),
      complaintSending = false,
      initedCommentsType = false;
  
  function initCommentsTypeList() {
    if (!initedCommentsType) {
      $.ajax({
        url: "/appeals/fetch_types",
        method: 'get',
        data: {'type': 'comment'},
        success: function (data) {
          var result = '';
          for (var i = 0; i < data.length; i++) {
            result = result + "<div class='item' data-value='" + data[i].id + "'>" + data[i].name + "</div>";
          }
          $complainCommentType.find('.menu').html(result);
        }
      });
      $complainCommentType.dropdown({showOnFocus: false});
      initedCommentsType = true;
    }
  }
  $complainCommentType.on('click', function() {
    $complaintCommentsModal.modal({
      autofocus: false,
      onApprove: function() {
        return false;
      },
      onHidden: function() {
        restoreCommonentDefault();
      }
    }).modal('show');
  });
  
  $complaintCommentsContent.on('change keyup', function(e) {
    var content = $(this).val();
    if ($.trim(content).length > 0 && $complainCommentType.dropdown('get value').length > 0 ) {
      $complaintCommentBtn.removeClass('disabled');
      return;
    }
    $complaintCommentBtn.addClass('disabled');
  });
  
  
  $complainCommentType.dropdown({
    showOnFocus: false,
    onChange: function(value, text, $selectedItem) {
      if (value.length > 0 && $.trim($complaintCommentsContent.val()).length > 0) {
        $complaintCommentBtn.removeClass('disabled');
        return
      }
      $complaintCommentBtn.addClass('disabled');
    }
  });
  
  function restoreCommonentDefault() {
    $complainCommentType.dropdown('restore defaults');
    $complaintCommentsContent.val('');
    $('.exceeded-size-tip').text('').hide();
    $complaintModalTip.text('').hide();
    setTimeout(function() {
      setCommentSendTip(false);
    }, 1500);
  }
  
  $complaintCommentBtn.on('click',function(e){
    var reason = $complaintCommentsContent.val();
    var appealableId = $('#landing-comments-complaint-modal').attr('data-id');
    if (complaintSending) {
      return;
    }
    var appealType = $complainCommentType.dropdown('get value');
    var formData = new FormData();
    formData.append('appeal_type_id', appealType);
    formData.append('reason', reason);
    formData.append('appeal_type','Note');
    formData.append('target_id',appealableId);
    $.ajax({
      type: 'POST',
      url: "/appeals",
      cache: false,
      contentType: false,
      processData: false,
      data: formData,
      beforeSend: function() {
        setCommentSendStatus(true);
      },
      success: function(res) {
        if (res.status == 200) {
          setCommentSendTip(true);
          setTimeout(function() {
            $complaintCommentsModal.modal('hide');
            restoreCommonentDefault();
          }, 3000);
        }
        setCommentSendStatus(false);
      },
      error: function(err) {
        showCommonTips(err.responseJSON.message, 'error');
        setCommentSendStatus(false);
      }
    })
  });
  
  function showCommonTips(text, type) {
    $complaintModalTip.text(text).show();
    if (type == 'error') {
      $complaintModalTip.removeClass('success').addClass('error');
    } else {
      $complaintModalTip.removeClass('error').addClass('success');
    }
  }
  
  function setCommentSendStatus(value) {
    complaintSending = value;
    if (complaintSending) {
      $complaintCommentBtn.addClass('loading');
      $complaintCommentsContent.attr('readonly', true);
      $complainCommentType.attr('readonly', true);
    } else {
      $complaintCommentBtn.removeClass('loading');
      $complaintCommentsContent.attr('readonly', false);
      $complainCommentType.attr('readonly', false);
    }
  }
  
  function setCommentSendTip(value) {
    if (value) {
      $('.appeal-success-tip').removeClass('hide');
      $('.appeal-tip').addClass('hide');
      $('.appeal-form').addClass('hide');
      $('#landing-comments-complaint-modal .actions').addClass('hide');
    } else {
      $('.appeal-success-tip').addClass('hide');
      $('.appeal-tip').removeClass('hide');
      $('.appeal-form').removeClass('hide');
      $('#landing-comments-complaint-modal .actions').removeClass('hide');
    }
  }
</script>

</div>
<script>
  "use strict";
  $('.js-check-star').checkbox('set unchecked')
</script>

</div>
</div>
</div>
<script>
  (function() {
    $(function() {
      Tree.init();
      return TreeCommentActions.init();
    });
  
  }).call(this);
</script>

</div>
<script>
  (function() {
    var donateModal;
  
    Gitee.modalHelper = new GiteeModalHelper({
      alertText: '提示',
      okText: '确定'
    });
  
    donateModal = new ProjectDonateModal({
      el: '#project-donate-modal',
      alipayUrl: '/ModelArts/ModelArts-Lab/alipay',
      wepayUrl: '/ModelArts/ModelArts-Lab/wepay',
      nameIsBlank: '名称不能为空',
      nameTooLong: '名称过长（最多为 36 个字符）',
      modalHelper: Gitee.modalHelper
    });
  
    if (null === 'true') {
      donateModal.show();
    }
  
    $('#project-donate').on('click', function() {
      return donateModal.show();
    });
  
  }).call(this);
</script>
<script>
  Tree.initHighlightTheme('white')
</script>


</div>
<div class='gitee-project-extension'>
<div class='extension lang'>Python</div>
<div class='extension public'>1</div>
<div class='extension https'>https://gitee.com/ModelArts/ModelArts-Lab.git</div>
<div class='extension ssh'>git@gitee.com:ModelArts/ModelArts-Lab.git</div>
<div class='extension namespace'>ModelArts</div>
<div class='extension repo'>ModelArts-Lab</div>
<div class='extension name'>ModelArts-Lab</div>
<div class='extension branch'>master</div>
</div>

<script>
  $(function() {
    GitLab.GfmAutoComplete.dataSource = "/ModelArts/ModelArts-Lab/autocomplete_sources"
    GitLab.GfmAutoComplete.Emoji.assetBase = '/assets/emoji'
    GitLab.GfmAutoComplete.setup();
  });
</script>

<footer id='git-footer-main'>
<div class='ui container'>
<div class='logo-row'>
<img class='logo-img' src='/static/images/logo-black.svg?t=158106666'>
</div>
<div class='name-important'>
深圳市奥思网络科技有限公司版权所有
</div>
<div class='ui two column grid d-flex-center'>
<div class='nine wide column git-footer-left'>
<div class='ui four column grid' id='footer-left'>
<div class='column'>
<div class='ui link list'>
<div class='item'>
<a class="item" href="/about_us">关于我们</a>
</div>
<div class='item'>
<a class="item" href="/terms">使用条款</a>
</div>
<div class='item'>
<a class="item" href="/oschina/git-osc/issues">意见建议</a>
</div>
<div class='item'>
<a class="item" href="/links.html">合作伙伴</a>
</div>
</div>
</div>
<div class='column'>
<div class='ui link list'>
<div class='item'>
<a class="item" href="/all-about-git">Git 大全</a>
</div>
<div class='item'>
<a class="item" href="https://oschina.gitee.io/learn-git-branching/">Git 命令学习</a>
</div>
<div class='item'>
<a class="item" href="https://copycat.gitee.com/">代码克隆检测</a>
</div>
<div class='item'>
<a class="item" href="/appclient">APP与插件下载</a>
</div>
</div>
</div>
<div class='column'>
<div class='ui link list'>
<div class='item'>
<a class="item" href="/gitee-stars">码云封面人物</a>
</div>
<div class='item'>
<a class="item" href="/gvp">GVP项目</a>
</div>
<div class='item'>
<a class="item" href="https://blog.gitee.com/">码云博客</a>
</div>
<div class='item'>
<a class="item" href="/enterprises#nonprofit-plan">Gitee 公益计划</a>
</div>
</div>
</div>
<div class='column'>
<div class='ui link list'>
<div class='item'>
<a class="item" href="/api/v5/swagger">OpenAPI</a>
</div>
<div class='item'>
<a class="item" href="/help">帮助文档</a>
</div>
<div class='item'>
<a class="item" href="/self_services">在线自助服务</a>
</div>
<div class='item'>
<a class="item" href="/git-osc">更新日志</a>
</div>
</div>
</div>
</div>
</div>
<div class='seven wide column right aligned followus git-footer-right'>
<div class='qrcode weixin'>
<img alt="Qrcode weixin" src="https://assets.gitee.com/assets/qrcode-weixin-9e7cfb27165143d2b8e8b268a52ea822.jpg" />
<p class='weixin-text'>微信服务号</p>
</div>
<div class='phone-and-qq column'>
<div class='ui list official-support-container'>
<div class='item'>
<a class="icon-popup" href="//shang.qq.com/wpa/qunwpa?idkey=df785aa7af71f7d74149ab062742d761b845464350ecba25eb440357a3e573b7" title="点击加入码云官方群"><i class='iconfont icon-logo-qq'></i>
<span>官方技术交流QQ群：1050025484</span>
</a></div>
<div class='item mail-and-zhihu'>
<a href="mailto: git@oschina.cn"><i class='iconfont icon-msg-mail'></i>
<span id='git-footer-email'>git#oschina.cn</span>
</a></div>
<div class='item mail-and-zhihu'>
<a href="https://www.zhihu.com/org/ma-yun-osc/" target="_blank"><i class='iconfont icon-zhihu'></i>
<span>码云Gitee</span>
</a></div>
<div class='item tel'>
<a>
<i class='iconfont icon-tel'></i>
<span>售前及售后使用咨询：400-606-0201</span>
</a>
</div>
</div>
</div>
</div>
</div>
</div>
<div class='bottombar'>
<div class='ui container'>
<div class='ui grid'>
<div class='seven wide column partner'>
<div class='copyright'>
<a href="http://www.beian.miit.gov.cn/">粤ICP备12009483号</a>
</div>
</div>
<div class='nine wide column right aligned'>
<i class='icon world'></i>
<a href="/language/zh-CN">简 体</a>
/
<a href="/language/zh-TW">繁 體</a>
/
<a href="/language/en">English</a>
</div>
</div>
</div>
</div>
</footer>
<script>
  var officialEmail = $('#git-footer-email').text()
  $('#git-footer-main .icon-popup').popup({ position: 'bottom center' })
  $('#git-footer-email').text(officialEmail.replace('#', '@'))
</script>


<div class='side-toolbar'>
<div class='button toolbar-help'>
<i class='iconfont icon-help'></i>
</div>
<div class='ui popup left center dark'>点此查找更多帮助</div>
<div class='toolbar-help-dialog'>
<div class='toolbar-dialog-header'>
<h3 class='toolbar-dialog-title'>搜索帮助</h3>
<form accept-charset="UTF-8" action="/help/load_keywords_data" class="toolbar-help-search-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<div class='ui icon input fluid toolbar-help-search'>
<input name='keywords' placeholder='请输入产品名称或问题' type='text'>
<i class='icon search'></i>
</div>
</form>

<i class='iconfont icon-close toolbar-dialog-close-icon'></i>
</div>
<div class='toolbar-dialog-content'>
<div class='toolbar-help-hot-search'>
<div class='toolbar-roll'>
<a class="init active" href="https://oschina.gitee.io/learn-git-branching/?utm_source==gitee-help-widget" title="Git 命令在线学习"><i class='Blue icon icon-command iconfont'></i>
<span>Git 命令在线学习</span>
</a><a class="init " href="https://gitee.com/help/articles/4261?utm_source==gitee-help-widget" title="如何在码云上导入 GitHub 仓库"><i class='icon icon-clipboard iconfont orange'></i>
<span>如何在码云上导入 GitHub 仓库</span>
</a></div>
<div class='toolbar-list'>
<div class='toolbar-list-item'>
<a href="/help/articles/4114">Git 仓库基础操作</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4166">企业版和社区版功能对比</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4191">SSH 公钥设置</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4194">如何处理代码冲突</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4232">仓库体积过大，如何减小？</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4279">如何找回被删除的仓库数据</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4283">Gitee 产品配额说明</a>
</div>
<div class='toolbar-list-item'>
<a href="/help/articles/4284">GitHub仓库快速导入Gitee及同步更新</a>
</div>
</div>
</div>
<div class='toolbar-help-search-reseult'>
<div class='toolbar-help-flex-column'>
<div class='ui centered inline loader toolbar-help-loader'></div>
<div class='toolbar-list'></div>
<div class='toolbar-help-link-to-help'>
<a href="" target="_blank">查看更多搜索结果</a>
</div>
</div>
</div>
</div>
</div>
<script>
  var opt = { position: 'left center'};
  var $helpSideToolbar = $('.button.toolbar-help');
  var $toolbarRoll = $('.toolbar-roll');
  
  $(function() {
    if (false) {
      $helpSideToolbar.popup(opt).popup({lastResort:'left center'})
    } else {
      $helpSideToolbar.popup({lastResort:'left center'}).popup('show', opt);
      setTimeout(function() {
        $helpSideToolbar.popup('hide', opt);
      }, 3000);
    }
  
    if ($toolbarRoll.length) {
      setInterval(function() {
        var $nextActiveLink = $toolbarRoll.find('a.active').next();
        if (!$nextActiveLink.length) {
          $nextActiveLink = $toolbarRoll.find('a:first-child');
        }
        $nextActiveLink.attr('class', 'active').siblings().removeClass('active init');
      }, 5000);
    }
  })
</script>

<div class='button share-link'>
<i class='iconfont icon-share'></i>
</div>
<div class='ui popup dark'>
<div class='header'>
分享到
</div>
<div class='bdsharebuttonbox' style='display: flex'>
<a class='iconfont icon-home-service-wechat' data-cmd='weixin' title='分享到微信'></a>
<a class='iconfont icon-weibo' data-cmd='tsina' title='分享到新浪微博'></a>
<a class='iconfont icon-qq' data-cmd='sqq' title='分享到QQ好友'></a>
<a class='iconfont icon-qzone' data-cmd='qzone' title='分享到QQ空间'></a>
</div>
</div>
<div class='popup button' id='home-comment'>
<i class='iconfont icon-comment'></i>
</div>
<div class='ui popup dark'>评论</div>
<div class='toolbar-appeal popup button'>
<i class='iconfont icon-report'></i>
</div>
<div class='ui popup dark'>
仓库举报
</div>
<script>
  $('.toolbar-appeal').popup({ position: 'left center' });
</script>

<div class='button gotop popup' id='gotop'>
<i class='iconfont icon-top'></i>
</div>
<div class='ui popup dark'>回到顶部</div>
</div>
<div class='form modal normal-modal tiny ui' id='unlanding-complaint-modal'>
<i class='iconfont icon-close close'></i>
<div class='header'>
登录提示
</div>
<div class='container actions'>
<div class='content'>
该操作需登录码云帐号，请先登录后再操作。
</div>
<div class='ui orange icon large button ok'>
立即登录
</div>
<div class='ui button blank cancel'>
没有帐号，去注册
</div>
</div>
</div>
<script>
  var $elm = $('.toolbar-appeal');
  
  $elm.on('click', function() {
    var modals = $("#unlanding-complaint-modal.normal-modal");
    if (modals.length > 1) {
      modals.eq(0).modal('show');
    } else {
      modals.modal('show');
    }
  })
  $("#unlanding-complaint-modal.normal-modal").modal({
    onDeny: function() {
      window.location.href = "/signup?from=";
    },
    onApprove: function() {
      window.location.href = "/login?from=";
    }
  })
</script>

<style>
  .side-toolbar .bdsharebuttonbox a {
    font-size: 24px;
    color: white !important;
    opacity: 0.9;
    margin: 6px 6px 0px 6px;
    background-image: none;
    text-indent: 0;
    height: auto;
    width: auto;
  }
</style>
<script>
  (function() {
    $('#project-user-message').popup({
      position: 'left center'
    });
  
  }).call(this);
</script>
<script>
  Gitee.initSideToolbar({
    hasComment: true,
    commentUrl: '/ModelArts/ModelArts-Lab#tree_comm_title'
  })
</script>
<script>
  window._bd_share_config = {
    "common": {
      "bdSnsKey": {},
      "bdText": document.title,
      "bdMini": "1",
      "bdMiniList": ["bdxc","tqf","douban","bdhome","sqq","thx","ibaidu","meilishuo","mogujie","diandian","huaban","duitang","hx","fx","youdao","sdo","qingbiji","people","xinhua","mail","isohu","yaolan","wealink","ty","iguba","fbook","twi","linkedin","h163","evernotecn","copy","print"],
      "bdPic": "",
      "bdStyle": "1",
      "bdSize": "32"
    },
    "share": {}
  }
</script>
<script src="/bd_share/static/api/js/share.js"></script>



<style>
  .gitee-stars-main-widget {
    display: none;
    position: fixed;
    left: 0;
    bottom: 0;
    z-index: 106; }
    .gitee-stars-main-widget .close-icon {
      position: absolute;
      top: 5px;
      cursor: pointer; }
    .gitee-stars-main-widget .people-image {
      width: 200px;
      padding: 0 10px; }
  
  .gitee-stars-main-widget.pendan-widget .close-icon {
    right: 20px; }
  .gitee-stars-main-widget.gitee-stars-widget .close-icon {
    left: 20px; }
</style>
<div class='gitee-stars-main-widget pendan-widget'>
<a href="https://gitee.com/Selected-Activities/Adapted-game/?utm_source=gitee-gj" target="_blank"><img alt="231008 48f1a665 1899542" class="people-image" src="https://images.gitee.com/uploads/images/2020/0712/231008_48f1a665_1899542.png" />
<img alt="231017 9a6720c6 1899542" class="close-icon" src="https://images.gitee.com/uploads/images/2020/0712/231017_9a6720c6_1899542.png" />
</a></div>
<script>
  $(function () {
    var $giteeStarsWidget = $('.gitee-stars-main-widget')
    var cookieKey = "visit-gitee--2020-07-12 23:15:49 +0800"
  
    if ($.cookie(cookieKey) == 1) {
      $giteeStarsWidget.hide()
    } else {
      $giteeStarsWidget.show()
    }
  
    $giteeStarsWidget.on('click', '.close-icon', function (e) {
      e.preventDefault()
      $.cookie(cookieKey, 1, {path: '/', expires: 60})
      $giteeStarsWidget.hide()
    })
  })
</script>


<script>
  (function() {
    this.__gac = {
      domain: 'www.oschina.net'
    };
  
  }).call(this);
</script>
<script defer src='//www.oschina.net/public/javascripts/cjl/ga.js?t=20160926' type='text/javascript'></script>

<script src="https://assets.gitee.com/assets/bdstatic/app-070a9e339ac82bf2bf7ef20375cd4121.js"></script>
</body>
</html>
