<h1>📥 Queue Data Structure Implementation in Python</h1>

<p>
  Repositori ini berisi implementasi dan pemahaman operasi dasar pada struktur data <b>Queue (Antrean)</b> menggunakan bahasa pemrograman <b>Python</b>. Proyek ini berfokus pada penerapan konsep <i>First In, First Out</i> (FIFO) serta manipulasi elemen antrean.
</p>

<hr>

<h2>🛠️ Operasi & File Latihan</h2>
<p>Berikut adalah rincian materi dan file skrip Python yang ada di repositori ini:</p>

<ul>
  <li>
    <b>1. Enqueue (Penambahan Data)</b>
    <br><i>Implementasi penambahan elemen ke dalam antrean menggunakan metode <code>append()</code> dan <code>appendleft()</code> via modul <code>collections.deque</code>.</i>
  </li>
  <br>
  <li>
    <b>2. Dequeue (Pengambilan Data)</b>
    <br><i>Implementasi pengambilan atau penghapusan elemen dari antrean berdasarkan urutan masuk (FIFO) menggunakan class kustom.</i>
  </li>
  <br>
  <li>
    <b>3. Front & Rear</b>
    <br><i>Pengaksesan elemen paling depan (Front) dan elemen paling belakang (Rear) pada struktur antrean.</i>
  </li>
  <br>
  <li>
    <b>4. isEmpty Check</b>
    <br><i>Pengecekan kondisi apakah suatu antrean dalam keadaan kosong atau memiliki isi.</i>
  </li>
</ul>

<hr>

<h2>🖥️ Sample Output Program</h2>
<p>Berikut adalah contoh hasil keluaran (output terminal) dari masing-masing skrip Python:</p>

<h3>🔹 Enqueue1.py</h3>
<pre>
Data: deque(['anfasa', 'farhan', 'zaki', 'sultan'])
deque(['sayyid', 'anfasa', 'farhan', 'zaki', 'sultan'])
</pre>

<h3>🔹 Dequeue.py</h3>
<pre>
antrean Awal ['farhan', 'zaki', 'sayyid', 'anfasa', 'sultan']
Data yang keluar: farhan
Antrean Sekarang: ['zaki', 'sayyid', 'anfasa', 'sultan']
</pre>

<h3>🔹 Front.py</h3>
<pre>
data: ['farhan', 'anfasa', 'zaki', 'jagdish']
data: ['farhan', 'anfasa', 'zaki', 'jagdish', 'acaa']
front; farhan
</pre>

<h3>🔹 Rear.py</h3>
<pre>
data: ['farhan', 'anfasa', 'zaki', 'jagdish']
data: ['farhan', 'anfasa', 'zaki', 'jagdish', 'dwi']
rear; dwi
</pre>

<h3>🔹 isEmpty.py</h3>
<pre>
false
</pre>

<hr>

<h2>📁 Struktur Repositori</h2>
<pre>
struktur-data-python/
├── 📄 Enqueue1.py   # Operasi penambahan data (deque.append)
├── 📄 Dequeue.py    # Class Queue & operasi pengambilan data
├── 📄 Front.py      # Pengaksesan elemen terdepan (Front)
├── 📄 Rear.py       # Pengaksesan elemen terbelakang (Rear)
└── 📄 isEmpty.py    # Pengecekan kondisi antrean kosong
</pre>

<hr>

<h2>💻 Cara Menjalankan Program Secara Lokal</h2>
<ol>
  <li>
    Clone repositori ini ke komputer kamu:
    <pre><code>git clone https://github.com/siregarrhann-jpg/struktur-data-python.git</code></pre>
  </li>
  <li>
    Buka terminal/command prompt, lalu jalankan salah satu file Python:
    <pre><code>python Dequeue.py</code></pre>
  </li>
</ol>

<hr>

<p><i>Dikembangkan oleh <b>M. Farhan Annas Siregar</b> — Mahasiswa Teknik Informatika.</i></p>
