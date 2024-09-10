1. step 1 : membuat project django baru dilakukan dengan membuat direktori lokal dan mengaktifkan virtual environment
   step 2 : menjalankan python manage.py startapp main pada direktori utama untuk membuat app main
   step 3 : membuat file urls.py di main untuk mengatur routing URL di app main. Untuk routing proyek, tambahkan path('', include('main.urls')) di urls.py direktori utama bagian urlpatterns
   step 4 : mengisi models.py pada app main dengan class Product. Saya membuat 4 atribut yaitu name, price, description, dan image
   step 5 : mengisi views,py dengan data yang diinginkan sesuai model yang sudah dibuat. Kemudian membuat template html untuk isi konten app.
   step 6 : menambahkan  path('', show_product, name='show_product') di urls.py app main untuk mapping fungsi yang sudah dibuat di views.py
   step 7 : melakukan makemigration, migrate, kemudian git add, commit, push pws main:master
2. Client Request
      |
      v
+-----------------+
|   urls.py       |  <-- Cocokkan URL dengan pola dan mengarahkan ke view yang tepat.
+-----------------+
      |
      v
+-----------------+
|   views.py      |  <-- Handle logika permintaan dan memutuskan tindakan.
+-----------------+
      |
      v
+-----------------------------+
|   models.py (Opsional)       |  <-- Mengambil atau memodifikasi data di database.
+-----------------------------+
      |
      v
+-----------------------------+
|   HTML Template              |  <-- Render hasil ke dalam format HTML untuk dikirim ke client.
+-----------------------------+
      |
      v
Client Response

3.
  - Mengelola versi kode: Melacak setiap perubahan kode, agar masih bisa kembali ke versi sebelumnya.
  - Kolaborasi tim: Memungkinkan banyak pengembang bekerja secara bersamaan tanpa bentrok.
  - Branching: Bekerja pada fitur terpisah tanpa mempengaruhi kode utama.
  - Merging: Menggabungkan cabang terpisah kembali ke proyek utama.
  - Conflict handling: Menangani konflik saat dua orang mengubah bagian kode yang sama.
  - History: Menyimpan semua perubahan yang pernah dibuat.
  - Distribusi: Memungkinkan pekerjaan offline dengan salinan lengkap proyek.
  - Backup otomatis: Setiap salinan berfungsi sebagai cadangan proyek.

4.
  - Menyediakan banyak fitur bawaan (seperti otentikasi, routing, ORM) yang mengurangi kebutuhan untuk memasang banyak library eksternal sehingga bisa langsung fokus pada logika
    aplikasi tanpa khawatir soal hal-hal teknis dasar.
  - Menerapkan arsitektur Model-View-Template (MVT) sehingga memudahkan pemahaman alur aplikasi dan pengembangan software yang terorganisir.

5. Model pada Django disebut ORM (Object-Relational Mapping) karena menghubungkan objek Python dengan tabel di database. Dengan ORM, developer bisa bekerja dengan data di database seperti bekerja dengan objek Python, tanpa perlu SQL sebagai database.
    
