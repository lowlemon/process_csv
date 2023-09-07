import os
import csv
import datetime

w, h = 640, 480

title = ['图像编号', '调查桩号', '设施类型', '损坏类型', '计量单位', '长度m', '宽度m', '面积㎡', '形状描述', '图像坐标', '经纬编码', '病害存档时间']

# 定义要创建的CSV文件的文件名

file_path = 'path/to/file'

distress_dir = {'0': 'crack', '1': ''}
current_time = str(datetime.datetime.now())
files = os.listdir(file_path)
csv_file = 'distress_information_process_automation.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(title)
# 打开CSV文件并写入数据
    for file in files:
        title_information = file.split('_')
        num_str = title_information[0]
        num = num_str.lstrip('0')
        gps = title_information[1] + '_' + title_information[2]
        milestone = title_information[-1].rstrip('.txt')

        if file.endswith('.txt'):
            txt_file_path = os.path.join(file_path, file)
            # 读取txt文件的内容并写入CSV文件
            with open(txt_file_path, 'r') as txt_file:
                lines = txt_file.readlines()

                for line in lines:
                    # 假设txt文件中的每行数据以空格分隔
                    data = line.strip().split(' ')

                    type = data[0]
                    xy_yolo = data[1] + '_' + data[2] + '_' + data[3] + '_' + data[4]
                    print(xy_yolo)
                    # Yolo: [x_center / w, y_center / h, width/w, height/h] ; Pascal vol: [x_min, y_min, x_max, y_max]
                    output = [num, milestone, '沥青路面', type, '_', '_', '_', '_', '矩形', xy_yolo, gps, current_time]

                    writer.writerow(output)



print("CSV文件已生成。")