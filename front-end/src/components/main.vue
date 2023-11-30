<template>
	<div class="maincontent">
		<img class="bg" src="../assets/bg1.jpg" />
		<div>
			<img class="yidong" :style="{ left: `${x-550}px`, top: `${y}px` }" src="../assets/yidong.png" alt="Moving Image" />  
		</div>  
		<div v-if="!ifstart">
			<h1 class="title">文物复活计划</h1>
			<div class="wenwu">  
			   <img src="../assets/wenwu1.png" class="shape shake" @mouseover="showDialog1" /> 
			   <img src="../assets/wenwu2.png" class="shape shake" @mouseover="showDialog2"/> 
			</div>
			<div class="dialog-wrapper" >
				<div class="dialog-mask"></div>
				<div class="dialog-content">
					<p @mouseleave="hideDialog">{{dialogContent}}</p>
				</div>
			</div>
			<div class="btn" @click="startpro">
				现在开始
			</div>
		</div>
		<div v-if="ifstart">
			
			<div v-loading="loading">
				  <br /><br />
			  <el-upload
			    class="upload-demo"
			    drag
			    action="http://localhost:8080/uploadvideo"
			    multiple
			  >
			    <el-icon class="el-icon--upload"><video-camera-filled /></el-icon>
			    <div class="el-upload__text">
			      Drop video here or <em>click to upload</em>
			    </div>
			    <template #tip>
			      <div class="el-upload__tip">
			        mp4 files with a size less than 100MB
			      </div>
			    </template>
			  </el-upload>
			<br /><br />
			  <el-upload
			    class="upload-demo"
			    drag
			    action="http://localhost:8080/uploadimg"
			    multiple
			  >
			    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
			    <div class="el-upload__text">
			      Drop file here or <em>click to upload</em>
			    </div>
			    <template #tip>
			      <div class="el-upload__tip">
			        jpg/png files with a size less than 500kb
			      </div>
			    </template>
			  </el-upload>
		<br /><br />
			<button @click="generateVideo" class="bot1">生成视频</button>
			<button @click="getVideo" class="bot2">下载视频</button>
			</div>
		
						
	
	
			
			
			
			
			
			
			<div @click="back" class="btn">退出</div>
		</div>
	</div>
</template>

<script>

import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'


	export default {
	  data() {  
	    return {  
	      x: 0,  
	      y: 0,  
		  // dialogVisible:false,
		  ifstart:false,
		  selectedFile: null,
		  dialogContent:"让文物动起来...",
		  hasvideo:false,
		  ifclick:false,
	    };  
	  },  
	  mounted() {  
	    window.addEventListener("mousemove", this.handleMouseMove);  
	  },  
	  beforeDestroy() {  
	    window.removeEventListener("mousemove", this.handleMouseMove);  
	  },  
	  methods: {  
	  generateVideo: async function() {
		    try {
		      this.loading = true
		      await axios.post('http://localhost:8080/generate-video')
		
		      this.loading = false
		
		      ElMessageBox.alert('视频生成成功，请点击下载按钮下载视频！', '生成视频', {
		        confirmButtonText: 'OK',
		        callback: (action) => { // 删除类型注解
		          ElMessage({
		            type: 'info',
		            message: `action: ${action}`
		          })
		        }
		      })
		
		      console.log('Video generated successfully')
		    } catch (error) {
		      console.error('Error generating video:', error)
		    }
		  },
		  getVideo: async function() {
		    try {
		      const response = await axios.get('http://localhost:8080/getvideo', {
		        responseType: 'blob' // 设置响应类型为 blob
		      })
		
		      // 获取文件名
		      const dispositionHeader = response.headers['content-disposition']
		      const fileNameMatch = dispositionHeader ? dispositionHeader.match(/filename="(.+)"/) : null
		      const fileName = fileNameMatch ? fileNameMatch[1] : 'video.mp4'
		
		      // 创建 URL 对象
		      const url = window.URL.createObjectURL(new Blob([response.data]))
		
		      // 创建一个新的链接元素，并设置 download 属性
		      const link = document.createElement('a')
		      link.href = url
		      link.setAttribute('download', fileName)
		
		      // 模拟点击链接来触发下载
		      link.click()
		
		      console.log('Video downloaded successfully')
		    } catch (error) {
		      console.error('Error downloading video:', error)
		    }
		  },
	    handleMouseMove(event) {  
	      this.x = event.clientX;  
	      this.y = event.clientY;  
	    },
		showDialog1(){
			// this.dialogVisible=true;
			this.dialogContent="你想让古老的飞天壁画跟随你而动吗？你想让古画中的仕女对你展颜微笑吗？这款在线工具，可以让你和文物之间进行一场跨越千百年的对望...";
		},
		showDialog2(){
			// this.dialogVisible=true;
			this.dialogContent="点击在线开始，上传一张文物原图像（五官、姿态清晰），上传一段驱动视频，你将会看到文物如你所愿地动起来！";
		},
		hideDialog()
		{
			// this.dialogVisible=false;
			this.dialogContent="让文物动起来...";
		},
		startpro()
		{
			this.ifstart=true;
		},
		back()
		{
			this.ifstart=false;
		},
		handleFileUpload() {  
		    this.selectedFile = this.$refs.fileInput.files[0];  
		},
		submitFile() {  
		    const formData = new FormData();  
		    formData.append('file', this.selectedFile);  
		  
		    axios.post('/upload', formData)  
		      .then(response => {  
		        // 处理上传成功的响应  
		        console.log(response);  
		      })  
		      .catch(error => {  
		        // 处理上传失败的情况  
		        console.error(error);  
		      });  
		}, 
		startVideo()
		{
			this.ifclick=true;
		}
	  },  
	};  
