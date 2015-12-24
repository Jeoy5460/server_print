import web
import json
urls = (
        '/', 'index',
        '/add', 'add'
)
app = web.application(urls, globals())
render = web.template.render('templates/')
db = web.database(dbn='sqlite', db='testdb')
class index:
    def GET(self):
        #todos = db.select('todo')
        #return render.index(todos)
        #return render.index(name)
        return "Hello, world"
class add:
    def POST(self):
        #i = web.input()
        #n = db.insert('todo', title=i.title)
        #val = web.debug(web.data())
        postData = web.data()
        json_val = json.loads(postData)
        print json_val["name"][-8::]
        #web.debug(val["mac"])
        #raise web.seeother('/')


if __name__ == "__main__":
    app.run()
else:
    application = app.wsgifunc()
