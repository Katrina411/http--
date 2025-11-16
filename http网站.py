from http.server import BaseHTTPRequestHandler, HTTPServer

# 定义处理请求的类
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 发送200响应状态码
        self.send_response(200)
        # 设置响应头，指定内容类型为纯文本
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        # 发送响应内容
        self.wfile.write(b'Hello, world')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)  # 空字符串表示监听所有网络接口
    httpd = server_class(server_address, handler_class)
    print(f'服务器已启动，监听端口 {port}...')
    print(f'本地访问: http://localhost:{port}')
    print(f'局域网访问: http://你的IP地址:{port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('服务器已停止')

if __name__ == '__main__':
    run()