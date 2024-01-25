from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Users(BaseModel):
    id: int
    name : str
    surname : str
    age : int
    hotmail : str


user_list = [Users(id=1,name="lucas",surname="Beccarini",age=26,hotmail="lucasbecca3@hotmail.com"),
             Users(id=2,name= "franco",surname="Beccarini",age=35,hotmail="franco_beca03@hotmail.com"), 
             Users(id=3,name= "tiziana", surname="Teilleri",age=23,hotmail="tiziana_teilleri@hotmail.com")]

@app.get("/users")
async def user():
    return list(user_list)



@app.get("/user/{id}") #Path
async def user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado al usuario"}
    

@app.get("/user/") #Querry
async def user(id: int):
    return search_user(id)
    
def search_user(id: int):
    users = list(filter(lambda user: user.id == id, user_list))
    try:
        return users[0]
    except IndexError:
        return {"Error":"No se ha encontrado al usuario"}
    
@app.post("/user/")
async def user(user: Users):
    if type(search_user(user.id)) == Users:
        return {"error":"El usuario ya existe"}
    else:
        user_list.append(user)
        return user



@app.put("/user/")
async def user(user: Users):

    found = False

    for index, save_user in enumerate(user_list):
        if save_user.id == user.id:
            user_list[index] = user
            found = True
    
    if not found:
        return {"error":"no se ha actualizado el usuario"}

    else:
        return user