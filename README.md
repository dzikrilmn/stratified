# Tugas 1

1. step 1 : membuat project django baru dilakukan dengan membuat direktori lokal dan mengaktifkan virtual environment
   step 2 : menjalankan python manage.py startapp main pada direktori utama untuk membuat app main
   step 3 : membuat file urls.py di main untuk mengatur routing URL di app main. Untuk routing proyek, tambahkan path('', include('main.urls')) di urls.py direktori utama bagian urlpatterns
   step 4 : mengisi models.py pada app main dengan class Product. Saya membuat 4 atribut yaitu name, price, description, dan image
   step 5 : mengisi views,py dengan data yang diinginkan sesuai model yang sudah dibuat. Kemudian membuat template html untuk isi konten app.
   step 6 : menambahkan  path('', show_product, name='show_product') di urls.py app main untuk mapping fungsi yang sudah dibuat di views.py
   step 7 : melakukan makemigration, migrate, kemudian git add, commit, push pws main:master
2. Berikut merupakan diagram request client ke platform django
      ![alt text](image.png)

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

# Tugas 2

1. 
      - Optimalisasi Interaksi Antara Klien dan Server: Platform membutuhkan mekanisme yang efisien untuk pertukaran data antara klien (seperti browser atau aplikasi) dan server. Proses ini melibatkan pengiriman permintaan HTTP dan penerimaan respons HTTP, yang harus dijalankan dengan cepat dan tepat untuk mengurangi waktu tunggu dan meningkatkan kepuasan pengguna.

      - Pengelolaan Respons HTTP yang Efektif: Terdapat berbagai metode permintaan HTTP seperti GET, POST, PUT, PATCH, dan DELETE memainkan peran penting dalam CRUD (Create, Read, Update, Delete) operasi pada data. Platform perlu mengelola respons ini secara efisien untuk menjamin data yang diakses adalah akurat dan terkini, yang sangat penting dalam operasi seperti update konten dinamis atau transaksi e-commerce.

      - Penggunaan AJAX dan JSON untuk Komunikasi Asinkron: AJAX (Asynchronous JavaScript and XML) dan JSON (JavaScript Object Notation) memungkinkan penggunaan data secara asinkron, yang berarti pengguna dapat terus berinteraksi dengan halaman web sementara data lain sedang dimuat sehingga membantu meningkatkan responsivitas dan kecepatan platform, memungkinkan pengguna merasakan pengalaman yang lebih mulus tanpa harus menunggu halaman dimuat sepenuhnya.

2. 
      - Lebih Ringkas: JSON memiliki format yang lebih sederhana dan ukuran file yang lebih kecil dibandingkan XML.
      - Lebih Cepat: JSON lebih cepat diproses karena lebih ringan dan mudah di-parse oleh bahasa pemrograman seperti JavaScript.
      - Kompatibilitas: JSON secara alami kompatibel dengan banyak bahasa pemrograman modern, khususnya JavaScript.
      - Mudah Dibaca: JSON lebih mudah dibaca oleh manusia dan mesin karena sintaks yang sederhana.
      - Populer di API Modern: JSON lebih umum digunakan dalam AJAX dan RESTful APIs karena kecepatan dan efisiensinya.

3. Dalam Django, method is_valid() digunakan pada form untuk memeriksa apakah data yang diinput oleh pengguna sesuai dengan aturan validasi yang telah didefinisikan di dalam form tersebut. Fungsi ini sangat penting untuk memastikan bahwa hanya data yang valid yang akan diproses lebih lanjut, seperti disimpan dalam database.

      ```
      form = ProductEntryForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
      form.save()  # Data valid disimpan ke database
      return redirect('main:show_main')
      ```

4. csrf_token dibutuhkan di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Token ini memastikan bahwa permintaan yang dikirim berasal dari sumber yang sah dan mencegah penyerang mengirim permintaan palsu atas nama pengguna.

      Tanpa csrf_token, aplikasi menjadi rentan terhadap serangan CSRF, di mana penyerang dapat memanfaatkan session pengguna yang valid untuk melakukan tindakan berbahaya seperti perubahan data atau transaksi tanpa sepengetahuan pengguna.

5. 
      - buat forms.py untuk input data:
            
            from django.forms import ModelForm
            from main.models import Product

            class ProductEntryForm(ModelForm):
            class Meta:
                  model = Product
                  fields = ["name", "price", "description"]
        
      - update views.py untuk form:
            
            from django.shortcuts import render, redirect
            from .forms import ProductEntryForm

            def create_product_entry(request):
            form = ProductEntryForm(request.POST or None)
            if form.is_valid() and request.method == 'POST':
                  form.save()
                  return redirect('main:show_main')
            return render(request, 'create_product_entry.html', {'form': form})

      - buat template form di create_product_entry.html
      - buat View untuk Format XML dan JSON

            from django.http import HttpResponse
            from django.core import serializers
            from .models import Product
                        
            def show_xml(request):
            data = Product.objects.all()

            def show_xml(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

            def show_json(request):
            data = Product.objects.all()

            def show_json(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

      - update routibg url :

            from django.urls import path
            from main.views import show_main
            from main.views import show_main, create_product_entry
            from main.views import show_main, create_product_entry, show_xml
            from main.views import show_main, create_product_entry, show_xml, show_json

            app_name = 'main'

            urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product-entry', create_product_entry, name='create_product_entry'),
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            ]

      ![alt text](image-1.png)
      ![alt text](image-2.png)





      



