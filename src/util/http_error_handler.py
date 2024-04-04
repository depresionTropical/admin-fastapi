from fastapi import Request, status
from fastapi.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp

class HTTPErrorHandlerMiddleware(BaseHTTPMiddleware):

  def __init__(self, app: ASGIApp) -> None:  
    super().__init__(app)

  async def dispatch(self, request: Request, call_next)-> Response | JSONResponse:
    try:
      return await call_next(request)
    except Exception as e:
      content = {'message': str(e)}
      status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
      return JSONResponse(content=content, status_code=status_code)