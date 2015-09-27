__author__ = 't35khan'

class GetAPI:
    def getapi(request):
        with open("../src/apikeys.txt") as file:
            for line in file:
                if line.split(" ")[0] == request:
                    return line.split(" = ")[1]




