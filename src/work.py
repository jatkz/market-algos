from mongo import AnalyticsQueue, DatasetsHandler
import pandas

def main():
    queue = AnalyticsQueue()
    datasetHandler = DatasetsHandler()
    while True:
        work_doc = queue.get()
        if work_doc is None:
            break

        datasetHandler.get_candles(work_doc['work_doc'], work_doc['symbol'])

        df = pandas.DataFrame()
        macros = {}
        ##### Switch case handle each work_doc type
        datasetHandler.upload_dataset("", work_doc['symbol'], df, macros)

        queue.remove(work_doc['work_doc'], work_doc['symbol'])

    print("Queue finished")

if __name__ == "__main__":
    main()
