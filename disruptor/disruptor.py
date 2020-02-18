
class Disruptor(object):
    """
       All work MUST be acquired and retired in sequential order, never out-of-order.
    """

    def __init__(self):
        self.__ringbuffer_size = 100
        self.__batch_size = 10

        self.__next_write_index = 0
        self.__next_read_index = 0
        self.__unretired_read_index = 0 # earliest index of ackquired work
        
        self.__total_enqueue_work_item_count = 0 # since started
        self.__rejected_work_item_count = 0  # since started

    def enqueue_work_item(self, work_item):
        """Adds work_item to next available slot or throws error if no available slots remaining.
           Should this error or block, or be configurable?
        """
        print('enqueue')

    def acquire_work_batch(self):
        """Acquires and returns up to batch_size of pending work_items.
           The next_read_index is updated for acquiring next batch size.
        """
        print('dequeue')

    def retire_work_items(self, work_item):
        """Advances the  all previously ackquired work_items up to the index of provided work_item 
        """
        print(f'retired {work_item.index}')

    def get_pending_work_item_count(self):
        """
        """
        return 0

    def get_acquired_work_item_count(self):
        """
        """
        return 0

    def get_rejected_work_item_count(self):
        """
        """
        return self.__rejected_work_item_count

    def get_total_enqueue_work_item_count(self):
        """
        """
        return self.__total_enqueue_work_item_count