from sanic import Sanic
from routes.item_routes import item_bp

app = Sanic("MySanicApp")
app.blueprint(item_bp)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)