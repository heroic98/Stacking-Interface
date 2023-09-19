本仓库提供世界地震工程论文《基于Stacking模型融合策略的日本俯冲带板缘地震动预测》（__截止2023年9月18日，论文仍在审稿阶段，未发表__）配套代码，用于调用地震动预测模型Stacking-Interface，本仓库包含文件为：Stacking模型调用代码.py（调用代码）、Stacking-Interface.pickle（模型文件）。

本代码用户在使用时可更改的地方有4处，其中 __1为模型文件的路径；2为地震参数，如震级等；3、4分别为将SA数据保存为txt文件，保存衰减曲线图片__。

本代码为 __Python__ 编写，仅支持Python编辑器调用，代码详细操作说明已在代码文件中各个位置注明。

modelFilePath为所下载模型Stacking-Interface.pickle在用户电脑中的路径，__必填__

用户需要输入 __必填__ 参数：
震级(MJMA)、震源距(km)、震源深度(km)、场地条件Vs30(m/s)。

txtFilePath与curveFilePath分别SA输出文件与衰减曲线文件保存路径，注：用户仅需输入文件夹路径即可，且此项为 __选填__。


其余代码为计算代码，用户无须更改
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/65f3fbc6-aa00-4fc7-a12a-801845d270c3">
</div>

此为所输出PGA与SA数据。
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/ec74fca0-714c-49d7-9c2f-e8d122dec9ee">
</div>


此为衰减曲线。
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/c341bba4-7dc2-4bbe-9a82-a3a13abb413b">
</div>

模型输出文件。
<div align=center>
<img src="https://github.com/heroic98/Stacking-Interface/assets/57880065/46d219d0-8d2e-48b1-9fc0-c5acd1c91c70">
</div>
