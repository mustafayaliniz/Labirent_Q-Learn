# Labirent Q-Learn

Bu proje, Pygame ve Q-öğrenme algoritmasını kullanarak bir labirent oyununu oynayan bir yapay zeka ajanını simüle eder. Oyuncunun amacı, labirent içinde hareket ederek muzu bulmaktır.

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Açıklaması](#proje-açıklaması)
  - [Ana Sınıf (`Main`)](#ana-sınıf-main)
  - [Q-Öğrenme Parametreleri](#q-öğrenme-parametreleri)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)
- [İletişim](#iletişim)

## Kurulum

Gerekli bağımlılıkları yüklemek için:

```bash
pip install pygame numpy
```

## Kullanım

Oyunu çalıştırmak için terminalden aşağıdaki komutu çalıştırın:

```bash
python main.py
```

## Proje Açıklaması

Bu proje, Pygame kullanarak görselleştirilen bir labirentte Q-öğrenme algoritması ile oyuncunun muzu bulmaya çalıştığı bir oyun oluşturur. 

### Ana Sınıf (`Main`)

`Main` sınıfı, oyunun ana döngüsünü ve Q-öğrenme algoritmasını içerir.

#### `__init__(self)`

- Pygame başlatılır ve oyun ekranı ayarlanır.
- Başlangıç labirenti yüklenir.
- Blok boyutu, oyuncu ve muzu başlangıç konumları ayarlanır.
- Oyuncu ve muz görselleri yüklenir.
- Q-öğrenme parametreleri ve Q-tablosu başlatılır.
- İzleme için değişkenler tanımlanır.

#### `draw_maze(self)`

Labirenti ekranda çizer. 1 değeri beyaz (geçilebilir) alanı, 0 değeri siyah (duvar) alanı temsil eder.

#### `draw_monkey(self)`

Oyuncuyu (maymun) ekranda çizer.

#### `draw_banana(self)`

Muzu ekranda çizer.

#### `move_player(self, action)`

Verilen aksiyona göre oyuncuyu hareket ettirir. Eğer oyuncu muzun bulunduğu konuma gelirse, ödül verir ve labirenti yeniden başlatır.

#### `update_q_table(self, state, action, reward, next_state)`

Q-tablosunu günceller. Temporal Difference (TD) öğrenme kuralını kullanarak Q-değerlerini hesaplar ve günceller.

#### `choose_action(self, state)`

Epsilon-Greedy politika ile aksiyon seçer. Belirli bir olasılıkla rastgele aksiyon, diğer durumda Q-tablosundaki en iyi aksiyon seçilir.

#### `run(self)`

Ana oyun döngüsünü yürütür. Oyuncu konumunu günceller, labirenti ve oyuncuyu çizer, Q-değerlerindeki değişiklikleri ekranda gösterir.

### Q-Öğrenme Parametreleri

- `alpha (öğrenme oranı)`: 0.1
- `gamma (indirim faktörü)`: 0.9
- `epsilon (keşif oranı)`: 0.1

Bu parametreler, Q-öğrenme algoritmasının performansını etkiler ve farklı değerler denenerek optimize edilebilir.

## Katkıda Bulunma

Katkılarınızı memnuniyetle kabul ediyoruz! Lütfen katkıda bulunmadan önce [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.

## İletişim

Proje ile ilgili sorularınız için [uzayk204@gmail.com](mailto:uzayk204@gmail.com) adresinden iletişime geçebilirsiniz.
