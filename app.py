from flask import Flask, request, render_template

import tensorflow as tf

app = Flask(__name__)

def prediction(params):
    model = tf.keras.models.load_model('models/mn_model_nn')
    pred = model.predict([params])
    return pred

@app.route('/', methods=['POST', 'GET'])
def predict():
    message = ''
    if request.method == 'POST':
        param_list = ('Плотность, кг/м3', 'модуль упругости, ГПа', 'Количество отвердителя, м.%', 
                      'Содержание эпоксидных групп,%_2', 'Температура вспышки, С_2', 'Поверхностная плотность, г/м2	', 
                      'Модуль упругости при растяжении, ГПа', 'Прочность при растяжении, МПа', 'Потребление смолы, г/м2',
                      'Угол нашивки, град', 'Шаг нашивки', 'Плотность нашивки')
        params = []
        for i in param_list:
            param = request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        message = f'Соотношение матрица-наполнитель: {prediction(params)}'
    return render_template('mn.html', message=message)

if __name__ == '__main__':
    app.run()
