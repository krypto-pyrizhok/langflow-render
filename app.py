from langflow.main import create_app
import os

app = create_app()

if __name__ == "__main__":
    # Цей блок для локального тестування, Gunicorn/uvicorn його ігнорують
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7860)))
