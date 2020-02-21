<template>
	<view class="d-flex border-top border-light-secondary" style="height: 100%; box-sizing: border-box;">
		<scroll-view scroll-y class="border-right border-light-secondary flex-1" style="height: 100%;">
			<view class="border-bottom border-light-secondary py-1"
			hover-class="bg-light-secondary"
			v-for="(item, index) in cate" :key="index">
				<view class="py-1 font-md text-muted text-center"
				:class="activeIndex === index ? 'active' : ''"
				@tap="changeAate(index)">{{item.name}}</view>
			</view>
		</scroll-view>
		<scroll-view scroll-y style="flex: 3.5; height: 100%;">
			<view class="row" v-for="(rowItem, rowIndex) in list" :key="rowIndex">
				<view class="span24-8 text-center py-2"
				v-for="(colItem, colIndex) in rowItem.list" :key="colIndex">
					<image :src="colItem.src" style="width: 120rpx; height: 120rpx;"></image>
					<text class="d-block">{{colItem.name}}</text>
				</view>
			</view>
		</scroll-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				activeIndex: 0,
				cate: [],
				list: []
			}
		},
		onLoad() {
			this.getData()
		},
		methods: {
			getData() {
				for (let i = 0; i < 20; i++) {
					this.cate.push({name:'分类'+i})
					this.list.push({list:[]})
				}
				for (let i = 0; i < this.list.length; i++) {
					for (let j = 0; j < 24; j++) {
						this.list[i].list.push({
							src: '/static/images/demo/cate_01.png',
							name: `分类${i}-商品${j}`
						})
					}
				}
			},
			changeAate(index) {
				this.activeIndex = index
			}
		}
	}
</script>

<style>
.active {
	border-left: 8rpx solid #FD6801;
	color: #FD6801!important;
}
</style>
