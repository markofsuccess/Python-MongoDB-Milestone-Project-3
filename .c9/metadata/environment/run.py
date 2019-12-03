{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return \"Hello World\"","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":13,"column":23},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return \"Hello World\"","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":3},{"start":{"row":0,"column":0},"end":{"row":23,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","","","@app.route('/contact')","def contact():","    return render_template(\"contact.html\")","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":18,"column":42},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":20,"column":0},"end":{"row":22,"column":42},"action":"insert","lines":["@app.route('/contact')","def contact():","    return render_template(\"contact.html\")"],"id":6}],[{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"remove","lines":["t"],"id":7},{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"remove","lines":["c"]},{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"remove","lines":["a"]},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["t"]},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":["n"]},{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["o"]},{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["c"]}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["s"],"id":8},{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["e"]},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["r"]},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["v"]},{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["i"]},{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":["c"]},{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":["s"],"id":9}],[{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"remove","lines":["t"],"id":10},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"remove","lines":["c"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"remove","lines":["a"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"remove","lines":["t"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"remove","lines":["n"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"remove","lines":["o"]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["s"],"id":11},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["e"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["r"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["v"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["i"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["c"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["e"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"remove","lines":["t"],"id":12},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["c"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["a"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["t"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":["n"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["o"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"remove","lines":["c"]}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"insert","lines":["s"],"id":13},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"insert","lines":["e"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"insert","lines":["r"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"insert","lines":["v"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["i"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["c"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["e"]},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":[" "],"id":14},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["u"]},{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["r"]},{"start":{"row":27,"column":26},"end":{"row":27,"column":27},"action":"insert","lines":["l"]}],[{"start":{"row":27,"column":27},"end":{"row":27,"column":28},"action":"insert","lines":[" "],"id":15}],[{"start":{"row":27,"column":28},"end":{"row":56,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","","","@app.route('/login')","def login():","    return render_template(\"login.html\")","","","@app.route('/signup')","def signup():","    return render_template(\"signup.html\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":16}],[{"start":{"row":28,"column":0},"end":{"row":56,"column":23},"action":"remove","lines":["from flask import Flask, render_template","","app = Flask(__name__)","","","@app.route('/')","def index():","    return render_template(\"index.html\")","","","@app.route('/about')","def about():","    return render_template(\"about.html\")","","","@app.route('/login')","def login():","    return render_template(\"login.html\")","","","@app.route('/signup')","def signup():","    return render_template(\"signup.html\")","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":17}],[{"start":{"row":23,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True) url import os",""],"id":18},{"start":{"row":23,"column":0},"end":{"row":26,"column":23},"action":"insert","lines":["if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":22,"column":43},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":42,"scrollleft":0,"selection":{"start":{"row":25,"column":35},"end":{"row":25,"column":35},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1575397308105,"hash":"520cc2a2a9271df45f887a18edb88b9a3b555b3f"}