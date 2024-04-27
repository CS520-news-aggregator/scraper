from fastapi import APIRouter, Body, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from models.scraper import ScrapeQuery, ScrapeData
from scraper.extract import ScrapeWebsite

scraper_router = APIRouter(prefix="/scraper")


@scraper_router.get("get-scrape-data")
async def get_scrape_data(_: Request, scrape_query: ScrapeQuery = Body(...)):

    try:
        scraper = ScrapeWebsite(scrape_query.link)
        scrape_data = scraper.return_article()
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="Could not scrape data due to timeout"
        )

    scrape_data = ScrapeData(source_id=scrape_query.source_id, content=scrape_data)
    return jsonable_encoder(scrape_data)