class Stack():
    def __init__(self, stack_size):
        self.top = -1
        self.bottom = -1
        self.stack_size = stack_size
        self.slots = ["" for _ in range(stack_size)]

    def isEmpty(self):
        return self.top == -1 and self.bottom == -1

    def isFull(self):
        return self.top == self.stack_size - 1

    def get_lastIndex(self):
        for index in range(len(self.slots)-1):
            if self.slots[index+1] == "":
                return index

        return index+1

    def push(self, push_num):
        if self.isEmpty():
            self.top = 0
            self.bottom = 0
            self.slots[self.top] = push_num
            return
        elif self.isFull():
            print("Can not push. Stack is full!")
            return 

        self.top += 1
        self.slots[self.top] = push_num

    def pop(self):
        last_index = self.get_lastIndex()
        pop_value = self.slots[last_index]
        self.top -= 1

        for index in range(last_index, len(self.slots)):
            self.slots[index] = ''

        return pop_value

    def sort_stack(self):
        last_index = self.get_lastIndex()
        for _ in range(last_index-1):
            for index in range(last_index-1):
                if self.slots[index] > self.slots[index+1]:
                    self.slots[index], self.slots[index+1] = self.slots[index+1], self.slots[index]

    def print_stack(self):
        print(self.slots)


if __name__ == "__main__":
    sample_list = [5, 1, 2, 9 ,10, 4, 3]

    # DEMO 1
    # sample_stack = Stack(5)

    # sample_stack.push(5)
    # sample_stack.push(1)
    # sample_stack.push(2)
    # sample_stack.push(9)
    # sample_stack.push(10)

    # print("Before pop: ")
    # sample_stack.print_stack()
    
    # print("\n============================\n")

    # print("After pop: ")
    # pop_value = sample_stack.pop()
    # pop_value = sample_stack.pop()
    # pop_value = sample_stack.pop()
    # print(pop_value)
    # sample_stack.print_stack()

    # print("\n============================\n")

    # print("Push some numbers and then sort: ")
    # sample_stack.push(3)
    # sample_stack.push(4)

    # sample_stack.sort_stack()

    # sample_stack.print_stack()



    # Demo 2
    # sample_stack = Stack(len(sample_list))
    # for num in sample_list:
    #     sample_stack.push(num)

    # print("Default Stack: ")
    # sample_stack.print_stack()

    # print("\n============================\n")

    # print("After popping two elements: ")
    # pop_value = sample_stack.pop()
    # pop_value = sample_stack.pop()
    # print(f"Pop Value: {pop_value}")
    # sample_stack.print_stack()

    # print("Inserting two more elements: ")
    # sample_stack.push(8)
    # sample_stack.push(7)
    # sample_stack.print_stack()

    # print("\n============================\n")

    # print("After sort: ")
    # sample_stack.sort_stack()
    # sample_stack.print_stack()

    # print("\n============================\n")
    # print("Pop again: ")
    # pop_value = sample_stack.pop()
    # print(f"Pop value: {pop_value}")
    # sample_stack.print_stack()
    

