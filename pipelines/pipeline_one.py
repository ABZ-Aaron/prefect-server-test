from prefect import flow
from utilities.common_functions import say_goodbye
import os

@flow(log_prints=True)
def my_flow():
    secret_value = os.getenv("environment")
    print(secret_value)
    print("Hello World")
    say_goodbye()
    
if __name__ == "__main__":
    my_flow()
    
    
