仓库还没有设立分支管理,等待后续完善

## Recognization仓库
该人脸识别功能的实现使用的是opencv自带分类器与识别器,目前测试下人脸正对时识别率较高(仅训练的一张照片状况下的结果,后续如果使用该方法再进行完善,实现多张照片的训练以提高识别率)

环境配置
1. 官网安装opencv,`pip install opencv-python`,`pip install opencv-contrib-python` 三者缺一不可
2. 先在train.py中上传自己的图片,命名格式类似为`0name.jpg`(后续会完善),注意将文件中的路径修改为本机相对应得路径,训练好后会在trainer文件夹下生成`trainer.yml`文件
3. `recognize.py`中注意修改`VideoCapture`的来源,可以选择文件或者是实时摄像头,然后运行即可,如果是正确的就会有`wait to do`的字样

整体来说目前还是比较简陋的一个人脸识别功能,会出现虚空画框的情况

