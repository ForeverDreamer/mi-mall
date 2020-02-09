<template>
	<view style="width: 372.5rpx;">
		<image :src="item.cover" mode="widthFix"></image>
		<view class="p-2 pt-1">
			<view class="font-md">{{item.title}}</view>
			<text class="d-block font text-light-muted">{{item.desc}}</text>
			<view class="d-flex my-1">
				<price>{{item.pprice}}</price>
				<view class="font-sm text-light-muted line-through a-self-end ml-1 line-h"
				>￥{{item.oprice}}</view>
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
	}
</script>

<style>
</style>
