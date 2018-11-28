import tornado.web
import tornado.ioloop
class lebron(tornado.web.RequestHandler):
    def get(self,m):
    
        m=int(m) if m is not None else 9
        html = '''
        <html>
        <body>
        <table>
        '''
        for i in range(1, m+1):
            html +='<TR>'
            for j in range(1, i+1):
                html += '<TD>%d*%d=%d</TD>' % (j,i,i*j)
            html +='</TR>'

        html +='''
        <ml>
        </body>
        </table>
        '''
        self.write(html)


        
if __name__ == '__main__':
    app=tornado.web.Application([
        (r"(?:/([0-9])?)",lebron)]
    )
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
