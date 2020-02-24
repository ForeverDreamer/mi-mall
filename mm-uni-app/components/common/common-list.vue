<template>
	<view style="width: 372.5rpx;" @click="openDetail">
		<image :src="item.cover_img" mode="widthFix"></image>
		<view class="p-2 pt-1">
			<view class="font-md">{{item.version}}</view>
			<text class="d-block font text-light-muted">{{item.color}}</text>
			<view class="d-flex my-1">
				<price>{{item.discount_price}}</price>
				<view class="font-sm text-light-muted line-through a-self-end ml-1 line-h"
				>￥{{item.original_price}}</view>
			</view>
		</view>
	</view>
</template>

<script>
	import price from "@/components/common/price.vue"
	
	export default{
		props:{
			item:Object,
			index:Number
		},
		components:{
			price
		},
		methods: {
			openDetail() {
				uni.navigateTo({
					url: '/pages/detail/detail'
				});
			}
		}
	}
</script>

<style>
</style>
