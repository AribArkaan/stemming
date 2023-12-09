from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Membuat objek stemmer untuk bahasa Indonesia
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Kata contoh
text = input("Masukkan kalimat: ")

# Melakukan stemming pada kata
output = stemmer.stem(text)

# Menampilkan hasil stemming
print("Kata asli:", text)
print("Setelah stemming:", output)
