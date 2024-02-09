import xmlrpc.client
class LibraryAPI():
    def __init__(self, host, port, db, user, pwd):
        common = xmlrpc.client.ServerProxy("http://%s:%d/xmlrpc/2/common" % (host, port))
        self.api = xmlrpc.client.ServerProxy("http://%s:%d/xmlrpc/2/object" % (host, port))
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        self.model = "library.book"

    def search_read(title):
        pass
    def create(title):
        pass
    def write(id, title):
        pass
    def unlink(id):
        pass
