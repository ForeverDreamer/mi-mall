<template>
	<view class="uni-card">
		<!-- 标题 -->
		<view v-if="showhead" class="p-2 border-bottom main-border-color">
			<slot name="title">
				<text class="font-md font-weight">{{headTile}}</text>
			</slot>
		</view>
		<!-- body -->
		<view>
			<image v-if="bodyCover" :src="bodyCover"
			mode="widthFix"
			></image>
			<slot name="body"></slot>
		</view>
	</view>
</template>

<script>
	export default {
		props:{
			// 头部标题
			headTile:String,
			// 封面图
			bodyCover:String,
			// 是否显示头部
			showhead:{
				type:Boolean,
				default:true
			}
		}
	}
</script>
	
<style>
</style>
