from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <body style="font-family:sans-serif; background:#f4f6f9; text-align:center; padding:50px;">
        <div style="max-width:500px; margin:0 auto; background:white; padding:30px; border-radius:10px; box-shadow:0 4px 6px rgba(0,0,0,0.1);">
            <h1 style="color:#4A2A7A;">🚨 ТВОЙ ПОМОЩНИК</h1>
            <p>Правовая помощь и интерактивный тест для учеников 7 класса.</p>
            <a href="/quiz" style="display:block; background:#FF6F61; color:white; padding:15px; margin:15px 0; text-decoration:none; border-radius:5px; font-weight:bold;">📝 Запустить онлайн-тест</a>
            <a href="/contacts" style="display:block; background:#4A2A7A; color:white; padding:15px; margin:15px 0; text-decoration:none; border-radius:5px; font-weight:bold;">📱 Куда звонить за помощью?</a>
        </div>
    </body>
    ''')

@app.route('/quiz')
def quiz():
    return render_template_string('''
    <body style="font-family:sans-serif; background:#f4f6f9; text-align:center; padding:20px;">
        <div style="max-width:500px; margin:0 auto; background:white; padding:30px; border-radius:10px;">
            <h2 id="q-num">Вопрос 1 из 3</h2>
            <p id="q-text" style="font-size:18px; font-weight:bold; text-align:left;">С какого возраста в России наступает уголовная ответственность за кражу и поджоги?</p>
            <div id="opts">
                <button onclick="check(this, false)" style="display:block; width:100%; padding:12px; margin:10px 0; text-align:left; cursor:pointer;">А) С 12 лет</button>
                <button onclick="check(this, true)" style="display:block; width:100%; padding:12px; margin:10px 0; text-align:left; cursor:pointer;">Б) С 14 лет</button>
            </div>
            <p id="exp" style="display:none; padding:15px; background:#e2d9f3; border-radius:5px; text-align:left;">💡 <strong>Правильно!</strong> По закону РФ за кражу и диверсии ответственность наступает именно с 14 лет.</p>
            <button id="next" onclick="nextQ()" style="display:none; width:100%; padding:12px; background:#4A2A7A; color:white; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">Дальше →</button>
            <br><a href="/" style="color:#4A2A7A; font-weight:bold; text-decoration:none;">← На главную</a>
        </div>
        <script>
            let step = 1;
            function check(btn, isCorrect) {
                let buttons = document.querySelectorAll('#opts button');
                buttons.forEach(b => b.disabled = true);
                if(isCorrect) { btn.style.background = '#d4edda'; } else { btn.style.background = '#f8d7da'; }
                document.getElementById('exp').style.display = 'block';
                document.getElementById('next').style.display = 'block';
            }
            function nextQ() {
                if(step === 1) {
                    step = 2;
                    document.getElementById('q-num').innerText = "Вопрос 2 из 3";
                    document.getElementById('q-text').innerText = "Что грозит подростку за зацепинг (проезд на крыше поезда)?";
                    document.getElementById('opts').innerHTML = `<button onclick="check(this, false)" style="display:block; width:100%; padding:12px; margin:10px 0; text-align:left; cursor:pointer;">А) Ничего, это спорт</button>
                    <button onclick="check(this, true)" style="display:block; width:100%; padding:12px; margin:10px 0; text-align:left; cursor:pointer;">Б) Штраф родителям и учет в полиции</button>`;
                    document.getElementById('exp').innerHTML = "💡 <strong>Правильно!</strong> За зацепинг штрафуют родителей и ставят на учет в ПДН. Это смертельно опасно!";
                    document.getElementById('exp').style.display = 'none'; document.getElementById('next').style.display = 'none';
                } else if(step === 2) {
                    step = 3;
                    document.getElementById('q-num').innerText = "Вопрос 3 из 3";
                    document.getElementById('q-text').innerText = "Накажут ли тебя, если ты просто 'стоял на шухере', пока твой друг ломал остановку?";
                    document.getElementById('opts').innerHTML = `<button onclick="check(this, false)" style="display:block; width:100%; padding:12px; margin:10px 0; text-align:left; cursor:pointer;">А) Нет, ты же сам ничего не ломал</button>
                    <button onclick="check(this, true)" style="display:block; width:100%; padding:12px; margin:10px 0; text-align:left; cursor:pointer;">Б) Да, ты полноценный соучастник</button>`;
                    document.getElementById('exp').innerHTML = "💡 <strong>Правильно!</strong> По статье 33 УК РФ тот, кто караулит ('стоит на шухере'), признается соучастником преступления.";
                    document.getElementById('exp').style.display = 'none'; document.getElementById('next').innerText = "Посмотреть результат"; document.getElementById('next').style.display = 'none';
                } else {
                    document.getElementById('q-num').innerText = "Тест успешно пройден! 🎉";
                    document.getElementById("q-text").innerHTML = "Ты отлично справился и разобрался в законах!";
                    document.getElementById('opts').style.display = 'none'; document.getElementById('exp').style.display = 'none'; document.getElementById('next').style.display = 'none';
                }
            }
        </script>
    </body>
    ''')

@app.route('/contacts')
def contacts():
    return render_template_string('''
    <body style="font-family:sans-serif; background:#f4f6f9; text-align:center; padding:50px 20px;">
        <div style="max-width:500px; margin:0 auto; background:white; padding:30px; border-radius:10px; box-shadow:0 4px 6px rgba(0,0,0,0.1);">
            <h2>📞 Единый телефон доверия</h2>
            <p>Если тебе страшно, одиноко или тебе угрожают в интернете, звони:</p>
            <div style="font-size:24px; color:#FF6F61; font-weight:bold; margin:20px 0;">8-800-2000-122</div>
            <p>Это полностью анонимно и бесплатно с любого телефона.</p>
            <a href="/" style="color:#4A2A7A; font-weight:bold; text-decoration:none;">← На главную</a>
        </div>
    </body>
    ''')
