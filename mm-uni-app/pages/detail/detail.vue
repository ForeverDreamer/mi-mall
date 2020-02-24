<template>
	<view>
		<!-- 商品详情大图 -->
		<swiper-image :resdata="detail.banners" height="750" preview />
		<!-- 基础详情 -->
		<base-info :detail="detail" />
		<!-- 滚动商品特性 w170*h110 -->
		<scrollAttrs :baseAttrs="detail.baseAttrs" />
		<!-- 属性选择 -->
		<view class="p-2">
			<view class="rounded border bg-light-secondary">
				<uni-list-item>
					<view class="d-flex">
						<text class="mr-2 text-muted">已选</text>
						<text>火焰红 64G 标配</text>
					</view>
				</uni-list-item>
				<uni-list-item>
					<view class="d-flex">
						<text class="mr-2 text-muted">配送</text>
						<text class="mr-2">北京 东城区</text>
						<text class="main-text-color">现配</text>
					</view>
				</uni-list-item>
				<uni-list-item extraWidth="15%">
					<view class="d-flex a-center">
						<view class="text-muted font d-flex a-center mr-2">
							<view class="iconfont icon-finish main-text-color"></view>小米自营
						</view>
						<view class="text-muted font d-flex a-center mr-2">
							<view class="iconfont icon-finish main-text-color"></view>小米发货
						</view>
						<view class="text-muted font d-flex a-center mr-2">
							<view class="iconfont icon-finish main-text-color"></view>七天无理由退货
						</view>
					</view>
				</uni-list-item>
			</view>
		</view>
		<!-- 横向滚动评论 
		     外层 w620*h380
			 头像 w70*h30
			 图片 h115
		-->
		<scroll-comments :comments="detail.comments" />
		<!-- 商品详情, 制作一系列图片展示就好, 不用使用uParse等富文本解析器, 太麻烦了 -->

		<!-- 热门推荐 -->
		<card headTitle="热门推荐" headTitleWeight="false">
			<view class="row j-sb">
				<common-list v-for="(item, index) in detail.recommend_list"
				:key="index" :item="item"></common-list>
			</view>
		</card>
		<!-- 底部操作条 -->
		<bottom-btn></bottom-btn>
	</view>
</template>

