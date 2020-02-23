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
	</view>
</template>

<script>
	import $H from '@/common/lib/request.js'
	import swiperImage from "@/components/index/swiper-image.vue"
	import baseInfo from "@/components/detail/base-info.vue"
	import scrollAttrs from "@/components/detail/scroll-attrs.vue"
	import uniListItem from "@/components/uni-ui/uni-list-item/uni-list-item.vue"
	
	export default {
		components: {
			swiperImage,
			baseInfo,
			scrollAttrs,
			uniListItem
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
					console.log(result);
					const data =  result.data;
					this.detail.title = data.title;
					this.detail.desc = data.desc;
					this.detail.sku_set = data.sku_set;
					for(let item of data.carousel_images){
						item.src = item.image
						this.detail.banners.push(item)
					}
					console.log(JSON.stringify(this.detail))
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
