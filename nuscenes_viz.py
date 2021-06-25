import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import numpy as np
import random
import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')

from ui.ui_form_v2 import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from utils.nuscenes import *
from numba import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        

class Form(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)
        self.datset_path = ''
        self.load_dataset_button.clicked.connect(self._load_dataset)
        self.nusc_viz_button.clicked.connect(self._show_dataset)

    def _load_dataset(self):
        '''
            1号按钮：加载数据集路径
        '''
        self.dataset_path = QFileDialog.getExistingDirectory(self, "选取数据集文件夹", "./")
        self.nusc = NuScenes(dataroot=self.dataset_path)

    @jit
    def _show_dataset(self):
        '''
            同步显示1-4号窗口
        '''
        scene_rec = self.nusc.get('scene', 'c5224b9b454b4ded9b5d2d2634bbda8a')
        sample_rec = self.nusc.get('sample', scene_rec['first_sample_token'])
        sd_rec_rgb = self.nusc.get('sample_data', sample_rec['data']['CAM_FRONT'])
        sd_rec_camera = self.nusc.get('sample_data', sample_rec['data']['CAM_FRONT'])
        sd_rec_lidar = self.nusc.get('sample_data', sample_rec['data']['LIDAR_TOP'])
        sd_rec_radar = self.nusc.get('sample_data', sample_rec['data']['RADAR_FRONT'])

        has_more_rgb, has_more_camera, has_more_lidar, has_more_radar = True, True, True, True
        while has_more_rgb and has_more_camera and has_more_lidar and has_more_radar:
            t0 = time.time()

            sd_rec_rgb, has_more_rgb = self._show_rgb(sd_rec_rgb) 
            sd_rec_camera, has_more_camera = self._show_camera(sd_rec_camera)
            sd_rec_lidar, has_more_lidar = self._show_lidar(sd_rec_lidar)
            sd_rec_radar, has_more_radar = self._show_radar(sd_rec_radar)

            QApplication.processEvents()

            t1 = time.time()
            print('time {0}'.format(t1-t0))
        
        msgbox = QMessageBox()
        msgbox.setWindowTitle('INFO')
        msgbox.setText('Thanks for your watching!')
        msgbox.exec()

    def _show_rgb(self, sd_rec_rgb):
        '''
            1号窗口：动态显示RGB原图像
        '''
        sd_rec_rgb, img, has_more_rgb = self.nusc.render_camera_channel(sd_rec_rgb, 
                                                                                                                                        with_annos=False)
        img_width, img_height = self.rgb_label.width(), self.rgb_label.height()
        qimg = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg).scaled(img_width, img_height)
        self.rgb_label.setPixmap(pixmap)

        return sd_rec_rgb, has_more_rgb

    def _show_camera(self, sd_rec_camera):
        '''
            2号窗口：动态显示含GT框的camera输出
        '''
        sd_rec_camera, img, has_more_camera = self.nusc.render_camera_channel(sd_rec_camera, 
                                                                                                                                                                    with_annos=True)
        img_width, img_height = self.camera_label.width(), self.camera_label.height()
        qimg = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg).scaled(img_width, img_height)
        self.camera_label.setPixmap(pixmap)

        return sd_rec_camera, has_more_camera

    @jit
    def _show_lidar(self, sd_rec_lidar):
        '''
            3号窗口：动态显示含GT框的lidar输出
        '''
        self.lidar_figure.clear()
        ax = self.lidar_figure.add_subplot(111)
        sd_rec_lidar, has_more_lidar = self.nusc.render_pc_channel(sd_rec_lidar,
                                                                                                    ax=ax, 
                                                                                                    underlay_map=True,
                                                                                                    with_anns=True,
                                                                                                    use_flat_vehicle_coordinates=True)
        self.lidar_canvas.draw()

        return sd_rec_lidar, has_more_lidar

    @jit
    def _show_radar(self, sd_rec_radar):
        '''
            4号窗口：动态显示含GT框的radar输出
        '''
        self.radar_figure.clear()
        ax = self.radar_figure.add_subplot(111)
        sd_rec_radar, has_more_radar = self.nusc.render_pc_channel(sd_rec_radar, 
                                                                                                    channel='RADAR_FRONT',
                                                                                                    ax=ax,
                                                                                                    underlay_map=True,
                                                                                                    with_anns=True,
                                                                                                    use_flat_vehicle_coordinates=True)
        self.radar_canvas.draw()

        return sd_rec_radar, has_more_radar


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ui = Form()
    ui.show()
    sys.exit(app.exec_())
