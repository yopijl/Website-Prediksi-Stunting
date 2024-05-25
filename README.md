# Sistem Prediksi Stunting Berbasis Web dengan Rekomendasi Kesehatan

# Deskripsi Singkat:
Proyek ini adalah sebuah aplikasi web yang dirancang untuk mendeteksi status stunting pada anak berdasarkan input data antropometri (tinggi badan dan umur) dan jenis kelamin. Sistem ini tidak hanya memberikan prediksi status stunting tetapi juga menyarankan langkah-langkah yang tepat untuk penanganan lebih lanjut. Proyek ini bertujuan untuk membantu orang tua dan tenaga medis dalam mendeteksi dini masalah stunting dan mengambil tindakan yang tepat untuk mengatasi masalah tersebut.

# Fitur Utama:
1. Input Data Antropometri: Pengguna dapat memasukkan data tinggi badan (dalam cm), umur (dalam bulan), dan jenis kelamin (laki-laki atau perempuan) anak.
2. Prediksi Status Stunting: Berdasarkan data yang diinput, sistem akan memprediksi status stunting anak yang terbagi menjadi empat kategori: Severely Stunted, Stunted, Normal, dan Tinggi.
3. Rekomendasi Kesehatan: Setelah prediksi status stunting ditampilkan, sistem juga memberikan rekomendasi kesehatan yang sesuai untuk setiap kategori. Rekomendasi ini mencakup saran tindakan selanjutnya setelah mengetahui hasil prediksi.

# Teknologi yang Digunakan:
1. Frontend: HTML5, CSS3, Bootstrap 4 untuk tampilan antarmuka pengguna yang responsif dan menarik.
2. Backend: Javascript dan Flask (Python) untuk logika aplikasi dan integrasi model prediksi.
3. Machine Learning: Model prediksi yang dilatih menggunakan algoritma machine learning untuk mengklasifikasikan status stunting berdasarkan data antropometri.
4. Libraries: Numpy untuk manipulasi array dan Pickle untuk memuat model prediksi.
   
# Arsitektur Sistem:
1. User Interface: Pengguna menginput data melalui formulir di halaman web.
2. Server-Side Processing: Data dikirim ke server Flask, di mana model machine learning memproses data dan menghasilkan prediksi status stunting.
3. Output: Hasil prediksi dan rekomendasi kesehatan ditampilkan kembali kepada pengguna di halaman web.
   
# Manfaat Proyek:
1. Deteksi Dini: Membantu orang tua dan tenaga medis dalam mendeteksi dini masalah stunting pada anak.
2. Aksi Preventif: Memberikan rekomendasi yang dapat membantu dalam pengambilan tindakan preventif atau korektif untuk menangani stunting.
3. Kemudahan Akses: Aplikasi berbasis web yang mudah diakses dari berbagai perangkat, membuatnya praktis untuk digunakan kapan saja dan di mana saja.
