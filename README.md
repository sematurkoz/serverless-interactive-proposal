# Serverless Interactive Proposal App

Bu proje, tamamen sunucusuz (Serverless) mimariyle geliştirilmiş dinamik ve interaktif bir web uygulamasıdır. İlk olarak **AWS Lambda + Function URL** üzerinde geliştirildi, ardından **Cloudflare Workers**'a taşındı.

## Bulut Mimarisi (Architecture)
**Güncel:** Kullanıcı (Tarayıcı) ➔ Cloudflare Edge Ağı ➔ Cloudflare Worker (JavaScript) ➔ Yanıt (HTML/CSS/JS)

**İlk sürüm:** Kullanıcı (Tarayıcı) ➔ AWS Lambda Function URL ➔ AWS Lambda (Python) ➔ Yanıt (HTML/CSS/JS)

## Kullanılan Teknolojiler
* **Backend:** Cloudflare Workers (JavaScript) — ilk sürüm: Python (AWS Lambda Handler)
* **Altyapı:** Serverless / Edge Computing (Cloudflare Workers, AWS Lambda)
* **Frontend:** HTML5, CSS3, JavaScript (Dynamic UI Animations)

## Proje İçeriği ve Görev Dağılımı
* **cloudflare-worker/worker.js:** Cloudflare'in edge sunucularında çalışır. İstek geldiği an tetiklenir ve HTML sayfasını tarayıcıya iletir.
* **cloudflare-worker/wrangler.toml:** Worker'ın adı ve giriş dosyası gibi dağıtım (deploy) ayarları.
* **sunucusuz-teklif-uygulamasi/lambda_function.py:** Aynı uygulamanın AWS Lambda (Python) sürümü.
* **HTML & CSS:** İşin vitrinidir. Ekrandaki soru metnini, renk paletini ve butonların yerleşimini belirler.
* **JavaScript:** İşin dinamiğidir. "Hayır" butonunun imleçten kaçmasını sağlayan koordinat hesaplamalarını ve "Evet" tıklandığında fırlayan emojileri yönetir.

## Nasıl Çalışır?
Kullanıcı linke tıkladığında, Worker 7/24 açık bir sunucuya (EC2 vb.) ihtiyaç duymadan, kullanıcıya en yakın Cloudflare veri merkezinde milisaniyeler içinde çalışır ve sayfayı tarayıcıya döner. Kullanılmadığı sürece maliyeti sıfırdır.

## Neden Taşındı? (AWS Lambda ➔ Cloudflare Workers)
Uygulamanın yaptığı iş (istek gelince HTML dönmek) iki platformda da aynıdır; sadece handler fonksiyonu değişti. Cloudflare Workers'ın ücretsiz planı süre sınırı olmadan çalıştığı için, demo linkinin kalıcı olarak ayakta kalması amacıyla taşındı.

| | AWS Lambda | Cloudflare Workers |
|---|---|---|
| Dil | Python | JavaScript |
| Giriş noktası | `lambda_handler(event, context)` | `fetch(request)` |
| Yanıt | `{statusCode, headers, body}` sözlüğü | `new Response(body, {status, headers})` |
| Erişim | Function URL | `*.workers.dev` adresi |

## Yerelde Çalıştırma ve Deploy
```bash
cd cloudflare-worker
npx wrangler dev      # yerelde test: http://localhost:8787
npx wrangler deploy   # Cloudflare'e yayınla
```

## Canlı Önizleme
https://serverless-interactive-proposal.sematurkoz.workers.dev
