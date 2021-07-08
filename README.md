Для Лёхи:
```python
import pyrealsense2 as rs
import open3d
import numpy as np


class OnlineFace:
    def __init__(self, distance_in_meters):
        self.flip_transform = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
        self.distance_in_meters = distance_in_meters

    def vis_point(self):
        ''' Начинаем работу с облаком точек '''
        align, pipeline = self.camera_config()

        try:
            ''' Врубаем все 3 объектива у камеры '''
            # ToDo вызывать ожидание 1 раз при запуске программы
            for i in range(25):
                frames = pipeline.wait_for_frames()
            aligned_frames = align.process(frames)

            aligned_depth_frame = aligned_frames.get_depth_frame()
            # color_frame = aligned_frames.get_color_frame()
            depth_frame = aligned_frames.get_depth_frame()
            intrinsic = open3d.camera.PinholeCameraIntrinsic(self.get_intrinsic_matrix(depth_frame))

            depth_image = open3d.geometry.Image(np.array(aligned_depth_frame.get_data()))
            # color_image = open3d.geometry.Image(np.asarray(color_frame.get_data()))

            ''' Соединяем данные от камеры с IK подсветкой с rgb камерой '''
            # rgbd_image = open3d.geometry.RGBDImage.create_from_color_and_depth(
            #     color_image, depth_image, depth_scale=1.0 / 0.001,
            #     depth_trunc=self.distance_in_meters, convert_rgb_to_intensity=False)

            dh_image = open3d.geometry.PointCloud.create_from_depth_image(
                depth_image, intrinsic, depth_scale=1.0 / 0.001, depth_trunc=self.distance_in_meters)
            dh_image.transform(self.flip_transform)

            # temp = open3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsic)
            # temp.transform(self.flip_transform)
            # open3d.visualization.draw_geometries([dh_image])

        finally:
            pipeline.stop()

        return dh_image.points, 0

    def camera_config(self):
        ''' Запускаем камеру '''
        pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.depth, rs.format.z16, 30)
        # config.enable_stream(rs.stream.color, rs.format.bgr8, 30)
        pipeline.start(config)
        align_to = rs.stream.color
        align = rs.align(align_to)
        return align, pipeline

    def get_intrinsic_matrix(self, frame):
        ''' Не помню зачем делал '''
        intrinsics = frame.profile.as_video_stream_profile().intrinsics
        out = open3d.camera.PinholeCameraIntrinsic(1280, 720, intrinsics.fx, intrinsics.fy, intrinsics.ppx, intrinsics.ppy)

        return out


if __name__ == '__main__':
    x = OnlineFace()
    x.vis_point()


```
Не для Лёхи.  
Get_PC_info.py - класс для получения информации о компьютере  
Пример вывода класса:
```text
Platform - Windows 
Platform release - 10 
Platform version - 10.0.19041 
Architecture - AMD64 
Hostname - PR41505 
Ip address - 192.168.56.1 
Mac address - 00:d8:61:4d:d2:94 
Processor - Intel64 Family 6 Model 158 Stepping 10, GenuineIntel 
Ram - 8 GB
```

OpenCL.py - класс для сравнения вычислительной мощность GPU и CPU  
Пример вывода класса:
```text
CPU Time: 49.049052 s
GPU Time: 0.00190783 s
GPU Kernel evaluation Time: 0.00014396 s
```

Find_Uniq.py - класс для сравнения того на сколько уникальны строки
Пример вывода класса:
```text
s1 = "ABCD ABCD"
s2 = "DCBA ABCD"
FuzzyWuzzy - 67%
Levenshtein - 92.5%
```

Сравнение нейронок 
![image](https://user-images.githubusercontent.com/57527303/118654149-eb247080-b7f0-11eb-84b7-6c5aade5d1b5.png)
