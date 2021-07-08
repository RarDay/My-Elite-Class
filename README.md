Для Лёхи:
```python
import realsense2 as rs

pipeline = rs.pipeline()  # Объект содержит методы для взаимодействия с потоком
config = rs.config()  # Дополнительный объект для хранения настроек потока
config.enable_stream(rs.stream.depth, rs.format.z16, 30)  # Включаем камеры глубины
# config.enable_stream(rs.stream.color, rs.format.bgr8, 30) # Включаем rgb камеру (пока не нужна) 
pipeline.start(config)
align_to = rs.stream.color
align = rs.align(align_to)

try:

    aligned_frames = align.process(frames)

    aligned_depth_frame = aligned_frames.get_depth_frame()
    depth_frame = aligned_frames.get_depth_frame()

    intrinsic = open3d.camera.PinholeCameraIntrinsic(self.get_intrinsic_matrix(depth_frame))
    depth_image = open3d.geometry.Image(np.array(aligned_depth_frame.get_data()))
    dh_image = open3d.geometry.PointCloud.create_from_depth_image(
        depth_image, intrinsic, depth_scale=1.0 / 0.001, depth_trunc=self.distance_in_meters)

    dh_image.transform(self.flip_transform)

finally:
    pipeline.stop()

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
