from flask import Flask
import socket
import os
import time

app = Flask(__name__)

# Получаем хостнейм (ID контейнера)
hostname = socket.gethostname()

# Добавляем счетчик запросов
request_count = 0

@app.route('/')
def hello():
    global request_count
    request_count += 1
    
    # Добавляем задержку, чтобы продемонстрировать работу балансировщика
    time.sleep(0.1)
    
    return f"""
    <html>
    <head>
        <title>Docker Scaling Demo</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }}
            .container {{ background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; }}
            .info {{ background-color: #e2f2ff; padding: 15px; border-radius: 5px; margin-top: 20px; }}
            .counter {{ background-color: #ffeeba; padding: 15px; border-radius: 5px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Привет из контейнера!</h1>
            <div class="info">
                <p><strong>Хостнейм (ID контейнера):</strong> {hostname}</p>
                <p><strong>Время сервера:</strong> {time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            <div class="counter">
                <p><strong>Счетчик запросов к этому контейнеру:</strong> {request_count}</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
