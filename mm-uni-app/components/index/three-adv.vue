<template>
	<!-- 左边w:373 h530 -->
	<!-- 右边w:375 h264 边h2 -->
	<view class="d-flex">
		<image :src="resdata.big.src"
		lazy-load
		style="width: 373rpx; height: 530rpx; border-right: 2rpx solid #F5F5F5;"
		@tap="event(resdata.big)"
		></image>
		<view class="d-flex flex-column">
			<image :src="resdata.smalltop.src"
			lazy-load
			style="width: 375rpx; height: 264rpx; border-bottom: 2rpx solid #F5F5F5;"
			@tap="event(resdata.smalltop)"
			></image>
			<image :src="resdata.smallbottom.src"
			lazy-load
			style="width: 375rpx; height: 264rpx;"
			@tap="event(resdata.smallbottom)"
			></image>
		</view>
	</view>
</template>

<script>
	export default {
		props:{
			resdata:Object
		},
		methods:{
			event(obj){
				console.log(obj)
			}
		}
	}
</script>

<style>
</style>
