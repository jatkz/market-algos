from mongo.connection import MongoDatabase
import datetime as dt
import pandas

class DatasetsHandler(MongoDatabase):
    def get_candles(self, collection_name, symbol):
        data_document = self.database[collection_name].find_one({'symbol': symbol})
        if data_document is None:
            raise Exception("data not found in ", collection_name, " ", symbol)
        df = pandas.DataFrame(data_document['candles'])
        df['datetime_readable'] = df['datetime'].apply(lambda x: dt.datetime.fromtimestamp(x / 1000))
        return df

    def upload_dataset(self, collection_name, symbol, dataframe, macro):
        document = {
                    "symbol": symbol,
                    "dataset": dataframe.to_dict('records'),
                    "macro": macro
                }
        self.database[collection_name].replace_one({'symbol':symbol}, document, upsert=True)
