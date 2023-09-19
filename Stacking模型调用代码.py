# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import pickle
import numpy as np
import os

plt.rc('font', family='Times New Roman', size=20)
'''
本代码为世界地震工程论文配套代码, 用于调用地震动预测模型Stacking-Interface
若有运行困难, 请在github仓库留言

 = 之间为用户使用时自行修改参数
 * 之间为代码执行计算, 尽量不要做修改

'''


#1 此处设置模型路径
#==============================================================================
# 此处更改模型文件路径, 若从github正常下载, 文件名应为:Stacking-InterFace.pickle
modelFilePath = r'C:/Users/DangHotil/Desktop/俯冲地区论文/世界地震工程修改/Stacking-Interface.pickle'
#==============================================================================

#2 此处更改地震动输入参数
#==============================================================================
M = 7.3 # 震级, 单位为MJMA
Rhypo = 177.19 #震源距, 单位为km
Depth = 8 #震源深度, 单位为km
Vs30 = 572.667 #场地条件Vs30, 单位为m/s
X = [Depth, M, Rhypo, Vs30]
#==============================================================================


#3 设置模型预测数据输出文件(TXT格式)路径, 若为空则不设置, 输出文件名为 SA-output.txt
#==============================================================================
# 例: r'C:\Users\DangHotil\Desktop'
txtFilePath = r'C:\Users\DangHotil\Desktop'
#==============================================================================


#4 设置模型预测衰减曲线图像(PNG格式)路径, 若为空则不设置, 输出文件名为 SA-figure.png
#==============================================================================
# 例: r'C:\Users\DangHotil\Desktop'
curveFilePath = r'C:\Users\DangHotil\Desktop'
#==============================================================================






# 以下为执行计算
#******************************************************************************
with open(modelFilePath, 'rb') as file:
    model = pickle.load(file)
    
# 调用模型, 计算输入地震动参数对应的输出结果
modelPre = model.predict([X])[0]

# 模型输出结果为对数形式, 因此转为以gal为单位
modelpre2Exp = np.exp(modelPre)
# 输出为：PGA与SA
XName = ['PGA', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08',
         '0.09', '0.1', '0.12', '0.14', '0.15', '0.16', '0.18', '0.2', '0.25',
         '0.3', '0.35', '0.4', '0.45', '0.5', '0.6', '0.7', '0.8', '0.9', '1',
         '1.25', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5']

# 打印显示模型预测结果
print("{:^10} {:^15}".format("T(s)", "gal"))
print("="*25)
for period, SA in zip(XName, modelpre2Exp):
    if period == 'PGA':
        print("{:^10} {:^15.3f}".format(period, SA))
    else:
        print("{:^10.2f} {:^15.3f}".format(float(period), SA))
#******************************************************************************



#******************************************************************************
if os.path.exists(txtFilePath):
    with open(os.path.join(txtFilePath, 'SA-output.txt'), 'w') as output:
        output.writelines('震源深度(km)    震级(MJMA)    震源距(km)    Vs30(m/s)\n')
        output.writelines('  {:.3f}         {:.2f}        {:.3f}       {:.3f}\n\n'.\
                          format(X[0], X[1], X[2], X[3]))
        output.writelines("{:^10} {:^15}\n".format("T(s)", "gal"))
        output.writelines('{}\n'.format("="*25))
        
        for period, SA in zip(XName, modelpre2Exp):
            if period == 'PGA':
                output.writelines("{:^10} {:^15.3f}\n".format(period, SA))
            else:
                output.writelines("{:^10.2f} {:^15.3f}\n".format(float(period), SA))
    print('输出文件已保存至{}'.format(os.path.join(txtFilePath, 'SA-output.txt')))
else:
    print('\033[1;31;40m提示: 路径 {}, 不存在于您的计算机。\033[0m'.format(txtFilePath))
    print('若不需要输出文件, 请忽略此条信息。')
#******************************************************************************




#******************************************************************************
SAList = ['0', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08',
          '0.09', '0.1', '0.12', '0.14', '0.15', '0.16', '0.18', '0.2', '0.25',
          '0.3', '0.35', '0.4', '0.45', '0.5', '0.6', '0.7', '0.8', '0.9', '1',
          '1.25', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5']
SAListNum = [float(single) for single in SAList]

plt.figure(figsize=(10, 8), dpi=100)
plt.plot(SAListNum, modelpre2Exp,color='red', marker='*')
plt.xlim(0.01,10)
plt.ylim(0.01,1000)
plt.yscale('log')
plt.xscale('log')
plt.yticks([0.01,0.1,1,10,100,1000])
plt.tick_params(which='major',length=5,width=2)
plt.tick_params(which='minor',length=5,width=2)
plt.ylabel('SA (gal)')
plt.text(0.012, 0.01, '$M_{JMA}$ = ' + str(X[1]) +'\n$R_{hypo}$ = ' + \
         str(round(X[2],2)) +'km\nD = ' + str(X[0]) +'km\n$V_{s30}$ = '\
         + str(round(X[3],3)) + 'm/s\n'+ '')
plt.xlabel('T(s)')
plt.ylabel('SA(gal)')

if os.path.exists(curveFilePath):
    plt.savefig(os.path.join(curveFilePath, 'SA-figure.png'))
    print('衰减曲线已保存至{}'.format(os.path.join(txtFilePath, 'SA-figure.png')))

else:
    print('\033[1;31;40m提示: 路径 {}, 不存在于您的计算机。\033[0m'.format(curveFilePath))
    print('若不需要输出文件, 请忽略此条信息。')
plt.show()
#******************************************************************************





        
        
        
        
    