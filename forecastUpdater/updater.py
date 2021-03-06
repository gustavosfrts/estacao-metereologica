from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecastApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(forecastApi.update_sensors_values, 'interval', minutes=1)
    scheduler.start()