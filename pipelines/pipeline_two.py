from prefect import flow
from .utilities.common_functions import say_goodbye

@flow(log_prints=True)
def my_flow():
    print("Hello World 2")
    say_goodbye()
    
if __name__ == "__main__":
    my_flow()
    
    
