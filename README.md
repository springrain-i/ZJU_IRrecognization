仓库还没有设立分支管理,等待后续完善
## 使用face_recognition库实现人脸识别
1. 请注意,此次修改了所有内容,使用train.py先提取人脸特征,再用face.py进行人脸识别(目前已实现多图片识别)
2. 还未对人脸识别的效率进行测试,参考仓库中有缩放图片的方法,可以尝试使用(经测试发现对精度有影响)
3. 如果精度有问题,可以将图片转换为灰度图后再进行训练
4. 图片命名格式请与Pictures中的保持一致
5. 环境配置:
`pip install dlib`
`pip install face_recognition`
`pip install json`

[参考仓库](https://github.com/ageitgey/face_recognition/tree/master)
<p align="right">by 时奇旭 2024.10.31</p>

---

## recognize-withDnn仓库

1. 由于我没有安装opencv而选择在vscode中实现，需要的opencv文件在文件夹"opencv_files"中，在vscode的terminal中安装所需的库即可，与初次的识别文件需要安装的库相同。
2. 同样，路径需要修改为本机对应路径。
3. 主要是在人脸检测功能上，替换原来的 `CascadeClassifier` 检测器为 OpenCV 的 DNN 模型，可以检测更复杂的场景。
4. 解决了虚空画框问题。同时经检测，可以较好地对多人视频进行检测画框。
5. 此外，可以尝试上传自己的照片进行训练，命名为仍为"nname"的格式，n表示训练图像的数字索引，同时上传视频进行测试。
需要改进的是人脸识别的精度，比如在test2.mp4雷军视频中仍有可能识别为索引为0的同学...以及数据集的构建。
<p align="right">by 肖惠文 2024.10.15</p>

---

## Recognization仓库
该人脸识别功能的实现使用的是opencv自带分类器与识别器,目前测试下人脸正对时识别率较高(仅训练的一张照片状况下的结果,后续如果使用该方法再进行完善,实现多张照片的训练以提高识别率)

环境配置
1. 官网安装opencv,`pip install opencv-python`,`pip install opencv-contrib-python` 三者缺一不可
2. 先在train.py中上传自己的图片,命名格式类似为`0name.jpg`(后续会完善),注意将文件中的路径修改为本机相对应得路径,训练好后会在trainer文件夹下生成`trainer.yml`文件
3. `recognize.py`中注意修改`VideoCapture`的来源,可以选择文件或者是实时摄像头,然后运行即可,如果是正确的就会有`wait to do`的字样

整体来说目前还是比较简陋的一个人脸识别功能,会出现虚空画框的情况
<p align="right">by 时奇旭 2024.10.12</p>

---