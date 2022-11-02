import datetime
from schedule import repeat, every, run_pending
import time

from Modulos_Bootcamp.A005.mercado_bitcoin.ingestors import DaySummaryIngestor
from Modulos_Bootcamp.A005.mercado_bitcoin.writers import DataWriter


# ============ Use the DaySummaryIngestor ============

if __name__ == '__main__':
    day_summary_ingestor = DaySummaryIngestor(
        writer=DataWriter, 
        coins=['BTC', 'ETH', 'LTC'], 
        default_start_date=datetime.date(2022,10,1)
    )
    
    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest()

    while True:
        run_pending()
        time.sleep(0.5)
