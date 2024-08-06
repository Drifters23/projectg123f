from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<center> 
    <video src="" width="420" height="240" autoplay controls style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

if __name__ == "__main__":
    app.run()
