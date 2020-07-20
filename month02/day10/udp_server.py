from socket import *
import pymysql


class Database():
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")
        self.cur = self.db.cursor()
    def close(self):
        self.cur.close()
        self.db.close()

    def find_word(self,word):
        try:
            sql = "select mean from words where word='%s'" % word
            self.cur.execute(sql)
            mean = self.cur.fetchone()
            return mean[0]
        except Exception as e:
            return "没有该单词"


def main():
    ADDR = ("0.0.0.0", 8888)
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(ADDR)
    while True:
        data,addr = udp_socket.recvfrom(1024)
        word = data.decode()
        print(word)
        db = Database()
        sen_mean = db.find_word(word)
        udp_socket.sendto(sen_mean.encode(),addr)

if __name__ == '__main__':
    main()
