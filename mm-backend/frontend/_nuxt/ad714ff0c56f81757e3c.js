(window.webpackJsonp=window.webpackJsonp||[]).push([[16],{926:function(e,t,l){"use strict";l.r(t);var r={name:"Service",data:function(){return{searchForm:{keyword:"",time:""},tableData:[],multipleSelection:[]}},methods:{handleSelectionChange:function(e){this.multipleSelection=e}}},n=l(32),component=Object(n.a)(r,(function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("div",{staticClass:"px-1"},[l("div",{staticClass:"d-flex justify-content-end align-items-cneter border-top border-bottom py-2 mb-3"},[l("el-date-picker",{attrs:{type:"daterange",size:"mini","range-separator":"至","start-placeholder":"开始日期","end-placeholder":"结束日期"},model:{value:e.searchForm.time,callback:function(t){e.$set(e.searchForm,"time",t)},expression:"searchForm.time"}}),e._v(" "),l("el-input",{staticClass:"w-25 mx-2",attrs:{size:"mini",placeholder:"请输入关键字"},model:{value:e.searchForm.keyword,callback:function(t){e.$set(e.searchForm,"keyword",t)},expression:"searchForm.keyword"}}),e._v(" "),l("el-button",{attrs:{type:"info",size:"mini"}},[e._v("搜索")])],1),e._v(" "),l("el-table",{ref:"multipleTable",staticStyle:{width:"100%"},attrs:{border:"",data:e.tableData,"tooltip-effect":"dark"},on:{"selection-change":e.handleSelectionChange}},[l("el-table-column",{attrs:{type:"selection",width:"55",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"orderId",label:"商品信息",width:"120",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"userName",label:"商品清单",width:"120",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"订单金额",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"收货信息",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"买家",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"交易状态"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"创建时间"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"操作"}})],1)],1)}),[],!1,null,"81eb7f88",null);t.default=component.exports}}]);