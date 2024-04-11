# Trafikte Uyuya Kalma Riskini Önleyen Python Uygulaması

Bu Python uygulaması, trafikte sürücülerin uyuya kalma riskini algılayarak uygun önlemleri almasına yardımcı olur. Göz izleme teknolojisi kullanarak sürücünün gözlerinin hareketini izler ve uyuklama belirtilerini tespit eder.

## Detaylı Çalışma Prensibi

Bu projenin nasıl çalıştığını daha ayrıntılı olarak açıklayan bir videoya aşağıdaki bağlantıdan erişebilirsiniz:

[![Detaylı Çalışma Prensibi](https://img.youtube.com/vi/o9t2ZGJpBAs/0.jpg)](https://www.youtube.com/shorts/o9t2ZGJpBAs)

## Dosya Yapısı

- `uyuklama.py`: Ana uygulama dosyasıdır.
- `database.csv`: Uyuklama olaylarının kaydedildiği CSV dosyasıdır.

## Gereksinimler

- Python 3.x
- OpenCV
- cvzone (FaceMeshModule)
- winsound

Gerekli kütüphaneleri yüklemek için:

 ```bash
pip install opencv-python
pip install cvzone
 ```

## Kullanım

1. Kodu çalıştırın: `python uyuklama.py`
2. Kamera penceresi açılacak ve uygulama başlayacak.
3. Uygulama, sürücünün göz hareketlerini izleyecek ve uyuklama riski algılandığında uyarı verecektir.

## Nasıl Çalışır

- Kamera görüntüsünden yüz tespiti yapar.
- Yüz içindeki gözlerin oranını hesaplar.
- Eğer gözlerin oranı belirli bir eşik değerinin altına düşerse, uyuklama riski olduğunu tespit eder.
- Uyuklama tespit edildiğinde, sesli ve görsel bir uyarı verir.


