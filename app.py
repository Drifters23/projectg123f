from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<center> 
    <video src="https://comunidadinformatica4-my.sharepoint.com/:v:/g/personal/scottth_comunidadinformatica4_onmicrosoft_com/Ef8a6wDFB9FPjiohZ7-DOUIBi8MdIwoKrZeFSJnvbp8k0w?download=1" width="420" height="240" autoplay controls style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

if __name__ == "__main__":
    app.run()
