'''This module simulates the queues of service requests in a bank'''
import queue
import time
import random

class Request:
    '''
    A class to represen a request
    ...
    Attributes
    ----------
    id: int
    type: str
    estimation_tim: int
    is_high_priority: bool
    '''

    id_counter = 1

    def __init__(self, _types):
        self.id = Request.id_counter
        Request.id_counter += 1
        self.type = random.choice(list(_types.keys()))
        self.estimation_time = types[self.type]
        self.is_high_priority = random.choices([True, False], weights=[0.25, 0.75])[0]

types = {
    'Відкрити поточний рахунок': 3,
    'Відкрити депозит': 3,
    'Відкрити кредитний рахунок': 5,
    'Закрити рахунок': 2,
    'Я просто спитати': 5
}

def generate_request(request_queue: queue, high_priority_queue: queue) -> str:
    '''
    Generate the request object and put in in one of the queue.
    '''
    request = Request(types)
    if request.is_high_priority:
        high_priority_queue.put(request)
        res = f"Надійшла приорітетна заявкa: {request.id}, типу {request.type}"
    else:
        request_queue.put(request)
        res = f"Надійшла заявкa: {request.id}, типу {request.type}"
    return res

def process_request(request_queue: queue, high_priority_queue: queue) -> str:
    '''
    Take one request from the queue and "process" it.
    Serves the hight_priority_queue first.
    '''
    current_queue = request_queue
    if not high_priority_queue.empty() : current_queue = high_priority_queue
    if not current_queue.empty():
        request = current_queue.get()
        processing_time = request.estimation_time + random.uniform(-1, 1.5)
        time.sleep(processing_time)
        res = f"Оброблена заявка {request.id} - {request.type}. Час обробки = {processing_time:.2f} c."
    else:
        res = "Черга пуста. Немає заявок для обробки"
    return res

def main():
    '''
    Implements the cycle of request generation and processing.
    Handles the termination of the cycle by pressing Ctrl + C
    '''
    request_queue = queue.Queue()
    high_priority_queue = queue.Queue()

    try:
        while True:

            # Generate new request
            if random.choices([True, False], weights=[55, 45])[0]:
                print(generate_request(request_queue, high_priority_queue))

            # Process request
            if random.choice([True, False]):
                print(process_request(request_queue, high_priority_queue))

    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем")

if __name__ == "__main__":
    main()
