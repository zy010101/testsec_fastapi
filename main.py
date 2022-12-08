from typing import Union

from fastapi import FastAPI, Response
import uvicorn
app = FastAPI()


@app.post("/path", )
async def read_root(response: Response):
    """HTTP/1.1 200 OK
Date: Fri, 01 Nov 2022 09:17:37 GMT
Server: Jetty(9.2.22.v20170606)
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=16070400; includeSubDomains
Content-Type: application/ json; charset=UTF-8
Allow:
Pragma: no-cache
Cache-Control: no-store
Cache-Control: no-cache
Cache-Control: must-revalidate
Expires: -1
Content-Length: 168
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self’ 'unsafe-inline’'usafe-eval’data: blob:: img-src 'self’data:http: / /127.4.1.1 http:/ /127.4.2.1
Keep-Alive: timeout=4,max=100
Connection: Keep-Alive

{"kind": "tm:util: bash:runstate", " command": "run","utilCmdArgs":" -c id', " commandResult":"uid=0(root) gid=0(root) groups=0(root) context=system_u: system_r:initrc_t:s0\n"}
"""
    "E-2022-1388 F5 BIG-IP API Unauthenticated RCE"
    # h = {
    #     "X-Frame-Options": "SAMEORIGIN",
    #     "Strict-Transport-Security": "max-age=16070400; includeSubDomains",
    #     "Content-Type": "application/ json; charset=UTF-8",
    #     "Allow": "",
    #     "Pragma": "no-cache",
    #     "Cache-Control": "no-store",
    #     "Cache-Control": "no-cache",
    #     "Cache-Control": "must-revalidate",
    #     "Expires": "-1",
    #     "Content-Length": "168",
    #     "X-Content-Type-Options": "nosniff",
    #     "X-XSS-Protection": "1; mode=block",
    #     "Content-Security-Policy": "default-src 'self’ 'unsafe-inline’'usafe-eval’data: blob: img-src 'self’data:http://127.4.1.1 http://127.4.2.1",
    #     "Keep-Alive": "timeout=4,max=100",
    #     "Connection": "Keep-Alive"
    # }
    
    # response.headers.update(h)
    
    response.headers.update({"server":"123"})
    
    return {"kind": "tm:util: bash:runstate", " command": "run","utilCmdArgs":" -c id", " commandResult":"uid=0(root) gid=0(root) groups=0(root) context=system_u: system_r:initrc_t:s0\n"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
