from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        phone = request.form.get('phone')
        # You can add validation or save data here
        return render_template('greetings.html', name=name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
