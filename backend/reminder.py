from apscheduler.schedulers.background import BackgroundScheduler
import datetime

scheduler = BackgroundScheduler()
scheduler.start()
#a changeee
#dfsasdfkjklksd
def send_reminder(message):
    print(f"Reminder: {message}")

def schedule_reminder(message, time):
    reminder_time = datetime.datetime.fromisoformat(time)
    scheduler.add_job(send_reminder, 'date', run_date=reminder_time, args=[message])
