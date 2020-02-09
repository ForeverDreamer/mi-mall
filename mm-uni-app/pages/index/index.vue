<template>
	<view>
		<!-- 轮播图组件 -->
		<swiper-image :resdata="swipers" />
		
		<!-- 首页分类 -->
		<index-nav :resdata="indexnavs" />
		
		<!-- 全局分割线 -->
		<divider />
		
		<!-- 三图广告 -->
		<three-adv :resdata="threeAdv" />
		
		<divider />
		
		<!-- 大图广告位 -->
		<card headTile="每日精选" bodyCover="/static/images/demo/demo4.jpg" />
		
		<!-- 公共列表组件 750-5=745 745/2=372.5 -->
			<view class="row j-sb">
				<block v-for="(item, index) in commonList" :key="index">
					<common-list :item="item" :index="index"></common-list>
				</block>
			</view>
		
	</view>
</template>

<script>
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
				swipers:[
					{src:"/static/images/demo/demo3.jpg"},
					{src:"/static/images/demo/demo4.jpg"},
					{src:"/static/images/demo/demo5.jpg"}
				],
				indexnavs:[
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
				],
				threeAdv:{
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
				commonList:[
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
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>

</style>
