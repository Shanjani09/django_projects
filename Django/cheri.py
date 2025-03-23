# import cherrypy
# import os
# class MyApp:
#     @cherrypy.expose
#     def index(self):
#         return "This is a text...!"
#     @cherrypy.expose
#     def external_html(self):
#         cherrypy.response.headers['Content-Type'] = 'text/html'
#         try:
#             file_path = os.path.join(os.path.dirname(__file__), 'externalfile.html')
#             with open(file_path, 'r') as f:
#                 return f.read()
#         except FileNotFoundError:
#             return "Error: external_page.html not found."
#     @cherrypy.expose
#     def html(self):
#         cherrypy.response.headers['Content-Type'] = 'text/html'
#         return """
#         <html>
#             <head>
#                 <title>CherryPy HTML Page.</title>
#             </head>
#             <body>
#                 <h1>Hello World! Welcome to CherryPy!</h1>
#                 <p>This is an HTML page by Cherrypy</p>
#             </body>
#         </html>
#         """
# if __name__ == '__main__':
#     cherrypy.quickstart(MyApp())


import cherrypy
import os
class MyApp:
    @cherrypy.expose
    def index(self):
        return "This is a text...!"
    @cherrypy.expose
    def external_html(self):
        cherrypy.response.headers['Content-Type'] = 'text/html'
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'externalfile.html')
            with open(file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "Error: external_page.html not found."
    @cherrypy.expose
    def html(self):
        cherrypy.response.headers['Content-Type'] = 'text/html'
        return """
        <html>
            <head>
                <title>CherryPy HTML Page.</title>
            </head>
            <body>
                <h1>Hello World! Welcome to CherryPy!</h1>
                <p>This is an HTML page by Cherrypy</p>
            </body>
        </html>
        """
if __name__ == '__main__':
    cherrypy.quickstart(MyApp())