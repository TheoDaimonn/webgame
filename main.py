from flask import  *
from subbulshit import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
@app.route('/', methods=['GET'])
def start():
    with open('playersdata.txt', 'r', encoding='utf-8') as f:
        myavka = f.readlines()
    f = 0
    for i in range(len(myavka)):
        try:
            if myavka[i].split()[0] == request.remote_addr:
                myavka.remove(myavka[i])
        except Exception:
            pass
    with open('playersdata.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(myavka) + request.remote_addr + ' 0' + '\n')
    return render_template('start.html')

@app.route('/1')
def fst():
    return render_template('1.html')

@app.route('/2')
def sc():
    with open('playersdata.txt', 'r', encoding='utf-8') as f:
        myavka = f.readlines()
    f = 0
    for i in range(len(myavka)):
        try:
            if myavka[i].split()[0] == request.remote_addr:

                a = int(myavka[i].split()[1])
                myavka[i] = request.remote_addr + ' ' + str(a + 1)
                f = 1
                print('''
            d
            d
            d
            d
            d''')
                print(myavka)
                print(myavka[i])
                break
        except Exception:
            pass
    if f == 1:
        with open('playersdata.txt', 'w', encoding='utf-8') as f:
            f.write(''.join(myavka) + '\n')
    if int(myavka[i].split()[1]) >= 20:
        return render_template('777.html')
    return render_template('2.html')

@app.route('/3', methods=['GET', 'POST'])
def thr():
        return render_template('3.html')
    
@app.route('/4', methods=['GET', 'POST'])
def frth():
    return render_template('4.html')

@app.route('/5', methods=['GET', 'POST'])
def fvth():
    return render_template('5.html')

@app.route('/6', methods=['GET', 'POST'])
def sx():
    return render_template('6.html')

@app.route('/7', methods=['GET', 'POST'])
def svth():
    return render_template('7.html')

@app.route('/8', methods=['GET', 'POST'])
def occt():
    return render_template('8.html')

@app.route('/9', methods=['GET', 'POST'])
def nine():
    return render_template('9.html')

@app.route('/10', methods=['GET', 'POST'])
def cent():
    return render_template('10.html')

@app.route('/11', methods=['GET', 'POST'])
def elf():
    return render_template('11.html')

@app.route('/12', methods=['GET', 'POST'])
def zw():
    return render_template('12.html')


@app.route('/13', methods=['GET', 'POST'])
def ustal():
    return render_template('13.html')

@app.route('/14', methods=['GET', 'POST'])
def dl():
    return render_template('14.html')

@app.route('/15', methods=['GET', 'POST'])
def fft():
    return render_template('15.html')

@app.route('/16', methods=['GET', 'POST'])
def ssxt():
    return render_template('16.html')

@app.route('/17', methods=['GET', 'POST'])
def ybaca():
    return render_template('17.html')

@app.route('/18', methods=['GET', 'POST'])
def zdrastvui():
    return render_template('18.html')

@app.route('/19', methods=['GET', 'POST'])
def nebo():
    return render_template('19.html')

@app.route('/20', methods=['GET', 'POST'])
def v():
    return render_template('20.html')

@app.route('/21', methods=['GET', 'POST'])
def tw_one():
    return render_template('21.html')

@app.route('/22', methods=['GET', 'POST'])
def tw_t():
    return render_template('22.html')

@app.route('/23', methods=['GET', 'POST'])
def tw_tr():
    return render_template('23.html')

@app.route('/24', methods=['GET', 'POST'])
def tw_f():
    return render_template('24.html')

@app.route('/25', methods=['GET', 'POST'])
def tw_fi():
    return render_template('25.html')

@app.route('/26', methods=['GET', 'POST'])
def tw_sx():
    return render_template('26.html')

@app.route('/27', methods=['GET', 'POST']) #мы тут
def tw_ss():
    return render_template('27.html')

@app.route('/28', methods=['GET', 'POST'])
def tw_ssss():
    return render_template('28.html')

@app.route('/29', methods=['GET', 'POST'])
def tw_ssdddd():
    return render_template('29.html')

@app.route('/30', methods=['GET', 'POST'])
def tw_ssddd():
    return render_template('30.html')

@app.route('/31', methods=['GET', 'POST'])
def tw_ssdd():
    return render_template('31.html')

@app.route('/32', methods=['GET', 'POST'])
def tw_ssd():
    form = Form()
    if form.validate_on_submit():
        if check(form.round.data):
            return render_template('33.html')
        else:
            return redirect('/22')
    return render_template('32.html', form=form)   
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')