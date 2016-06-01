from kazoo.client import KazooClient

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def run(zk_host):

    client = KazooClient(zk_host)
    client.start(timeout=15)

    zk_server_version = client.server_version()

    client.add_listener()
    print 'Server Version: {0}'.format(zk_server_version)

    queue = Queue()
    queue.enqueue('/')

    while queue.size() > 0:
        path = queue.dequeue()
        path_node = client.get(path)

        print '[{0}] {1}'.format(path_node[1].created, path)
        path_children = client.get_children(path)

        for child in path_children:
            queue.enqueue(path + child + '/')

    client.stop()

