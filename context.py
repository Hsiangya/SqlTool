from context_db import Connect

"""通过with进行上下文管理"""
with Connect() as obj:
    # print(obj.conn)
    # print(obj.cursor)
    ret = obj.fetch_one("select * from d1")
    print(ret)

    ret = obj.fetch_one("select * from d1 where id=%(id)s", id=3)
    print(ret)
