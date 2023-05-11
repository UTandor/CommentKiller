from flask import Flask, render_template, request
import re

app = Flask(__name__)

def remove_comments(text):
    text = re.sub(r'(//|#|/\*).*?(\*/|$)', '', text, flags=re.DOTALL)
    return text

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        code = request.form.get('code')
        p_code = '/n'.join(code.split('\n'))
        uncommented_code = remove_comments(p_code)
        return render_template('home.html', output=uncommented_code, code=code)
    else:
        uncommented_code = ''
        code = ''        
        return render_template('home.html', output=uncommented_code, code=code)

if __name__ == '__main__':
    app.run(debug=True)
