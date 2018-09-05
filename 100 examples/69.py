#---------------------------------------------------
#题目：用一个地图展示最热的几个城市的温度。
#2018-8-26
#---------------------------------------------------
import numpy as np
import pandas as pd
from pyecharts import Geo
value = [28,30,31,29,31.5,30,29,30.5,32,33]
attr = ['福州','重庆','海口','长沙','南昌','武汉','南宁','西安','广州','郑州']
geo = Geo('全国最热十个城市',width = 1200,height = 600)
geo.add('各城市温度',attr, value, type = 'effectScatter',border_color = '#ffffff',
        symbol_size = 20,is_label_show = True, label_text_color = '#00FF00', label_pos = 'inside',symbol = 'circle',
        symbol_color="#FF0000", geo_norma_color = '#006edd',geo_emphasis_color = '#0000ff')
geo.show_config()
geo.render('temperature.html')