
#
# import sqlite3
# from libs.db.dba import getConn
#
# def create_table():
#     conn = getConn()     # db와 접속 정보
#     cur = conn.cursor()    # db를 보는 포인터
#     cur.execute('''
#         create table test(name text, kor int, eng int, mat int)
#         ''')
#     conn.commit()
#     conn.close()    # db와의 접속을 끊음
#
# if __name__ == '__main__':
#     create_table()

a=int(input())
for i in range(1,10):
    print(a,"*",i,"=",a*i)