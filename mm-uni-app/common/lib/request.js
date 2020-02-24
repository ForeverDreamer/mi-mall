export default {
	// 全局配置
	common: {
		base_url: 'http://192.168.31.124:8000/',
		base_media: 'http://192.168.31.124:8000/media/',
		header: {
			'Content-Type': 'application/json; charset-UTF-8',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Authorization': 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgyNTI1MTQzLCJqdGkiOiIxZmZjMTBkNTRjM2E0NzZlOTg0YWRjMzUxYTdlZTE0MyIsInVzZXJfaWQiOjN9.6f3fCGbL58CUJHWdfxQAYydKlNd11UZgneL3NqF3ckg'
		},
		data: {},
		method: 'GET',
		dataType: 'json'
	},
	// 请求 返回promise
	request(options = {}) {
		options.url = this.common.base_url + options.url
		options.header = options.header || this.common.header
		options.data = options.data || this.common.data
		options.method = options.method || this.common.method
		options.dataType = options.dataType || this.common.dataType
		
		return new Promise((res, rej) => {
			uni.request({
				...options,
				success: (result) => {
					// 服务端失败
					if (result.statusCode !== 200) {
						uni.showToast({
							title: result.statusCode + ' ' + JSON.stringify(result.data),
							icon: 'none'
						});
						return rej(result);
					}
					// 成功
					// let data = result.data;
					res(result);
				},
				fail: (error) => {
					// 通常是网络错误
					uni.showToast({
						title: error.errMsg || '请求失败',
						icon: 'none'
					});
					return rej(error);
				}
			});
		})
	},
	get(url,data = {},options = {}){
		options.url = url
		options.data = data
		options.method = 'GET'
		return this.request(options)
	},
	post(url,data = {},options = {}){
		options.url = url
		options.data = data
		options.method = 'POST'
		return this.request(options)
	},
	patch(url,data = {},options = {}){
		options.url = url
		options.data = data
		options.method = 'PATCH '
		return this.request(options)
	},
	put(url,data = {},options = {}){
		options.url = url
		options.data = data
		options.method = 'PUT'
		return this.request(options)
	},
	del(url,data = {},options = {}){
		options.url = url
		options.data = data
		options.method = 'DELETE'
		return this.request(options)
	}
}