from ui.ui_form import Ui_form
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from utils.nuscenes import *

import os 
import numpy as np
import random
import time


class Form(QWidget,Ui_form):

    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)
        self.sample = {}
        self.img_cache_path = ''
        self.rgb_button.clicked.connect(self._show_rgb)
        self.rgb_lidar_button.clicked.connect(self._show_rgb_lidar)
        self.rgb_radar_button.clicked.connect(self._show_rgb_radar)
        self.camera_button.clicked.connect(self._show_camera)
        self.lidar_button.clicked.connect(self._show_lidar)
        self.radar_button.clicked.connect(self._show_radar)

    def _show_rgb(self):
        '''
            1号窗口：显示原RGB图像
        '''
        data_path = QFileDialog.getExistingDirectory(self, "选取数据集文件夹", "./")
        self.img_cache_path = os.path.join(data_path, 'img_cache')        
        if not os.path.exists(self.img_cache_path):
            os.makedirs(self.img_cache_path)
        self._remove_img_cache(self.img_cache_path)

        self.nusc = NuScenes(dataroot=str(data_path))
        self.sample = self.nusc.sample[random.randint(1,400)]
        rgb_path = self.nusc.get_sample_data_path(self.sample['data']['CAM_FRONT'])
        img_width, img_height = self.rgb_label.width(), self.rgb_label.height()
        pixmap = QPixmap(rgb_path).scaled(img_width, img_height)
        self.rgb_label.setPixmap(pixmap)

    def _remove_img_cache(self, filepath):
        '''
            清空缓存文件夹中的所有文件
        '''
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def _show_rgb_lidar(self):
        '''
            2号窗口：显示Lidar点云投影后的RGB图像
        '''
        img_name = time.strftime('%H%M%S') + '.jpg'
        out_path = self.img_cache_path + '/' + img_name
        self.nusc.render_pointcloud_in_image(self.sample['token'],
                                                                                        pointsensor_channel='LIDAR_TOP',
                                                                                        camera_channel='CAM_FRONT',
                                                                                        render_intensity=True,
                                                                                        out_path=out_path,
                                                                                        verbose=False)

        img_width, img_height = self.rgb_lidar_label.width(), self.rgb_lidar_label.height()
        pixmap = QPixmap(out_path).scaled(img_width, img_height)
        self.rgb_lidar_label.setPixmap(pixmap)

    def _show_rgb_radar(self):
        '''
            3号窗口：显示Radar点云投影后的RGB图像
        '''
        img_name = time.strftime('%H%M%S') + '.jpg'
        out_path = self.img_cache_path + '/' + img_name
        self.nusc.render_pointcloud_in_image(self.sample['token'],
                                                                                        pointsensor_channel='RADAR_FRONT',
                                                                                        camera_channel='CAM_FRONT',
                                                                                        out_path=out_path,
                                                                                        verbose=False)
        
        img_width, img_height = self.rgb_radar_label.width(), self.rgb_radar_label.height()
        pixmap = QPixmap(out_path).scaled(img_width, img_height)
        self.rgb_radar_label.setPixmap(pixmap)

    def _show_camera(self):
        '''
            4号窗口：显示含GT框的Camera输出
        '''
        img_name = time.strftime('%H%M%S') + '.jpg'
        out_path = self.img_cache_path + '/' + img_name
        self.nusc.render_sample_data(self.sample['data']['CAM_FRONT'],
                                                                        out_path=out_path,
                                                                        verbose=False)
        
        img_width, img_height = self.camera_label.width(), self.camera_label.height()
        pixmap = QPixmap(out_path).scaled(img_width, img_height)
        self.camera_label.setPixmap(pixmap)

    def _show_lidar(self):
        '''
            5号窗口：显示含GT框的Lidar输出
        '''
        img_name = time.strftime('%H%M%S') + '.jpg'
        out_path = self.img_cache_path + '/' + img_name
        self.nusc.render_sample_data(self.sample['data']['LIDAR_TOP'],
                                                                        nsweeps=10,
                                                                        underlay_map=True,
                                                                        out_path=out_path,
                                                                        verbose=False)
        
        img_width, img_height = self.lidar_label.width(), self.lidar_label.height()
        pixmap = QPixmap(out_path).scaled(img_width, img_height)
        self.lidar_label.setPixmap(pixmap)

    def _show_radar(self):
        '''
            6号窗口：显示含GT框的Radar输出
        '''
        img_name = time.strftime('%H%M%S') + '.jpg'
        out_path = self.img_cache_path + '/' + img_name
        self.nusc.render_sample_data(self.sample['data']['RADAR_FRONT'],
                                                                        nsweeps=10,
                                                                        underlay_map=True,
                                                                        out_path=out_path,
                                                                        verbose=False)
        
        img_width, img_height = self.radar_label.width(), self.radar_label.height()
        pixmap = QPixmap(out_path).scaled(img_width, img_height)
        self.radar_label.setPixmap(pixmap)


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ui = Form()
    ui.show()
    sys.exit(app.exec_())

