(window.webpackJsonp=window.webpackJsonp||[]).push([[27],{920:function(t,e,r){"use strict";r.r(e);var n={name:"Transaction",data:function(){return{tabs:[{name:"支付设置"},{name:"购物设置"}],activeTabIndex:0,payments:[],orderForm:{},editIndex:-1}},created:function(){this.initData()},methods:{initData:function(){this.payments=[{name:"支付宝支付",key:"alipay",desc:"该系统支持即时到账接口",src:"http://wxcs.niuteam.cn/addons/NsAlipay/ico.png"},{name:"微信支付",key:"wxpay",desc:"该系统支持微信网页支付和扫码支付",src:"http://wxcs.niuteam.cn/addons/NsWeixinpay/ico.png"}],this.orderForm={closeDays:1,confirmDays:10,afterSaleDays:30,transportCosts:""}},handleClick:function(t,e){console.log(this.activeTabIndex)},config:function(t,e){}}},l=r(32),component=Object(l.a)(n,(function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"px-1"},[r("el-tabs",{on:{"tab-click":t.handleClick},model:{value:t.activeTabIndex,callback:function(e){t.activeTabIndex=e},expression:"activeTabIndex"}},t._l(t.tabs,(function(e,n){return r("el-tab-pane",{key:n,attrs:{label:e.name}},["0"===t.activeTabIndex?[r("el-table",{staticStyle:{width:"100%"},attrs:{border:"",data:t.payments,"tooltip-effect":"dark"}},[r("el-table-column",{attrs:{label:"支付方式"},scopedSlots:t._u([{key:"default",fn:function(e){return[r("div",{staticClass:"d-flex align-items=center"},[r("b-img",{attrs:{src:e.row.src,width:"40",height:"40"}}),t._v(" "),r("div",{staticClass:"ml-2"},[r("h6",{staticClass:"text-left mb-0"},[t._v(t._s(e.row.name))]),t._v(" "),r("small",{staticClass:"text-secondary d-block"},[t._v(t._s(e.row.desc))])])],1)]}}],null,!0)}),t._v(" "),r("el-table-column",{attrs:{label:"操作",width:"150",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[r("el-button",{attrs:{type:"text",size:"mini",plain:""},on:{click:function(r){return t.config(e.$index,e.row)}}},[t._v("\n                配置\n              ")])]}}],null,!0)})],1)]:[r("el-form",{ref:"orderForm",refInFor:!0,attrs:{model:t.orderForm,"label-width":"120px"}},[r("el-form-item",{attrs:{label:"未支付订单"}},[r("el-input",{staticClass:"w-25",attrs:{type:"number",size:"mini",min:0},model:{value:t.orderForm.closeDays,callback:function(e){t.$set(t.orderForm,"closeDays",e)},expression:"orderForm.closeDays"}},[r("template",{slot:"append"},[t._v("天后自动关闭")])],2),t._v(" "),r("p",{staticClass:"text-secondary"},[t._v("订单下达未付款，多少天后自动关闭，设置0天不自动关闭")])],1),t._v(" "),r("el-form-item",{attrs:{label:"已发货订单"}},[r("el-input",{staticClass:"w-25",attrs:{type:"number",size:"mini",min:0},model:{value:t.orderForm.confirmDays,callback:function(e){t.$set(t.orderForm,"confirmDays",e)},expression:"orderForm.confirmDays"}},[r("template",{slot:"append"},[t._v("天后自动确认收货")])],2),t._v(" "),r("p",{staticClass:"text-secondary"},[t._v("如果在期间未确认收货，系统自动完成收货，设置0天不自动收货")])],1),t._v(" "),r("el-form-item",{attrs:{label:"已完成订单"}},[r("el-input",{staticClass:"w-25",attrs:{size:"mini",min:0},model:{value:t.orderForm.afterSaleDays,callback:function(e){t.$set(t.orderForm,"afterSaleDays",e)},expression:"orderForm.afterSaleDays"}},[r("template",{slot:"append"},[t._v("天后允许申请售后")])],2),t._v(" "),r("p",{staticClass:"text-secondary"},[t._v("订单完成后，用户在多少天内可以发起售后申请，设置0天不允许申请售后")])],1),t._v(" "),r("el-form-item",{attrs:{label:"运费组合策略"}},[r("el-select",{attrs:{size:"mini",placeholder:"请选择组合策略"},model:{value:t.orderForm.transportCosts,callback:function(e){t.$set(t.orderForm,"transportCosts",e)},expression:"orderForm.transportCosts"}},[r("el-option",{attrs:{label:"普通会员",value:"status1"}}),t._v(" "),r("el-option",{attrs:{label:"黄金会员",value:"status2"}})],1)],1),t._v(" "),r("el-form-item",[r("el-button",{attrs:{type:"primary",size:"mini"}},[t._v("保存")])],1)],1)]],2)})),1)],1)}),[],!1,null,"5a6caac0",null);e.default=component.exports}}]);