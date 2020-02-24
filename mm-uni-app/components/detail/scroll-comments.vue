<template>
	<view class="p-2 pr-0">
		<scroll-view scroll-x class="scroll-row">
			<view class="scroll-row-item rounded bg-light-secondary mr-2 a-center" 
			style="width: 620rpx; height: 380rpx;"
			v-for="(item, index) in comments" :key="index">
				<view class="d-flex a-center m-2">
					<image :src="item.userPic" mode="widthFix" 
					style="width: 70rpx; height: 70rpx;"
					class="rounded-circle"></image>
					<view class="ml-2">
						<text class="font-md line-h">{{item.nickName}}</text>
						<text class="d-block font text-light-muted line-h">{{item.creatTime}}</text>
					</view>
					<view class="iconfont icon-dianzan text-light-muted font ml-auto">
					{{item.likes}}</view>
				</view>
				<text class="d-block font-md mx-2 mb-2">{{item.text}}</text>
				<view class="row">
					<view class="span24-8 px-2" v-for="(img, i) in item.imgList" :key="i">
						<image :src="img" mode="widthFix"
						style="height: 115rpx;"
						class="rounded"></image>
					</view>
				</view>
			</view>
		</scroll-view>
		<view class="d-flex a-center j-center py-2 mt-2 text-primary"
		hover-class="bg-light-secondary">
			更多评论<view class="iconfont icon-you"></view>
		</view>
	</view>
</template>

<script>
	export default {
		props: ['comments']
	}
</script>

<style>
</style>
