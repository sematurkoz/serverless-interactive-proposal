# Serverless Interactive Proposal App 

Bu proje, AWS Lambda ve API Gateway (Function URL) mimarisi kullanılarak tamamen sunucusuz (Serverless) olarak geliştirilmiş dinamik ve interaktif bir web uygulamasıdır.

## Bulut Mimarisi (Architecture)
Kullanıcı (Tarayıcı) ➔ AWS Lambda Function URL ➔ AWS Lambda (Python) ➔ Yanıt (HTML/CSS/JS)

## Kullanılan Teknolojiler
* **Backend:** Python (AWS Lambda Handler)
* **Altyapı:** AWS Serverless (Sunucusuz Mimari)
* **Frontend:** HTML5, CSS3, JavaScript (Dynamic UI Animations)

## Proje İçeriği ve Görev Dağılımı
* **lambda_function.py (Python):**  AWS sunucularında çalışır. İstek geldiği an tetiklenir ve HTML sayfasını tarayıcıya iletir.
* **HTML & CSS:** İşin vitrinidir. Ekrandaki soru metnini, renk paletini ve butonların yerleşimini belirler.
* **JavaScript:** İşin dinamiğidir. "Hayır" butonunun imleçten kaçmasını sağlayan koordinat hesaplamalarını ve "Evet" tıklandığında fırlayan emojileri yönetir.

## Nasıl Çalışır?
Kullanıcı benzersiz AWS Function URL linkine tıkladığında, AWS Lambda fonksiyonu arkada hiçbir 7/24 aktif sunucu (EC2) yönetimine ihtiyaç duymadan milisaniyeler içinde uyanır, kodu çalıştırır ve dinamik içeriği tarayıcıya döner. Sayfa kapalıyken bulut maliyeti sıfırdır.

## Canlı Önizleme
https://z7khvq5uff6iezk3k75oxxfjfa0sclnj.lambda-url.eu-north-1.on.aws/
