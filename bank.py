__author__ = 'roctbb'
import tornado.web
import tornado.httpserver
import pickle
import Orange.classification

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    def post(self):
        with open('credit.pickle', 'rb') as f:
            clf = pickle.load(f)
        data = Orange.data.Table("credit.arff")
        data[0]["class"] = ""
        data[0]["checking_status"] = str(self.get_argument("checking_status"))
        data[0]["duration"] = self.get_argument("duration")
        data[0]["credit_history"] = str(self.get_argument("credit_history"))
        data[0]["purpose"] = str(self.get_argument("purpose"))
        data[0]["credit_amount"] = self.get_argument("credit_amount")
        data[0]["savings_status"] = str(self.get_argument("savings_status"))
        data[0]["employment"] = str(self.get_argument("employment"))
        data[0]["installment_commitment"] = str(self.get_argument("installment_commitment"))
        data[0]["personal_status"] = str(self.get_argument("personal_status"))
        data[0]["other_parties"] = str(self.get_argument("other_parties"))
        data[0]["residence_since"] = self.get_argument("residence_since")
        data[0]["property_magnitude"] = str(self.get_argument("property_magnitude"))
        data[0]["age"] = self.get_argument("age")
        data[0]["other_payment_plans"] = str(self.get_argument("other_payment_plans"))
        data[0]["housing"] = str(self.get_argument("housing"))
        data[0]["existing_credits"] = self.get_argument("existing_credits")
        data[0]["job"] = str(self.get_argument("job"))
        data[0]["num_dependents"] = self.get_argument("num_dependents")
        data[0]["own_telephone"] = str(self.get_argument("own_telephone"))
        data[0]["foreign_worker"] = str(self.get_argument("foreign_worker"))
        result = str(clf(data[0]))
        if result == "bad":
            self.render("bad.html")
        else:
            self.render("good.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", MainHandler),]
        settings = dict()
        super(Application, self).__init__(handlers, **settings)
def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()