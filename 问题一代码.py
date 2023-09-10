Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... import pandas as pd
... def calculate_depths_coverages_overlaps():
...     D_center = 70  
...     theta = math.radians(120)  
...     alpha = math.radians(1.5) 
...     d = 200  
...     distances_from_center = [-800, -600, -400, -200, 0, 200, 400, 600, 800]
...     depths_list = []
...     coverage_widths_list = []
...     overlap_percentages_list = []
... 
...     previous_width = None
...     for dist in distances_from_center:
...         D = D_center - dist * math.tan(alpha)
...         depths_list.append(D)
... 
...         W_prime = 2 * D * math.tan(theta/2) * math.cos(alpha)
...         coverage_widths_list.append(W_prime)
... 
...         if previous_width is not None:
...             overlap = 1 - (d / ((previous_width + W_prime) / 2))
...             overlap_percentages_list.append(overlap * 100)
...         else:
...             overlap_percentages_list.append(0) 
...         previous_width = W_prime
...     df_result10 = pd.DataFrame({
...         '测线距中心点处的距离/m': distances_from_center,
...         '海水深度/m': depths_list,
...         '覆盖宽度/m': coverage_widths_list,
...         '与前一条测线的重叠率/%': overlap_percentages_list
...     })
...     file_path = "result10.xlsx"
...     df_result10.to_excel(file_path, index=False)
...     print(f"结果已保存到 {file_path}")

