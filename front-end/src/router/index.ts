import {createRouter,createWebHashHistory} from "vue-router"
const router = createRouter({
  //内部提供了history模式的实现。为了简单起见，我们在这里使用hash模式。
  history: createWebHashHistory(),
  routes:[
	 
	  {name:"homepage",path:"/",component:()=>import("../components/main.vue")},
	  

	
  ]
})
export default router

