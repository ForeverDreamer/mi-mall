<template>
	<view class="uni-card">
		<!-- 标题 -->
		<view v-if="showhead" class="p-2 main-border-color" :class="getHeadClass">
			<slot name="title">
				<text class="font-md font-weight">{{headTitle}}</text>
			</slot>
		</view>
		<!-- body -->
		<view :class="getBodyClass">
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
			headTitle:String,
			// 封面图
			bodyCover:String,
			// 是否显示头部
			showhead:{
				type:Boolean,
				default:true
			},
			// 是否显示下边线
			headBorderBottom:{
				type:Boolean,
				default:true
			},
			// 是否给body加padding
			bodyPadding:{
				type:Boolean,
				default:false
			}
		},
		computed: {
			getHeadClass() {
				return {'border-bottom': this.headBorderBottom}
			},
			getBodyClass() {
				return {'p-2': this.bodyPadding}
			}
		}
	}
</script>
	
<style>
</style>
