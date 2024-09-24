angle1 = int(input())
angle2 = int(input())

sum_angle = angle1 + angle2 - ((angle1 + angle2) // 360 * 360)
print(sum_angle)