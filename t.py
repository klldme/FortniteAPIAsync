import urllib.request
from os import system

system("pip install py-cord")

from os import environ as ENV

app = Sanic("images")

@app.route("/")
async def index(request):
  return redirect("")

@app.route("/Provicali.otf")
async def Provicali(request):
  return await file("Provicali.otf")







app.run(
  host='0.0.0.0', 
  port=6942
  workers=4
)
