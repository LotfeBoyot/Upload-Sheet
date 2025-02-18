import os
import sys
import time
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.core.management import call_command
from bulkexcel.models import TriggerUploadSheet  # Adjust based on your app structure

def check_and_run_command():
    try:
        # Check if there is an active trigger
        trigger = TriggerUploadSheet.objects.filter(active=True).first()
        if trigger:
            # Run the management command
            call_command('populate_dummy_tables')
            # Set active to False
            trigger.active = False
            trigger.save()
            print("Command executed and active set to False.")
        else:
            print("No active triggers found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        check_and_run_command()
        time.sleep(60)  # Check every minute