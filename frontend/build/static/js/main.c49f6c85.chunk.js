(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{39:function(e,t,c){},69:function(e,t,c){"use strict";c.r(t);c(38),c(39);var a,s=c(0),n=c(34),o=c.n(n),l=c(10),i=c(13),r=c(3),d=c(9),j=c.n(d),m=c(14),b=function e(){Object(m.a)(this,e),this.id=0,this.peso=0,this.data_nascimento="",this.nome="",this.tipo=""},h=function e(){Object(m.a)(this,e),this.content=void 0,this.page_number=0,this.page_size=0},u=c(71),O=function(e,t){var c=new Date(e),a=new Date(c.valueOf()+60*c.getTimezoneOffset()*1e3);return Object(u.a)(a,t)},x=c(1),f=function(e){return Object(x.jsx)("button",{className:e.className,onClick:e.onClick,children:e.children})},p=function(e){e.className;var t,c=e.page,a=e.changePage,n=(e.reloadFormPage,e.setReloadFormPage),o=Object(r.f)();Object(s.useEffect)((function(){a()}),[]);return Object(x.jsx)("div",{className:"table-responsive",children:Object(x.jsxs)("table",{className:"table table-striped table-sm table-dark",children:[Object(x.jsx)("thead",{children:Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:"Data de Nascimento"}),Object(x.jsx)("td",{children:"Nome"}),Object(x.jsx)("td",{children:"Tipo"}),Object(x.jsx)("td",{children:"Peso"}),Object(x.jsx)("td",{children:"Alterar"}),Object(x.jsx)("td",{children:"Excluir"})]})}),Object(x.jsx)("tbody",{children:null===(t=c.content)||void 0===t?void 0:t.map((function(e){return Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:O(e.data_nascimento,"dd/MM/yyyy")}),Object(x.jsx)("td",{children:e.nome}),Object(x.jsx)("td",{children:e.tipo}),Object(x.jsx)("td",{children:e.peso}),Object(x.jsx)("td",{children:Object(x.jsx)(f,{className:"btn-primary btn",onClick:function(){var t;t=e.id,j.a.get("/animal/".concat(t)).then((function(e){n(e.data),o.push("new-animal")}))},children:"Alterar"})}),Object(x.jsx)("td",{children:Object(x.jsx)(f,{className:"btn-danger btn",onClick:function(){var t;t=e.id,j.a.delete("/animal/".concat(t)).then((function(e){a()}))},children:"Excluir"})})]},e.id)}))})]})})},g=function(e){var t=e.reloadFormPage,c=e.setReloadFormPage,a=Object(s.useState)(!1),n=Object(l.a)(a,2),o=n[0],r=n[1],d=Object(s.useState)(new h),m=Object(l.a)(d,2),b=m[0],u=m[1];return Object(s.useEffect)((function(){j.a.get("/animal/").then((function(e){u(e.data)})).catch((function(e){console.log(e)}))}),[o]),Object(x.jsxs)("div",{className:"container",children:[Object(x.jsx)("div",{className:"row mt-5",children:Object(x.jsx)("div",{className:"col",children:Object(x.jsx)(i.b,{to:"/new-animal",className:"btn-primary btn",children:"Novo Animal"})})}),Object(x.jsx)("div",{className:"row mt-4",children:Object(x.jsx)(p,{className:"col-4",reloadFormPage:t,setReloadFormPage:c,page:b,changePage:function(){r(!o)}})})]})},N=c(11),v=c(19),y=c(37),P=function(e){var t=e.className,c=e.reloadFormPage,a=e.setReloadFormPage,n=Object(v.b)({mode:"onBlur"}),o=n.register,l=n.handleSubmit,i=n.formState.errors,d=n.setValue,m=(n.reset,Object(r.f)());Object(s.useEffect)((function(){d("id",c.id,{shouldDirty:!0}),d("nome",c.nome,{shouldDirty:!0}),d("tipo",c.tipo,{shouldDirty:!0}),d("peso",0!==c.peso?c.peso:"",{shouldDirty:!0});var e=""!==c.data_nascimento?O(c.data_nascimento,"dd/MM/yyyy"):"";d("data_nascimento",e,{shouldDirty:!0})}),[c]);return Object(x.jsx)("div",{className:t,children:Object(x.jsxs)("form",{onSubmit:l((function(e){var t=e.id;delete e.id,0!==t?j.a.put("/animal/".concat(t),e).then((function(e){console.log(e)})).catch((function(e){console.log(e)})).finally((function(){m.push("/")})):j.a.post("/animal/",e).then((function(e){console.log(e)})).catch((function(e){console.log(e)})).finally((function(){m.push("/")}))})),className:"container w-50",children:[Object(x.jsx)(y.a,{errors:i,name:"singleErrorInput"}),Object(x.jsx)("div",{className:"jumbotron p-5 bg-dark",children:Object(x.jsx)("div",{className:"row justify-content-md-center",children:Object(x.jsxs)("div",{className:"col-12 offset-6",children:[Object(x.jsx)("div",{className:"invisible",children:Object(x.jsx)("input",Object(N.a)(Object(N.a)({id:"id"},o("id")),{},{type:"text"}))}),Object(x.jsxs)("div",{className:"form-group row g-3 align-items-center",children:[Object(x.jsx)("label",{for:"Nome",className:"col-sm-2 mt-4 col-form-label",children:"Nome"}),Object(x.jsx)("div",{className:"col-auto",children:Object(x.jsx)("input",Object(N.a)(Object(N.a)({},o("nome",{required:!0,maxLength:20})),{},{type:"text",id:"nome",className:"form-control","aria-describedby":"Nome"}))})]}),Object(x.jsxs)("div",{className:"form-group row g-3 align-items-center",children:[Object(x.jsx)("div",{className:"col-sm-2 col-form-label",children:Object(x.jsx)("label",{for:"Tipo",className:"col-sm-2  mt-4 col-form-label",children:"Tipo"})}),Object(x.jsx)("div",{className:"col-auto",children:Object(x.jsxs)("select",Object(N.a)(Object(N.a)({id:"tipo"},o("tipo",{required:!0})),{},{className:"form-select","aria-label":"Tipo",children:[Object(x.jsx)("option",{selected:!0}),Object(x.jsx)("option",{value:"cachorro",children:"Cachorro"}),Object(x.jsx)("option",{value:"gato",children:"Gato"}),Object(x.jsx)("option",{value:"papagaio",children:"Papagaio"}),Object(x.jsx)("option",{value:"hamster",children:"hamster"})]}))})]}),Object(x.jsxs)("div",{className:"form-group row g-3 align-items-center",children:[Object(x.jsx)("div",{className:"col-sm-2 col-form-label",children:Object(x.jsx)("label",{for:"Peso",className:"col-form-label",children:"Peso"})}),Object(x.jsx)("div",{className:"col-auto",children:Object(x.jsx)("input",Object(N.a)(Object(N.a)({},o("peso",{required:!0})),{},{type:"text",id:"peso",className:"form-control","aria-describedby":"Peso"}))})]}),Object(x.jsxs)("div",{className:"form-group row g-3 align-items-center",children:[Object(x.jsx)("div",{className:"col-sm-2 col-form-label",children:Object(x.jsx)("label",{for:"data_nascimento",className:"col-form-label",children:"Data de Nascimento"})}),Object(x.jsx)("div",{className:"col-auto",children:Object(x.jsx)("input",Object(N.a)(Object(N.a)({placeholder:"ex: dd/mm/yyyy"},o("data_nascimento",{required:!0,pattern:"/^d{2}/d{2}/d{4}$/"})),{},{type:"text",id:"data_nascimento",className:"form-control","aria-describedby":"Data"}))})]}),Object(x.jsxs)("div",{className:"form-group row g-3 align-items-center",children:[Object(x.jsx)("div",{className:"col-sm-2 col-form-label",children:Object(x.jsx)("input",{type:"button",className:"btn-danger btn form-control",value:"Cancelar",onClick:function(){a(new b),m.push("/")}})}),Object(x.jsx)("div",{className:"col-sm-2",children:Object(x.jsx)("input",{type:"submit",className:"btn-primary btn form-control",value:"Salvar"})})]})]})})})]})})},w=function(e){return Object(x.jsx)(P,{className:"mt-5",reloadFormPage:e.reloadFormPage,setReloadFormPage:e.setReloadFormPage})},F=function(){var e=Object(s.useState)(new b),t=Object(l.a)(e,2),c=t[0],a=t[1];return Object(x.jsx)(i.a,{children:Object(x.jsxs)(r.c,{children:[Object(x.jsx)(r.a,{path:"/",exact:!0,children:Object(x.jsx)(g,{reloadFormPage:c,setReloadFormPage:a})}),Object(x.jsx)(r.a,{path:"/new-animal",exact:!0,children:Object(x.jsx)(w,{reloadFormPage:c,setReloadFormPage:a})})]})})},k=function(){return Object(x.jsx)(i.a,{children:Object(x.jsx)(F,{})})},D=null!==(a="https://leomath-animal-crud.herokuapp.com/")?a:"http://localhost:5000";j.a.defaults.baseURL=D,j.a.defaults.headers.post["Content-Type"]="application/x-www-form-urlencoded",o.a.render(Object(x.jsx)(k,{}),document.getElementById("root"))}},[[69,1,2]]]);
//# sourceMappingURL=main.c49f6c85.chunk.js.map