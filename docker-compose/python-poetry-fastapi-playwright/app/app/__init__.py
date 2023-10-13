import typing
import uvicorn 
import fastapi
import io
import sys
import re
import time
import base64
import playwright

from playwright.async_api import async_playwright
from functools import reduce
from PIL import Image
from pydantic import BaseModel

global_context = {"browser": None}

def start(args=sys.argv):
    devmode = "--devmode" in args
    if devmode:
        dev()
    else:
        prod()

def dev():
    app = fastapi.FastAPI()

    @app.on_event("startup")
    async def init_browser():
        playwright = await async_playwright().start()
        global_context["browser"] = await playwright.chrome.launch()
    
    @app.get("/api/v1/playwright/examples/screenshot")
    async def handle_playwright_examples_screenshot():
        return await take_page_screenshot("https://www.google.com/doodles")

    uvicorn.run(app,host="0.0.0.0", port=8080)

def prod():
    app = fastapi.FastAPI()

    @app.on_event("startup")
    async def init_browser():
        playwright = await async_playwright().start()
        global_context["browser"] = await playwright.firefox.launch()
    
    @app.get("/api/v1/playwright/examples/screenshot")
    async def handle_playwright_examples_screenshot():
        return await take_page_screenshot("https://www.google.com/doodles")

    uvicorn.run(app,host="0.0.0.0", port=8080)

async def take_page_screenshot(url):
    browser = global_context["browser"]
    page = await browser.new_page()
    await page.goto(url,timeout=5000,wait_until="load")
    img = await page.screenshot(type="png")
    return {"b64png":base64.b64encode(img)}