<script>
	import $H from '@/common/lib/request.js'
	import swiperImage from "@/components/index/swiper-image.vue"
	import baseInfo from "@/components/detail/base-info.vue"
	import scrollAttrs from "@/components/detail/scroll-attrs.vue"
	import uniListItem from "@/components/uni-ui/uni-list-item/uni-list-item.vue"
	import scrollComments from "@/components/detail/scroll-comments.vue"
	import card from "@/components/common/card.vue"
	import commonList from "@/components/common/common-list.vue"
	import bottomBtn from "@/components/detail/bottom-btn.vue"
	
	const base_media = $H.common.base_media
	
	export default {
		components: {
			swiperImage,
			baseInfo,
			scrollAttrs,
			uniListItem,
			scrollComments,
			card,
			commonList,
			bottomBtn
		},
		data() {
			return {
				detail: {
					title: '',
					desc: '',
					banners: [],
					sku_set: [],
					baseAttrs: [
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'},
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'},
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'},
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'},
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'},
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'},
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'},
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'},
						{icon: 'icon-cpu', title: 'CPU', desc: '蛟龙845八核'}
					],
					comments: [
						{
							userPic: '/static/images/demo/demo6.jpg',
							nickName: '楚绵',
							creatTime: '2019-07-31',
							likes: 123,
							text: '评论内容',
							imgList: [
								'/static/images/demo/demo6.jpg',
								'/static/images/demo/demo6.jpg',
								'/static/images/demo/demo6.jpg'
							]
						},
						{
							userPic: '/static/images/demo/demo6.jpg',
							nickName: '楚绵',
							creatTime: '2019-07-31',
							likes: 123,
							text: '评论内容',
							imgList: [
								'/static/images/demo/demo6.jpg',
								'/static/images/demo/demo6.jpg',
								'/static/images/demo/demo6.jpg'
							]
						},
						{
							userPic: '/static/images/demo/demo6.jpg',
							nickName: '楚绵',
							creatTime: '2019-07-31',
							likes: 123,
							text: '评论内容',
							imgList: [
								'/static/images/demo/demo6.jpg',
								'/static/images/demo/demo6.jpg',
								'/static/images/demo/demo6.jpg'
							]
						}
					],
					recommend_list: [
						{
							"version": "i5 8G 512G PCle MX250",
							"color": "银色",
							"cover_img": "image/product/4/cover/2a4df6ab-14b2-4edf-80cb-cefa8bc5491d.jpg",
							"original_price": 5699,
							"discount_price": 5699
						}, {
							"version": "Pro H 高效除菌",
							"color": "白色",
							"cover_img": "image/product/5/cover/fb39046d-5b2e-4277-8aaa-c4b0bd76143b.jpg",
							"original_price": 1699,
							"discount_price": 1699
						}, {
							"version": "55英寸",
							"color": "灰色",
							"cover_img": "image/product/6/cover/070461b2-0879-4639-9723-e0005f5e4632.jpg",
							"original_price": 2999,
							"discount_price": 2999
						}, {
							"version": "i5 8G 256G PCle 集显",
							"color": "银色",
							"cover_img": "image/product/4/cover/c9978d00-e1b9-4a0f-899c-75e9546f6fe5.jpg",
							"original_price": 4999,
							"discount_price": 4999
						}, {
							"version": "6GB+128GB",
							"color": "冰雪极光",
							"cover_img": "image/product/3/cover/2eaccd2c-e47d-4ebc-a392-5b688e1fbb59.jpg",
							"original_price": 2799,
							"discount_price": 2799
						}, {
							"version": "6GB+128GB",
							"color": "魔法绿境",
							"cover_img": "image/product/3/cover/bbf41644-5581-4ec8-8f08-acafecb1fb00.jpg",
							"original_price": 2799,
							"discount_price": 2799
						}, {
							"version": "6GB+128GB",
							"color": "暗夜魅影",
							"cover_img": "image/product/3/cover/7fd7681a-1030-4648-946b-7a614a9f7910.jpg",
							"original_price": 2799,
							"discount_price": 2799
						}, {
							"version": "i7 8G 512G PCle MX250",
							"color": "银色",
							"cover_img": "image/product/4/cover/273e207e-c166-4716-a483-8665db5dd6be.jpg",
							"original_price": 5699,
							"discount_price": 5699
						}
					]
				}
			}
		},
		onLoad() {
			this.__init();
		},
		methods: {
			async __init() {
				let result = await $H.get('product/3/')
				if (result) {
					// console.log('请求成功');
					// console.log(result);
					const data =  result.data;
					this.detail.title = data.title;
					this.detail.desc = data.desc;
					this.detail.sku_set = data.sku_set;
					for(let item of data.carousel_images){
						item.src = item.image
						this.detail.banners.push(item)
					}
					// console.log(JSON.stringify(this.detail))
				}
				for(let item of this.detail.recommend_list){
					item.cover_img = base_media + item.cover_img
					// this.carousel.push(item)
				}
				// console.log('初始化数据');
				// let [error, result] = await uni.request({
				// 	url: base_url + 'product/3/',
				// 	// url: 'https://itman.icu/product/recommends/',
				// 	method: 'GET',
				// 	header: {
				// 	        'Authorization': access_token //自定义请求头信息
				// 	},
				// });
				// if (error) {
				// 	return uni.showToast({
				// 		title: error.errMsg,
				// 		icon: 'none'
				// 	});
				// }
				// if (result.statusCode !== 200) {
				// 	return uni.showToast({
				// 		title: result.statusCode + ' ' + result.data,
				// 		icon: 'none'
				// 	})
					
				// }
				// console.log(error)
				// console.log(result)
				
			}
		}
	}
</script>

<style>

</style>
