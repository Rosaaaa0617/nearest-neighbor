import numpy as np

def sort_points(data):
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
    return new_sorted_data





