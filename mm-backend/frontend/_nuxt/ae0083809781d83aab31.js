(window.webpackJsonp=window.webpackJsonp||[]).push([[15],{927:function(e,t,l){"use strict";l.r(t);var n={name:"Invoice",data:function(){return{searchForm:{keyword:"",time:""},tableData:[],multipleSelection:[]}},methods:{handleSelectionChange:function(e){this.multipleSelection=e}}},r=l(32),component=Object(r.a)(n,(function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("div",{staticClass:"px-1"},[l("div",{staticClass:"d-flex justify-content-end align-items-cneter border-top border-bottom py-2 mb-3"},[l("el-date-picker",{attrs:{type:"daterange",size:"mini","range-separator":"至","start-placeholder":"开始日期","end-placeholder":"结束日期"},model:{value:e.searchForm.time,callback:function(t){e.$set(e.searchForm,"time",t)},expression:"searchForm.time"}}),e._v(" "),l("el-input",{staticClass:"w-25 mx-2",attrs:{size:"mini",placeholder:"请输入关键字"},model:{value:e.searchForm.keyword,callback:function(t){e.$set(e.searchForm,"keyword",t)},expression:"searchForm.keyword"}}),e._v(" "),l("el-button",{attrs:{type:"info",size:"mini"}},[e._v("搜索")])],1),e._v(" "),l("el-table",{ref:"multipleTable",staticStyle:{width:"100%"},attrs:{border:"",data:e.tableData,"tooltip-effect":"dark"},on:{"selection-change":e.handleSelectionChange}},[l("el-table-column",{attrs:{type:"selection",width:"55",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"orderId",label:"订单编号",width:"120",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"userName",label:"用户名",width:"120",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"开票金额",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"抬头",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"发票内容",align:"center"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"纳税人识别号"}}),e._v(" "),l("el-table-column",{attrs:{prop:"amount",label:"操作"}})],1)],1)}),[],!1,null,"1e29605d",null);t.default=component.exports}}]);