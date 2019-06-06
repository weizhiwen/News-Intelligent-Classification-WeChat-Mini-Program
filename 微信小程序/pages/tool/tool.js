var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    category: '??',
    inputValue: '',
  },

  /**
   * 用户自定义的函数
   */
  // 新闻智能分类
  category_news: function(e) {
    that = this
    title = e.detail.value
    that.predict_news(that, title)
  },

  // 预测新闻分类
  predict_news(that, title) {
    wx.showLoading({
      title: '预测中',
    })
    setTimeout(function () {
      wx.hideLoading()
    }, 2000)
    wx.request({
      url: app.globalData.host + 'news/' + title,
      header: {
        'content-type': 'application/json'
      },
      // 如果请求成功，并且 msg 为 success
      success(res) {
        // 设置新闻数组和数量
        if (res.data.code == 0) {
          that.setData({
            category: res.data.data.items,
          })
        }
      }
    })
  },

  // 扫一扫
  rich_scan: function() {
    var that = this;
    wx.scanCode({
      // 只允许从相机中扫描
      onlyFromCamera: false,
      success: (res) => {
        title = res.result
        that.predict_news(that, title)
        wx.showToast({
          title: '成功',
          icon: 'success'
        })
      },
      fail: (res) => {
        wx.showToast({
          title: '失败',
          icon: 'fail'
        })
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function() {

  }
})