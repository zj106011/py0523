# VUE

### 什么是vue.js?

作者:尤雨溪   (Angular 团队工作)

- Vue是目前最火的一款前端框架(weex也是用于APP开发,IOS结合web=webview);
- React是目前最流行的前端框架(React拥有成熟的APP开发机制);
- Angular 是国外目前最流行的前端框架;



### 前端框架架构思想和后端框架架构思想?

- 前端:MVVM
- 后端:MVC (Python   MTV)

```MVC
MVC:model(数据模型) View(前端视图)  Ctrl(控制前后端关系的,控制器)

MVVM:model(数据连接) View(前端视图) viewmodel(控制前后端关系的,控制器)
```



### 为什么比较前沿的框架大家喜欢?

```
前沿的框架都是在老框架的基础上进行迭代.

现代的前沿框架, 提高了企业开发的效率,效率就是金钱.

学习前沿的框架,有竞争力
```

### 框架和库的区别

```
库:提供了一些小功能.jquery 由于偏底层,所以开发效率低.

框架:一套完整的前端解决方案,方方面面都很全. vue注重的是视图开发
```





### 1.Vue的插值表达式

###### 直接插值可能会出现闪动,vue.js的老版本出现的

```vue
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<link rel='stylesheet' href='bootstrap.css' />
		<script src="vue-2.6.10.js"></script>
	</head>
	<body>
		<div id='div1'>
			<table class="table table-striped" style='width:500px;margin: auto;'>
				<tr>
					<td>{{account}}</td>
					<td><input type='text' name='account' class='form-control' placeholder="邮箱/手机/账户"/></td>
				</tr>
				<tr>
					<td>{{pwd}}</td>
					<td><input type='password' name='pwd' class='form-control' placeholder="密码"/></td>
				</tr>
				<tr>
					<td><input type="submit" value='登录' class='btn btn-success'/></td>
					<td><input type="reset" value='重置' class='btn'/></td> 
				</tr>
			</table>
		</div>
		<script>
			//1.需要实例化
			//块状控制,盒子模型,一个实例化,可以控制一个盒子
			//MVVM 
			var vm = new Vue({
				//2.设置elments(绑定盒子模型)
				el:'#div1',
				//3.设置数据部分,data的值必须是一个object-json类型
				data:{
					account:'用户:',
					pwd:'密码:',
					submit_:'登录',
					reset_:'重置',
				},
			});
		</script>
	</body>
</html>
```

###### v-cloak,v-html,v-text

```
v-cloak解决闪动
```

```vue
<td v-cloak>{{account}}</td>

<td v-text='account'></td>

<td v-html='pwd'></td>
```

### 3.vue设置函数

```vue
//vue设置函数在methods中设置
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<link rel='stylesheet' href='bootstrap.css' />
		<script src="vue-2.6.10.js"></script>
		<style>
			p {
				border-top:2px solid red;
				border-bottom:2px solid gray;
				border-left:2px solid greenyellow;
				border-right:2px solid orange;
			}
		</style>
	</head>
	<body>
		<div id='div1' style='margin: auto;width:500px;'>
            <!--v-on:click  =  @:click-->
			<p v-on:mousemove="lang()" v-on:mouseout="stop()">{{msg}}</p>
			<table class="table table-striped" style='width:500px;'>
				<tr>
					<td v-text='account'></td>
					<td><input type='text' name='account' class='form-control' placeholder="邮箱/手机/账户"/></td>
				</tr>
				<tr>
					<td v-html='pwd'></td>
					<td><input type='password' name='pwd' class='form-control' placeholder="密码"/></td>
				</tr>
				<tr>
					<td><input type="submit" value='登录' class='btn btn-success'/></td>
					<td><input type="reset" value='重置' class='btn'/></td> 
				</tr>
			</table>
		</div>
		<script>
			//1.需要实例化
			//块状控制,盒子模型,一个实例化,可以控制一个盒子
			//MVVM 
			var vm = new Vue({
				//2.设置elments(绑定盒子模型)
				el:'#div1',
				//3.设置数据部分,data的值必须是一个object-json类型
				data:{
					account:'用户:',
					pwd:'<b>密码:</b>',
					submit_:'登录',
					reset_:'重置',
					msg:'王宝强和好兄弟贾乃亮天生一对!王宝强和好兄弟贾乃亮天生一对!',
					intervalId:null,
				},
				//4.函数的定义
				methods:{
					lang(){
						//滚动条
						//this就是Vue对象
						//()=>{} 这样的话this返回的是vue对象
						//function(){}返回的window
						
						//if下面有且只有一行代码的时候{}可以不用写
						if(this.intervalId!=null) return
		
						this.intervalId = window.setInterval(()=>{
//							this = vue
							var head = this.msg.substring(0,1);
							var body = this.msg.substring(1);
							this.msg = body+head;
						},100);
//						window.setInterval(function(){
//							//this=window
//							var head = this.vm.msg.substring(0,1);
//							var body = this.vm.msg.substring(1);
//							this.vm.msg = body+head;
//						},100);
//							
					},
					stop(){
						//clearInterval()
						clearInterval(this.intervalId);
						this.intervalId=null;
					},
				},
			});
		</script>
	</body>
</html>

```

#### 4.vue中的v-bind,v-model

```vue
v-bind 单向绑定,MVVM,将M层自动绑定到V,在input中使用,value中使用{{}}不合适

v-model 双向绑定,将M层自动绑定到V,也可以将V的值绑定到M上.
```

```vue
#{{}}插值表达式在 value中是无效的
```

### 5.事件修饰符

```javascript
1.  `.stop` 阻止事件冒泡(v-on:click.stop)
#btn在inner内部

2.`.prevent` 阻止默认行为 
#a当中有一个href,会实现跳转,组织以后,跳转就失效了

3.`.capture`事件捕获
#添加了.captrue的元素会被优先执行,如果全部都加上了,安照冒泡事件的反顺序执行(从外到内)

4.`.self` 点击到自己,才会触发
#.stop在指定成级上终止冒泡,.self当前标签不参加冒泡

5. `once` 事件触发一次以后,自动解除绑定
```

### 6.案例:简单计算器

```html

```

### 7.vue中的class样式

```html

```

### 8.css样式

```html

```

### 9.v-for循环

```html

```

### 10.v-for中的key属性

```html

```

#### 11.v-if & v-show

```html

```

### 12.案例:简易后台页面

```html


```

### 13.vue远程请求

```html


```





























