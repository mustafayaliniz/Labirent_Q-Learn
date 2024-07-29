# Labirent Q-Learn

Bu proje, Q-öğrenme algoritmasını kullanarak bir labirent içinde hareket eden bir oyuncu (maymun) ve onun bir hedefi (muz) içeren bir oyun simülasyonudur. Proje, Python ve Pygame kütüphanesi kullanılarak geliştirilmiştir.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki gereksinimlere ihtiyacınız var:

- Python 3.x
- Pygame kütüphanesi
- Numpy kütüphanesi

## Kurulum

Öncelikle, gerekli kütüphaneleri kurmak için aşağıdaki komutları çalıştırın:

```bash
pip install pygame numpy
```

Projeyi klonlayın veya indirin ve çalışma dizininizde `images` klasöründe `monkey.bmp` ve `banana.bmp` dosyalarının bulunduğundan emin olun.

## Kullanım

Proje dosyalarının bulunduğu dizine gidin ve aşağıdaki komutu çalıştırarak oyunu başlatın:

```bash
python main.py
```

Oyunu çalıştırdığınızda, labirent içinde hareket eden bir maymun ve bir muz göreceksiniz. Maymun, Q-öğrenme algoritmasını kullanarak labirent içinde hareket eder ve muza ulaşmaya çalışır. 

## Dosya Açıklamaları

- `main.py`: Oyun döngüsü ve Q-öğrenme algoritmasının bulunduğu ana dosya.
- `labirentler.py`: Labirent yapılarını tanımlayan yardımcı dosya.

### main.py

Bu dosya, oyunun ana mantığını ve Q-öğrenme algoritmasını içerir. İçerisinde şu sınıflar ve fonksiyonlar bulunur:

#### Main Sınıfı

- `__init__(self)`: Pygame'i başlatır, ekranı ayarlar, labirenti yükler, oyuncu ve muzun başlangıç konumlarını belirler ve Q-öğrenme parametrelerini ayarlar.
- `draw_maze(self)`: Labirenti ekrana çizer.
- `draw_monkey(self)`: Oyuncuyu ekrana çizer.
- `draw_banana(self)`: Muz'u ekrana çizer.
- `move_player(self, action)`: Oyuncuyu verilen yönde hareket ettirir.
- `update_q_table(self, state, action, reward, next_state)`: Q tablosunu günceller.
- `choose_action(self, state)`: Epsilon-greedy politika ile hareket seçimi yapar.
- `run(self)`: Oyun döngüsünü çalıştırır.

### labirentler.py

Bu dosya, labirent yapılarını tanımlar. `Maze` sınıfı içinde `maze` fonksiyonu ile çeşitli labirent yapıları oluşturulabilir.

## Q-Öğrenme Algoritması

Q-öğrenme, bir ajan (bu durumda maymun) ve bir ortam (bu durumda labirent) arasındaki etkileşimlerden öğrenen model tabanlı bir pekiştirmeli öğrenme algoritmasıdır. Ajan, ortamda gezinirken belirli bir politika izleyerek ödül alır ve bu ödüllere dayanarak gelecekteki hareketlerini optimize etmeye çalışır.

Algoritmada kullanılan temel parametreler:

- `alpha`: Öğrenme hızı
- `gamma`: Gelecek ödüllerin bugünkü değeri
- `epsilon`: Keşif oranı (epsilon-greedy politika için)

## Görseller

- `monkey.bmp`: Oyuncu karakterinin görseli
- `banana.bmp`: Hedefin görseli

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasını inceleyebilirsiniz.
