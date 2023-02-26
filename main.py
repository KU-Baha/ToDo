from models import Todo, TodoItem
print('1 - Добавить задачу\n'
      '2 - Найти задачу\n'
'3 - Просмотреть задачи\n'
      '4 - Выйти')
my_todo = Todo()
my_task = TodoItem
def main():

    while True:
        choose = int(input("Введите желаюмую задачу:"))
        if choose == 1:
            result = Todo.add_todo
            result2 = Todo.add_todo(item=my_task(input("Введите задачу")), self=my_todo)
        elif choose == 2:
            result = Todo.find
            result2 = Todo.find(word=my_task(input("Введите искомую задачу")), self=my_todo)
        elif choose == 3:
            result = Todo.list_items
            result2 = Todo.list_items(self=my_todo)
        elif choose == 4:
            break
        else:
            result = 'wrong'

        with open('new_history.txt', 'a') as f:
            f.write(f' {str(choose)} --- {result.__name__}----{result2}\n')


main()