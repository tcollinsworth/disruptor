from disruptor.disruptor import Disruptor

def test_enqueue_dequeue():
    d = Disruptor()
    # d.enqueue_work_item()
    # d.acquire_work_batch()
    # assert d.get_pending() == 0