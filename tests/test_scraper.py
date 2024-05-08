from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from main import app

client = TestClient(app)


def test_get_scrape():
    response = client.get("/scraper/scrape_data")
    assert response.status_code == 404
    # TODO
    # assert response.json() == {"message": "Observer subscribed"}
