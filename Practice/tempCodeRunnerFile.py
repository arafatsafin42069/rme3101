    parent_index = index

        while True:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            if left_child_index >= len(self.heap) and right_child_index >= len(self.heap):
                break

            max_child_index = parent_index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[max_child_index]:
                max_child_index = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[max_child_index]:
                max_child_index = right_child_index

            if max_child_index != parent_index:
                self.heap[max_child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[max_child_index]
                parent_index = max_child_index
            else:
                break

