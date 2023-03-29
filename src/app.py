from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine, text
from query_file import generate_query


engine = create_engine('sqlite:///weather.db', echo=True)


app = FastAPI()


@app.get("/api/weather/")
def get_weather_data(date: str = Query(None), station_id: str = Query(None),
                         page: int = Query(1), size: int = Query(10)):
    offset = (page - 1) * size
    filters = [f"Date == '{date}'"] if date else []
    filters += [f"Station_ID == '{station_id}'"] if station_id else []
    query=generate_query(filters,size,offset,"weather_records")
    with engine.connect() as conn:
        rows = conn.execute(text(query)).fetchall()
        if not rows:
            raise HTTPException(
                status_code=404, detail="No data found for the specified dates")
        weather_data = [{"station_id": row[5],"date": row[1],"max_temp": row[2],"min_temp": row[3],"precipitation": row[4],} for row in rows ]
        return weather_data


@app.get("/api/weather/stats")
def get_weather_stats(year: str = Query(None), station_id: str = Query(None),
                       page: int = Query(1), size: int = Query(10)):
    offset = (page - 1) * size
    filters = [f"Date == '{year}'"] if year else []
    filters += [f"Station_ID == '{station_id}'"] if station_id else []
    query=generate_query(filters,size,offset,"weather_stats")
    with engine.connect() as conn:
        rows = conn.execute(text(query)).fetchall()
        if not rows:
            raise HTTPException(
                status_code=404, detail="No data found for the specified dates")
        weather_data = [{"station_id": row[1], "date": row[2], "avg_max_temp": row[3], "avg_min_temp": row[4], "total_acc_precipitation": row[5]} for row in rows]
        return weather_data
