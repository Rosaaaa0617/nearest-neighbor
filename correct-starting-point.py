import numpy as np
import matplotlib.pyplot as plt

# 读取 CSV 文件
data = np.genfromtxt('default dataset.csv', delimiter=',')

# 排序点
sorted_points = [data[0]]
remaining_points = np.delete(data, 0, axis=0)

for _ in range(len(data) - 1):
    nearest_idx = np.argmin(np.linalg.norm(sorted_points[-1] - remaining_points, axis=1))
    sorted_points.append(remaining_points[nearest_idx])
    remaining_points = np.delete(remaining_points, nearest_idx, axis=0)


# 找到距离最远的两个点
distances = np.sqrt(np.sum(np.diff(sorted_points, axis=0)**2, axis=1))
max_distance_index = np.argmax(distances)

# 重新排列点
new_sorted_data = np.roll(sorted_points, -max_distance_index - 1, axis=0)

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
