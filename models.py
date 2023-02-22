class Todo:
    def __init__(self):
        self.todo_items = []

    def add_todo(self, item):
        if not isinstance(item, TodoItem):
            return
        self.todo_items.append(item)

    def list_items(self):
        for i, v in enumerate(self.todo_items):
            print(f"{i}. {v} - {v.is_done}")

    def find(self, word):
        find_item = []
        for i, item in enumerate(self.todo_items):
            if word in item.task:
                find_item.append((i, item))
        return find_item


class TodoItem:
    def __init__(self, task):
        self.__task = task
        self.__is_done = False

    @property
    def is_done(self):
        return self.__is_done

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, task):
        self.__task = task

    def done(self):
        if self.__is_done:
            self.__is_done = False
        else:
            self.__is_done = True

    def __repr__(self):
        return self.__task
