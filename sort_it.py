import numpy as np
import matplotlib.pyplot as plt
from cuu import sort_points

# 读取 CSV 文件
data = np.genfromtxt('default.csv', delimiter=',')
new_sorted_data = sort_points(data)

# 排序点
# 保存重新排列后的点到另一个 CSV 文件中
np.savetxt('reordered_points.csv', new_sorted_data, delimiter=',')

# 绘制连接线
x_values = new_sorted_data[:, 0]
y_values = new_sorted_data[:, 1]

plt.figure(figsize=(6, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Connected Points')
plt.grid(True)
plt.show()