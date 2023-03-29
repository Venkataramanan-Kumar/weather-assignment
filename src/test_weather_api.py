from fastapi.testclient import TestClient

from app import app

test_client = TestClient(app)


def test_get_weather_stats_filter_by_station_id():
    '''
    Test for filter by station id for stats
    '''
    response = test_client.get("/api/weather/stats?station_id=USC00110187")
    assert response.status_code == 200
    assert response.json()[0]["station_id"] == "USC00110187"



def test_get_weather_records_filter_by_station_id():
    '''
    Test for filter by station id for weather records
    '''
    response = test_client.get("/api/weather/?station_id=USC00110187")
    assert response.status_code == 200
    assert all(data["station_id"] == "USC00110187" for data in response.json())


def test_get_weather_stats_no_filter():
    '''
    Test weather stats endpoint
    '''
    response = test_client.get("/api/weather/stats")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_get_weather_stats_filter_by_year():
    '''
    Test for weather stats by year
    '''
    response = test_client.get("/api/weather/stats?year=1986")
    assert response.status_code == 200
    assert all(data["date"].startswith("1986") for data in response.json())




def test_get_weather_records_no_filter():
    '''
    Test weather record endpoint
    '''
    response = test_client.get("/api/weather/")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_get_weather_records_filter_by_date():
    '''
    Test weather records by date
    '''
    response = test_client.get("/api/weather/?date=19860101")
    assert response.status_code == 200
    assert response.json()[0]["date"] == 19860101