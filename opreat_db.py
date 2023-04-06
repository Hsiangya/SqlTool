from db import db

"""导入db实例对象"""
db.exec("insert into d1(name) values(%(name)s)", name="武沛齐666")

ret = db.fetch_one("select * from d1")
print(ret)

ret = db.fetch_one("select * from d1 where id=%(nid)s", nid=3)
print(ret)

ret = db.fetch_all("select * from d1")
print(ret)

ret = db.fetch_all("select * from d1 where id>%(nid)s", nid=2)
print(ret)
