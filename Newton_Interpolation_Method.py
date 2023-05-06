# 문제 7 Newton 보간법

# 0초 : 높이 100m, 각도 0
# 300초 : 높이 105m, 각도 24
# 600초 : 높이 112m, 각도 41
# 900초 :  높이 130m, 각도 65
# 1200초 : 높이 150m, 각도 78

t_data = [0, 300, 600, 900, 1200] # 시간 데이터
height_data = [100, 105, 112, 130, 150] # 높이 데이터
angle_data = [0, 24, 41, 65, 78] # 각도 데이터

# 차분 구하는 함수
def divided_difference(t, data):
    if len(t) == 1:
        return data[0]
    else:
        return (divided_difference(t[1:], data[1:]) - divided_difference(t[:-1], data[:-1])) / (t[-1] - t[0])

# 뉴턴 보간법 함수
def newton_interpolation(t_data, data, t):
    result = data[0]
    temp_t = t_data.copy()
    
    for i in range(1, len(t_data)):
        coef = divided_difference(temp_t[:i+1], data[:i+1])
        term = 1
        for j in range(i):
            term *= (t - t_data[j])
        result += coef * term
        
    return result

t_target = 1000
height_1000 = newton_interpolation(t_data, height_data, t_target)
angle_1000 = newton_interpolation(t_data, angle_data, t_target)

print("1000초일 때 높이:", height_1000)
print("1000초일 때 각도:", angle_1000)


