from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Flask</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color: #f0f2f5;
            }
            .container {
                text-align: center;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                max-width: 800px;
            }
            h1 {
                color: #2b5876;
                margin-bottom: 20px;
            }
            p {
                color: #333;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Flask</h1>
            <p>
                Flask is a lightweight WSGI web application framework in Python. 
                It's designed to be simple and easy to use, making it a great choice 
                for building web applications. Flask is called a micro-framework because 
                it doesn't require particular tools or libraries, giving developers 
                the flexibility to choose the tools and libraries they want to use.
            </p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

   
    

