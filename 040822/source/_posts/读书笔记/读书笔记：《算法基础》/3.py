class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    """
    链表类，用于创建和操作链表数据结构。
    """

    def __init__(self):
        """
        初始化链表对象。
        """
        self.head = Node(None) #哨兵节点

    def append(self, data):
        """
        在链表尾部添加节点，尾插法。
        参数：
            - data: 要添加的节点数据。
        """
        new_node = Node(data)
        if self.head.next is None:
            self.head.next = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self, data):
        """
        在链表头部添加节点，头插法。
        参数：
            - data: 要添加的节点数据。
        """
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def Iterate(self):
        """
        遍历链表并打印元素。
        """
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
    
    def len(self):
        """
        返回链表的长度。
        """
        length = 0
        cur_node = self.head
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length
        
    
    def FindCell(self,target):
        """
        查找链表中具有给定目标数据的节点。
        如果找到，返回该节点；否则返回None。
        参数：
            - target: 要查找的目标数据。
        """
        cur_node = self.head
        while cur_node:
            if cur_node.data == target:
                return cur_node
            cur_node = cur_node.next
        return None
    
    def InsertAfter(self,data,target_node=None,target_data=None):
        """
        在目标节点之后插入具有给定数据的新节点。
        目标节点可以通过直接提供目标节点或提供要搜索的目标数据来指定。
        参数：
            - data: 要插入的新节点的数据。
            - target_node: 目标节点。
            - target_data: 要搜索的目标数据。
        """
        if target_data is None and target_node is None:
            print('目标节点不存在')
            return
        if target_node is None and target_data is not None:
            target_node = self.FindCell(target_data)
        if target_node is None:
            print('目标节点不存在')
            return
        new_node = Node(data)
        new_node.next = target_node.next
        target_node.next = new_node
    
    def DeleteNode(self,target_node):
        """
        删除链表中的指定节点。
        参数：
            - target_node: 要删除的节点。
        """
        if target_node is None:
            print('目标节点不存在')
            return
        cur_node = self.head
        while cur_node.next:
            if cur_node.next == target_node:
                cur_node.next = target_node.next
                return
            cur_node = cur_node.next
        print('目标节点不存在')

class DoubleNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    """
    双向链表类，用于创建和操作双向链表数据结构。
    """

    def __init__(self):
        """
        初始化双向链表对象。
        """
        self.head = DoubleNode(None) #哨兵节点
        self.tail = DoubleNode(None) #哨兵节点x2
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, data):
        """
        在链表尾部添加节点，尾插法。
        参数：
            - data: 要添加的节点数据。
        """
        new_node = DoubleNode(data)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
    
    def prepend(self, data):
        """
        在链表头部添加节点，头插法。
        参数：
            - data: 要添加的节点数据。
        """
        new_node = DoubleNode(data)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node

    def Iterate(self):
        """
        遍历链表并打印元素。
        """
        cur_node = self.head.next
        while cur_node != self.tail:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
    
    def FindCell(self,target):
        """
        查找链表中具有给定目标数据的节点。
        如果找到，返回该节点；否则返回None。
        参数：
            - target: 要查找的目标数据。
        """
        cur_node = self.head.next
        while cur_node != self.tail:
            if cur_node.data == target:
                return cur_node
            cur_node = cur_node.next
        return None
    
    def InsertAfter(self,data,target_node=None,target_data=None):
        """
        在目标节点之后插入具有给定数据的新节点。
        目标节点可以通过直接提供目标节点或提供要搜索的目标数据来指定。
        参数：
            - data: 要插入的新节点的数据。
            - target_node: 目标节点。
            - target_data: 要搜索的目标数据。
        """
        if target_data is None and target_node is None:
            print('目标节点不存在')
            return
        if target_node is None and target_data is not None:
            target_node = self.FindCell(target_data)
        if target_node is None:
            print('目标节点不存在')
            return
        new_node = DoubleNode(data)
        new_node.next = target_node.next
        new_node.prev = target_node
        target_node.next.prev = new_node
        target_node.next = new_node

class OrderedLinkedList(LinkedList):
    """
    有序链表类，用于创建和操作有序链表数据结构。
    重写了父类的append和prepend方法，确保链表保持有序。
    """

    def __init__(self):
        """
        初始化有序链表对象。
        """
        super().__init__()

    def append(self, data):
        """
        在有序链表中添加节点，确保链表保持有序。
        参数：
            - data: 要添加的节点数据。
        """
        new_node = Node(data)
        if self.head.next is None:
            self.head.next = new_node
            return
        last_node = self.head
        while last_node.next:
            if last_node.next.data > data:
                new_node.next = last_node.next
                last_node.next = new_node
                return
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """
        在有序链表中添加节点，确保链表保持有序，这里直接调用append方法。
        父类的prepend方法是头插法，不适用于有序链表。
        参数：
            - data: 要添加的节点数据。
        """
        self.append(data)


class selfOrganiingLinkedList(LinkedList):
    """
    自组织链表类，用于创建和操作自组织链表数据结构。
    """

    def __init__(self):
        """
        初始化自组织链表对象。
        """
        super().__init__()

    def FindCell(self, target):
        cur_node = self.head.next
        while cur_node != self.tail:
            if cur_node.data == target:
                self.MoveToHead(cur_node) #三种自组织方法
                return cur_node
            cur_node = cur_node.next
        return None

    def MoveToHead(self,target_node):
        """
        将指定节点移动到链表头部。
        前移（MTF）将最新访问的节点移动到链表头部，以提高访问效率。
        参数：
            - target_node: 要移动的节点。
        """
        if target_node is None:
            print('目标节点不存在')
            return
        cur_node = self.head
        while cur_node.next:
            if cur_node.next == target_node:
                cur_node.next = target_node.next
                target_node.next = self.head.next
                self.head.next = target_node
                return
            cur_node = cur_node.next
        print('目标节点不存在')
    
    def Transpose(self,target_node):
        """
        将指定节点与其前一个节点交换位置。
        交换（Transpose）将最近访问的节点与其前一个节点交换位置，以提高访问效率。
        参数：
            - target_node: 要交换的节点。
        """
        if target_node is None:
            print('目标节点不存在')
            return
        if target_node == self.head.next:
            return
        cur_node = self.head
        while cur_node.next:
            if cur_node.next == target_node:
                cur_node.next = target_node.next
                target_node.next = cur_node.next.next
                cur_node.next.next = target_node
                return
            cur_node = cur_node.next
        print('目标节点不存在')

    def Count(self,target_node):
        """
        计算指定节点的访问次数。
        计数（Count）将最近访问的节点的访问次数加1，以提高访问效率。
        参数：
            - target_node: 要计数的节点。
        """
        # TODO: count方法没想好怎么写。要么给节点增加一个count属性，要么给链表增加一个字典属性，记录节点的访问次数。可能还需要再实现一个排序方法。
        if target_node is None:
            print('目标节点不存在')
            return
        target_node.count += 1

    