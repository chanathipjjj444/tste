from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

TEMPLATE = Jinja2Templates("html")
class Profile:
    def __init__(self, prefix, name, surname, email, phone_number):
        self._prefix = prefix
        self._name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number

class User:
    def __init__(self, name, id, password):
        self.__id = id
        self.__password = password
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def password(self):
        return self.__password

class Admin:
    def __init__(self, name, id, password):
        self.__id = id
        self.__password = password
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def password(self):
        return self.__password
    
class Login:
    def __init__(self):
        self.__user_list = []
    
    @property
    def user_list(self):
        return self.__user_list

    def add_user(self, user):
        if type(self.check_id(user)) != str:
            self.__user_list.append(user)

    def check_id(self, account):
        for user in self.__user_list:
            if user.id != account.id:
                if user.id == account.id and user.password == account.password:
                    return "ซ้ำโว้ยยย"
                else:
                    return account
            else:
                return "ID ซ้ำาา"

    def show_detail(self, account):
        view_account = {
            "name" : account.name,
            "email" : account.id,
            "password" : account.password
        }
        return view_account


user = User("Tung","kiki123@gmail.com","12345678")
user2 = User("Tung","kiki123@gmail.com","12345678")

login = Login()
login.add_user(user)
login.add_user(user2)
print(login.user_list)

# @app.get("/create_account/{name}")
# async def get_user(name:str):
#     for detail in login.user_list:
#         if  detail.name == name:
#             return login.show_detail(detail)
        
@app.get("/list_account")
async def get_list():
    return {"list" : login.user_list}

@app.get("/login",response_class=HTMLResponse)
async def webLogin(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("login.html", page_data)

@app.post("/check_login",response_class=HTMLResponse)
async def webLogin(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("login.html", page_data)

@app.get("/register",response_class=HTMLResponse)
async def WebRegister(request: Request):
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("register.html", page_data)

@app.get("/add_account",response_class=HTMLResponse)
async def add(request: Request, name, email, password):
    user = User(name, email, password)
    admin = Admin(name, email, password)
    login.add_user(user)
    page_data = {"request": request}
    return TEMPLATE.TemplateResponse("login.html", page_data)

# @app.post("/list_account")
# async def add_account(name, id, password):
#     account = User(name, id, password)
#     login.user_list.append(account)
#     return {"Data" : login.user_list}

# r = requests.get("http://127.0.0.1:8000/list_account")
# print(r.json())

# print(login.show_detail(user))