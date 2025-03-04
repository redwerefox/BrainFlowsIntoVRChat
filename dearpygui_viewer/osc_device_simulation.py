from pythonosc import udp_client
from osc_server import OSC_PATHS_TO_KEY, ELAPSED_TIME_PATH

import time

SLEEP_TIME = 0.1 #seconds

startTime = time.time()

osc_paths = [ key for key in OSC_PATHS_TO_KEY.keys()]

def run_client():
    client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

    print(osc_paths)
    assert isinstance(osc_paths[0], str)

    def _get_debuggable_times(time = 0.0):
        return 0.33 if (time % 1.0) > 0.5 else 0.66 

    try:
        while True:
            for idx, path in enumerate(osc_paths):
                client.send_message(path, _get_debuggable_times(time.time() + 0.1 * idx))

            elapsedTime = time.time() - startTime
            client.send_message(ELAPSED_TIME_PATH, elapsedTime)
            print(f"Elapsed time send: {elapsedTime}")
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print("Shutting down testing client...")
    finally :
        print("Done")

if __name__ == "__main__":
    run_client()  
        