from threading import Condition

class Request:
    """Encapsulates the request data and blocks the request thread, making it wait for the response to be asynchronously computed.
    """

    def __init__(self):
        """
            Attributes

        """
        self.__id = -1
        self.__condition = Condition()

    def __str__(self):
        return f'id {self.__id}'
    
    def __repr__(self):
        return f'id {self.__id}'

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        return (self.__class__ == other.__class__
                and self.__id == other._Request__id)

    def await_resp(self, timeout_sec):
        self.__condition.acquire()
        try:
            self.__condition.wait(timeout_sec)
        finally:
            self.__condition.release()

    def response_ready(self):
        self.__condition.acquire()
        try:
            self.__condition.notify_all()
        finally:
            self.__condition.release()
    
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, id):
        self.__id = id


