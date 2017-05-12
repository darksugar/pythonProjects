# #Authon Ivor
# ###########增############
# obj = Users(name="alex0", extra='sb')
# session.add(obj)
# session.add_all([
#     Users(name="alex1", extra='sb'),
#     Users(name="alex2", extra='sb'),
# ])
# session.commit()
#
# ###########删############
# session.query(Users).filter(Users.id > 2).delete()
# session.commit()
#
# ###########改############
# session.query(Users).filter(Users.id > 2).update({"name" : "099"})
# session.query(Users).filter(Users.id > 2).update({Users.name: Users.name + "099"}, synchronize_session=False)
# session.query(Users).filter(Users.id > 2).update({"num": Users.num + 1}, synchronize_session="evaluate")
# session.commit()
#
# ###########查############
# ret = session.query(Users).all()
# ret = session.query(Users.name, Users.extra).all()
# ret = session.query(Users).filter_by(name='alex').all()
# ret = session.query(Users).filter_by(name='alex').first()
#
#
# ###########其他############
# 　条件
# ret = session.query(Users).filter_by(name='alex').all()
# ret = session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()
# ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all()
# ret = session.query(Users).filter(Users.id.in_([1,3,4])).all()
# ret = session.query(Users).filter(~Users.id.in_([1,3,4])).all()
# ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter_by(name='eric'))).all()
# from sqlalchemy import and_, or_
# ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all()
# ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all()
# ret = session.query(Users).filter(
#     or_(
#         Users.id < 2,
#         and_(Users.name == 'eric', Users.id > 3),
#         Users.extra != ""
#     )).all()
#
#
# # 通配符
# ret = session.query(Users).filter(Users.name.like('e%')).all()
# ret = session.query(Users).filter(~Users.name.like('e%')).all()
#
# # 限制
# ret = session.query(Users)[1:2]
#
# # 排序
# ret = session.query(Users).order_by(Users.name.desc()).all()
# ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()
#
# # 分组
# from sqlalchemy.sql import func
#
# ret = session.query(Users).group_by(Users.extra).all()
# ret = session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)).group_by(Users.name).all()
#
# ret = session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) >2).all()
#
# # 连表
#
# ret = session.query(Users, Favor).filter(Users.id == Favor.nid).all()
#
# ret = session.query(Person).join(Favor).all()
#
# ret = session.query(Person).join(Favor, isouter=True).all()
#
#
# # 组合
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union(q2).all()
#
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union_all(q2).all()