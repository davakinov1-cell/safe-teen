from flask import Flask, render_template_string

app = Flask(__name__)

# ─── 1. ГЛАВНАЯ СТРАНИЦА ───
@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8"><title>Твой Помощник</title>
        <style>
            body { font-family: sans-serif; background: #f4f6f9; text-align: center; padding: 20px; }
            .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            h1 { color: #4A2A7A; }
            .btn { display: block; background: #FF6F61; color: white; padding: 15px; margin: 15px 0; text-decoration: none; border-radius: 5px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚨 ТВОЙ ПОМОЩНИК</h1>
            <p>Правовая помощь и интерактивный тест для учеников 7 класса.</p>
            <a href="/law" class="btn">⚖️ Узнать правила закона</a>
            <a href="/quiz" class="btn">📝 Запустить онлайн-тест</a>
            <a href="/contacts" class="btn">📱 Куда звонить за помощью?</a>
        </div>
    </body>
    </html>
    """)

# ─── 2. СТРАНИЦА ЗАКОНОВ ───
@app.route('/law')
def law():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ru">
    <head><meta charset="UTF-8"><title>Законы</title>
    <style>body{font-family:sans-serif;background:#f4f6f9;padding:20px;}.box{max-width:600px;margin:0 auto;background:white;padding:30px;border-radius:10px;}.item{background:#f8f9fa;padding:15px;margin:15px 0;border-left:5px solid #FF6F61;text-align:left;}</style></head>
    <body><div class="box">
        <h2>⚖️ Важные правила для 7 класса</h2>
        <div class="item"><h3>⚡ Диверсии в интернете</h3><p>За поджоги шкафов на ж/д по заданиям из сети судят строго <strong>с 14 лет</strong> (ст. 281 УК РФ).</p></div>
        <div class="item"><h3>🚄 Зацепинг</h3><p>Это грозит крупным штрафом родителям и постановкой на учет в ПДН (полицию).</p></div>
        <a href="/" style="display:block; text-align:center; color:#4A2A7A; font-weight:bold; text-decoration:none;">← На главную</a>
    </div></body></html>
    """)

# ─── 3. СТРАНИЦА С ТЕСТОМ (3 ВОПРОСА С КНОПКОЙ ДАЛЬШЕ) ───
@app.route('/quiz')
def quiz():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8"><title>Тест</title>
        <style>
            body { font-family: sans-serif; background: #f4f6f9; padding: 20px; text-align: center; }
            .box { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
            button { display: block; width: 100%; padding: 12px; margin: 10px 0; background: #f8f9fa; border: 2px solid #ddd; border-radius: 5px; cursor: pointer; font-size: 16px; text-align: left; }
            .correct { background: #d4edda !important; border-color: #28a745 !important; }
            .wrong { background: #f8d7da !important; border-color: #dc3545 !important; }
            #exp { display: none; margin-top: 15px; padding: 15px; background: #e2d9f3; border-radius: 5px; text-align: left; }
            #next-btn { display: none; margin-top: 15px; background: #4A2A7A; color: white; border: none; padding: 12px; width: 100%; border-radius: 5px; font-weight: bold; cursor: pointer; text-align: center; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2 id="q-num">Вопрос 1 из 3</h2>
            <p id="q-text" style="font-size: 18px; font-weight: bold; text-align: left;"></p>
            
            <div id="options-block">
                <button id="opt0" onclick="check(0)"></button>
                <button id="opt1" onclick="check(1)"></button>
                <button id="opt2" onclick="check(2)"></button>
            </div>
            
            <div id="exp"></div>
            <button id="next-btn" onclick="nextQ()">Дальше →</button>
            <br><br>
            <a href="/" style="color: #4A2A7A; font-weight: bold; text-decoration: none;">← Выйти на главную</a>
        </div>

        <script>
            const data = [
                {
                    q: "С какого возраста в России наступает уголовная ответственность за кражу и поджоги (диверсии)?",
                    opts: ["А) С 12 лет", "Б) С 14 лет", "В) С 16 лет"],
                    correct: 1,
                    exp: "💡 <strong>Правильно!</strong> По закону РФ за кражу и диверсии ответственность наступает именно с 14 лет."
                },
                {
                    q: "Что грозит подростку за зацепинг (проезд на крыше поезда)?",
                    opts: ["А) Ничего, это просто экстремальный спорт", "Б) Штраф родителям и постановка на жесткий учет в ПДН", "В) Только устное предупреждение"],
                    correct: 1,
                    exp: "💡 <strong>Правильно!</strong> За зацепинг выписывают крупный штраф родителям, а самого подростка ставят на учет в полицию. А еще это смертельно опасно (27 000 Вольт в проводах!)."
                },
                {
                    q: "Накажут ли тебя, если ты просто 'стоял на шухере', пока твой друг ломал остановку?",
                    opts: ["А) Нет, ты ведь сам ничего руками не портил", "Б) Накажут, только если попадешь на камеру", "В) Да, по закону ты считаешься полноценным соучастником"],
                    correct: 2,
                    exp: "💡 <strong>Правильно!</strong> По статье 33 УК РФ тот, кто караулит ('стоит на шухере'), признается соучастником. Наказание группа получает более строгое, чем один человек."
                }
            ];

            let cur = 0;

            function loadQ() {
                document.getElementById("exp").style.display = "none";
                document.getElementById("next-btn").style.display = "none";
                document.getElementById("q-num").innerText = "Вопрос " + (cur + 1) + " из " + data.length;
                document.getElementById("q-text").innerText = data[cur].q;
                
                for(let i=0; i<3; i++) {
                    let b = document.getElementById("opt" + i);
                    b.innerText = data[cur].opts[i];
                    b.className = "";
                    b.disabled = false;
                }
            }

            function check(idx) {
                let buttons = document.querySelectorAll('#options-block button');
                buttons.forEach(b => b.disabled = true);
                
                let correctIdx = data[cur].correct;
                if(idx === correctIdx) {
                    document.getElementById("opt" + idx).classList.add("correct");
                } else {
                    document.getElementById("opt" + idx).classList.add("wrong");
                    document.getElementById("opt" + correctIdx).classList.add("correct");
                }
                
                document.getElementById("exp").innerHTML = data[cur].exp;
                document.getElementById("exp").style.display = "block";
                document.getElementById("next-btn").style.display = "block";
            }

            function nextQ() {
                cur++;
                if(cur < data.length) {
                    loadQ();
                } else {
                    document.getElementById("q-num").innerText = "Тест пройден! 🎉";
                    document.getElementById("q-text").innerText = "Ты отлично справился и разобрался в законах!";
                    document.getElementById("options-block").style.display = "none";
                    document.getElementById("exp").style.display = "none";
                    document.getElementById("next-btn").style.display = "none";
                }
            }

            loadQ();
        </script>
    </body>
    </html>
    """)

# ─── 4. СТРАНИЦА КОНТАКТОВ ───
@app.route('/contacts')
def contacts():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ru">
    <head><meta charset="UTF-8"><title>Помощь</title>
    <style>body{font-family:sans-serif;background:#f4f6f9;text-align:center;padding:50px 20px;}.box{max-width:500px;margin:0 auto;background:white;padding:30px;border-radius:10px;}.phone{font-size:24px;color:#FF6F61;font-weight:bold;margin:20px 0;}</style></head>
    <body><div class="box">
        <h2>📞 Единый телефон доверия</h2>
        <p>Если тебе страшно, одиноко или тебе угрожают в интернете, звони:</p>
        <div class="phone">8-800-2000-122</div>
        <p>Это полностью анонимно и бесплатно с любого телефона.</p>
        <a href="/" style="color:#4A2A7A; font-weight: bold; text-decoration: none;">← На главную</a>
    </div></body></html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

