import matplotlib.pyplot as plt
from collections import deque

class CircularQueueVisualizer:
    def __init__(self, max_size):
        self.max_size = max_size
        self.circular_queue = deque(maxlen=max_size)

        # Set up the plot
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, max_size)
        self.ax.set_ylim(0, 1)
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.axis('off')

        # Draw initial empty circular queue
        self.draw_queue()

    def draw_queue(self):
        self.ax.clear()
        self.ax.set_xlim(0, self.max_size)
        self.ax.set_ylim(0, 1)
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.axis('off')

        # Draw the circular queue
        for i, item in enumerate(self.circular_queue):
            self.ax.text(i + 0.5, 0.5, str(item), ha='center', va='center', fontsize=12, color='black',
                         bbox=dict(facecolor='lightblue', edgecolor='blue', boxstyle='round,pad=0.3'))

        # Draw arrow indicating front and rear
        if self.circular_queue:
            self.ax.arrow(len(self.circular_queue) - 0.5, 0.5, 0.2, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
            self.ax.arrow(0.5, 0.5, -0.2, 0, head_width=0.05, head_length=0.1, fc='green', ec='green')

        plt.pause(0.1)
        plt.draw()

    def enqueue(self, item):
        self.circular_queue.append(item)
        self.draw_queue()

    def dequeue(self):
        if self.circular_queue:
            self.circular_queue.popleft()
            self.draw_queue()

# Example usage
if __name__ == "__main__":
    max_size = 5
    visualizer = CircularQueueVisualizer(max_size)

    visualizer.enqueue(1)
    visualizer.enqueue(2)
    visualizer.enqueue(3)
    visualizer.dequeue()
    visualizer.enqueue(4)
    visualizer.enqueue(5)
    visualizer.enqueue(6)

    plt.show()
