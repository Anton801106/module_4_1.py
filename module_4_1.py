# Домашняя работа по уроку "Модули и пакеты"


from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(80, 2)
result2 = fake_divide(60, 0)
result3 = true_divide(66, 3)
result4 = true_divide(45, 0)
print(result1)
print(result2)
print(result3)
print(result4)
