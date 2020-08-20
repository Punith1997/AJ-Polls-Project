from django.http import HttpResponse

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return self.get_response(request)

    def process_exception(self,request,exception):
        a='<a href="/logout">Logout</a> and Login again</h3>'
        return HttpResponse("<h1>Don't try to reset password or login to another account when you are logged in</h1><br><h3>Please "+a )
