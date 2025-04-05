##################### 列表/数组 #####################

""" sort 方法，指定对象属性排序 """
from operator import itemgetter
arr = [{'name': 'zhangsan', 'age': 12}, {'name': 'lisi', 'age': 18}, {'name': 'wangwu', 'age': 15}]
arr = sorted(arr, key=itemgetter('age'))
# arr = sorted(arr, key=itemgetter('age'), reverse=True)
print(arr)

""" sort 方法 """
arr = [1, 2, 3, 4, 5, 3, 2, 5, 5]
arr = sorted(arr)
print(arr)

""" [:n] 取列表前n个元素 """
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())


""" count 方法 """
arr = [1, 2, 3, 4, 5, 3, 2, 5, 5]
cnt = arr.count(3)
print(cnt)

### rang, [2,11)，步长为2的列表 ###
even_numbers = list(range(2, 11, 2))
print(even_numbers)

### rang, [1,6)的列表 ###
numbers = list(range(1, 6))
print(numbers)

### rang ###
arr = range(5)
print(arr[-1])
print(arr)

arr = list(range(5))
print(arr)

### len方法,下标-1 ###
arr = [1, 2, 3, 4, 8]
print(len(arr))
print(arr[-1])

### 示例1 ###
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

### 示例2 ###
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

### 示例3，删除列表元素 ###
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

### 示例4，整型列表遍历 ###
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)



### 示例6，列表拷贝 ###
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

### 示例7, 字符串列表遍历 ###
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")




### 示例9, 创建列表 ###
squares = [value**2 for value in range(1, 11)]
print(squares)