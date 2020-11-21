from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('hello_world.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/dynamic')
def dynamic():
    Cup = 'Hello, Student. Welcome To The Page.'
    cut = 'Three Cups of Tea presents an extraordinary account of bravery and compassion. The authors present several points of interest to the reader based on normative statements and politics against a background of cultural discourse that is being used to justify the continuing war on terrorism by America and its allies.'
    name = 'Michael'
    fiends = ['Bryan Bonilla', 'Thalia Markowski', 'Jamir Geidi', 'Hailey Wong', 'Ruba Rubeth']
    return render_template('dynamic.html', Cup=Cup, cut=cut, name=name, fiends=fiends)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
