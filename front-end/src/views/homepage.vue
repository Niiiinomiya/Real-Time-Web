<template>
  <div v-loading="loading">
	  
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

    <el-button type="success" @click="generateVideo">生成视频</el-button>
    <el-button type="success" @click="getVideo">下载视频</el-button>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { VideoCameraFilled } from '@element-plus/icons-vue'
import { UploadFilled } from '@element-plus/icons-vue'
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'

const loading = ref(false)

const generateVideo = async () => {
  try {
	loading.value=true
    await axios.post('http://localhost:8080/generate-video')

	 loading.value=false
	  ElMessageBox.alert('视频生成成功，请点击下载按钮下载视频！', '生成视频', {
	     confirmButtonText: 'OK',
	     callback: (action: Action) => {
	       ElMessage({
	         type: 'info',
	         message: `action: ${action}`,
	       })
	     },
	   })
    console.log('Video generated successfully')
  } catch (error) {
    console.error('Error generating video:', error)
  }
}

const getVideo = async () => {
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
}
</script>