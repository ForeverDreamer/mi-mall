(window.webpackJsonp=window.webpackJsonp||[]).push([[9],{867:function(e,t,n){var content=n(888);"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(47).default)("bd3579e8",content,!0,{sourceMap:!1})},887:function(e,t,n){"use strict";var o=n(867);n.n(o).a},888:function(e,t,n){(t=n(46)(!1)).push([e.i,".custom-active[data-v-2ab19c4d]{color:#67c23a!important;background-color:#f0f9eb!important;border-color:#c237b0!important}.el-dropdown-link[data-v-2ab19c4d]{cursor:pointer;color:#409eff}.el-icon-arrow-down[data-v-2ab19c4d]{font-size:12px}.el-container__outer[data-v-2ab19c4d]{position:absolute;left:200px;right:0;top:55px;bottom:0;overflow:hidden}.el-aside[data-v-2ab19c4d],.el-header[data-v-2ab19c4d],.el-main[data-v-2ab19c4d]{background-color:#fff}.el-aside[data-v-2ab19c4d]{left:0;border-right:1px solid #dee2e6}.el-aside[data-v-2ab19c4d],.el-main__inner[data-v-2ab19c4d]{position:absolute;top:60px;bottom:60px}.el-main__inner[data-v-2ab19c4d]{left:200px;right:0}",""]),e.exports=t},929:function(e,t,n){"use strict";n.r(t);n(420),n(29);var o={name:"Photo",components:{AlbumItem:n(410).a},data:function(){return{imageList:[],imageSlectedList:[],searchInfo:{orderBy:"相册名称",keyword:"图片数量"},activeIndex:0,albums:[],dialogVisible:!1,editForm:{name:"",order:"",editIndex:-1},uploadDialogVisible:!1,currentPage:1}},computed:{editFormTitle:function(){return this.editForm.editIndex>-1?"编辑相册":"创建相册"}},created:function(){this.initData()},methods:{initData:function(){for(var i=0;i<20;i++)this.albums.push({name:"相册"+i,num:Math.floor(100*Math.random()),order:0});for(var e=0;e<30;e++)this.imageList.push({id:e,name:"图片"+e,url:"https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg",srcList:["https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg","https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg","https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg"],selected:!1,selectOrder:0})},changeAlbum:function(e){this.activeIndex=e},delAlbum:function(e){var t=this;this.$confirm("是否删除该相册?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){t.albums.splice(e,1),t.$message({type:"success",message:"删除成功!"})})).catch((function(){}))},openEditForm:function(e){console.log(JSON.stringify(e)),e?(this.editForm.name=e.item.name,this.editForm.order=e.item.order,this.editForm.editIndex=e.index):this.editForm={name:"",order:0,editIndex:-1},this.dialogVisible=!0},confirmEdit:function(){this.editForm.editIndex>-1?this.editAlbum():this.albums.unshift({name:this.editForm.name,order:this.editForm.order,num:0}),this.dialogVisible=!1},editAlbum:function(){this.albums[this.editForm.editIndex].name=this.editForm.name,this.albums[this.editForm.editIndex].order=this.editForm.order},editImage:function(e,t){var n=this;this.$prompt("请输入新名称","提示",{confirmButtonText:"确定",cancelButtonText:"取消",inputValue:e.name,inputValidator:function(e){if(""===e)return"图片名称不能为空"}}).then((function(t){var o=t.value;e.name=o,n.$message({type:"success",message:"修改成功"})})).catch((function(){}))},delImage:function(e){var t=this;this.$confirm("是否删除该图片","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){t.imageList.splice(e,1),t.$message({type:"success",message:"删除成功!"})})).catch((function(){}))},batchDelImage:function(){var e=this;this.$confirm("是否删除选中的所有图片","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){var t=e.imageList.filter((function(image){return!e.imageSlectedList.some((function(e){return e.id===image.id}))}));e.imageList=t,e.imageSlectedList=[],e.$message({type:"success",message:"删除成功!"})})).catch((function(){}))},imgSelected:function(e){var t=this;if(e.selected){var n=this.imageSlectedList.findIndex((function(t){return t.id===e.id}));if(-1===n)return;var o=this.imageSlectedList.length;if(n+1<o)for(var l=function(e){var i=t.imageList.findIndex((function(n){return n.id===t.imageSlectedList[e].id}));i>-1&&t.imageList[i].selectOrder--},r=n;r<o;r++)l(r);this.imageSlectedList.splice(n,1),e.selected=!1,e.selectOrder=0}else this.imageSlectedList.push({id:e.id,url:e.url}),e.selectOrder=this.imageSlectedList.length,e.selected=!0},cancelSelected:function(){var e=this;this.imageList.forEach((function(t){var n=e.imageSlectedList.findIndex((function(e){return e.id===t.id}));n>-1&&(t.selected=!1,t.selectOrder=0,e.imageSlectedList.splice(n,1))}))},handleSizeChange:function(e){console.log("每页 ".concat(e," 条"))},handleCurrentChange:function(e){console.log("当前页: ".concat(e))}}},l=(n(887),n(32)),component=Object(l.a)(o,(function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-container",{staticClass:"el-container__outer"},[n("el-header",{staticClass:"d-flex align-items-center"},[n("div",{staticClass:"d-flex align-items-center mr-auto"},[n("el-select",{staticClass:"mr-2",attrs:{placeholder:"排序方式",size:"medium"},model:{value:e.searchInfo.orderBy,callback:function(t){e.$set(e.searchInfo,"orderBy",t)},expression:"searchInfo.orderBy"}},[n("el-option",{attrs:{label:"区域一",value:"北京"}}),e._v(" "),n("el-option",{attrs:{label:"区域二",value:"上海"}})],1),e._v(" "),n("el-input",{staticClass:"mr-2",attrs:{placeholder:"请输入相册名称",size:"medium"},model:{value:e.searchInfo.keyword,callback:function(t){e.$set(e.searchInfo,"keyword",t)},expression:"searchInfo.keyword"}}),e._v(" "),n("el-button",{attrs:{type:"success",size:"medium"}},[e._v("\n        搜索\n      ")])],1),e._v(" "),e.imageSlectedList.length>0?n("el-button",{attrs:{type:"warning",size:"medium"},on:{click:e.cancelSelected}},[e._v("\n      取消选中\n    ")]):e._e(),e._v(" "),e.imageSlectedList.length>0?n("el-button",{attrs:{type:"danger",size:"medium"},on:{click:e.batchDelImage}},[e._v("\n      批量删除\n    ")]):e._e(),e._v(" "),n("el-button",{attrs:{type:"success",size:"medium"},on:{click:function(t){return e.openEditForm(null)}}},[e._v("\n      创建相册\n    ")]),e._v(" "),n("el-button",{attrs:{type:"warning",size:"medium"},on:{click:function(t){e.uploadDialogVisible=!0}}},[e._v("\n      上传图片\n    ")])],1),e._v(" "),n("el-container",[n("el-aside",{staticClass:"ml-3",attrs:{width:"200px"}},[n("ul",{staticClass:"list-group list-group-flush"},e._l(e.albums,(function(t,o){return n("album-item",{key:o,attrs:{item:t,index:o,active:e.activeIndex===o},on:{change:e.changeAlbum,edit:e.openEditForm,del:e.delAlbum}})})),1)]),e._v(" "),n("el-main",{staticClass:"el-main__inner"},[n("el-row",{attrs:{gutter:10}},e._l(e.imageList,(function(t,o){return n("el-col",{key:o,attrs:{xs:24,sm:12,md:8,lg:4}},[n("el-card",{staticClass:"position-relative mb-3",staticStyle:{cursor:"pointer"},attrs:{"body-style":{padding:"0px"},shadow:"hover"}},[n("div",{staticClass:"border",class:{"border-danger":t.selected},on:{click:function(n){return e.imgSelected(t)}}},[t.selected?n("span",{staticClass:"badge badge-danger position-absolute",staticStyle:{top:"0",right:"0","z-index":"1"}},[e._v("\n                "+e._s(t.selectOrder)+"\n              ")]):e._e(),e._v(" "),n("div",{staticClass:"demo-image__preview w-100",on:{click:function(e){e.stopPropagation()}}},[n("el-image",{staticStyle:{height:"100px"},attrs:{src:t.url,"preview-src-list":t.srcList,fit:"fill",alt:"点击预览图片"}})],1),e._v(" "),n("div",{staticClass:"w-100 mt-n4 text-white position-absolute p-1",staticStyle:{background:"rgba(0,0,0,0.5)"}},[n("span",[e._v(e._s(t.name))])]),e._v(" "),n("div",{staticClass:"p-2 text-center"},[n("el-button-group",[n("el-button",{staticClass:"p-2",attrs:{icon:"el-icon-edit",size:"mini"},on:{click:function(n){return n.stopPropagation(),e.editImage(t,o)}}}),e._v(" "),n("el-button",{staticClass:"p-2",attrs:{icon:"el-icon-delete",size:"mini"},on:{click:function(t){return t.stopPropagation(),e.delImage(o)}}})],1)],1)])])],1)})),1)],1)],1),e._v(" "),n("el-dialog",{attrs:{title:e.editFormTitle,visible:e.dialogVisible,width:"30%"},on:{"update:visible":function(t){e.dialogVisible=t}}},[n("el-form",{ref:"editForm",attrs:{model:e.editForm,"label-width":"80px"}},[n("el-form-item",{attrs:{label:"名称"}},[n("el-input",{attrs:{size:"medium",placeholder:"请输入相册名称"},model:{value:e.editForm.name,callback:function(t){e.$set(e.editForm,"name",t)},expression:"editForm.name"}})],1),e._v(" "),n("el-form-item",{attrs:{label:"排序"}},[n("el-input-number",{attrs:{min:0,size:"small"},model:{value:e.editForm.order,callback:function(t){e.$set(e.editForm,"order",t)},expression:"editForm.order"}})],1)],1),e._v(" "),n("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:function(t){e.dialogVisible=!1}}},[e._v("取 消")]),e._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:e.confirmEdit}},[e._v("确 定")])],1)],1),e._v(" "),n("el-dialog",{attrs:{title:"上传图片",visible:e.uploadDialogVisible,width:"30%"},on:{"update:visible":function(t){e.uploadDialogVisible=t}}},[n("div",{staticClass:"text-center"},[n("el-upload",{staticClass:"upload-demo",attrs:{drag:"",action:"https://jsonplaceholder.typicode.com/posts/",multiple:""}},[n("i",{staticClass:"el-icon-upload"}),e._v(" "),n("div",{staticClass:"el-upload__text"},[e._v("\n          将文件拖到此处，或"),n("em",[e._v("点击上传")])]),e._v(" "),n("div",{staticClass:"el-upload__tip",attrs:{slot:"tip"},slot:"tip"},[e._v("\n          只能上传jpg/png文件，且不超过500kb\n        ")])])],1)]),e._v(" "),n("el-footer",{staticClass:"border-top ml-3 d-flex align-items-center px-0"},[n("div",{staticClass:"h-100 d-flex align-items-center justify-content-center flex-shrink-0 border-right",staticStyle:{width:"183px"}},[n("el-button-group",[n("el-button",{attrs:{icon:"el-icon-arrow-left",size:"mini"}},[e._v("\n          上一页\n        ")]),e._v(" "),n("el-button",{attrs:{size:"mini"}},[e._v("\n          下一页"),n("i",{staticClass:"el-icon-arrow-right el-icon--right"})])],1)],1),e._v(" "),n("div",{staticClass:"flex-grow-1 px-2"},[n("el-pagination",{attrs:{"current-page":e.currentPage,"page-sizes":[100,200,300,400],"page-size":100,layout:"total, sizes, prev, pager, next, jumper",total:400},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}})],1)])],1)}),[],!1,null,"2ab19c4d",null);t.default=component.exports}}]);