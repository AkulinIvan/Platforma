import sys
import requests

def main():
    callee = sys.argv[1]  # Caller ID
    caller = sys.argv[2]  # Manager's number
    recording_file = sys.argv[3]  # Path to recording file
    
    url = "http://127.0.0.1/api/calls/"
    data = {
        'callee': callee,
        'caller': caller,
            'recording': recording_file,
        }
    response = requests.post(url, data=data)
    print("Ответ от сервера:", response.text)

if __name__ == "__main__":
    main()