</script>

<style scoped>
.bot1{
	position: relative;
	z-index: 1;
	right: 100;
	bottom: 100;
	background-image: url(../assets/btn.png);
	background-size: 100% 100%;
	background-position: center;

}
.bot2{
	position: relative;
	z-index: 1;
	right: 200;
	bottom: 200;
	background-image: url(../assets/btn.png);
	background-size: 100% 100%;
	background-position: center;

}
.upload-demo{
	width: 200px;
	height: 200px;
	margin-left: 100px;
	
}
.maincontent{
	position: absolute;  
	top: 0;  
	left: 550px;  
	width: 380px;
	height: 700px;
}

.bg{
	position: absolute;
	top: 0;
	left: 0;  
	width: 100%;
	height: 100%;
	z-index: 0;
}
.yidong {  
  position: absolute;  
  pointer-events: none;  
  width: 30px;
  height: 30px;
  z-index: 2;
}  
.title{
	position: relative;
	text-align: center;
	margin-top: 15%;
	color: #ae5643;
}
.smalltitle{
	position: relative;
	text-align: center;
	color: #ae5643;
}
.wenwu{
	position: absolute;
	width: 100%;
	top:0;
	left: 0;
	display: flex;  
	justify-content: space-between;
	align-items: flex-end;
}
.shape {
            width: 20%;
            height: 20%;
        }
        .shake:hover {
            animation: shake 800ms ease-in-out;
        }
        @keyframes shake { /* 水平抖动，核心代码 */
            10%, 90% { transform: translate3d(-1px, 0, 0); }
            20%, 80% { transform: translate3d(+2px, 0, 0); }
            30%, 70% { transform: translate3d(-4px, 0, 0); }
            40%, 60% { transform: translate3d(+4px, 0, 0); }
            50% { transform: translate3d(-4px, 0, 0); }
}
.btn{
	position: absolute;
	z-index: 1;
	right: 0;
	bottom: 0;
	margin: 5%;
	height: 5%;
	background-image: url(../assets/btn.png);
	background-size: 100% 100%;
	background-position: center;
	padding-top: 20px;
	padding-left: 20px;
	padding-right: 20px;
}
.dialog-wrapper{
	margin-top: 15%;
	margin-right: 5%;
	margin-left: 5%;
	position: relative;
	display: flex;
	justify-content: center;
	align-items: center;
}
.dialog-mask{
	position: relative;
	/* background-color: rgba(0,0,0,0.6); */
}
.dialog-content{
	/* background-color: white; */
	background-image: url(../assets/dialog.png);
	background-size: 100% 100%;
	opacity: 0.8;
	width: 400px;
	height: 250px;
	display: flex;  
	align-items: center;  
	justify-content: center;  
	/* border-radius: 4px; */
	/* box-shadow: 0 0 10px rgba(0,0,0,0.5); */
}
.dialog-content p{
	margin: 40px 40px;
	font-size: 20px;
}
.biaodan{
	position: relative;
	z-index: 1;
	text-align: center;
}
.biaodan button{
	font-size: 15px;
}
.question{
	position: relative;
	z-index: 1;
	font-size: 20px;
	left: 10px;
	color: #d9d1a8;
}
.showVideo{
	position: relative;
	top: 50px;
	width: 80%;
	left: 5%;
	padding: 10px 20px;
	z-index: 1;
	text-align: center;
	background-image: url(../assets/dialog.png);
	background-size: 100% 100%;
}
.showVideo p{
	margin: 10px auto;
	font-size: 20px;
	position: absolute;
	left: 50%;
	color: #f4e6db;
}
input{
	font-family: 'xingkai';
	font-size: 15px;
	color: #7c7b77;
}
.btnvideo{
	position: absolute;
	bottom: 0;
	left:0;
	width:320px;
	margin-left: 17px;
	margin-bottom: 15px;
	font-family: 'xingkai';
	background-color: #797774;
	border-radius: 5px;
	opacity: 0.8;
	height: 30px;
	font-size: 150%;
	color:#d9d1a8 ;
}
</style>
