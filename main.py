from APIRepository.DcardAPI import DcardAPI
from String.StringResources import StringResource
from getpass import getpass
import os

if __name__ == '__main__':
    Repo = DcardAPI()
    Str = StringResource()
    while(True):
        os.system("cls")
        print(Str.Line)
        print(Str.FuncLogin)
        print(Str.FuncHotPosts)
        print(Str.FuncShowMeJsonData)
        print(Str.Exit)
        print(Str.Line)
        ans = input(Str.ChooseFunc)
        if ans =="1":
            account = input(Str.InputAccount)
            password = getpass(Str.InputPassword)
            Repo.Login(account, password)
        elif ans == "2":
            before = Repo.hotPosts()
            while(before!=None):
                choice = input(Str.loadNextPage)
                if(choice.upper() == "Y"):
                    before = Repo.hotPosts(before=before)
                else:
                    break
        elif ans == "3":
            Repo.showJsonMe()
        elif ans == "4":
            Repo.Logout()
            break
        os.system("pause")