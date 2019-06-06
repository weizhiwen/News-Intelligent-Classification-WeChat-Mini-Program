var app = getApp()
Page({
  data: {
    news: [],
    categoryIcon: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAwklEQVRYR+2WMQ7CMAxFa+U4MDnKDNyBA/VA3AGYo3iC41hGRu1QgmhrITWDO/srzov0fqHb+IONz+/aWiDn3IcQDiJy/EUGAG7MfE8p9TpnzWl2QoCIHiKyW/IsAPBExL3OWnPVAqUUWXL4OBNjfF/AmvMFnIATaI8AEV3nLDg6QG2IiKdBRKZcRWBQ6nnOhmpBZr58qHh1rlpgjQX/Nett6G04IWCtVWuuPRFZb2LNOQEn8O233NRq1hb1NvQ6VgIvfmMgMBn2T0cAAAAASUVORK5CYII=',
    show: false,
    currentCategory: '',
    inputValue: '',
    keyword: '',
    categories: ['国内', '国际', '军事', '体育', '社会', '财经', '娱乐'],
    offset: 0,
    totalCount: 0,
    searchLoading: false, //"上拉加载"的变量，默认false，隐藏
    searchLoadingComplete: false //“没有数据”的变量，默认false，隐藏
  },

  /**
   * 用户自定义的函数
   */

  // 新闻搜索
  search_news: function(e) {
    that = this
    keyword = e.detail.value
    // 在发送请求前把新闻数据数组清空
    that.setData({
      currentCategory:'',
      news: [],
      offset: 0,
    })
    that.fetch_news(that, '', keyword)
  },

  // 弹出分类侧栏
  tap_category: function(e) {
    var that = this
    if (that.data.show) {
      that.setData({
        show: false,
        categoryIcon: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAwklEQVRYR+2WMQ7CMAxFa+U4MDnKDNyBA/VA3AGYo3iC41hGRu1QgmhrITWDO/srzov0fqHb+IONz+/aWiDn3IcQDiJy/EUGAG7MfE8p9TpnzWl2QoCIHiKyW/IsAPBExL3OWnPVAqUUWXL4OBNjfF/AmvMFnIATaI8AEV3nLDg6QG2IiKdBRKZcRWBQ6nnOhmpBZr58qHh1rlpgjQX/Nett6G04IWCtVWuuPRFZb2LNOQEn8O233NRq1hb1NvQ6VgIvfmMgMBn2T0cAAAAASUVORK5CYII='
      });
    } else {
      that.setData({
        show: true,
        categoryIcon: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAB/klEQVRYR+1WPWgTYRh+3s/cpQ4KLQ720qGD4N1llQ4uUoqDi1BsK4VCCw4u4iKC3drJDt2K0KHgZClOBQehIM2mDp0kuQMLBWm+BMSfrdwFv1cu6SU9f5ofPkgCuem4e+55n+95f+4ldPmiLsfHQEBvOZAJ3Dm+wKFMebtna+PqiT0uBJZ01YtM+ysxV90BK3Cfg/hZ9IKZl0tpfy0GWaFzBGBclwAQvZFG4W7EVxeQCZ0cA7eqQQi70vCmo9sxzl5TFfVZW/Aav5SGl0kIsALnPgjbAAIl6F45VXjbcMB9CbC2FIB5NU5DbxWhVptbJBs40DsOWIE9T4JmmPFOGGLnmPLf4zRmQntJgRZbTGtTGP/i1fJFP5dow9HQfk2g2dogooVSuvDqdA6MqIr61pS1PcCBNL0bLQmIQFbocHv856MZyJVMb/KPQfT/FFz5ev2SeZme6BLxz3+BLvJ2eXqnC9pVrgvfPw6McXZEx6kFBH+hTz9irjMLib0CohkAH4Qh1o4pf9gYRO4mgx/qEHDK8Uia3otkG1acIhhWDUCPpVnYqA6iMDuhoD5qDB5R/ZSmN5wUEDpbAB5UHxLfLBr++zioVXH2wLitTQTzukz7TxMCaqsX31EKh+WhxjZUT8OJO6VFQIpU0cjv/1UDWsg7IOmfNuzgcC19MnDgNyWYqyFyPnQ0AAAAAElFTkSuQmCC'
      });
    }
  },

  // 选择分类
  select_category: function(e) {
    var that = this
    var category = e.currentTarget.dataset.text
    // 在发送请求前把新闻数据数组清空
    that.setData({
      currentCategory: category,
      news: [],
      offset: 0,
    })
    that.fetch_news(that, category, that.data.keyword)
  },

  // 根据分类和关键字获取新闻数据
  fetch_news(that, category, keyword) {
    wx.request({
      url: app.globalData.host + 'news/' + that.data.offset + '/' + app.globalData.limit,
      data: {
        category: category,
        keyword: keyword,
      },
      header: {
        'content-type': 'application/json'
      },
      // 如果请求成功，并且 msg 为 success
      success(res) {
        // 设置新闻数组和数量
        if (res.data.code == 0) {
          var news = that.data.news.concat(res.data.data.items)
          that.setData({
            news: news,
            offset: that.data.offset + app.globalData.limit,
            totalCount: res.data.data.count,
          })
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    var that = this
    that.fetch_news(that, that.data.currentCategory, that.data.keyword)
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
    that = this
    // 如果还有数据就加载数据
    if (that.data.offset < that.data.totalCount) {
      that.fetch_news(that, that.data.currentCategory, that.data.keyword)
    }
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function() {

  }
})