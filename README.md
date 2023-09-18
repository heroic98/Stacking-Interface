本仓库提供世界地震工程论文《基于Stacking模型融合策略的日本俯冲带板缘地震动预测》（__截止2023年9月18日，论文仍在审稿阶段，未发表__）配套代码，用于调用地震动预测模型Stacking-Interface，本仓库包含文件为：Stacking模型调用代码.py（调用代码）、Stacking-Interface.pickle（模型文件）。

本代码用户在使用时需要更改的地方有4处，其中1为模型文件的路径；2为地震参数，如震级等；3、4分别为将SA数据保存为txt文件，保存衰减曲线图片。

本代码为Python编写，仅支持Python编辑器调用，代码详细操作说明已在代码文件中各个位置注明。

modelFilePath为所下载模型Stacking-Interface.pickle在用户电脑中的路径，__必填__

用户需要输入 __必填__ 参数：
震级(MJMA)、震源距(km)、震源深度(km)、场地条件Vs30(m/s)。

txtFilePath与curveFilePath分别SA输出文件与衰减曲线文件保存路径，注：用户仅需输入文件夹路径即可，且此项为 __选填__。

其余代码为计算代码，用户无须更改

<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/bf35cd7a-1d12-42d2-a1ae-21912e951b7f">
</div>

此为所输出PGA与SA数据。
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/edb6fc1c-1c45-4824-a899-91c9d57280bb">
</div>

此为衰减曲线。
![image](https://github.com/heroic98/Stacking-Interface/assets/57880065/46bd25f2-a002-4887-ad62-6e596d071d7a)
