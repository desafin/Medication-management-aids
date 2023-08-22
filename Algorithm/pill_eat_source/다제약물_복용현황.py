import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

# 데이터 설정
ages = ['45세 미만', '45세~54세', '55세~65세', '65세~74세', '75세~84세', '85세']
ratio = [0.06,0.61,2.27,6.91,14.57,15.74]
explode = [0,0,0,0,0.10,0.10]
colors = [ 'lightgray', 'lightgray', 'lightgray', 'lightgray','blue','green']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.title('연령별 다제약물 복용현황',size=20)
plt.pie(ratio, labels=ages, autopct='%1.1f%%', startangle=140,shadow=True,explode=explode,colors=colors,wedgeprops=wedgeprops,textprops={'size':18})
plt.legend(ages,loc='best')

plt.show()  # 그래프 출력
