import scrapy
import bs4
import fastapi
import transformers
import uvicorn

app = fastapi.FastAPI()


# https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html
@app.middleware("http")
async def addSecureHeaders(
    request: fastapi.Request, call_next
) -> fastapi.Response:
    """adds security headers proposed by OWASP"""
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    response.headers["Content-Security-Policy"] = "default-src-https"
    response.headers["Strict-Transport-Security"] = "max-age=63072000"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Access-Control-Allow-Methods"] = "GET,OPTIONS"
    return response


@app.get("/health")
def sentiments():
    return {"Content-Type": "application/json", "isOK": True}
