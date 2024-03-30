from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the data from the form
        text_content = request.form['text_content']
        file_name = request.form['file_name']
        file_content = request.form['file_content']

        # Save the file
        with open(file_name, 'w') as file:
            file.write(file_content)
        
        return 'File saved successfully!'

    # Render the HTML template with the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
