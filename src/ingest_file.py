import os
import dask.dataframe as ddf
from sqlalchemy import create_engine

def ingest_data(directory):
    db_engine = create_engine('sqlite:///weather.db', echo=True)
    df = [
        ddf.read_csv(
                urlpath=os.path.join(directory, file_d), 
                sep="\t", 
                header=None, 
                names=["date", "max_temp", "min_temp", "precipitation"]
                ).assign(Station_ID=file_d[:11]) 
        for file_d in os.listdir(directory) if file_d.endswith(".txt")
    ]
    # Concatenate all df 
    file_data = ddf.concat(df)

    # Compute the dataframe 
    file_data = file_data.compute()
    file_data = file_data.reset_index(drop=True)

    # Get rid of any rows with  missing temp data and percp data
    result = file_data[(file_data['max_temp'] != -9999) |
                  (file_data['min_temp'] != -9999) | (file_data['precipitation'] != -9999)]

    result = result.groupby(['Station_ID', file_data['date'].map(str).str[:4]]).agg({
        'max_temp': 'mean',
        'min_temp': 'mean',
        'precipitation': 'sum'
    }).reset_index()

    # Rename the columns to more descriptive names
    result.rename(columns={'max_temp': 'AvgMaxtemp', 'min_temp': 'AvgMintemp',
               'precipitation': 'TotalAccPrecipitation'}, inplace=True)

    # Establish a connection to the database and create a db_session object
    db_session = db_engine.raw_connection()

    # Make changes in the weather file_data to a table in the database
    file_data.to_sql("weather_records", db_session, if_exists="replace",
                index=True, index_label='id')
    result.to_sql("weather_stats", db_session, if_exists="replace",
                  index=True, index_label='id')
    db_session.commit()
    db_session.close()


# Call the dataIngestion function with the specified directory
ingest_data('../wx_data')
