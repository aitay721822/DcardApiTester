import sys
sys.path.append('..')
import json

from .APIPackage import APIPackage
from .APIResourse import APIResourse

# import StringResource #
from String.StringResources import StringResource
# import StringResource #

class DcardAPI(APIPackage):

    OK = 200
    EMPTY_CONTENT = 204

    def __init__(self):
        # INITIAL REQUEST CLIENT
        super().__init__()
        # LOGIN FLAG
        self.isLogin = False
        # API RESOURCE
        self.data = APIResourse()
        # GET RESPONSE CSRF
        self.Ping()

    def hotPosts(self,before = None):
        dcardForum = APIResourse.dcardHostName + APIResourse.dcardForum[1]
        method = APIResourse.dcardForum[0]
        # limit = Posts count #
        getData = {"popular":"true","limit":5} if before == None else {"popular":"true","limit":5,"before":before}
        response = self.requests(dcardForum,method,getData)
        if response.status_code == self.OK:
            JsonResponse = json.loads(response.text)
            displayResponse = json.dumps(JsonResponse,indent=4,ensure_ascii=False)
            print(displayResponse)
            print(StringResource.enterSuccessful)
            return JsonResponse[len(JsonResponse) - 1]["id"]
        else:
            print(StringResource.enterFail)
            return None

    def Ping(self):
        PingUrl = APIResourse.dcardHostName + APIResourse.dcardPing[1]
        method = APIResourse.dcardPing[0]
        response = self.requests(PingUrl, method, None)
        if self.csrf != None and response.status_code == self.EMPTY_CONTENT:
            print(StringResource.UpdateSuccessful)

    def Login(self,email,password):
        if self.isLogin :
            return
        LoginUrl = APIResourse.dcardHostName + APIResourse.dcardLogin[1]
        method = APIResourse.dcardLogin[0]
        data = json.dumps({"email":email,"password":password})
        response = self.requests(LoginUrl,method,data)
        if response.status_code == self.EMPTY_CONTENT :
            self.isLogin = True
            print(StringResource.LoginSuccessfully)
        else:
            print(response.text)
            print(StringResource.LoginFail)

    def Logout(self):
        if not self.isLogin:
            return
        LogoutUrl = APIResourse.dcardHostName + APIResourse.dcardLogout[1]
        method = APIResourse.dcardLogout[0]
        response = self.requests(LogoutUrl,method,None)
        if response.status_code == self.OK:
            self.isLogin = False
            print(StringResource.LogoutSuccessfully)
        else:
            print(StringResource.LogoutFail)

    def showJsonMe(self):
        if not self.isLogin:
            print(StringResource.NotLogin)
            return
        meUrl = APIResourse.dcardHostName + APIResourse.dcardJsonMe[1]
        method = APIResourse.dcardJsonMe[0]
        response = self.requests(meUrl, method, None)
        if response.status_code == self.OK :
            jsonRes = json.dumps(json.loads(response.text),indent=4,ensure_ascii=False)
            print(jsonRes)
            print(StringResource.enterSuccessful)
        else:
            self.isLogin = False
            print(StringResource.NotLogin)