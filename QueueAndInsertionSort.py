class Queue():
    def __init__(self, queue_size):
        '''
        This is the constructor of the class.
        It has initial properties of what normal queue will have. 
        '''
        self.front = -1
        self.rear = -1
        self.queue_size = queue_size

        #This is a list comprehension. It is a feature offered only in python. 
        #List comprehension is basically the way to create a list (or perhaps known as array in other programming language)
        self.slots = ["" for _ in range(queue_size)]

        #The code at line 13 basically do this:
        #self.slots = ["", "", "", "", "", . . . . . . . . as many as the queue size]

    def isEmpty(self):
        '''
        Self explanatory, this is a method to check whether a queue is--
        -- empty or not. 
        '''
        if self.front == 0 and self.rear == 0:
            return True 
        return False

    def isFull(self):
        '''
        Self explanatory, this is a method to check whether a queue is--
        -- full or not.
        '''
        if self.rear == self.queue_size -1:
            return True
        return False

    def check_queue_last_index(self):
        '''
        This is a method to check the last occupied slot of a queue. 
        For example: 
        A queue has members: [1, 2, 3, 4, '', '', ''].
        This function will return 3 because the last occupied slot is 4 which is at index 3. 
        '''
        if self.isFull():
            return len(self.slots) - 1
        for index in range(len(self.slots)):
            if self.slots[index+1] == '':
                return index

        return index
    
    def enqueue(self, num):
        '''
        This is a method to add an item to a queue. 
        The process to add and remove an item in queue is using FIFO rule. 
        IN THIS PROGRAM, THE QUEUE WILL ADD AN ITEM FROM 'REAR'
        '''

        #Can not add more item if the queue is full. 
        if self.isFull():
            print("Queue is full.")
            return

        #If the queue is empty, the front and the rear of queue will be the same when--
        #-- a new item arrives. Directly insert the new item as the first element. 
        elif self.isEmpty():
            self.slots[0] = num
            self.front = 0
            self.rear = 0
            return

        #If the queue is not empty or full, increase the value of rear to be one so--
        #-- that the new item will not override the previous item. 
        self.rear += 1
        self.slots[self.rear] = num

    def dequeue(self):
        '''
        This is a method to remove an item to a queue. 
        The process to add and remove an item in queue is using FIFO rule. 
        IN THIS PROGRAM, THE QUEUE WILL REMOVE AN ITEM FROM 'FRONT'
        '''

        #Checking the last occupied index of the queue. 
        last_index = self.check_queue_last_index()

        #Since the removed item will always the item at the beginning,--
        #-- directly take it from index 0. 
        first_val = self.slots[0]

        #Decrement the rear value by -1 to avoid conflict with enqueue. 
        self.rear -= 1

        #Start shifting the element one by one. 
        #sample_list = [1, 2, 3, 4, 5]
        #If 1 will be removed, shift 2-5 to the left
        #the list must become [2, 3, 4, 5, '']
        for index in range(1, last_index+1):
            self.slots[index-1] = self.slots[index]

        #Replacing the value from last occupied index to the end with '' to--
        #-- indicate an empty slot. 
        if last_index != len(self.slots) - 1:
            for index in range(last_index, len(self.slots)):
                self.slots[index] = ''
        else:
            self.slots[last_index] = ''

        #Return the taken value. 
        return first_val

    def sort_queue(self):
        '''
        This is a method to sort the queue. 
        The method to sort the queue is using insertion sort.
        '''
        last_index = self.check_queue_last_index()

        #Iterate the items from the second item to the last occupied cell. 
        for index in range(1, last_index+1):
            hold_value = self.slots[index]
            marker = index

            while(marker > 0 and self.slots[marker-1] > hold_value):
                self.slots[marker] = self.slots[marker-1]
                marker -= 1

            self.slots[marker] = hold_value

    def print_queue(self):
        print(self.slots)


if __name__ == "__main__":
    sample_list = [5, 1, 2, 9, 10, 8, 6, 7]

    #DEMO 1
    #UNCOMMENT THIS SECTION AND RUN THE CODE TO SEE THE DEMO FROM DEVELOPER.
    #=====================================================================================
    # the_queue = Queue(8)
    # the_queue.enqueue(5)
    # the_queue.enqueue(4)
    # the_queue.enqueue(1)

    # the_queue.enqueue(10)
    # the_queue.enqueue(24)

    # the_queue.enqueue(2)
    # the_queue.enqueue(9)
    # the_queue.enqueue(7)

    # print("Before sorting: ")
    # the_queue.print_queue()

    # print("After sorting: ")
    # the_queue.sort_queue()
    # the_queue.print_queue()

    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()

    # the_queue.print_queue()

    # print("\n================================\n")

    # the_queue.enqueue(5)
    # the_queue.enqueue(1)
    # the_queue.enqueue(9)
    # the_queue.enqueue(3)
    # the_queue.enqueue(4)

    # the_queue.sort_queue()
    # the_queue.print_queue()

    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()
    # pop_val = the_queue.dequeue()

    # the_queue.print_queue()

    #=====================================================================================


    #DEMO 2
    #UNCOMMENT THIS SECTION AND RUN THE CODE TO SEE THE DEMO FROM DEVELOPER.
    #=====================================================================================

    # my_queue = Queue(len(sample_list))

    # for num in sample_list:
    #     my_queue.enqueue(num)

    # print("The queue before sorting: ")
    # my_queue.print_queue()

    # my_queue.sort_queue()

    # print("The queue after sorting: ")
    # my_queue.print_queue()

    # pop_val = my_queue.dequeue()
    # print(f"\nThe dequeued number is: {pop_val}\nThe queue is now: ")
    # my_queue.print_queue()

    #=====================================================================================

    