(window.webpackJsonp=window.webpackJsonp||[]).push([[25],{919:function(e,t,n){"use strict";n.r(t);n(7),n(5),n(4),n(3),n(6);var l=n(0);function r(object,e){var t=Object.keys(object);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(object);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(object,e).enumerable}))),t.push.apply(t,n)}return t}function o(e){for(var i=1;i<arguments.length;i++){var source=null!=arguments[i]?arguments[i]:{};i%2?r(Object(source),!0).forEach((function(t){Object(l.a)(e,t,source[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(source)):r(Object(source)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(source,t))}))}return e}var c={name:"Shipping",filters:{formatChargeMode:function(e){return["按重量","按件数"][e]}},data:function(){return{tabs:[{name:"运费模板"},{name:"物流跟踪"}],activeTabIndex:0,form:{username:"",accessKey:""},addTemplateForm:{},addTemplateDialogVisible:!1,tableData:[],editIndex:-1}},created:function(){this.initData()},methods:{initData:function(){this.resetAddTemplateForm(),this.tableData={currentPage:1,templates:[]},this.tableData.templates.push({title:"全国统一邮费",chargeMode:0,order:100,createTime:"2019-7-23 18:25:27",active:!0})},resetAddTemplateForm:function(){this.addTemplateForm={title:"",chargeMode:"",order:0,active:!1}},handleClick:function(e,t){console.log(this.activeTabIndex)},addTemplate:function(){},editTemplate:function(e,t){this.addTemplateForm=o({},t),this.editIndex=e,this.addTemplateDialogVisible=!0},deleteTemplate:function(e){var t=this;this.$confirm("此操作将永久删除该模板，是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){t.tableData.templates.splice(e,1),t.$message({type:"success",message:"删除成功!"})})).catch((function(){}))},close:function(){this.addTemplateDialogVisible=!1,this.resetAddTemplateForm()},confirm:function(){var e=this;this.$refs.addLevelForm.validate((function(t){if(t){var n="";if(-1===e.editIndex)n="添加",e.tableData.levels.unshift(o({},e.addLevelForm));else{n="修改";var l=e.tableData.levels[e.editIndex];l.level=e.addLevelForm.level,l.active=e.addLevelForm.active,l.totalConsumption=e.addLevelForm.totalConsumption,l.times=e.addLevelForm.times,l.discount=e.addLevelForm.discount,e.editIndex=-1}e.close(),e.$message({type:"success",message:"".concat(n,"成功")})}}))},save:function(){}}},d=n(32),component=Object(d.a)(c,(function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"px-1"},[n("el-tabs",{on:{"tab-click":e.handleClick},model:{value:e.activeTabIndex,callback:function(t){e.activeTabIndex=t},expression:"activeTabIndex"}},e._l(e.tabs,(function(t,l){return n("el-tab-pane",{key:l,attrs:{label:t.name}},["0"===e.activeTabIndex?n("div",[n("div",{staticClass:"border-top border-bottom py-2 mb-3"},[n("el-button",{attrs:{type:"success",size:"mini"},on:{click:e.addTemplate}},[e._v("\n            添加模板\n          ")])],1),e._v(" "),n("el-table",{staticStyle:{width:"100%"},attrs:{border:"",data:e.tableData.templates,"tooltip-effect":"dark"}},[n("el-table-column",{attrs:{prop:"title",label:"模板名称",align:"center"}}),e._v(" "),n("el-table-column",{attrs:{label:"计费方式",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v("\n              "+e._s(e._f("formatChargeMode")(t.row.chargeMode))+"\n            ")]}}],null,!0)}),e._v(" "),n("el-table-column",{attrs:{prop:"order",label:"排序",width:"80",align:"center"}}),e._v(" "),n("el-table-column",{attrs:{prop:"createTime",label:"添加时间",align:"center"}}),e._v(" "),n("el-table-column",{attrs:{label:"状态",width:"80",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-switch",{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},model:{value:t.row.active,callback:function(n){e.$set(t.row,"active",n)},expression:"scope.row.active"}})]}}],null,!0)}),e._v(" "),n("el-table-column",{attrs:{label:"操作",width:"150",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-button",{attrs:{type:"text",size:"mini",plain:""},on:{click:function(n){return e.editTemplate(t.$index,t.row)}}},[e._v("\n                修改\n              ")]),e._v(" "),n("el-button",{attrs:{type:"text",size:"mini",plain:""},on:{click:function(n){return e.deleteTemplate(t.$index)}}},[e._v("\n                删除\n              ")])]}}],null,!0)})],1)],1):n("el-form",{ref:"form",refInFor:!0,attrs:{model:e.form,"label-width":"120px"}},[n("el-form-item",{attrs:{label:"快递100 用户名"}},[n("el-input",{staticClass:"w-25",attrs:{size:"mini"},model:{value:e.form.username,callback:function(t){e.$set(e.form,"username",t)},expression:"form.username"}}),e._v(" "),n("p",{staticClass:"text-secondary"},[e._v("用于查询物流信息， "),n("a",{attrs:{href:"https://www.kuaidi100.com/"}},[e._v("快递100申请")])])],1),e._v(" "),n("el-form-item",{attrs:{label:"快递100 密钥"}},[n("el-input",{staticClass:"w-25",attrs:{size:"mini"},model:{value:e.form.accessKey,callback:function(t){e.$set(e.form,"accessKey",t)},expression:"form.accessKey"}})],1),e._v(" "),n("el-form-item",[n("el-button",{attrs:{type:"primary",size:"mini"},on:{click:e.save}},[e._v("保存")])],1)],1)],1)})),1)],1)}),[],!1,null,"efea2022",null);t.default=component.exports}}]);