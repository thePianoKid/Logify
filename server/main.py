from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
debug_level = 'debug' # Options: 'critical', 'error', 'warning', 'info', 'debug', 'trace'.

app.mount('/static', StaticFiles(directory='static'), name='static')


templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/msg')
def read_msg(info: dict):
    return info

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=5000, log_level=debug_level)