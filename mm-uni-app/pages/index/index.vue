<template>
	<view>
		
		<!-- 顶部选项卡 -->
		<scroll-view scroll-x class="border-bottom scroll-row" style="height: 80rpx;"
		:scroll-into-view="scrollInto" :scroll-with-animation="true">
			<view class="scroll-row-item px-4"
			@click="changeTab(index)"
			style="height: 80rpx; line-height: 80rpx;"
			v-for="(item, index) in newsItems" :key="index"
			:class="tabIndex === index ? 'main-text-color' : ''"
			:id="'tab'+index">
				<text class="font-md">{{item.name}}</text>
			</view>
		</scroll-view>
		
		<swiper :duration="150" :current="tabIndex" 
		:style="'height:'+scrollH+'px;'" @change="onChangeTab">
			<swiper-item v-for="(item, index) in newsItems" :key="index">
				<scroll-view scroll-y :style="'height:'+scrollH+'px;'" @scrolltolower="loadmore(index)">
					<block v-for="(list, listIndex) in item.list" :key="listIndex">
						<!-- 轮播图组件 -->
						<swiper-image v-if="list.type === 'swiper'" :resdata="list.data" />
						
						<!-- 首页分类 -->
						<template v-else-if="list.type === 'indexNav'">
							<index-nav :resdata="list.data" />
							<!-- 全局分割线 -->
							<divider />
						</template>
						
						<!-- 三图广告 -->
						<template v-else-if="list.type === 'threeAdv'">
							<three-adv v-if="list.type === 'threeAdv'" :resdata="list.data" />
							<divider />
						</template>
						
						<!-- 大图广告位 -->
						<!-- <card headTile="每日精选" bodyCover="/static/images/demo/demo4.jpg" /> -->
						
						<!-- 推荐列表组件 750-5=745 745/2=372.5 -->
						<view class="row j-sb" v-else-if="list.type === 'recommendList'">
							<block v-for="(item2, index2) in list.data" :key="index2">
								<common-list :item="item2" :index="index2"></common-list>
							</block>
						</view>
					</block>
					<!-- 上拉加载更多 -->
					<divider />
					<view class="d-flex a-center j-center text-light-muted font-md py-3">
						{{loadText}}
					</view>
				</scroll-view>
			</swiper-item>
		</swiper>
		
	</view>
</template>

<script>
	let newsItems = [
		{
			name: '关注',
			list: [
				{
					type: 'swiper',
					data: [
						{src:"/static/images/demo/demo3.jpg"},
						{src:"/static/images/demo/demo4.jpg"},
						{src:"/static/images/demo/demo5.jpg"}
					]
				},
				{
					type: 'indexNav',
					data: [
						{src:"/static/images/indexnav/1.png", text:"新品分类"},
						{src:"/static/images/indexnav/2.gif", text:"小米众筹"},
						{src:"/static/images/indexnav/3.gif", text:"以旧换新"},
						{src:"/static/images/indexnav/4.gif", text:"一分拼团"},
						{src:"/static/images/indexnav/5.gif", text:"超值特卖"},
						{src:"/static/images/indexnav/6.gif", text:"小米秒杀"},
						{src:"/static/images/indexnav/7.gif", text:"真心想要"},
						{src:"/static/images/indexnav/8.gif", text:"电视热卖"},
						{src:"/static/images/indexnav/9.gif", text:"加点热卖"},
						{src:"/static/images/indexnav/10.gif", text:"米粉卡"}
					]
				},
				{
					type: 'threeAdv',
					data:{
						big:{
							src:"/static/images/demo/demo1.jpg"
						},
						smalltop:{
							src:"/static/images/demo/demo2.jpg"
						},
						smallbottom:{
							src:"/static/images/demo/demo2.jpg"
						}
					},
				},
				{
					type: "recommendList",
					data:[
						{
							cover:"/static/images/demo/list/1.jpg",
							title:"米家空调",
							desc:"1.5匹变频",
							oprice:2699,
							pprice:1399
						},
						{
							cover:"/static/images/demo/list/1.jpg",
							title:"米家空调",
							desc:"1.5匹变频",
							oprice:2699,
							pprice:1399
						},
						{
							cover:"/static/images/demo/list/1.jpg",
							title:"米家空调",
							desc:"1.5匹变频",
							oprice:2699,
							pprice:1399
						}
					]
				}
			]
		},
		{
			name:"体育",
			list: []
		},
		{
			name:"热点",
			list: []
		},
		{
			name:"财经",
			list: []
		},
		{
			name:"娱乐",
			list: []
		},
		{
			name:"军事",
			list: []
		},
		{
			name:"历史",
			list: []
		},
		{
			name:"本地",
			list: []
		}
	]
	
	let moreData = [
		{
			cover:"/static/images/demo/list/1.jpg",
			title:"米家空调",
			desc:"1.5匹变频",
			oprice:2699,
			pprice:1399
		},
		{
			cover:"/static/images/demo/list/1.jpg",
			title:"米家空调",
			desc:"1.5匹变频",
			oprice:2699,
			pprice:1399
		},
		{
			cover:"/static/images/demo/list/1.jpg",
			title:"米家空调",
			desc:"1.5匹变频",
			oprice:2699,
			pprice:1399
		}
	]
					
	import swiperImage from "@/components/index/swiper-image.vue"
	import indexNav from "@/components/index/index-nav.vue"
	import threeAdv from "@/components/index/three-adv.vue"
	import card from "@/components/common/card.vue"
	import commonList from "@/components/common/common-list.vue"
	
	export default {
		components:{
			swiperImage,
			indexNav,
			threeAdv,
			card,
			commonList
		},
		data() {
			return {
				scrollInto:"",
				scrollH:500,
				tabIndex:0,
				newsItems: [],
				loadText: '上拉加载更多'
			}
		},
		onLoad() {
			// 获取可视区域高度
			uni.getSystemInfo({
				success: (res) => {
					this.scrollH = res.windowHeight - uni.upx2px(82);
				}
			})
			this.__init();
		},
		methods: {
			// 初始化数据
			__init() {
				this.newsItems = newsItems;
			},
			// 切换选项卡
			changeTab(index){
				if (this.tabIndex === index) {
					return;
				}
				this.tabIndex = index;
				this.scrollInto = 'tab' + index;
				this.loadData();
			},
			// 监听滑动列表
			onChangeTab(e) {
				this.changeTab(e.detail.current);
			},
			// 加载数据
			loadData() {
				let index = this.tabIndex;
				// 向服务端请求数据
				if (this.newsItems[index].list.length !== 0) {
					console.log('使用缓存数据');
					return;
				}
				console.log('向服务端请求数据');
				this.newsItems[index].list = []
			},
			// 上拉加载更多
			loadmore(index) {
				if (this.loadText !== '上拉加载更多') {
					return;
				}
				this.loadText = '加载中...';
				setTimeout(() => {
					this.newsItems[index].list[3].data = [
						...this.newsItems[index].list[3].data,
						...moreData
					];
					this.loadText = '上拉加载更多';
				}, 2000);
			}
		}
	}
</script>

<style>

</style>
