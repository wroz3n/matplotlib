import matplotlib.pyplot as plt
import numpy as np
# # 1
# x = [1, 2, 3, 4, 5, 6]
# y = [2, 4, 3, 6, 5, 2]
# plt.plot(x, y, color='red', marker='x', markersize=10, markerfacecolor='black')
# for i in range(len(x)):
#     plt.annotate(f'({x[i]}, {y[i]})', xy=(x[i], y[i]), xytext=(0, 15), textcoords="offset points")
# plt.xlabel('Интервалы --->')
# plt.ylabel('')
# plt.title('Шкала значений')
# plt.show()

# # 2
# sizes = [33, 33, 7, 7, 5, 5]
# labels = ["1.Клубничное", "2.Сливочное", "3. Шоколадное", "4.Фисташковое", "5.Карамельный", "6. Другой вид"]
# numbers = ["Клубничное", "сливочное", "Шоколадное", "Фисташковое", "Карамельное", "Другой вид"]
# colors = ['blue', 'green', 'orange', 'red', 'pink', 'grey']
# plt.pie(sizes, labels=numbers, colors=colors)
# plt.title("Любимое мороженое")
# plt.legend(sizes,labels=labels, loc='upper right', bbox_to_anchor=(1.5, 1))
# plt.show()

# #3
# years = ['2013', '2015', '2016']
# categories = ['Телевизоры', 'Кухонная техника', 'Смартфоны и компьютерная техника']
# values = [
#     [40, 30, 30],  # 2013
#     [35, 25, 40],  # 2015
#     [30, 25, 45]   # 2016
# ]
# values = np.array(values)
# y = np.arange(len(categories))
# plt.barh(y, values[:, 0], label=categories[0], color='blue', height=0.4)
# plt.barh(y, values[:, 1], left=values[:, 0], label=categories[1], color='orange', height=0.4)
# plt.barh(y, values[:, 2], left=values[:, 0] + values[:, 1], label=categories[2], color='grey', height=0.4)
# plt.yticks(y, years)
# plt.title('График соотношений')
# plt.xlim(0, 100)
# plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.20), ncol=3)
# plt.show()

# #4
# months = ["Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
# values = [15,5,10,15,25,30,40,60,65,50,30]
# plt.bar(months, values, color='pink', width=0.35)
# plt.ylim(0,70)
# plt.grid(axis='y')
# plt.title("Диаграмма годового количества осадков")
# plt.xticks(rotation=45)
# plt.show()

# # 5
# x = np.arange(20, 81, 1)
# y_trend = 0.5 * x + 30 + np.random.normal(size=x.size)
# y_hetero = np.random.normal(loc=y_trend, scale=10)
# y_homo = np.random.normal(loc=y_trend, scale=5)
# plt.figure(figsize=(10, 6))
# plt.plot(x, y_trend, color='blue', label='Y тренд', linewidth=2)
# plt.scatter(x, y_hetero, color='green', label='Y норм.разб. (гетероседастичность)', alpha=0.7)
# plt.scatter(x, y_homo, color='red', label='Y норм.разб. (гомоседастичность)', alpha=0.7)
# plt.title('Линейный тренд')
# plt.legend(bbox_to_anchor=(0.5, -0.15), loc='lower center',ncol=3)
# plt.grid(axis='y')
# plt.xlim(20, 80)
# plt.ylim(0, 140)
# plt.show()

