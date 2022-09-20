import multiprocessing
import random
import sys
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.random()
            self.queue.put(item)
            print(f"Producer ==> {item}")
            time.sleep(1)
        print("Producer is done!")


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        time.sleep(5) # this is a delay of 5 seconds before the consumer starts. this is why the consumer starts after the producer and then finishes after
        while True:
            if self.queue.empty():
                print("Consumer is done!")
                break
            else:
                item = self.queue.get()
                print(f"Consumer <== {item}")
                time.sleep(1)




def main():
    queue = multiprocessing.Queue()
    producer = Producer(queue)
    consumer = Consumer(queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    return 0


if __name__ == "__main__":
    sys.exit(main())
