<template>
	<scroll-view scroll-x class="scroll-row p-2">
		<view class="scroll-row-item" style="width: 170rpx; height: 110rpx;"
		v-for="(item, index) in baseAttrs" :key="index">
			<view class="iconfont line-h-sm" :class="item.icon"></view>
			<view class="line-h-sm">{{item.title}}</view>
			<view class="text-light-muted font-sm line-h-sm">
				{{item.desc}}
			</view>
		</view>
	</scroll-view>
</template>

<script>
	export default {
		props: ['baseAttrs']
	}
</script>

<style>
</style>
