from fastapi import FastAPI



app = FastAPI()


#el get() forma parte de las comunicaciones en HTTP://
#para crear un usuario en una api se usa post()
#para actualizar el usuario se usaria un put()
#para borrar el usuario se usaria un delete()




@app.get("/")
async def root():
    return "Hola fastAPI"

