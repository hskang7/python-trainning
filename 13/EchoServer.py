import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('클라이언트 접속 : {0}'.format(self.client_address[0]))
        sock = self.request
        
        rbuff  = sock.recv(1024)
        received = str(rbuff, encoding="utf-8")
        print('수신 : {0}'.format(received))
        
        # 수신한 데이터를 그대로 돌려보냄.
        sock.send(rbuff)
        print('송신 : {0}'.format(received))
        sock.close()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('{0} <Bind IP>'.format(sys.argv[0]))
        sys.exit()
        
    bindIP = sys.argv[1]
    bindPort = 5425

    server = socketserver.TCPServer((bindIP, bindPort), MyTCPHandler)
    
    print('메아리 서버 시작...')
    server.serve_forever()