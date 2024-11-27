class Film:
    def __init__(self, ad, yonetmen, yil, tur):
       
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil
        self.tur = tur

    def __str__(self): #filmi okunabilir formata çevirir
       
        return f"Ad: {self.ad}, Yönetmen: {self.yonetmen}, Yıl: {self.yil}, Tür: {self.tur}"


class FilmYoneticisi:
    def __init__(self):
       
        self.filmler = []  # Filmlerin tutulduğu liste.

    def film_ekle(self, ad, yonetmen, yil, tur):
       
        yeni_film = Film(ad, yonetmen, yil, tur)
        self.filmler.append(yeni_film)
        print(f"Film başarıyla eklendi: {yeni_film}")

    def film_sil(self, ad):   #adı verilen filmi sil
       
        for film in self.filmler:
            if film.ad == ad:
                self.filmler.remove(film)
                print(f"Film başarıyla silindi: {ad}")
                return
        print(f"Film bulunamadı: {ad}")

    def filmleri_listele(self, filtre_turu=None, filtre_degeri=None):
        
        if not self.filmler:
            print("Hiç film bulunmamaktadır.")
            return

        print("\nFilm Listesi")
        for film in self.filmler:
            if filtre_turu == "tur" and film.tur != filtre_degeri:
                continue
            if filtre_turu == "yil" and str(film.yil) != str(filtre_degeri):
                continue
            print(film)
        print("--- Liste Sonu ---")


# Ana program akışı
def main():
    yonetici = FilmYoneticisi() #filmleri adına türüne ve yılına göre lsiteleme
    while True:
        print("\"\nFilm Yönetim Sistemi ")
        print("1. Film Ekle")
        print("2. Film Sil")
        print("3. Filmleri Listele")
        print("4. Türe Göre Listele")
        print("5. Yıla Göre Listele")
        
        print("6. Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ad = input("Film Adı: ")
            yonetmen = input("Yönetmen: ")
            yil = input("Yıl: ")
            tur = input("Tür: ")
            yonetici.film_ekle(ad, yonetmen, yil, tur)
        elif secim == "2":
            ad = input("Silinecek Filmin Adı: ")
            yonetici.film_sil(ad)
        elif secim == "3":
            yonetici.filmleri_listele()
        elif secim == "4":
            tur = input("Filtrelemek istediğiniz tür: ")
            yonetici.filmleri_listele(filtre_turu="tur", filtre_degeri=tur)
        elif secim == "5":
            yil = input("Filtrelemek istediğiniz yıl: ")
            yonetici.filmleri_listele(filtre_turu="yil", filtre_degeri=yil)
        elif secim == "6":
            print("Çıkış yapılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()

    
#class film ;film sınıfıdır,filmlerin bilgilerini içerir
# class FilmYoneticisi ;film işlemlerini yönetir.