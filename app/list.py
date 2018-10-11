"""
двусвязный список
"""
class Item:
    """
    создаем класс узел
    """
    def __init__(self, next_, prev, elem):
        self.next_ = next_
        self.prev = prev
        self.elem = elem

class DoubleLinkedList:
    """
    объявление класса
    """
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__length = 0

    def push(self, elem):
        """
        добавляем элемент в коней списка
        """
        self.__length += 1
        if self.__first is None:
            self.__first = Item(None, None, elem)
            self.__last = self.__first
        elif self.__first == self.__last:
            self.__last = Item(None, self.__last, elem)
            self.__first.next_ = self.__last
        else:
            node = Item(None, self.__last, elem)
            self.__last.next_ = node
            self.__last = node

    def pop(self):
        """
        Достаем элемент из концы списка
        """
        if self.__last is None:
            return None
        elif self.__last == self.__first:
            data = self.__last
            self.__last = None
            self.__first = None
            self.__length -= 1
            return data.elem
        else:
            data = self.__last
            self.__last = self.__last.prev
            self.__length -= 1
            return data.elem

    def shift(self):
        """
        достаем элемент из начала списка
        """
        data = self.__first
        if data is None:
            return None
        self.__length -= 1
        self.__first = data.next_
        if self.__first is None:
            self.__last = None
        return data.elem

    def unshift(self, elem):
        """
        Добавляем элемент в начало списка
        """
        self.__length += 1
        if self.__first is None:
            self.__first = Item(None, None, elem)
        else:
            data = Item(self.__first, None, elem)
            self.__first.prev = data
            self.__first = data

    def len(self):
        """
        определяем длину списка
        """
        return self. __length

    def first(self):
        """
        возвращаем первый Item
        """
        if self.__first is not None:
            return self.__first
        else:
            return None

    def last(self):
        """
        возвращаем последний Item
        """
        if self.__last is not None:
            return self.__last
        else:
            return None

    def delete(self, elem):
        """
        удаляем эленемент из списка
        """
        if self.__first is None:
            return
        del_el = self.__first
        while del_el is not None:
            if del_el.elem == elem:
                if del_el == self.__first:
                    if del_el.next_ is not None:
                        self.__first = del_el.next_
                        self.__first.prev = None
                    else:
                        self.__first = None
                        self.__last = None
                elif del_el == self.__last:
                    if del_el.prev is not None:
                        self.__last = del_el.prev
                        self.__last.next_ = None
                    else:
                        self.__last = None
                        self.__first = None
                elif del_el.prev is not None and del_el.next_ is not None:
                    del_el.next_.prev = del_el.prev
                    del_el.prev.next_ = del_el.next_
                self.__length -= 1
            del_el = del_el.next_

    def contains(self, elem):
        """
        принадлежит ли эленемент списку
        """
        if self.__first is None:
            return False
        con_el = self.__first
        while con_el is not None:
            if con_el.elem == elem:
                return True
            con_el = con_el.next_
        return False

if __name__ == "__main__":
    A = DoubleLinkedList()
    print("length:", A.len())
    A.push(5)
    A.push(4)
    A.push(3)
    A.push(2)
    A.push(1)
    print("length:", A.len())
    A.unshift(10)
    print("length:", A.len())
    while A.first() is not None and A.last() is not None:
        print(A.shift())
    A.push(5)
    A.push(4)
    A.push(3)
    A.push(2)
    A.push(1)
    print("length:", A.len())
    A.delete(5)
    print(A.contains(4))
    while A.first() is not None and A.last() is not None:
        print(A.pop())
    print("length:", A.len())
    A.push(1)
    A.delete(1)
    print(A.pop())
    while A.first() is not None and A.last() is not None:
        print(A.pop())
