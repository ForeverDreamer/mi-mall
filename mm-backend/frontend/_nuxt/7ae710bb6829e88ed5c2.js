(window.webpackJsonp=window.webpackJsonp||[]).push([[12],{860:function(e,t,r){"use strict";var o={name:"ButtonSearch",props:{placeholder:{type:String,default:""}},data:function(){return{keyword:"",advanceSearch:!1}},methods:{closeAdvanceSearch:function(){this.advanceSearch=!1}}},l=r(32),component=Object(l.a)(o,(function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("div",{staticClass:"d-flex align-items-cneter border-top border-bottom py-2 mb-3"},[e._t("left"),e._v(" "),e._t("right",[r("div",{directives:[{name:"show",rawName:"v-show",value:!e.advanceSearch,expression:"!advanceSearch"}],staticClass:"ml-auto"},[r("div",{staticClass:"d-flex align-items-cneter ml-auto"},[r("el-input",{staticClass:"mr-2",attrs:{placeholder:e.placeholder,size:"mini"},model:{value:e.keyword,callback:function(t){e.keyword=t},expression:"keyword"}}),e._v(" "),r("el-button",{attrs:{type:"info",size:"mini"},on:{click:function(t){return e.$emit("search",e.keyword)}}},[e._v("搜索")]),e._v(" "),r("el-button",{attrs:{size:"mini"},on:{click:function(t){e.advanceSearch=!0}}},[e._v("高级搜索")])],1)])])],2),e._v(" "),r("el-card",{directives:[{name:"show",rawName:"v-show",value:e.advanceSearch,expression:"advanceSearch"}],staticClass:"my-3"},[r("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[r("span",[e._v("高级搜索")]),e._v(" "),r("el-button",{staticStyle:{float:"right",padding:"3px 0"},attrs:{type:"text"},on:{click:e.closeAdvanceSearch}},[e._v("\n        收起\n      ")])],1),e._v(" "),e._t("searchForm")],2)],1)}),[],!1,null,"95cf784e",null);t.a=component.exports},864:function(e,t,r){var content=r(882);"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,r(47).default)("9c54f0da",content,!0,{sourceMap:!1})},881:function(e,t,r){"use strict";var o=r(864);r.n(o).a},882:function(e,t,r){(t=r(46)(!1)).push([e.i,".el-footer[data-v-2c17c536]{position:fixed;bottom:0;left:200px;right:0;z-index:1}",""]),e.exports=t},937:function(e,t,r){"use strict";r.r(t);r(7),r(5),r(4),r(3),r(6);var o=r(0);function l(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(object);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,r)}return t}function n(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?l(Object(source),!0).forEach((function(t){Object(o.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):l(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}var c={name:"Index",inject:["app"],components:{ButtonSearch:r(860).a},data:function(){return{addMemberForm:{},addMemberDialogVisible:!1,searchForm:{},tableData:[],editIndex:-1}},created:function(){this.initData()},methods:{initData:function(){this.resetAddMemberForm(),this.resetSearchForm(),this.tableData={currentPage:1,members:[]},this.tableData.members.push({id:1,username:"用户名",headImage:"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3917638111,1851287468&fm=26&gp=0.jpg",registerTime:"2019-07-24 15:52:56",lastLoginTime:"2019-07-24 15:52:56",level:"普通用户",active:!0})},resetAddMemberForm:function(){this.addMemberForm={username:"",password:"",nickname:"",headImage:"",level:"",phone:"",email:"",gender:"",active:!0}},resetSearchForm:function(){this.searchForm={keyword:"",level:"",time:""}},addMember:function(){this.resetAddMemberForm(),this.addMemberDialogVisible=!0},editMember:function(e,t){this.addMemberForm=n({},t),this.editIndex=e,this.addMemberDialogVisible=!0},deleteMember:function(e){var t=this;this.$confirm("此操作将永久删除该会员，是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){t.tableData.members.splice(e,1),t.$message({type:"success",message:"删除成功!"})})).catch((function(){}))},search:function(){var param=arguments.length>0&&void 0!==arguments[0]?arguments[0]:null;"string"==typeof param?console.log("简单搜索!",param):console.log("高级搜索!",param),this.resetSearchForm()},clearAll:function(){console.log("clearAll!"),this.resetSearchForm(),this.$refs.buttonSearch.closeAdvanceSearch()},chooseImage:function(){var e=this;this.app.chooseImage((function(t){console.log("chooseImage",t[0].url),e.addMemberForm.headImage=t[0].url}))},close:function(){this.addMemberDialogVisible=!1,this.resetAddMemberForm()},confirm:function(){var e=this;this.$refs.addMemberForm.validate((function(t){if(t){var r="";if(-1===e.editIndex){r="添加";e.tableData.members.unshift(n({},{id:2,registerTime:"2019-07-24 15:52:56",lastLoginTime:"2019-07-24 15:52:56"},{},e.addMemberForm))}else{r="修改";var o=e.tableData.members[e.editIndex];o.username=e.addMemberForm.username,o.password=e.addMemberForm.password,o.nickname=e.addMemberForm.nickname,o.headImage=e.addMemberForm.headImage,o.level=e.addMemberForm.level,o.phone=e.addMemberForm.phone,o.email=e.addMemberForm.email,o.gender=e.addMemberForm.gender,o.active=e.addMemberForm.active,e.editIndex=-1}e.close(),e.$message({type:"success",message:"".concat(r,"成功")})}}))}}},m=(r(881),r(32)),component=Object(m.a)(c,(function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"px-1"},[r("button-search",{ref:"buttonSearch",attrs:{placeholder:"手机号/邮箱/会员昵称"},on:{search:e.search},scopedSlots:e._u([{key:"left",fn:function(){return[r("el-button",{attrs:{type:"success",size:"mini"},on:{click:e.addMember}},[e._v("添加会员")])]},proxy:!0},{key:"searchForm",fn:function(){return[r("el-form",{ref:"searchForm",attrs:{inline:!0,model:e.searchForm}},[r("el-form-item",{staticClass:"mb-0",attrs:{label:"搜索内容"}},[r("el-input",{attrs:{size:"mini",placeholder:"手机号/邮箱/会员昵称"},model:{value:e.searchForm.keyword,callback:function(t){e.$set(e.searchForm,"keyword",t)},expression:"searchForm.keyword"}})],1),e._v(" "),r("el-form-item",{staticClass:"mb-0",attrs:{label:"会员等级"}},[r("el-select",{attrs:{placeholder:"请选择会员等级",size:"mini"},model:{value:e.searchForm.level,callback:function(t){e.$set(e.searchForm,"level",t)},expression:"searchForm.level"}},[r("el-option",{attrs:{label:"等级1",value:"status1"}}),e._v(" "),r("el-option",{attrs:{label:"等级2",value:"status2"}})],1)],1),e._v(" "),r("el-form-item",{staticClass:"mb-0",attrs:{label:"注册时间"}},[r("el-date-picker",{attrs:{type:"daterange",size:"mini","range-separator":"至","start-placeholder":"开始日期","end-placeholder":"结束日期"},model:{value:e.searchForm.time,callback:function(t){e.$set(e.searchForm,"time",t)},expression:"searchForm.time"}})],1),e._v(" "),r("el-form-item",[r("el-button",{attrs:{type:"info",size:"mini"},on:{click:e.search}},[e._v("\n            搜索\n          ")]),e._v(" "),r("el-button",{attrs:{size:"mini"},on:{click:e.clearAll}},[e._v("\n            清空筛选条件\n          ")])],1)],1)]},proxy:!0}])}),e._v(" "),r("el-dialog",{attrs:{title:"添加会员",center:"",visible:e.addMemberDialogVisible,width:"40%"},on:{"update:visible":function(t){e.addMemberDialogVisible=t}}},[r("el-form",{ref:"addMemberForm",attrs:{model:e.addMemberForm,"label-width":"80px"}},[r("el-form-item",{attrs:{label:"用户名",prop:"username"}},[r("el-input",{staticClass:"w-25",attrs:{size:"mini"},model:{value:e.addMemberForm.username,callback:function(t){e.$set(e.addMemberForm,"username",t)},expression:"addMemberForm.username"}})],1),e._v(" "),r("el-form-item",{attrs:{label:"密码",prop:"password"}},[r("el-input",{staticClass:"w-25",attrs:{size:"mini"},model:{value:e.addMemberForm.password,callback:function(t){e.$set(e.addMemberForm,"password",t)},expression:"addMemberForm.password"}})],1),e._v(" "),r("el-form-item",{attrs:{label:"昵称",prop:"nickname"}},[r("el-input",{staticClass:"w-25",attrs:{size:"mini"},model:{value:e.addMemberForm.nickname,callback:function(t){e.$set(e.addMemberForm,"nickname",t)},expression:"addMemberForm.nickname"}})],1),e._v(" "),r("el-form-item",{attrs:{label:"头像"}},[e.addMemberForm.headImage?r("b-img",{attrs:{src:e.addMemberForm.headImage,width:"60",height:"60"},on:{click:e.chooseImage}}):r("span",{staticClass:"btn btn-light border p-1 mr-2",staticStyle:{"line-height":"1"},on:{click:e.chooseImage}},[r("i",{staticClass:"el-icon-plus p-2"})])],1),e._v(" "),r("el-form-item",{staticClass:"mb-0",attrs:{label:"等级"}},[r("el-select",{attrs:{size:"mini",placeholder:"请选择会员等级"},model:{value:e.searchForm.level,callback:function(t){e.$set(e.searchForm,"level",t)},expression:"searchForm.level"}},[r("el-option",{attrs:{label:"普通会员",value:"status1"}}),e._v(" "),r("el-option",{attrs:{label:"黄金会员",value:"status2"}})],1)],1),e._v(" "),r("el-form-item",{attrs:{label:"手机",prop:"phone"}},[r("el-input",{staticClass:"w-25",attrs:{size:"mini"},model:{value:e.addMemberForm.phone,callback:function(t){e.$set(e.addMemberForm,"phone",t)},expression:"addMemberForm.phone"}})],1),e._v(" "),r("el-form-item",{attrs:{label:"邮箱",prop:"email"}},[r("el-input",{staticClass:"w-25",attrs:{size:"mini"},model:{value:e.addMemberForm.email,callback:function(t){e.$set(e.addMemberForm,"email",t)},expression:"addMemberForm.email"}})],1),e._v(" "),r("el-form-item",{attrs:{label:"性别",prop:"gender"}},[r("el-radio-group",{attrs:{size:"mini"},model:{value:e.addMemberForm.gender,callback:function(t){e.$set(e.addMemberForm,"gender",t)},expression:"addMemberForm.gender"}},[r("el-radio-button",{attrs:{label:0,border:""}},[e._v("保密")]),e._v(" "),r("el-radio-button",{attrs:{label:1,border:""}},[e._v("男生")]),e._v(" "),r("el-radio-button",{attrs:{label:2,border:""}},[e._v("女生")])],1)],1),e._v(" "),r("el-form-item",{attrs:{label:"状态"}},[r("el-switch",{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},model:{value:e.addMemberForm.active,callback:function(t){e.$set(e.addMemberForm,"active",t)},expression:"addMemberForm.active"}})],1)],1),e._v(" "),r("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[r("el-button",{on:{click:e.close}},[e._v("取 消")]),e._v(" "),r("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.confirm(-1)}}},[e._v("确 定")])],1)],1),e._v(" "),r("el-table",{staticStyle:{width:"100%"},attrs:{border:"",data:e.tableData.members,"tooltip-effect":"dark"}},[r("el-table-column",{attrs:{label:"会员",width:"280"},scopedSlots:e._u([{key:"default",fn:function(t){return[r("b-media",{scopedSlots:e._u([{key:"aside",fn:function(){return[r("b-img",{attrs:{src:t.row.headImage,width:"60",height:"60",alt:"placeholder",rounded:"circle"}})]},proxy:!0}],null,!0)},[e._v(" "),r("div",[r("div",{staticClass:"d-flex"},[r("h6",{staticClass:"mr-auto"},[e._v(e._s(t.row.username))]),e._v(" "),r("el-button",{attrs:{type:"text",size:"mini"}},[e._v("详情")])],1),e._v(" "),r("p",[e._v("用户id: "+e._s(t.row.id))])])])]}}])}),e._v(" "),r("el-table-column",{attrs:{prop:"level",label:"会员等级",width:"120",align:"center"}}),e._v(" "),r("el-table-column",{attrs:{label:"登录/注册",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[r("p",[e._v("注册时间: "+e._s(t.row.registerTime))]),e._v(" "),r("div",[e._v("最后登录: "+e._s(t.row.lastLoginTime))])]}}])}),e._v(" "),r("el-table-column",{attrs:{label:"状态",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[r("el-switch",{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},model:{value:t.row.active,callback:function(r){e.$set(t.row,"active",r)},expression:"scope.row.active"}})]}}])}),e._v(" "),r("el-table-column",{attrs:{label:"操作",width:"150",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[r("el-button-group",[r("el-button",{attrs:{type:"text",size:"mini",plain:""},on:{click:function(r){return e.editMember(t.$index,t.row)}}},[e._v("修改")]),e._v(" "),r("el-button",{staticClass:"mx-1",attrs:{type:"text",size:"mini",plain:""}},[e._v("重置密码")]),e._v(" "),r("el-button",{attrs:{type:"text",size:"mini",plain:""},on:{click:function(r){return e.deleteMember(t.$index)}}},[e._v("删除")])],1)]}}])})],1),e._v(" "),r("div",{staticStyle:{height:"60px"}}),e._v(" "),r("el-footer",{staticClass:"border-top d-flex align-items-center px-0 bg-white"},[r("div",{staticClass:"flex-grow-1 px-2"},[r("el-pagination",{attrs:{"current-page":e.tableData.currentPage,"page-sizes":[100,200,300,400],"page-size":100,layout:"total, sizes, prev, pager, next, jumper",total:400}})],1)])],1)}),[],!1,null,"2c17c536",null);t.default=component.exports}}]);