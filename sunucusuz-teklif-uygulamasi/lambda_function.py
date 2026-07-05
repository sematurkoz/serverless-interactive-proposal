import json

def lambda_handler(event, context):
    html_icerik = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Özel Bir Soru</title>
        <style>
            body { font-family: 'Arial', sans-serif; text-align: center; margin-top: 100px; background-color: #fff5f7; color: #4a0e17; overflow: hidden; height: 100vh; width: 100vw; margin: 0; padding: 0; }
            
           
            h1 { font-size: 38px; color: #94b03a; position: relative; z-index: 10; background-color: #ffd1dc; display: inline-block; padding: 15px 30px; border-radius: 15px; margin-top: 80px; box-shadow: 0 6px 20px rgba(255, 209, 220, 0.4); border: 2px solid #ffb6c1; text-shadow: 1px 1px 1px rgba(0,0,0,0.05); }
            
            .btn-container { margin-top: 50px; position: relative; height: 120px; z-index: 10; }
            button { font-size: 22px; padding: 12px 28px; border: none; border-radius: 8px; cursor: pointer; position: absolute; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            
           
            #yesBtn { background-color: #e84393; color: white; left: 40%; transform: translateX(-50%); } 
            #noBtn { background-color: #ffd1dc; color: #94b03a; left: 60%; transform: translateX(-50%); transition: all 0.05s linear; } 
            
            .falling-emoji { position: fixed; z-index: 1; pointer-events: none; animation: popIn 0.5s ease-out forwards, spin 6s linear infinite; user-select: none; }
            
            @keyframes popIn { 0% { transform: scale(0); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
            @keyframes spin { 100% { transform: rotate(360deg); } }
        </style>
    </head>
    <body>

        <h1 id="mainTitle">Benimle çıkar mısın🤨?</h1>
        
        <div id="controls" class="btn-container">
            <button id="yesBtn" onclick="evetSecildi()">Evet</button>
            <button id="noBtn" onmouseover="kac()" onclick="kac()">Hayır</button>
        </div>

        <script>
            const emojiler = [
                "🌸","🌼","⭐","🌟","☀️","❄️","💧","🫧","🫐","🍓","🧿","❤️",
                "🩷","💛","🧡","💚","🩵","💙","💜","💝","💞","💕","🪄","🎉",
                "🔮","🎠","🎲","🍭","🎂","🍩","🍿","🌻","💐","🐳","🐧","🐤",
                "🐰","🦆","🦋"
            ];

            function kac() {
                var btn = document.getElementById('noBtn');
                var x = Math.random() * (window.innerWidth - btn.clientWidth - 20);
                var y = Math.random() * (window.innerHeight - btn.clientHeight - 20);
                
                if (y < 200 && x > (window.innerWidth/2 - 220) && x < (window.innerWidth/2 + 220)) {
                    y = window.innerHeight - btn.clientHeight - 50;
                }
                
                btn.style.position = 'fixed';
                btn.style.left = x + 'px';
                btn.style.top = y + 'px';
            }

            function emojiOlustur() {
                var element = document.createElement('div');
                element.className = 'falling-emoji';
                
                var rastgeleEmoji = emojiler[Math.floor(Math.random() * emojiler.length)];
                element.innerText = rastgeleEmoji;
                
                var boyut = Math.floor(Math.random() * 46) + 24;
                element.style.fontSize = boyut + 'px';
                
                var x = Math.random() * (window.innerWidth - boyut - 20);
                var y = Math.random() * (window.innerHeight - boyut - 20);
                
                element.style.left = x + 'px';
                element.style.top = y + 'px';
                
                document.body.appendChild(element);
            }

            function evetSecildi() {
                document.getElementById('mainTitle').style.display = 'none';
                document.getElementById('controls').style.display = 'none';
                
                for(let i=0; i<5; i++) {
                    emojiOlustur();
                }
                
                setInterval(emojiOlustur, 400);
            }
        </script>
    </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': html_icerik
    }