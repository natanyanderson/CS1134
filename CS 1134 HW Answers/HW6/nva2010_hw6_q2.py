from DoublyLinkedList import *

class Integer:
    def __init__(self,num_str):
        self.data = DoublyLinkedList()
        for elem in num_str[::-1]:
            self.data.add_last(elem)

    def __add__(self, other):
        longer_num = max(len(self.data), len(other.data))
        sums_str = ""
        starting_self = self.data.trailer
        starting_other = other.data.trailer
        carry_over = 0
        for i in range(longer_num):
            if starting_self.prev.data != None and starting_other.prev.data != None:
                starting_self = starting_self.prev
                starting_other = starting_other.prev
                sum_of_both = str(int(starting_self.data) + int(starting_other.data) + int(carry_over))

            elif starting_self.prev.data == None:
                starting_other = starting_other.prev
                sum_of_both = str(int(carry_over) + int(starting_other.data))

            elif starting_other.prev.data == None:
                starting_self = starting_self.prev
                sum_of_both = str(int(carry_over) + int(starting_self.data))

                if len(sum_of_both) > 1:
                    carry_over = sum_of_both[0]
                    sums_str = sum_of_both[1] + sums_str
                else:
                    carry_over = 0
                    sums_str = sum_of_both + sums_str
        if carry_over != 0:
            sums_str = carry_over + sums_str
        while sums_str[0] == "0":
            sums_str = sums_str[1:]
        return Integer(sums_str)

    def __mul__(self, other):
        starting_num = self.data.trailer.prev.data
        final_answer = 0
        for i in range(len(self.data)):
            acc = str(0) * i
            other_num = other.data.last_node()
            carry_over = 0
            for e in range(len(other.data)):
                product = str((int(starting_num.data) * int(other_num.data)) + int(carry_over))
                if len(product) > 1:
                    carry_over = product[0]
                    acc = product[1] + acc
                else:
                    carry_over = 0
                    acc = product + acc
                other_num = other_num.prev
            starting_num = starting_num.prev
            if carry_over != 0:
                acc = carry_over + acc
            final_answer += int(acc)
        return final_answer

    def __repr__(self):
        return "".join([str(item) for item in self.data])