#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deck Data: Suit of Swords (14 Cards: Ace to King)
Element of Air: Mind, Intellect, Truth, Clarity, Justice, Communication, Overcoming Mental Conflict.
"""

SWORDS_CARDS = [
    {
        "id": "ace-of-swords",
        "name": "Ace of Swords",
        "slug": "ace-of-swords",
        "image": "/assets/tarot/cards/Ace of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "Ace",
        "uprightKeywords": ["Terobosan Mental", "Kejernihan Mutlak", "Kebenaran Tajam", "Keputusan Tegas", "Pedang Keadilan"],
        "reversedKeywords": ["Kebingungan Pikiran", "Kata-kata Menyakitkan", "Penyalahgunaan Nalar", "Keraguan Ekstrem"],
        "description": "Sebuah tangan putih muncul dari awan menggenggam pedang bermata dua tegak lurus yang menembus mahkota emas berhias daun zaitun dan palem. Latar belakangnya adalah pegunungan tandus dan langit biru jernih. Ace of Swords melambangkan kejernihan pikiran mutlak, terobosan intelektual, penyingkapan kebenaran tanpa kompromi, dan ketegasan memutus ilusi.",
        "readings": {
            "love": {
                "title": "Kejernihan Komunikasi dan Pengungkapan Kebenaran Hati",
                "summary": "Membicarakan hal yang mengganjal dengan kejujuran tulus dan memutus pola kebohongan.",
                "meaning": "Ace of Swords dalam percintaan adalah pedang kejujuran. Waktu untuk berpura-pura telah usai. Kamu dan pasangan diajak melakukan percakapan yang jujur, terbuka, dan langsung ke inti masalah. Meski terasa tajam pada awalnya, kejujuran inilah yang akan membebaskan hubunganmu dari kepalsuan.",
                "advice": "Bicaralah dengan jujur namun tetap santun; gunakan kata-katamu untuk memperjelas keadaan, bukan untuk melukai.",
                "reflectionQuestion": "Kebenaran apa dalam hubunganmu yang selama ini kamu pendam dan kini siap kamu ungkapkan?",
                "keywords": ["Kejujuran Mutlak", "Percakapan Terbuka", "Memutus Kebohongan", "Kejernihan Asmara"]
            },
            "work": {
                "title": "Terobosan Logika dan Solusi Masalah yang Tajam",
                "summary": "Menemukan akar masalah kerja yang rumit dan menyusun solusi yang sangat presisi.",
                "meaning": "Di lingkungan kerja, Ace of Swords adalah anugerah ketajaman analisis. Kabut kebingungan sirna dan kamu melihat inti persoalan proyek dengan sangat jelas. Keputusan yang kamu ambil tepat sasaran dan mampu memotong rantai birokrasi yang berbelit-belit.",
                "advice": "Gunakan argumen berbasis data dan logika yang kokoh; sampaikan gagasanmu secara lugas tanpa bertele-tele.",
                "reflectionQuestion": "Masalah kerja rumit apa yang saat ini dapat kamu selesaikan dengan analisis yang tajam dan objektif?",
                "keywords": ["Analisis Presisi", "Solusi Tajam", "Logika Kokoh", "Memotong Birokrasi"]
            },
            "career": {
                "title": "Keputusan Karier yang Menentukan dan Visi Jernih",
                "summary": "Membuat keputusan tegas mengenai arah profesi dan memenangkan negosiasi penting.",
                "meaning": "Karier di bawah pengaruh kartu ini menandakan keberhasilan dalam ujian kompetensi, debat profesional, atau penandatanganan kontrak penting. Ketajaman intelektualmu diakui oleh pimpinan. Kamu memiliki otoritas untuk memimpin perubahan strategis.",
                "advice": "Berdirilah di atas kebenaran dan fakta; jadikan integritas intelektual sebagai pembeda utamamu.",
                "reflectionQuestion": "Keputusan profesional tegas apa yang perlu kamu ambil hari ini untuk mempercepat kemajuan kariermu?",
                "keywords": ["Keputusan Tegas", "Otoritas Intelektual", "Negosiasi Menang", "Integritas Karier"]
            },
            "finance": {
                "title": "Audit Keuangan yang Ketat dan Memotong Beban",
                "summary": "Mengambil keputusan tegas memangkas pengeluaran yang tidak perlu demi menyelamatkan anggaran.",
                "meaning": "Secara finansial, Ace of Swords menuntut ketegasan memotong pos-pos anggaran yang bocor. Singkirkan langganan yang tidak terpakai, pangkas biaya konsumtif, dan buat rencana pembayaran utang yang ketat. Kejernihan angka-angka riil adalah penyelamat keuanganmu.",
                "advice": "Lakukan audit kas secara objektif; jangan ragu memotong pengeluaran gengsi demi kestabilan masa depan.",
                "reflectionQuestion": "Pengeluaran apa yang jika kamu potong secara tegas hari ini akan memberikan kelegaan finansial terbesar?",
                "keywords": ["Potong Pengeluaran", "Audit Kas Ketat", "Kejernihan Angka", "Keputusan Finansial"]
            },
            "selfGrowth": {
                "title": "Memutus Pola Pikir Negatif (Mental Breakthrough)",
                "summary": "Menggunakan pedang kesadaran untuk memenggal pikiran overthinking dan ilusi ketakutan.",
                "meaning": "Pengembangan diri kartu Ace of Swords adalah kemenangan akal budi atas kekacauan emosi. Kamu tidak lagi menjadi budak dari narasi negatif di kepalamu sendiri. Dengan pedang ketajaman pikiran, kamu membedah mana ketakutan yang nyata dan mana yang sekadar drama buatan egomu.",
                "advice": "Tuliskan kekhawatiranmu dan bantah satu per satu dengan fakta objektif; bebaskan pikiranmu dari penjara ilusi.",
                "reflectionQuestion": "Keyakinan salah atau mitos tentang dirimu apa yang siap kamu tebas dengan pedang kebenaran hari ini?",
                "keywords": ["Mental Breakthrough", "Memotong Overthinking", "Kejernihan Budi", "Pedang Kesadaran"]
            },
            "relationships": {
                "title": "Menegaskan Batasan Personal dan Mengakhiri Drama",
                "summary": "Menyelesaikan kesalahpahaman sosial dengan komunikasi yang lugas dan tidak ambigu.",
                "meaning": "Dalam pergaulan dan keluarga, kartu ini meminta ketegasan bersikap. Jika ada desas-desus atau gosip yang merugikan, hadapi secara langsung dengan klarifikasi terbuka di depan semua pihak. Kebenaran yang disampaikan dengan santun akan menghentikan fitnah seketika.",
                "advice": "Lakukan klarifikasi secara langsung kepada pihak terkait; hindari berbicara di belakang punggung orang lain.",
                "reflectionQuestion": "Kesalahpahaman apa dalam lingkaran pergaulanmu yang perlu kamu luruskan dengan kejujuran?",
                "keywords": ["Klarifikasi Tegas", "Hentikan Gosip", "Komunikasi Lugas", "Batasan Jelas"]
            },
            "spirituality": {
                "title": "Pedang Kebenaran Ilahi yang Memisahkan Hak dan Batil",
                "summary": "Mendapatkan karunia furqan: kemampuan membedakan jalan yang lurus dari kesesatan.",
                "meaning": "Secara spiritual, Ace of Swords adalah pedang Al-Haq (Kebenaran Mutlak Tuhan). Di hadapan cahaya kebenaran, segala kepalsuan dan kemunafikan akan tersingkap. Jiwamu dianugerahi kejernihan untuk melihat mana jalan yang diridhai Tuhan dan mana yang menjauhkanmu dari-Nya.",
                "advice": "Pilihlah kebenaran meski terasa pahit; mohonkan keteguhan iman agar kakimu senantiasa kokoh di jalan yang lurus.",
                "reflectionQuestion": "Bagaimana caramu menjadikan kebenaran firman Tuhan sebagai standar penilai seluruh perbuatanmu?",
                "keywords": ["Pedang Al-Haq", "Pemisah Hak dan Batil", "Kejernihan Iman", "Jalan Lurus"]
            }
        }
    },
    {
        "id": "two-of-swords",
        "name": "Two of Swords",
        "slug": "two-of-swords",
        "image": "/assets/tarot/cards/Two of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "2",
        "uprightKeywords": ["Dilema Sulit", "Mata Tertutup", "Kebuntuan Keputusan", "Gencatan Senjata", "Menimbang Logika"],
        "reversedKeywords": ["Membuka Penutup Mata", "Kebenaran Terungkap", "Mengambil Keputusan", "Keluar dari Kebuntuan"],
        "description": "Seorang wanita bergaun putih dengan mata tertutup kain duduk di bangku batu di tepi laut berbatu di bawah bulan sabit, menyilangkan dua pedang berat di dadanya secara simetris. Two of Swords melambangkan kebuntuan pikiran, dilema sulit antara dua pilihan yang sama beratnya, penutupan mata terhadap fakta menyakitkan, dan perlunya ketenangan batin untuk mengambil keputusan.",
        "readings": {
            "love": {
                "title": "Dilema Hati dan Penyangkalan Kenyataan Asmara",
                "summary": "Menolak melihat kenyataan dalam hubungan karena takut menghadapi rasa sakit atau perpisahan.",
                "meaning": "Two of Swords dalam percintaan menandakan kebuntuan emosional. Kamu mungkin berada di antara dua pilihan sulit atau sengaja menutup mata terhadap masalah nyata dalam hubungan demi menjaga kedamaian semu (gencatan senjata). Menunda keputusan hanya akan memperpanjang ketegangan batinmu.",
                "advice": "Buka penutup matamu dan hadapi kenyataan; perdamaian sejati hanya lahir setelah kamu berani menatap kebenaran.",
                "reflectionQuestion": "Kenyataan pahit apa dalam hubunganmu yang selama ini kamu tolak untuk kamu lihat secara jujur?",
                "keywords": ["Dilema Asmara", "Buka Mata Hati", "Hindari Penyangkalan", "Keputusan Sulit"]
            },
            "work": {
                "title": "Kebuntuan Keputusan dan Konflik Kepentingan",
                "summary": "Dihadapkan pada dua opsi strategi kerja yang bertentangan dan memerlukan pertimbangan matang.",
                "meaning": "Di lingkungan kerja, proyek mengalami jalan buntu karena adanya perbedaan pandangan tajam antarpimpinan. Kamu mungkin merasa terjepit di tengah konflik kepentingan. Waktu jeda ini diperlukan untuk mengumpulkan data tambahan sebelum menentukan langkah terbaik.",
                "advice": "Jangan terburu-buru memilih di bawah tekanan; cari pihak ketiga yang netral untuk membantu menimbang opsi.",
                "reflectionQuestion": "Data objektif apa yang masih kurang untuk membantumu mengambil keputusan kerja terbaik?",
                "keywords": ["Jalan Buntu Proyek", "Menimbang Opsi", "Netralitas", "Kumpulkan Fakta"]
            },
            "career": {
                "title": "Persimpangan Karier: Bertahan atau Melompat",
                "summary": "Dilema antara kenyamanan posisi saat ini dengan risiko mencoba peluang baru yang menantang.",
                "meaning": "Karier di bawah pengaruh Two of Swords menandakan keraguan profesional. Kamu memiliki dua tawaran atau dua jalur karier yang sama-sama memiliki kelebihan dan kekurangan. Keengganan mengambil risiko membuatmu merasa mandek.",
                "advice": "Daftarkan pro dan kontra secara tertulis; ingatlah bahwa tidak membuat keputusan pun sesungguhnya adalah sebuah keputusan.",
                "reflectionQuestion": "Pilihan karier mana yang jika kamu ambil akan paling mendorong pertumbuhan pribadimu dalam lima tahun ke depan?",
                "keywords": ["Persimpangan Karier", "Pro dan Kontra", "Hentikan Keraguan", "Langkah Berani"]
            },
            "finance": {
                "title": "Menunda Keputusan Pengeluaran Besar",
                "summary": "Membekukan transaksi atau investasi sementara waktu hingga situasinya menjadi lebih jelas.",
                "meaning": "Secara finansial, kartu ini menyarankan sikap 'wait and see'. Jangan menandatangani kontrak pinjaman atau investasi baru saat pikiranmu masih diliputi keraguan. Ketenangan pikiran jauh lebih berharga daripada terburu-buru mengambil risiko yang tidak kamu pahami.",
                "advice": "Simpan danamu dalam instrumen yang likuid dan aman; tunggu hingga ketidakpastian pasar mereda.",
                "reflectionQuestion": "Keputusan keuangan apa yang sebaiknya kamu tunda keputusannya sampai informasi lebih lengkap?",
                "keywords": ["Wait and See", "Bekukan Transaksi", "Hindari Spekulasi", "Ketenangan Materi"]
            },
            "selfGrowth": {
                "title": "Keberanian Membuka Mata Batin dan Menghadapi Fakta",
                "summary": "Berhenti lari dari kenyataan hidup dan berani mengambil tanggung jawab atas pilihanmu.",
                "meaning": "Pengembangan diri kartu Two of Swords adalah tentang mengatasi cognitive dissonance (penyangkalan kognitif). Kita sering menutup mata kita sendiri bukan karena tidak tahu, melainkan karena takut pada rasa sakit yang ditimbulkan oleh kebenaran. Membuka penutup mata adalah langkah awal kemerdekaan jiwamu.",
                "advice": "Akui apa yang kamu rasakan tanpa rasa malu; hadapi realitas dengan keberanian dan ketenangan hati.",
                "reflectionQuestion": "Fakta tentang dirimu atau hidupmu apa yang paling membuatmu takut untuk kamu akui secara terbuka?",
                "keywords": ["Buka Penutup Mata", "Atasi Penyangkalan", "Tatap Kenyataan", "Kemerdekaan Pikiran"]
            },
            "relationships": {
                "title": "Gencatan Senjata dan Meredakan Ketegangan Keluarga",
                "summary": "Mengambil jeda dari perdebatan keluarga demi mencegah kata-kata kasar yang melukai.",
                "meaning": "Dalam pergaulan dan keluarga, Two of Swords menandakan gencatan senjata sementara. Kedua belah pihak memilih untuk tidak memperpanjang perdebatan agar suasana tidak memanas. Gunakan waktu hening ini untuk mendinginkan kepala sebelum memulai dialog kembali.",
                "advice": "Hormati keheningan sejenak; jangan paksakan berdialog saat emosi salah satu pihak masih membara.",
                "reflectionQuestion": "Bagaimana caramu menciptakan suasana dialog yang aman saat ketegangan keluarga mereda?",
                "keywords": ["Gencatan Senjata", "Jeda Mendinginkan", "Hindari Menyakiti", "Dialog Santun"]
            },
            "spirituality": {
                "title": "Mencari Petunjuk di Tengah Keheningan Samudra Batin",
                "summary": "Menyilangkan pedang logika demi mendengarkan bisikan nurani di hadirat Tuhan.",
                "meaning": "Secara spiritual, wanita bermata tertutup melambangkan penarikan indra lahiriah (pratyahara). Ketika pandangan fisik dimatikan dan nalar berhenti berdebat, telinga batinmu mulai mampu mendengar bisikan petunjuk Tuhan yang lembut. Di dalam keheningan total, jawaban yang kamu cari akan tersingkap.",
                "advice": "Lakukan salat sunnah atau meditasi hening di tengah malam; mintalah kepada Tuhan agar membuka tabir keraguan hatimu.",
                "reflectionQuestion": "Bagaimana caramu menenangkan kebisingan pikiran agar suara petunjuk Tuhan dapat terdengar jelas?",
                "keywords": ["Penarikan Indra", "Keheningan Total", "Salat Istikharah", "Tabir Tersingkap"]
            }
        }
    },
    {
        "id": "three-of-swords",
        "name": "Three of Swords",
        "slug": "three-of-swords",
        "image": "/assets/tarot/cards/Three of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "3",
        "uprightKeywords": ["Patah Hati", "Luka Emosional", "Kekecewaan Mendalam", "Kebenaran Menyakitkan", "Pembersihan Jiwa"],
        "reversedKeywords": ["Pemulihan Luka", "Memaafkan Pengkhianatan", "Pelepasan Rasa Sakit", "Optimisme Bangkit"],
        "description": "Sebuah jantung merah melayang di tengah awan badai abu-abu dan hujan lebat, tertusuk oleh tiga bilah pedang baja. Three of Swords melambangkan patah hati, luka emosional mendalam, kekecewaan akibat pengkhianatan atau kata-kata kasar, namun juga mengajarkan bahwa rasa sakit adalah sarana pembersihan jiwa menuju kedewasaan hakiki.",
        "readings": {
            "love": {
                "title": "Luka Patah Hati dan Mengobati Kekecewaan Asmara",
                "summary": "Menghadapi kenyataan pahit pengkhianatan atau perpisahan dengan ketabahan jiwa.",
                "meaning": "Three of Swords adalah simbol luka asmara yang paling nyata: kata-kata yang menyayat hati, perselisihan yang membekas, atau perpisahan yang tak terhindarkan. Rasa sakit yang kamu rasakan adalah nyata dan valid. Namun ingatlah, hujan badai ini sedang membersihkan hatimu agar siap menerima cinta yang lebih suci di kemudian hari.",
                "advice": "Izinkan dirimu berduka dan menangis; jangan tutupi rasa sakitmu dengan kepura-puraan tegar yang palsu.",
                "reflectionQuestion": "Luka emosional apa yang saat ini paling membutuhkan pelukan welas asih dan pengampunan darimu?",
                "keywords": ["Patah Hati", "Luka Emosional", "Tangisan Pembersih", "Validasi Rasa Sakit"]
            },
            "work": {
                "title": "Kritik Tajam dan Kekecewaan Profesional",
                "summary": "Menerima kabar buruk mengenai proyek kerja atau kritik pedas yang menusuk harga diri.",
                "meaning": "Di lingkungan kerja, kamu mungkin mengalami penolakan usulan yang menyakitkan, pembatalan kontrak sepihak, atau kritik kasar dari atasan. Pisahkan antara kritik terhadap hasil kerja dengan nilai dirimu sebagai manusia. Jangan biarkan kekecewaan kerja merusak rasa percaya dirimu.",
                "advice": "Tarik napas dalam-dalam dan jangan membalas dengan amarah; ambil intisari pelajarannya dan perbaiki kualitas kinerjamu.",
                "reflectionQuestion": "Bagaimana caramu memisahkan antara kritik profesional yang membangun dengan serangan emosional yang tidak berdasar?",
                "keywords": ["Kritik Tajam", "Evaluasi Diri", "Ketahanan Mental", "Jangan Ambil Hati"]
            },
            "career": {
                "title": "Menghadapi Kemunduran Karier dan Pengkhianatan Rekan",
                "summary": "Melewati masa-masa pahit persaingan tidak sehat demi menemukan arah yang lebih bermartabat.",
                "meaning": "Karier di bawah pengaruh Three of Swords menguji integritasmu. Ada rekan yang mungkin menusuk dari belakang atau ingkar janji bisnis. Pengalaman pahit ini adalah pelajaran berharga tentang siapa yang layak kamu percaya. Bangkitlah dari rasa sakit ini dengan profesionalisme yang lebih matang.",
                "advice": "Dokumentasikan seluruh fakta secara profesional; selesaikan masalah dengan jalur resmi dan elegan tanpa dendam.",
                "reflectionQuestion": "Pelajaran kebijaksanaan apa yang kamu peroleh dari peristiwa pengkhianatan profesional ini?",
                "keywords": ["Ujian Integritas", "Pelajaran Kepercayaan", "Jalur Resmi", "Kedewasaan Karier"]
            },
            "finance": {
                "title": "Kerugian Finansial yang Menyakitkan dan Pemulihan",
                "summary": "Kekecewaan akibat tertipu investasi atau kerugian modal yang menuntut keikhlasan lapang dada.",
                "meaning": "Secara finansial, kartu ini melambangkan guncangan kerugian materi: utang yang tidak dibayar teman, investasi yang anjlok drastis, atau biaya darurat tak terduga. Rasa sesal itu wajar, namun jangan biarkan uang yang hilang merenggut kesehatan mental dan kebahagiaan hidupmu.",
                "advice": "Ikhlaskan apa yang telah hilang; tata kembali anggaranmu dari nol dengan strategi yang jauh lebih hati-hati.",
                "reflectionQuestion": "Bagaimana caramu memandang kerugian materi ini sebagai biaya belajar untuk menjadi lebih bijak mengelola uang?",
                "keywords": ["Kerugian Menyakitkan", "Keikhlasan Materi", "Tata Ulang Anggaran", "Pelajaran Finansial"]
            },
            "selfGrowth": {
                "title": "Alkimia Patah Hati: Mengubah Luka Menjadi Kebijaksanaan",
                "summary": "Menyadari bahwa hati yang pernah patah adalah hati yang memiliki ruang empati paling luas.",
                "meaning": "Pengembangan diri kartu Three of Swords adalah rahasia para bijak bestari. Seperti kata Rumi, 'Luka adalah tempat di mana cahaya masuk ke dalam dirimu.' Manusia yang tidak pernah terluka sering kali sombong dan kurang berempati. Rasa sakit yang kamu alami hari ini sedang melunakkan hatimu menjadi pribadi yang penuh kasih sayang.",
                "advice": "Rawatlah hatimu yang terluka selayaknya merawat anak kecil yang sakit; jadikan lukamu sebagai pintu masuk cahaya Tuhan.",
                "reflectionQuestion": "Bagaimana luka masa lalumu telah membentukmu menjadi pribadi yang lebih bijak dan berempati hari ini?",
                "keywords": ["Cahaya Masuk", "Empati Mendalam", "Alkimia Luka", "Hati Melunak"]
            },
            "relationships": {
                "title": "Menyembuhkan Keretakan Akibat Kata-kata Menyakitkan",
                "summary": "Memulihkan hubungan keluarga yang sempat terluka oleh amarah atau kesalahpahaman masa lalu.",
                "meaning": "Dalam keluarga dan persahabatan, Three of Swords melambangkan lidah yang lebih tajam daripada pedang. Kata-kata kasar di masa lalu masih menyisakan perih di dada. Untuk menyembuhkannya, dibutuhkan pengakuan kesalahan yang tulus dan waktu untuk memulihkan rasa saling percaya.",
                "advice": "Mintalah maaf secara tulus jika kamu pernah melukai hati orang lain; belajarlah memaafkan mereka yang menyakitimu.",
                "reflectionQuestion": "Kata-kata menyakitkan apa yang pernah kamu lontarkan yang kini perlu kamu tebus dengan permohonan maaf tulus?",
                "keywords": ["Lidah Tajam", "Permohonan Maaf", "Penyembuhan Retak", "Memaafkan Tulus"]
            },
            "spirituality": {
                "title": "Hati yang Hancur di Hadapan Keagungan Tuhan",
                "summary": "Menyadari bahwa Tuhan amat dekat dengan hati hamba-hamba-Nya yang sedang hancur terluka.",
                "meaning": "Secara spiritual, Three of Swords adalah misteri 'qalb al-munkasir' (hati yang remuk redam). Dalam sebuah hadis qudsi disebutkan: 'Aku berada di sisi orang-orang yang remuk redam hatinya karena mengingat-Ku.' Saat segala sandaran duniamu hancur, saat itulah jiwamu paling dekat dengan hadirat Ilahi.",
                "advice": "Tumpahkan seluruh air matamu dalam sujud panjang; rasakan betapa Tuhan sedang memeluk dan membalut luka hatimu.",
                "reflectionQuestion": "Bagaimana kamu merasakan kehadiran dan penghiburan Tuhan di saat-saat paling sunyi dan menyakitkan dalam hidupmu?",
                "keywords": ["Qalb Munkasir", "Pelukan Ilahi", "Sujud Panjang", "Penghiburan Suci"]
            }
        }
    },
    {
        "id": "four-of-swords",
        "name": "Four of Swords",
        "slug": "four-of-swords",
        "image": "/assets/tarot/cards/Four of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "4",
        "uprightKeywords": ["Istirahat Total", "Pemulihan Pikiran", "Meditasi Tenang", "Retret Batin", "Menyepi Sementara"],
        "reversedKeywords": ["Kelelahan Akut", "Terbangun dari Tidur", "Menolak Istirahat", "Kembali Beraktivitas"],
        "description": "Patung seorang ksatria berbaju zirah berbaring tenang dengan tangan terkatup berdoa di atas makam batu di dalam gereja tua. Tiga pedang tergantung di dinding di atasnya menunjuk ke bawah, dan satu pedang terukir mendatar di sisi ranjang makamnya. Cahaya jendela kaca patri bergambar orang suci menyinari keheningan ruangan. Four of Swords melambangkan istirahat total, pemulihan mental setelah pertempuran sengit, meditasi sunyi, dan pengisian ulang daya jiwa.",
        "readings": {
            "love": {
                "title": "Jeda Tenang dari Perdebatan Asmara",
                "summary": "Mengambil waktu untuk beristirahat dan menenangkan emosi sebelum melanjutkan pembicaraan penting.",
                "meaning": "Four of Swords dalam percintaan menyarankan gencatan emosi total. Jika kamu dan pasangan baru saja melewati pertengkaran yang melelahkan, jangan paksakan mencari penyelesaian sekarang. Luangkan waktu untuk tidur cukup, merenung dalam hening, dan membiarkan amarah mereda secara alami.",
                "advice": "Sepakati jeda istirahat bersama pasangan; gunakan waktu ini untuk menenangkan pikiran masing-masing.",
                "reflectionQuestion": "Apakah kamu dan pasangan membutuhkan waktu untuk beristirahat sejenak demi memulihkan kejernihan pikiran?",
                "keywords": ["Jeda Tenang", "Pemulihan Emosi", "Ketenangan Tidur", "Hindari Reaktif"]
            },
            "work": {
                "title": "Mengambil Cuti dan Mencegah Burnout",
                "summary": "Mengistirahatkan pikiran dari beban kerja yang menumpuk demi menjaga kesehatan mental dan fisik.",
                "meaning": "Di lingkungan kerja, kartu ini adalah resep dokter untuk mengambil cuti. Otakmu sudah bekerja melampaui batas kapasitasnya. Memaksakan diri terus bekerja dalam kondisi kelelahan akut hanya akan menghasilkan kesalahan fatal dan menurunkan produktivitasmu secara drastis.",
                "advice": "Ajukan cuti kerja segera; matikan surel kantor selama akhir pekan dan nikmati istirahat total tanpa rasa bersalah.",
                "reflectionQuestion": "Kapan terakhir kali kamu benar-benar beristirahat tanpa memikirkan tugas-tugas pekerjaanmu?",
                "keywords": ["Ambil Cuti", "Cegah Burnout", "Istirahat Total", "Pemulihan Mental"]
            },
            "career": {
                "title": "Masa Hibernasi Strategis dan Pengisian Ulang Daya",
                "summary": "Menarik diri sejenak dari hiruk-pikuk industri untuk merencanakan langkah besar berikutnya.",
                "meaning": "Karier di bawah pengaruh Four of Swords menandakan fase konsolidasi dan inkubasi. Sebelum meluncurkan kampanye baru atau memulai jabatan baru, kamu perlu mengosongkan cawan pikiranmu. Ksatria yang bijak selalu mengasah pedangnya dalam keheningan sebelum terjun ke medan laga berikutnya.",
                "advice": "Gunakan masa jeda ini untuk membaca buku, belajar hal baru dengan tenang, dan memulihkan vitalitas energimu.",
                "reflectionQuestion": "Bagaimana kamu memanfaatkan masa hibernasi karier ini untuk mempersiapkan kebangkitan profesionalmu?",
                "keywords": ["Hibernasi Strategis", "Mengasah Pedang", "Inkubasi Ide", "Vitalitas Pulih"]
            },
            "finance": {
                "title": "Membekukan Transaksi dan Menghentikan Pengeluaran Impulsif",
                "summary": "Mengambil jeda dari aktivitas belanja dan membiarkan rekening tabunganmu beristirahat.",
                "meaning": "Secara finansial, Four of Swords adalah 'puasa belanja'. Jangan melakukan pembelian barang-barang besar atau membuat komitmen keuangan baru saat ini. Biarkan arus kasmu tenang dan stabil tanpa gangguan spekulasi materi.",
                "advice": "Terapkan tantangan no-spend week (minggu tanpa belanja sekunder); nikmati apa yang sudah ada di rumahmu.",
                "reflectionQuestion": "Pengeluaran apa yang dapat kamu hentikan selama dua minggu ke depan untuk menenangkan keuanganmu?",
                "keywords": ["Puasa Belanja", "Kestabilan Kas", "No-Spend Week", "Ketenangan Materi"]
            },
            "selfGrowth": {
                "title": "Seni Keheningan: Meditasi dan Tidur yang Berkualitas",
                "summary": "Memulihkan sistem saraf tubuh melalui keheningan, relaksasi napas, dan istirahat mendalam.",
                "meaning": "Pengembangan diri kartu Four of Swords adalah tentang pentingnya keheningan (stillness). Di zaman modern yang serba bising, kemampuan untuk duduk diam tanpa melakukan apa pun adalah kekuatan langka. Berbaring tenang dan berdoa akan menyembuhkan peradangan batin dan memulihkan ketajaman intuisimu.",
                "advice": "Lakukan latihan pernapasan dalam setiap malam sebelum tidur; ciptakan kamar tidur yang gelap, sejuk, dan bebas gawai.",
                "reflectionQuestion": "Bagaimana caramu menciptakan ruang keheningan suci di tengah rutinitas harianmu yang padat?",
                "keywords": ["Keheningan Suci", "Tidur Berkualitas", "Penyembuhan Saraf", "Relaksasi Napas"]
            },
            "relationships": {
                "title": "Menjaga Jarak Sejenak dari Riuhnya Pergaulan Sosial",
                "summary": "Mengambil waktu untuk diri sendiri tanpa merasa bersalah menolak ajakan kumpul sosial.",
                "meaning": "Dalam pergaulan dan keluarga, kamu membutuhkan masa detoks sosial. Kamu tidak marah pada siapa pun; kamu hanya sedang kehabisan energi sosial (social battery). Sahabat sejati akan memahami dan menghormati kebutuhanmu untuk beristirahat di rumah.",
                "advice": "Tolak ajakan kumpul dengan santun dan ramah; jelaskan bahwa kamu sedang butuh waktu beristirahat.",
                "reflectionQuestion": "Berapa banyak waktu kesendirian yang kamu butuhkan minggu ini untuk mengisi ulang energimu?",
                "keywords": ["Detoks Sosial", "Baterai Sosial", "Istirahat di Rumah", "Menolak Santun"]
            },
            "spirituality": {
                "title": "Khalwat di Dalam Bait Ibadah yang Tenang",
                "summary": "Menyepi sejenak dari hiruk-pikuk duniawi demi bertafakur di hadirat Sang Maha Damai.",
                "meaning": "Secara spiritual, Four of Swords adalah laku khalwat atau iktikaf di dalam bait suci. Tiga pedang di dinding melambangkan pikiran yang telah digantungkan dengan tenang di hadapan Tuhan. Di bawah cahaya jendela kaca patri ilahi, jiwamu dibasuh oleh ketenteraman surgawi yang melampaui segala pemahaman manusia.",
                "advice": "Luangkan waktu beriktikaf di tempat ibadah atau menyepi di sudut kamar untuk bertafakur dan bermunajat.",
                "reflectionQuestion": "Bagaimana rasanya membiarkan jiwamu beristirahat sepenuhnya di dalam pelukan rahmat Tuhan?",
                "keywords": ["Khalwat Iktikaf", "Tafakur Tenang", "Bait Ibadah", "Ketenteraman Surgawi"]
            }
        }
    },
    {
        "id": "five-of-swords",
        "name": "Five of Swords",
        "slug": "five-of-swords",
        "image": "/assets/tarot/cards/Five of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "5",
        "uprightKeywords": ["Kemenangan Kosong", "Ego Mengalahkan Hati", "Konflik Sengit", "Perasaan Dikhianati", "Memilih Medan Pertempuran"],
        "reversedKeywords": ["Mencari Rekonsiliasi", "Mengubur Kapak Peperangan", "Menyadari Kesia-siaan", "Minta Maaf"],
        "description": "Seorang pria dengan seringai licik memegang tiga bilah pedang sambil memandang dua sosok lawan yang berjalan menjauh tertunduk sedih di tepi pantai berawan kelabu bergerigi. Dua pedang lainnya tergeletak di tanah. Five of Swords melambangkan kemenangan semu (Pyrrhic victory) di mana ego memenangkan perdebatan namun menghancurkan hubungan, persaingan tidak sehat, dan kesia-siaan memaksakan kehendak.",
        "readings": {
            "love": {
                "title": "Kemenangan Ego yang Menghancurkan Cinta",
                "summary": "Memenangkan argumen dengan menyakiti hati pasangan hanya akan menghasilkan kesepian dan penyesalan.",
                "meaning": "Five of Swords dalam percintaan adalah peringatan keras terhadap racun gengsi dan keinginan untuk selalu benar. Kamu mungkin berhasil membungkam pasangan dalam perdebatan, namun seringai kemenanganmu dibayar mahal dengan pudarnya rasa cinta dan kepercayaan. Cinta tidak mencari pemenang; cinta mencari kebersamaan.",
                "advice": "Turunkan senjatamu; mintalah maaf atas kata-kata pedasmu dan peluklah pasanganmu demi memulihkan hubungan.",
                "reflectionQuestion": "Apakah kamu lebih mencintai egomu untuk terlihat benar atau mencintai kebahagiaan pasanganmu?",
                "keywords": ["Kemenangan Semu", "Racun Gengsi", "Kata-kata Menusuk", "Turunkan Senjata"]
            },
            "work": {
                "title": "Politik Kantor yang Toxic dan Persaingan Kotor",
                "summary": "Waspada terhadap intrik kantor yang saling menjatuhkan atau godaan menggunakan cara tidak etis.",
                "meaning": "Di lingkungan kerja, kartu ini menyoroti atmosfer persaingan yang tidak sehat di mana rekan kerja saling menyalahkan atau mencuri kredit proyek. Jangan biarkan dirimu terseret ke dalam lumpur intrik kotor ini. Menang dengan cara licik hanya akan menghancurkan reputasi jangka panjangmu.",
                "advice": "Tolak terlibat dalam sabotase atau gunjingan kantor; pertahankan integritas profesionalmu meski orang lain bermain curang.",
                "reflectionQuestion": "Pertempuran kantor mana yang sebaiknya kamu tinggalkan karena tidak ada gunanya untuk dimenangkan?",
                "keywords": ["Politik Kantor", "Persaingan Kotor", "Integritas Etika", "Tinggalkan Konflik"]
            },
            "career": {
                "title": "Memilih Medan Pertempuran yang Layak Diperjuangkan",
                "summary": "Menyadari kapan harus mundur dari perselisihan yang hanya membuang-buang waktu dan energi profesional.",
                "meaning": "Karier di bawah pengaruh Five of Swords mengajarkan kebijaksanaan strategis. Tidak semua perdebatan harus kamu menangkan. Terkadang, mengalah dalam urusan kecil demi menjaga fokus pada sasaran besar adalah tindakan paling cerdas yang bisa kamu ambil.",
                "advice": "Pilihlah medan pertempuranmu dengan bijak; fokuskan energimu untuk menghasilkan karya unggul daripada meladeni lawan debat.",
                "reflectionQuestion": "Konflik atau perselisihan mana yang saat ini hanya menguras energimu tanpa memberi nilai tambah bagi kariermu?",
                "keywords": ["Kebijaksanaan Strategis", "Memilih Medan", "Fokus Karya", "Mengalah untuk Menang"]
            },
            "finance": {
                "title": "Sengketa Keuangan dan Waspada Kerugian Akibat Ego",
                "summary": "Menghindari perselisihan warisan atau sengketa bisnis yang menghabiskan biaya perkara tinggi.",
                "meaning": "Secara finansial, Five of Swords memperingatkan bahaya sengketa hukum yang dipicu oleh gengsi. Berperkara di pengadilan sering kali membuat kedua belah pihak sama-sama merugi akibat biaya pengacara yang membengkak. Pilihlah jalan musyawarah mufakat untuk mencapai kompromi yang adil.",
                "advice": "Utamakan jalur mediasi dan kompromi damai dalam menyelesaikan perselisihan materi; hindari pertarungan yang merugikan semua pihak.",
                "reflectionQuestion": "Apakah kompromi damai lebih menguntungkan masa depan finansialmu daripada memaksakan kemenangan mutlak?",
                "keywords": ["Mediasi Damai", "Hindari Sengketa", "Kompromi Adil", "Kerugian Ego"]
            },
            "selfGrowth": {
                "title": "Menaklukkan Kebutuhan Ego untuk Selalu Menang",
                "summary": "Menyadari bahwa keinginan membuktikan diri sering kali lahir dari rasa minder yang tersembunyi.",
                "meaning": "Pengembangan diri kartu ini adalah tentang menjinakkan arogansi intelektual. Mengapa kamu merasa harus selalu membantah dan mengoreksi orang lain? Pribadi yang benar-benar percaya diri tidak membutuhkan kemenangan debat untuk merasa berharga. Kematangan sejati diukur dari kemampuanmu mendengarkan dengan lapang dada.",
                "advice": "Latihlah untuk menahan diri tidak mendebat hal-hal sepele; biarkan orang lain memiliki pendapatnya tanpa perlu kamu sanggah.",
                "reflectionQuestion": "Mengapa kamu merasa begitu terancam saat seseorang tidak sependapat dengan pandanganmu?",
                "keywords": ["Arogansi Intelektual", "Menjinakkan Ego", "Lapang Dada", "Kedewasaan Sejati"]
            },
            "relationships": {
                "title": "Mengubur Kapak Peperangan dan Memulihkan Tali Silaturahmi",
                "summary": "Mengakhiri permusuhan keluarga yang melelahkan demi kedamaian generasi penerus.",
                "meaning": "Dalam pergaulan dan keluarga, Five of Swords menandakan keretakan yang menyakitkan akibat kata-kata kasar. Suasana dingin dan penuh dendam meracuni kebahagiaan bersama. Seseorang harus berjiwa besar untuk mengalah dan mengulurkan tangan perdamaian.",
                "advice": "Jadilah orang yang pertama kali berinisiatif mengubur kapak peperangan; katakan: 'Mari kita sudahi perselisihan ini demi kebaikan bersama.'",
                "reflectionQuestion": "Siapa kerabat atau sahabat yang permusuhannya denganmu sudah saatnya diakhiri demi kedamaian hati?",
                "keywords": ["Kubur Kapak", "Inisiatif Damai", "Hentikan Permusuhan", "Jiwa Besar"]
            },
            "spirituality": {
                "title": "Bahaya Kesombongan Intelektual di Hadapan Tuhan",
                "summary": "Menyadari bahwa penyakit hati paling mematikan adalah rasa merasa lebih benar dan lebih mulia dari orang lain.",
                "meaning": "Secara spiritual, Five of Swords adalah cermin bagi bahaya ujub (merasa kagum pada diri sendiri) dan takabbur (meremehkan orang lain). Iblis terusir dari surga bukan karena kurang ilmu, melainkan karena kesombongan merasa lebih mulia. Kembalilah kepada kerendahan hati mutlak di hadapan Sang Maha Mengetahui.",
                "advice": "Perbanyak istigfar dan rendahkan hatimu di hadapan sesama hamba Tuhan; ketahuilah bahwa kemuliaan sejati ada dalam ketundukan taqwa.",
                "reflectionQuestion": "Bagaimana caramu menjaga hatimu dari rasa merasa lebih sholeh atau lebih pintar dibandingkan orang lain?",
                "keywords": ["Bahaya Ujub", "Kerendahan Hati", "Tunduk Taqwa", "Istigfar Mendalam"]
            }
        }
    },
    {
        "id": "six-of-swords",
        "name": "Six of Swords",
        "slug": "six-of-swords",
        "image": "/assets/tarot/cards/Six of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "6",
        "uprightKeywords": ["Transisi Menuju Tenang", "Perjalanan Pemulihan", "Meninggalkan Badai", "Bantuan Tiba", "Masa Depan Lebih Cerah"],
        "reversedKeywords": ["Terjebak di Tengah Badai", "Bagasi Emosional Berat", "Menolak Pindah", "Rintangan Perjalanan"],
        "description": "Seorang nakhoda mendayung perahu melintasi perairan yang tenang menuju daratan seberang yang damai, membawa seorang wanita berselubung kain dan seorang anak kecil. Enam bilah pedang tertancap tegak di haluan perahu. Di sebelah kanan perahu air tampak berombak kasar, namun di sebelah kiri dan depan air mengalir sangat tenang. Six of Swords melambangkan transisi bertahap keluar dari masa sulit menuju perairan yang lebih damai dan penuh harapan.",
        "readings": {
            "love": {
                "title": "Transisi Menuju Kedamaian Asmara dan Pemulihan",
                "summary": "Meninggalkan masa-masa konflik dan berlayar bersama pasangan menuju hubungan yang lebih tenang dan matang.",
                "meaning": "Six of Swords dalam percintaan membawa kelegaan yang luar biasa. Badai pertengkaran dan drama emosional mulai mereda di belakang kalian. Kalian berdua sedang berlayar menuju perairan yang tenang dan saling menyembuhkan. Bagi yang lajang, kartu ini menandakan bahwa kamu berhasil move on dari masa lalu yang menyakitkan.",
                "advice": "Fokuskan pandanganmu ke daratan masa depan; jangan terus menoleh ke belakang melihat ombak yang sudah kamu lalui.",
                "reflectionQuestion": "Bagaimana kamu dan pasangan bisa saling mendukung dalam proses pemulihan emosi bersama ini?",
                "keywords": ["Move On Damai", "Perairan Tenang", "Pemulihan Asmara", "Menatap Masa Depan"]
            },
            "work": {
                "title": "Keluar dari Lingkungan Kerja Toxic Menuju Tempat yang Lebih Sehat",
                "summary": "Peralihan ke divisi baru atau tempat kerja baru yang jauh lebih suportif dan menghargai karyamu.",
                "meaning": "Di lingkungan kerja, Six of Swords adalah sinyal transisi yang sangat melegakan. Masa-masa sulit, krisis operasional, atau tekanan atasan yang berlebihan mulai berlalu. Kamu sedang dipindahkan atau beralih ke proyek baru yang memiliki atmosfer kerja yang jauh lebih kondusif.",
                "advice": "Bawa serta pengalaman dan keahlianmu (enam pedang di perahu); tinggalkan dendam dan kepahitan masa lalu di dermaga lama.",
                "reflectionQuestion": "Kebiasaan kerja positif apa yang ingin kamu terapkan di lingkungan barumu agar kinerjamu lebih optimal?",
                "keywords": ["Transisi Kerja", "Atmosfer Sehat", "Lingkungan Kondusif", "Tinggalkan Kepahitan"]
            },
            "career": {
                "title": "Relokasi Profesional dan Perjalanan Mencari Peluang Baru",
                "summary": "Pindah kota atau beralih industri demi mendapatkan prospek karier yang lebih cerah.",
                "meaning": "Karier di bawah pengaruh kartu ini sering kali melibatkan perpindahan fisik: relokasi dinas, pindah ke kantor cabang lain, atau menempuh studi lanjutan di tempat baru. Perpindahan ini mungkin menuntut adaptasi, namun akan membawa kemajuan karier yang sangat stabil.",
                "advice": "Rangkul proses adaptasi dengan pikiran terbuka; percayalah bahwa tempat baru ini telah disiapkan untuk pertumbuhanmu.",
                "reflectionQuestion": "Langkah adaptasi apa yang perlu kamu persiapkan untuk menyambut peran atau tempat kerjamu yang baru?",
                "keywords": ["Relokasi Karier", "Adaptasi Tempat Baru", "Prospek Cerah", "Pertumbuhan Stabil"]
            },
            "finance": {
                "title": "Pemulihan Finansial Bertahap Menuju Stabilitas",
                "summary": "Masa-masa krisis keuangan mulai terlewati dan arus kas kembali bergerak ke arah yang positif.",
                "meaning": "Secara finansial, Six of Swords menandakan perbaikan bertahap namun pasti. Beban utang mulai terurai satu per satu, dan kamu mulai mampu menyisihkan uang untuk tabungan masa depan. Meskipun belum bergelimang kekayaan, ketenangan batin materi sudah kamu rasakan kembali.",
                "advice": "Pertahankan pola hidup hemat dan disiplin anggaran yang telah membantumu keluar dari krisis keuangan.",
                "reflectionQuestion": "Kebiasaan finansial bijak apa yang berhasil menyelamatkanmu dari masa-masa sulit kemarin?",
                "keywords": ["Pemulihan Finansial", "Keluar dari Krisis", "Arus Kas Positif", "Ketenangan Materi"]
            },
            "selfGrowth": {
                "title": "Membawa Luka Masa Lalu Sebagai Pelajaran Berharga",
                "summary": "Enam pedang di perahu melambangkan memori yang tidak dilupakan namun tidak lagi menyakitimu.",
                "meaning": "Pengembangan diri kartu Six of Swords adalah seni berdamai dengan sejarah hidupmu. Kamu tidak membuang pedang-pedang masa lalumu ke dasar laut; kamu membawanya sebagai pengingat betapa tangguhnya dirimu melewati badai. Luka-luka itu kini telah sembuh dan berubah menjadi mutiara kearifan.",
                "advice": "Hormati perjalanan hidupmu; sadarilah bahwa kamu yang hari ini adalah pribadi yang jauh lebih bijak berkat badai yang telah kamu lalui.",
                "reflectionQuestion": "Bagaimana caramu memandang masa-masa tersulitmu sebagai guru terbaik yang mendewasakan jiwamu?",
                "keywords": ["Mutiara Kearifan", "Berdamai Sejarah", "Perjalanan Jiwa", "Kedewasaan Mental"]
            },
            "relationships": {
                "title": "Dukungan Sahabat yang Menuntun Keluar dari Masa Sulit",
                "summary": "Kehadiran seseorang yang bersedia menjadi 'nakhoda' penolong di saat kamu merasa tak berdaya.",
                "meaning": "Dalam pergaulan dan keluarga, kartu ini mengingatkan bahwa kamu tidak perlu menyeberangi badai sendirian. Ada sahabat, pasangan, atau konselor yang dengan tulus mendayung perahu dan menuntunmu menuju tempat yang aman. Terimalah uluran tangan mereka dengan rasa syukur.",
                "advice": "Ucapkan terima kasih kepada orang-orang yang telah membantumu melewati masa-masa kelam hidupmu.",
                "reflectionQuestion": "Siapa sosok penolong yang jasanya paling besar dalam membantumu keluar dari masa-masa sulitmu?",
                "keywords": ["Sosok Penolong", "Uluran Tangan", "Dukungan Sahabat", "Rasa Terima Kasih"]
            },
            "spirituality": {
                "title": "Bimbingan Malaikat Menyeberangi Samudra Kehidupan",
                "summary": "Menyadari bahwa Tuhan senantiasa mengutus pertolongan dan nakhoda gaib bagi jiwa-jiwa yang berserah.",
                "meaning": "Secara spiritual, Six of Swords adalah perlindungan ilahi dalam perjalanan jiwa. Nakhoda perahu adalah simbol rahmat dan bimbingan Tuhan yang senantiasa menuntun bahtera hidupmu melintasi ombak duniawi menuju pantai keselamatan akhirat. Berserahlah; kamu berada di tangan yang aman.",
                "advice": "Perbanyak doa memohon keselamatan lahir batin; percayakan kemudi hidupmu kepada pemeliharaan Tuhan.",
                "reflectionQuestion": "Bagaimana rasanya melepaskan rasa cemas dan mempercayai bahwa Tuhan sedang menuntunmu menuju tempat yang lebih damai?",
                "keywords": ["Bahtera Keselamatan", "Bimbingan Gaib", "Perlindungan Rahmat", "Pantai Kedamaian"]
            }
        }
    },
    {
        "id": "seven-of-swords",
        "name": "Seven of Swords",
        "slug": "seven-of-swords",
        "image": "/assets/tarot/cards/Seven of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "7",
        "uprightKeywords": ["Kecerdikan Strategis", "Tindakan Sembunyi", "Waspada Penipuan", "Menghindari Konfrontasi Langsung", "Merahasiakan Rencana"],
        "reversedKeywords": ["Kebohongan Terbongkar", "Mengakui Kesalahan", "Hati Nurani Bicara", "Kembali Berintegritas"],
        "description": "Seorang pria berjingkat-jingkat membawa lima bilah pedang curian dari perkemahan musuh, sambil menoleh ke belakang melihat dua pedang yang tertinggal tertancap di tanah. Seven of Swords melambangkan kelihaian strategi, tindakan sembunyi-sembunyi, perlunya menjaga kerahasiaan rencana, serta peringatan terhadap ketidakjujuran atau penipuan.",
        "readings": {
            "love": {
                "title": "Waspada Rahasia Terselubung dan Kejujuran Asmara",
                "summary": "Menghindari perilaku menyembunyikan sesuatu dari pasangan demi menjaga keutuhan kepercayaan.",
                "meaning": "Seven of Swords dalam percintaan adalah peringatan terhadap rahasia, kebohongan kecil (white lies), atau ketidakterusterangan. Hubungan yang sehat tidak dapat bertahan di atas fondasi kerahasiaan. Jika ada sesuatu yang kamu sembunyikan, inilah saatnya mengakuinya secara jujur sebelum kebenaran terungkap dengan cara yang menyakitkan.",
                "advice": "Bicaralah apa adanya; jangan tutupi kesalahan dengan kebohongan baru yang justru memperkeruh keadaan.",
                "reflectionQuestion": "Rahasia apa yang selama ini kamu sembunyikan dari pasangan yang sebenarnya perlu dibicarakan?",
                "keywords": ["Waspada Rahasia", "Kejujuran Asmara", "Hindari Kebohongan", "Pulihkan Kepercayaan"]
            },
            "work": {
                "title": "Kecerdikan Strategis dan Melindungi Kekayaan Intelektual",
                "summary": "Menyimpan strategi kunci secara rahasia dan waspada terhadap pencurian ide di kantor.",
                "meaning": "Di lingkungan kerja, Seven of Swords menyarankan kehati-hatian tingkat tinggi. Jangan mengumbar ide inovatifmu sebelum hak cipta atau patennya terlindungi. Gunakan strategi cerdik dan diplomasi halus untuk melewati rintangan politik kantor tanpa harus terlibat dalam benturan frontal.",
                "advice": "Simpan dokumen dan password dengan aman; lindungi hasil karyamu dari pihak yang suka mengklaim kerja keras orang lain.",
                "reflectionQuestion": "Langkah pengamanan apa yang perlu kamu pasang untuk melindungi ide dan data kerjamu dari pencurian?",
                "keywords": ["Strategi Cerdik", "Kerahasiaan Rencana", "Lindungi Hak Cipta", "Hindari Benturan"]
            },
            "career": {
                "title": "Bermanuver Cerdas di Jalur Karier yang Penuh Persaingan",
                "summary": "Mencapai tujuan profesional melalui taktik gerilya, fleksibilitas, dan kelihaian membaca peluang.",
                "meaning": "Karier di bawah pengaruh kartu ini menuntut kelincahan bermanuver. Ketika jalur utama tersumbat oleh birokrasi kaku, kamu harus mampu menemukan celah alternatif yang legal dan efektif. Namun ingatlah batas etika: jangan mengorbankan integritas moral demi mencapai target.",
                "advice": "Gunakan kecerdasanmu untuk kebaikan; carilah solusi alternatif yang cerdas tanpa melanggar kode etik profesi.",
                "reflectionQuestion": "Jalur alternatif legal apa yang dapat kamu tempuh untuk mewujudkan sasaran kariermu lebih cepat?",
                "keywords": ["Manuver Cerdas", "Solusi Alternatif", "Kelincahan Karier", "Batas Etika"]
            },
            "finance": {
                "title": "Waspada Terhadap Penipuan dan Kebocoran Dana Halus",
                "summary": "Memeriksa mutasi rekening dari transaksi mencurigakan dan menjaga kerahasiaan data perbankan.",
                "meaning": "Secara finansial, Seven of Swords adalah sinyal bahaya terhadap penipuan daring (phishing), skimming kartu, atau pengeluaran tersembunyi yang menggerogoti saldo secara halus. Periksa tagihan kartu kreditmu dan pastikan tidak ada biaya siluman yang dibebankan kepadamu.",
                "advice": "Ganti password perbankan secara berkala; jangan pernah membagikan kode OTP atau data pribadi kepada siapa pun.",
                "reflectionQuestion": "Apakah kamu sudah cukup teliti memeriksa laporan mutasi rekening dan tagihan keuanganmu setiap bulan?",
                "keywords": ["Waspada Phishing", "Biaya Siluman", "Keamanan Finansial", "Lindungi Password"]
            },
            "selfGrowth": {
                "title": "Menghentikan Kebiasaan Membohongi Diri Sendiri",
                "summary": "Menyadari bahwa orang pertama yang paling sering kita tipu adalah diri kita sendiri.",
                "meaning": "Pengembangan diri kartu Seven of Swords adalah teguran moral bagi batin. Kita sering mencari-cari pembenaran atas kemalasan atau kebiasaan buruk kita dengan alasan palsu. Pria yang menoleh ke belakang tahu bahwa perbuatannya tidak benar. Berhentilah mencari dalih; hadapi dirimu dengan kejujuran mutlak.",
                "advice": "Hentikan rasionalisasi palsu atas kebiasaan burukmu; akui kelemahanmu dan mulailah mengambil langkah perbaikan nyata.",
                "reflectionQuestion": "Kebohongan atau alasan palsu apa yang paling sering kamu bisikkan kepada dirimu sendiri untuk menunda kebaikan?",
                "keywords": ["Jujur pada Diri", "Hentikan Dalih", "Integritas Batin", "Menghadapi Kelemahan"]
            },
            "relationships": {
                "title": "Mendeteksi Kepalsuan dalam Lingkaran Pergaulan",
                "summary": "Memilih untuk merahasiakan rencana pribadimu dari kenalan yang memiliki motif terselubung.",
                "meaning": "Dalam pergaulan dan keluarga, kartu ini menyarankan untuk tidak terlalu naif. Tidak semua orang yang tersenyum di hadapanmu tulus mendukung kesuksesanmu. Ada baiknya menyimpan rencana masa depanmu untuk dirimu sendiri sampai segalanya benar-benar terwujud.",
                "advice": "Terapkan prinsip 'privacy is power'; jangan bagikan seluruh detail kehidupan pribadimu di media sosial.",
                "reflectionQuestion": "Siapa dalam lingkaran pergaulanmu yang gerak-geriknya menunjukkan adanya kepalsuan atau motif tersembunyi?",
                "keywords": ["Privasi Adalah Kekuatan", "Waspada Naif", "Jaga Rahasia", "Menyaring Teman"]
            },
            "spirituality": {
                "title": "Mata Batin yang Mengetahui Rahasia Tersembunyi",
                "summary": "Menyadari bahwa tiada satu rahasia pun yang dapat disembunyikan dari penglihatan Tuhan.",
                "meaning": "Secara spiritual, Seven of Swords mengingatkan sifat Tuhan Yang Maha Melihat (Al-Bashir) dan Maha Mengetahui yang Gaib (Al-'Alim). Manusia mungkin bisa berjingkat-jingkat menyembunyikan keburukan dari pandangan sesama manusia, namun di hadapan Tuhan, segalanya telanjang benderang. Kesadaran inilah yang melahirkan keikhlasan murni.",
                "advice": "Tegakkan muraqabah (rasa senantiasa diawasi Tuhan) dalam kesendirian; jadikan kebersihan batin sebagai perhiasanmu.",
                "reflectionQuestion": "Apakah tindakanmu di saat sendirian sudah sama bersihnya dengan tindakanmu di hadapan orang banyak?",
                "keywords": ["Muraqabah", "Al-Bashir", "Tiada Rahasia", "Kebersihan Niat"]
            }
        }
    },
    {
        "id": "eight-of-swords",
        "name": "Eight of Swords",
        "slug": "eight-of-swords",
        "image": "/assets/tarot/cards/Eight of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "8",
        "uprightKeywords": ["Merasa Terjebak", "Penjara Pikiran Sendiri", "Ketidakberdayaan Semu", "Mata Tertutup Ketakutan", "Kunci Pembebasan"],
        "reversedKeywords": ["Membuka Ikatan", "Melihat Jalan Keluar", "Kemerdekaan Mental", "Keberanian Melangkah"],
        "description": "Seorang wanita terikat longgar dengan kain merah dan matanya ditutup kain, berdiri di tanah berlumpur dikelilingi oleh delapan bilah pedang yang menancap di tanah. Di belakangnya tampak kastel di atas bukit tinggi. Namun, pedang-pedang itu tidak mengurungnya rapat dan ikatannya sebenarnya cukup longgar untuk dilepas jika ia melangkah maju. Eight of Swords melambangkan perasaan terjebak oleh ilusi ketidakberdayaan, penjara mental ciptaan sendiri, dan keberanian melepaskan diri dari ketakutan.",
        "readings": {
            "love": {
                "title": "Merasa Terjebak dalam Hubungan yang Mengekang",
                "summary": "Menyadari bahwa belenggu yang menahanmu sesungguhnya adalah rasa takutmu sendiri untuk melangkah.",
                "meaning": "Eight of Swords dalam percintaan menandakan perasaan tidak berdaya: merasa terjebak dalam hubungan yang tidak membahagiakan namun takut untuk keluar, atau merasa tidak layak dicintai akibat trauma lama. Sadarilah bahwa ikatan yang melilitmu sesungguhnya longgar: kamu memiliki hak dan kekuatan untuk membebaskan dirimu kapan pun kamu mau.",
                "advice": "Buka penutup matamu; jangan biarkan rasa takut akan kesendirian membuatmu rela dipenjara dalam ketidakbahagiaan.",
                "reflectionQuestion": "Ketakutan apa yang selama ini membuatmu merasa tidak berdaya untuk mengubah nasib asmaramu?",
                "keywords": ["Penjara Asmara", "Ketidakberdayaan Semu", "Buka Ikatan", "Keberanian Memilih"]
            },
            "work": {
                "title": "Merasa Mandek di Kantor dan Menemukan Jalan Keluar",
                "summary": "Mengatasi perasaan bahwa kamu tidak memiliki pilihan lain dalam karier atau tugas kerja.",
                "meaning": "Di lingkungan kerja, kamu merasa terjebak oleh birokrasi, atasan yang menekan, atau beban tugas yang seolah tanpa jalan keluar. Perasaan terjebak ini sering kali membatasi kreativitasmu. Jika kamu mundur satu langkah dan melihat gambaran besar, kamu akan menemukan celah jalan keluar di antara pedang-pedang tersebut.",
                "advice": "Carilah perspektif dari luar tim; bicaralah dengan mentor untuk melihat opsi-opsi solusi yang sebelumnya tidak kamu sadari.",
                "reflectionQuestion": "Pilihan atau alternatif kerja apa yang selama ini sengaja kamu abaikan karena merasa mustahil?",
                "keywords": ["Merasa Mandek", "Celah Jalan Keluar", "Perspektif Luar", "Pemberdayaan Kerja"]
            },
            "career": {
                "title": "Membongkar Keyakinan yang Membatasi Potensi Profesional",
                "summary": "Menghilangkan sindrom imposter dan menyadari bahwa kamu memiliki kualifikasi untuk maju.",
                "meaning": "Karier di bawah pengaruh kartu ini menyoroti pembatasan diri (self-limiting beliefs). Kamu mungkin merasa tidak cukup pintar, tidak cukup berpengalaman, atau terlalu tua/muda untuk melamar posisi impianmu. Hambatan terbesar dalam kariermu saat ini bukanlah kompetitor, melainkan pikiranmu sendiri.",
                "advice": "Lawan bisikan ketidakberdayaan di kepalamu; lamarlah peluang baru itu dan buktikan kemampuanmu.",
                "reflectionQuestion": "Label pembatas apa yang selama ini kamu tempelkan pada dirimu yang kini siap kamu robek?",
                "keywords": ["Self-Limiting Beliefs", "Hancurkan Imposter", "Potensi Terkunci", "Langkah Bebas"]
            },
            "finance": {
                "title": "Kecemasan Finansial yang Melumpuhkan Tindakan",
                "summary": "Mengatasi kepanikan atas masalah utang dengan menyusun langkah praktis satu per satu.",
                "meaning": "Secara finansial, Eight of Swords menggambarkan kepanikan saat melihat tagihan atau masalah utang hingga membuatmu merasa lumpuh dan ingin menghindar. Menutup mata tidak akan melunasi utang. Lepaskan penutup matamu, buka tagihan tersebut, dan susun rencana pelunasan praktis langkah demi langkah.",
                "advice": "Hadapi angka keuanganmu secara realistis; buat daftar prioritas pelunasan dan konsultasikan dengan penasihat keuangan.",
                "reflectionQuestion": "Langkah kecil apa yang bisa kamu ambil hari ini untuk mulai mengurai benang kusut keuanganmu?",
                "keywords": ["Kepanikan Finansial", "Hadapi Angka", "Urai Benang Kusut", "Tindakan Nyata"]
            },
            "selfGrowth": {
                "title": "Meruntuhkan Penjara Mental dan Menemukan Kebebasan Batin",
                "summary": "Menyadari bahwa satu-satunya orang yang memenjarakanmu adalah pikiranmu sendiri.",
                "meaning": "Pengembangan diri kartu Eight of Swords adalah pembebasan radikal. Selama ini kamu merasa menjadi korban keadaan, padahal pedang-pedang itu tidak pernah menusukmu dan kain merah itu tidak diikat mati. Ketika kamu memutuskan untuk melangkah keluar dari lumpur keraguan, kebebasan sejati langsung menjadi milikmu.",
                "advice": "Tantang setiap pikiran negatif yang berkata 'kamu tidak bisa'; buktikan bahwa kamu memiliki kedaulatan atas hidupmu.",
                "reflectionQuestion": "Apa yang akan kamu lakukan hari ini jika kamu tahu bahwa kamu sepenuhnya bebas dan berkuasa atas pilihanmu?",
                "keywords": ["Penjara Mental", "Kedaulatan Batin", "Kebebasan Sejati", "Meretas Batasan"]
            },
            "relationships": {
                "title": "Melepaskan Ketergantungan pada Opini Orang Lain",
                "summary": "Berhenti merasa terpenjara oleh ekspektasi keluarga atau penilaian masyarakat.",
                "meaning": "Dalam pergaulan dan keluarga, kamu merasa terikat oleh aturan-aturan kaku atau tuntutan sosial yang membuatmu tidak bisa bernapas. Sadarilah bahwa kamu tidak hidup untuk menyenangkan semua orang. Kamu berhak menentukan jalan bahagiamu sendiri.",
                "advice": "Tegaskan pendirianmu dengan tenang; jangan biarkan rasa takut dicap buruk memenjarakan kepribadian autentikmu.",
                "reflectionQuestion": "Ekspektasi orang lain mana yang selama ini paling mengekang kebebasan berekspresimu?",
                "keywords": ["Ekspektasi Sosial", "Kemandirian Sikap", "Lepaskan Ketergantungan", "Hak Hidup"]
            },
            "spirituality": {
                "title": "Pertolongan Tuhan yang Membuka Belenggu Jiwa",
                "summary": "Menyadari bahwa doa dan kepasrahan kepada Tuhan adalah kunci pembuka segala kebuntuan.",
                "meaning": "Secara spiritual, Eight of Swords mengingatkan firman ilahi: 'Dan barangsiapa bertakwa kepada Tuhan, niscaya Dia akan membukakan jalan keluar baginya.' Ketika segala pintu bumi tampak terkunci oleh pikiranmu, pintu langit senantiasa terbuka lebar. Bersujudlah dan mohonkan pertolongan-Nya untuk membukakan jalan keluar.",
                "advice": "Panjatkan doa memohon jalan keluar (doa al-faraj); percayalah bahwa rahmat Tuhan jauh lebih luas daripada masalahmu.",
                "reflectionQuestion": "Bagaimana caramu menyerahkan kebuntuan hidupmu kepada kemahakuasaan Tuhan yang tak terbatas?",
                "keywords": ["Jalan Keluar Ilahi", "Doa Al-Faraj", "Pertolongan Dekat", "Kemerdekaan Rohani"]
            }
        }
    },
    {
        "id": "nine-of-swords",
        "name": "Nine of Swords",
        "slug": "nine-of-swords",
        "image": "/assets/tarot/cards/Nine of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "9",
        "uprightKeywords": ["Kecemasan Malam", "Insomnia", "Overthinking Menghantui", "Rasa Bersalah Batin", "Fajar Pembebasan"],
        "reversedKeywords": ["Kecemasan Mereda", "Mencari Pertolongan", "Menghadapi Ketakutan", "Fajar Tiba"],
        "description": "Seorang figur duduk tegak di tempat tidurnya menutup wajahnya dengan kedua tangan dalam keputusasaan atau kecemasan mendalam di tengah malam gelap. Di dinding kayu di atas ranjangnya tergantung sembilan bilah pedang horizontal yang menunjuk ke kanan. Selimutnya dihias motif mawar merah dan tanda zodiak. Nine of Swords melambangkan kecemasan malam (nightmare/insomnia), overthinking yang menyiksa, rasa bersalah, dan ketakutan yang sering kali membesar di dalam pikiran melebihi kenyataan sebenarnya.",
        "readings": {
            "love": {
                "title": "Kecemasan Hubungan dan Overthinking di Malam Hari",
                "summary": "Pikiran kalut yang membayangkan skenario terburuk asmara yang sebenarnya belum tentu terjadi.",
                "meaning": "Nine of Swords dalam percintaan menggambarkan malam-malam tanpa tidur akibat kecemasan: takut pasangan berpaling, cemas akan masa depan hubungan, atau penyesalan atas kata-kata masa lalu. Sebagian besar ketakutan ini adalah monster yang diciptakan oleh overthinking-mu sendiri. Bawalah kekhawatiran ini ke dalam dialog nyata di siang hari.",
                "advice": "Jangan biarkan imajinasi buruk menyiksamu di malam hari; bicarakan kecemasanmu secara terbuka dengan pasangan saat pikiran segar.",
                "reflectionQuestion": "Kekhawatiran asmara apa yang selama ini paling sering mengganggu tidur malammu tanpa dasar fakta riil?",
                "keywords": ["Kecemasan Asmara", "Insomnia Cinta", "Monster Overthinking", "Dialog Nyata"]
            },
            "work": {
                "title": "Tekanan Tenggat Waktu dan Sindrom Takut Gagal",
                "summary": "Kelelahan mental akibat beban kerja dan kekhawatiran berlebihan akan membuat kesalahan fatal.",
                "meaning": "Di lingkungan kerja, kartu ini menyoroti stres kerja yang memuncak. Kamu mungkin terbangun di tengah malam memikirkan email kantor, tenggat waktu proyek, atau presentasi penting. Ingatlah bahwa panik tidak akan menyelesaikan pekerjaan. Tarik napas dalam-dalam, buat daftar tugas terstruktur, dan selesaikan satu per satu di jam kerja.",
                "advice": "Tegakkan batas tegas antara jam kerja dan jam istirahat; jangan bawa berkas atau gawai kerja ke atas tempat tidurmu.",
                "reflectionQuestion": "Bagaimana caramu mengelola stres kerja agar tidak merampas hak tubuhmu untuk tidur nyenyak?",
                "keywords": ["Stres Kerja", "Takut Gagal", "Batas Jam Istirahat", "Struktur Tugas"]
            },
            "career": {
                "title": "Menghadapi Ketakutan Terbesar dan Menyadari Ilusinya",
                "summary": "Menyadari bahwa ketakutan profesional sering kali lebih menakutkan di dalam kepala daripada kenyataannya.",
                "meaning": "Karier di bawah pengaruh Nine of Swords menguji keberanian mentalmu. Kamu mungkin takut dipecat, takut bisnis bangkrut, atau takut reputasimu hancur. Namun ketika fajar menyingsing dan kamu menatap langsung masalahmu, kamu akan menyadari bahwa kamu memiliki kapasitas untuk mengatasinya.",
                "advice": "Uraikan skenario terburukmu dan buat rencana mitigasi konkret; ketika kamu siap menghadapi yang terburuk, rasa takutmu akan lenyap.",
                "reflectionQuestion": "Skenario terburuk apa yang paling kamu takuti dalam kariermu, dan apa rencana konkretmu jika hal itu terjadi?",
                "keywords": ["Mitigasi Ketakutan", "Fajar Menanti", "Keberanian Mental", "Rencana Konkret"]
            },
            "finance": {
                "title": "Kekhawatiran Keuangan Malam Hari dan Mencari Solusi Nyata",
                "summary": "Mengatasi kepanikan atas masalah utang dengan berkonsultasi dan menyusun restrukturisasi dana.",
                "meaning": "Secara finansial, kartu ini melambangkan beban pikiran atas kewajiban materi yang mengganggu tidur. Menatap langit-langit kamar sambil mencemaskan tagihan tidak akan mendatangkan uang. Di pagi hari, hubungi pihak bank, konsultasikan restrukturisasi utang, dan ambil langkah penataan kas yang nyata.",
                "advice": "Jangan tanggung kecemasan finansial sendirian; carilah bantuan profesional atau bicarakan dengan pasangan secara terbuka.",
                "reflectionQuestion": "Langkah nyata apa yang bisa kamu ambil besok pagi untuk mengatasi sumber kecemasan finansialmu?",
                "keywords": ["Kecemasan Finansial", "Restrukturisasi Utang", "Cari Bantuan", "Solusi Terbuka"]
            },
            "selfGrowth": {
                "title": "Menghalau Hantu Pikiran dengan Cahaya Kesadaran",
                "summary": "Menyadari bahwa 90% kekhawatiran kita tidak pernah benar-benar terjadi di dunia nyata.",
                "meaning": "Pengembangan diri kartu Nine of Swords adalah penaklukan overthinking. Pedang-pedang di dinding tidak menusuk tubuh figur di ranjang; mereka hanya melayang di atas kepalanya sebagai simbol beban pikiran. Saat matahari terbit, bayangan-bayangan menakutkan itu akan memudar. Latihlah dirimu untuk hadir utuh di momen saat ini.",
                "advice": "Tuliskan seluruh isi pikiranmu di jurnal sebelum tidur untuk mengosongkan beban kepalamu; latihlah mindfulness.",
                "reflectionQuestion": "Kekhawatiran masa lalu apa yang dulu sempat membuatmu tidak bisa tidur namun ternyata tidak pernah terjadi?",
                "keywords": ["Jurnal Sebelum Tidur", "Hentikan Overthinking", "Mindfulness", "Fajar Kesadaran"]
            },
            "relationships": {
                "title": "Membagi Beban Batin kepada Sahabat Terpercaya",
                "summary": "Membuka diri dan menceritakan kegundahanmu kepada orang yang tulus menyayangimu.",
                "meaning": "Dalam pergaulan dan keluarga, kartu ini memperingatkan bahaya memendam masalah sendirian. Menutup wajah dalam kesendirian hanya memperbesar rasa sakit. Berbagilah cerita dengan sahabat karib, orang tua, atau konselor. Beban berat akan terasa jauh lebih ringan saat dipikul bersama.",
                "advice": "Hubungi sahabat karibmu dan katakan: 'Aku sedang merasa sangat cemas, bisakah kita mengobrol sebentar?'; izinkan dirimu ditolong.",
                "reflectionQuestion": "Siapa sosok terpercaya yang kehadirannya selalu mampu menenangkan dan menghibur hatimu yang gundah?",
                "keywords": ["Bagi Beban", "Jangan Memendam", "Sahabat Terpercaya", "Mencari Pertolongan"]
            },
            "spirituality": {
                "title": "Munajat di Sepertiga Malam: Menyerahkan Gulita Jiwa kepada Tuhan",
                "summary": "Mengubah insomnia kecemasan menjadi sujud tahajud yang membasahi kalbu dengan kedamaian.",
                "meaning": "Secara spiritual, Nine of Swords adalah panggilan untuk bangun di sepertiga malam terakhir. Jangan habiskan waktu malammu untuk melamunkan ketakutan; bangkitlah, basuh wajahmu dengan air wudhu, dan bersujudlah di hadirat Tuhan. Di dalam sujud malam itulah segala kecemasan duniawi akan lebur menjadi ketenteraman abadi.",
                "advice": "Lakukan salat malam dan berdoalah dengan tulus; tumpahkan seluruh air matamu kepada Sang Maha Pengasih.",
                "reflectionQuestion": "Bagaimana caramu mengubah rasa cemas di tengah malam menjadi momentum bermesraan dengan Tuhan dalam doa?",
                "keywords": ["Sujud Tahajud", "Sepertiga Malam", "Leburkan Cemas", "Kedamaian Abadi"]
            }
        }
    },
    {
        "id": "ten-of-swords",
        "name": "Ten of Swords",
        "slug": "ten-of-swords",
        "image": "/assets/tarot/cards/Ten of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "10",
        "uprightKeywords": ["Titik Terendah (Rock Bottom)", "Akhir Rasa Sakit", "Fajar Matahari Terbit", "Pelepasan Mutlak", "Kebangkitan Baru"],
        "reversedKeywords": ["Mulai Bangkit", "Pemulihan dari Kehancuran", "Lolos dari Musibah", "Harapan Menyingsing"],
        "description": "Seorang figur berbaju merah berbaring telungkup di tepi pantai dengan sepuluh pedang tertancap di sepanjang punggungnya. Langit di atasnya hitam pekat, namun di cakrawala kejauhan tampak fajar keemasan matahari mulai menyingsing menerangi perairan yang tenang. Ten of Swords melambangkan titik terendah (rock bottom), akhir mutlak dari rasa sakit dan pengkhianatan, serta kabar gembira bahwa situasi terburuk telah berlalu dan jalan satu-satunya dari sini adalah bangkit kembali.",
        "readings": {
            "love": {
                "title": "Akhir Mutlak dari Hubungan yang Menyakitkan",
                "summary": "Menyadari bahwa siklus penderitaan asmara telah tuntas dan fajar kehidupan baru sedang terbit.",
                "meaning": "Ten of Swords dalam percintaan adalah titik akhir dari hubungan yang menguras air mata. Tidak ada lagi yang bisa diselamatkan dari dinamika yang merusak ini. Namun inilah kabar baiknya: penderitaanmu telah mencapai puncaknya dan kini telah tuntas. Badai terburuk telah lewat, dan hatimu siap untuk disembuhkan.",
                "advice": "Terimalah kenyataan bahwa hubungan ini telah usai; lepaskan genggamanmu dan tatap fajar keemasan yang menanti di depanmu.",
                "reflectionQuestion": "Kelegaan apa yang mulai kamu rasakan saat menyadari bahwa kamu tidak perlu lagi menanggung penderitaan ini?",
                "keywords": ["Titik Terendah Asmara", "Akhir Penderitaan", "Fajar Keemasan", "Pelepasan Tuntas"]
            },
            "work": {
                "title": "Penutupan Babak Kerja Lama dan Menatap Peluang Baru",
                "summary": "Proyek yang kandas secara tuntas atau akhir dari perselisihan kantor yang melelahkan.",
                "meaning": "Di lingkungan kerja, Ten of Swords menandakan akhir dari sebuah situasi sulit. Proyek yang bermasalah mungkin dibatalkan secara resmi atau kontrak kerja berakhir. Jangan meratapi apa yang telah usai; akhir ini membebaskan energimu dari beban yang selama ini menekanmu.",
                "advice": "Tuntaskan seluruh administrasi penutupan dengan kepala tegak; bersiaplah menyambut lembaran kerja baru yang lebih segar.",
                "reflectionQuestion": "Bagaimana berakhirnya proyek bermasalah ini justru membebaskan waktumu untuk peluang yang jauh lebih baik?",
                "keywords": ["Penutupan Tuntas", "Akhir Beban", "Kepala Tegak", "Peluang Segar"]
            },
            "career": {
                "title": "Titik Balik Karier: Bangkit dari Reruntuhan Menuju Kejayaan",
                "summary": "Menjadikan kegagalan profesional sebagai fondasi paling kokoh untuk membangun masa depan.",
                "meaning": "Karier di bawah pengaruh kartu ini melambangkan titik balik radikal. Kamu mungkin merasa telah kehilangan segalanya dalam kariermu (rock bottom). Namun, ketika kamu sudah berada di titik terendah, jalan satu-satunya adalah melangkah naik. Banyak tokoh besar dunia memulai kejayaannya tepat setelah mengalami Ten of Swords.",
                "advice": "Bangkitlah dari lantai keterpurukan; gunakan seluruh pengalaman pahit ini sebagai amunisi untuk membangun kesuksesan barumu.",
                "reflectionQuestion": "Kekuatan batin apa yang bangkit di dalam dirimu saat kamu menyadari bahwa kamu telah melewati masa terburukmu?",
                "keywords": ["Titik Balik Karier", "Rock Bottom", "Bangkit Naik", "Fondasi Kejayaan"]
            },
            "finance": {
                "title": "Masa Terburuk Finansial Telah Lewat",
                "summary": "Menuntaskan seluruh kerugian materi dan memulai rekonstruksi keuangan dari titik nol.",
                "meaning": "Secara finansial, Ten of Swords menandakan bahwa kerugian terburuk telah terjadi dan tidak akan ada lagi kejutan buruk baru. Masa-masa paling mencemaskan telah tuntas. Sekarang saatnya membersihkan debu, menyusun kembali anggaran dasar, dan melangkah perlahan menuju pemulihan ekonomi.",
                "advice": "Akui kondisi riil finansialmu tanpa rasa malu; mulailah menabung kembali dari nominal terkecil dengan disiplin.",
                "reflectionQuestion": "Langkah pemulihan keuangan paling dasar apa yang siap kamu jalankan mulai hari ini?",
                "keywords": ["Krisis Berakhir", "Rekonstruksi Dana", "Mulai dari Nol", "Disiplin Pemulihan"]
            },
            "selfGrowth": {
                "title": "Kematian Ego Lama dan Terbitnya Fajar Kesadaran Baru",
                "summary": "Menyadari bahwa kehancuran total masa lalu adalah ruang kosong yang suci bagi kelahiran jiwamu.",
                "meaning": "Pengembangan diri kartu Ten of Swords adalah transformasi agung. Sepuluh pedang melambangkan tuntasnya seluruh siklus penderitaan mental pikiranmu. Kamu tidak bisa disakiti lagi oleh hal yang sama karena kamu telah melewati yang terburuk. Di cakrawala, fajar keemasan sedang merekah menyambut kelahiran dirimu yang baru.",
                "advice": "Tinggalkan jubah kelapukan masa lalumu; bangkitlah dan sambut sinar matahari pagi dengan senyuman baru.",
                "reflectionQuestion": "Siapakah dirimu yang baru yang kini lahir dari abu pengalaman pahit masa lalumu?",
                "keywords": ["Fajar Menyingsing", "Kelahiran Baru", "Kematian Ego", "Ketangguhan Mutlak"]
            },
            "relationships": {
                "title": "Mengakhiri Lingkaran Hubungan Toxic Selamanya",
                "summary": "Memutus ikatan dengan orang-orang yang terus melukaimu dan memulai hidup baru yang tenang.",
                "meaning": "Dalam pergaulan dan keluarga, Ten of Swords adalah keputusan berani untuk tidak lagi menjadi korban perlakuan buruk orang lain. Siklus manipulasi atau kekerasan verbal telah berakhir secara mutlak. Kamu memilih kedamaian hidupmu di atas segala kepura-puraan sosial.",
                "advice": "Tutup pintu masa lalu rapat-rapat; kelilingi dirimu hanya dengan orang-orang yang tulus menghargai dan menyayangimu.",
                "reflectionQuestion": "Hubungan toxic mana yang kini sudah sepenuhnya berhasil kamu tinggalkan demi kesehatan jiwamu?",
                "keywords": ["Putus Siklus Toxic", "Tutup Pintu Rapat", "Kedamaian Hakiki", "Perlindungan Diri"]
            },
            "spirituality": {
                "title": "Fajar Terbit Setelah Malam Paling Gelap",
                "summary": "Menyaksikan bukti bahwa di balik setiap kehancuran lahiriah terdapat fajar kebangkitan rohani yang agung.",
                "meaning": "Secara spiritual, Ten of Swords mengajarkan rahasia matahari terbit (fajar shadiq). Malam yang paling gelap selalu terjadi tepat sebelum fajar merekah. Ketika segala kebanggaan ego manusiawi telah runtuh di tanah, saat itulah cahaya ketuhanan menyinari jiwa dengan keindahan yang tak terkatakan.",
                "advice": "Sujudlah ke tanah dengan penuh kepasrahan; yakinlah bahwa Tuhan sedang menyiapkan fajar kemuliaan bagi jiwamu.",
                "reflectionQuestion": "Bagaimana kamu merasakan secercah harapan dan cahaya baru yang mulai menerangi relung hatimu?",
                "keywords": ["Fajar Shadiq", "Cahaya Ketuhanan", "Kebangkitan Rohani", "Kepasrahan Penuh"]
            }
        }
    },
    {
        "id": "page-of-swords",
        "name": "Page of Swords",
        "slug": "page-of-swords",
        "image": "/assets/tarot/cards/Page of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "Page",
        "uprightKeywords": ["Pikiran Kritis", "Rasa Ingin Tahu Tajam", "Kewaspadaan Cekatan", "Pengamatan Cermat", "Haus Ilmu"],
        "reversedKeywords": ["Gosip Menyimpang", "Bicara Tanpa Berpikir", "Sinis Berlebih", "Mata-mata Licik"],
        "description": "Seorang pemuda lincah berdiri di bukit berumput hijau memegang pedang tegak dengan kedua tangannya, bersiap siaga dengan tatapan tajam menoleh ke samping. Di langit, awan putih bergerak dinamis ditiup angin kencang dan kawanan burung terbang melintas. Page of Swords melambangkan pikiran kritis yang tajam, kewaspadaan tinggi, rasa ingin tahu intelektual, dan pembawa ide-ide baru yang berani.",
        "readings": {
            "love": {
                "title": "Komunikasi yang Tajam, Cerdas, dan Penuh Antusiasme",
                "summary": "Diskusi asmara yang merangsang intelektual, obrolan mendalam tentang berbagai topik, dan rasa penasaran saling mengenal.",
                "meaning": "Page of Swords membawa dinamika obrolan cerdas dalam hubungan. Kamu dan pasangan menikmati perdebatan hangat yang menambah wawasan, saling bertukar buku, atau menganalisis film bersama. Hubungan ini diwarnai oleh kejujuran lugas dan rasa ingin tahu yang tinggi.",
                "advice": "Gunakan kecerdasanmu untuk menghibur dan memahami pasangan; hindari bersikap terlalu analitis atau mengoreksi hal-hal sepele.",
                "reflectionQuestion": "Topik pembicaraan mendalam apa yang ingin kamu diskusikan bersama pasanganmu untuk merangsang pikiran?",
                "keywords": ["Obrolan Cerdas", "Kejujuran Lugas", "Stimulasi Mental", "Rasa Penasaran"]
            },
            "work": {
                "title": "Riset Data yang Teliti dan Pengawasan Kritis",
                "summary": "Menemukan kesalahan data atau peluang tersembunyi berkat ketelitian dan kejelian analisismu.",
                "meaning": "Di lingkungan kerja, Page of Swords adalah sosok peneliti muda yang sangat teliti. Kamu mampu memeriksa dokumen tebal, mendeteksi kesalahan hitung, dan menyajikan temuan kritis kepada tim. Kewaspadaanmu menyelamatkan perusahaan dari potensi kerugian.",
                "advice": "Sampaikan temuan kritismu secara santun dan konstruktif; sertakan solusi nyata bersama data yang kamu temukan.",
                "reflectionQuestion": "Bagian mana dari laporan atau sistem kerjamu yang saat ini memerlukan pengecekan ulang secara teliti?",
                "keywords": ["Riset Teliti", "Pengawasan Kritis", "Kejelian Analisis", "Solusi Konstruktif"]
            },
            "career": {
                "title": "Eksplorasi Karier di Bidang Analitik, Hukum, dan Riset",
                "summary": "Memulai peran baru sebagai analis data, jurnalis investigasi, asisten hukum, atau akademisi muda.",
                "meaning": "Karier di bawah pengaruh kartu ini mendukung profesi yang membutuhkan ketajaman logika dan kemahiran komunikasi: media digital, riset kebijakan, sains data, audit kepatuhan, atau penulisan teknis. Kecepatan belajarmu adalah aset terbesarmu.",
                "advice": "Teruslah mengasah keterampilan analisismu; jangan takut menyampaikan pertanyaan-pertanyaan kritis yang berbobot.",
                "reflectionQuestion": "Keahlian riset atau analisis baru apa yang ingin kamu perdalam untuk menunjang kemajuan kariermu?",
                "keywords": ["Analis Data", "Jurnalisme Kritis", "Kecepatan Belajar", "Pertanyaan Berbobot"]
            },
            "finance": {
                "title": "Membaca Syarat dan Ketentuan Finansial dengan Teliti",
                "summary": "Kewaspadaan memeriksa klausul kontrak pinjaman, biaya admin, atau polis asuransi.",
                "meaning": "Secara finansial, Page of Swords mengingatkan pentingnya membaca 'tulisan kecil' (fine print) sebelum menyetujui transaksi apa pun. Ketelitianmu memeriksa rincian biaya akan menghindarkanmu dari jebakan biaya siluman dan denda tak terduga.",
                "advice": "Tanyakan setiap rincian biaya yang belum kamu pahami sebelum menandatangani dokumen perbankan.",
                "reflectionQuestion": "Dokumen finansial atau polis apa yang selama ini belum pernah kamu baca secara saksama?",
                "keywords": ["Baca Fine Print", "Klausul Teliti", "Hindari Jebakan", "Kewaspadaan Finansial"]
            },
            "selfGrowth": {
                "title": "Mengasah Pisau Analisis dan Berpikir Kritis",
                "summary": "Tidak mudah menelan mentah-mentah informasi hoax atau opini publik tanpa verifikasi fakta.",
                "meaning": "Pengembangan diri kartu Page of Swords adalah pembentukan 'critical thinking' (berpikir kritis). Di era banjir informasi, kemampuan memverifikasi fakta dan membedakan antara opini dan kebenaran adalah tameng perlindungan jiwamu. Jadilah pencari ilmu yang kritis namun tetap rendah hati.",
                "advice": "Periksa sumber primer dari setiap informasi yang kamu terima; latihlah dirimu untuk tidak reaktif terhadap provokasi.",
                "reflectionQuestion": "Informasi atau asumsi apa belakangan ini yang kamu percaya begitu saja tanpa memeriksa faktanya terlebih dahulu?",
                "keywords": ["Critical Thinking", "Verifikasi Fakta", "Anti Hoax", "Ketajaman Nalar"]
            },
            "relationships": {
                "title": "Menghindari Gosip dan Menjaga Kejujuran dalam Pertemanan",
                "summary": "Berhati-hati dalam berbicara agar tidak memicu kesalahpahaman di lingkaran pergaulan.",
                "meaning": "Dalam pergaulan dan keluarga, kartu ini mengingatkan bahaya terlalu banyak mengamati dan mengkritik orang lain. Kejelianmu melihat kelemahan orang lain seharusnya digunakan untuk membantu, bukan untuk dijadikan bahan perbincangan di belakang mereka.",
                "advice": "Gunakan kata-katamu untuk membangun, bukan menjatuhkan; jika ada yang mengganjal, tanyakan langsung secara santun.",
                "reflectionQuestion": "Bagaimana caramu menyampaikan masukan kritis kepada sahabat tanpa membuatnya merasa tersinggung?",
                "keywords": ["Hindari Gunjingan", "Komunikasi Santun", "Masukan Membangun", "Kejujuran Pergaulan"]
            },
            "spirituality": {
                "title": "Pencarian Ilmu Hakiki dan Menghilangkan Keraguan Iman",
                "summary": "Mempelajari ajaran agama dengan telaah kritis dan pemahaman yang mendalam, bukan sekadar taklid buta.",
                "meaning": "Secara spiritual, Page of Swords adalah pencari ilmu agama yang haus pemahaman. Kamu didorong untuk mempelajari dalil, sejarah, dan hikmah di balik setiap perintah ibadah. Iman yang kokoh dibangun di atas ilmu yang sahih dan pemahaman yang jernih, bukan sekadar ikut-ikutan tradisi tanpa mengerti.",
                "advice": "Belajarlah kepada guru-guru yang berilmu luas dan bersanad sahih; jadikan ilmu sebagai penuntun amalmu.",
                "reflectionQuestion": "Pertanyaan spiritual apa yang selama ini ingin kamu pelajari jawabannya secara mendalam?",
                "keywords": ["Pencari Ilmu", "Anti Taklid Buta", "Pemahaman Sahih", "Iman Berilmu"]
            }
        }
    },
    {
        "id": "knight-of-swords",
        "name": "Knight of Swords",
        "slug": "knight-of-swords",
        "image": "/assets/tarot/cards/Knight of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "Knight",
        "uprightKeywords": ["Gerak Cepat", "Determinasi Tajam", "Berani Menerjang", "Fokus Tak Terhentikan", "Membela Kebenaran"],
        "reversedKeywords": ["Agresif Kasar", "Terburu-buru Ceroboh", "Mendikte Orang Lain", "Menabrak Aturan"],
        "description": "Seorang ksatria berbaju zirah lengkap menunggang kuda perang putih yang melesat kencang menembus badai angin dan awan kelabu yang terkoyak. Pedangnya terhunus tegak ke depan dengan ekspresi tekad yang tak tergoyahkan. Knight of Swords melambangkan kecepatan aksi, determinasi intelektual yang membara, keberanian menerjang rintangan demi menegakkan kebenaran, dan fokus yang tak terhentikan.",
        "readings": {
            "love": {
                "title": "Keberanian Memperjuangkan Kepastian Asmara",
                "summary": "Menuntut kejelasan status hubungan dan menyelesaikan masalah cinta dengan ketegasan tanpa ragu.",
                "meaning": "Knight of Swords dalam percintaan adalah dorongan untuk bertindak cepat dan tegas. Kamu tidak tahan lagi berada dalam ketidakpastian (situationship). Kamu atau pasangan siap menyatakan perasaan atau menuntut kejelasan komitmen masa depan secara lugas tanpa basa-basi.",
                "advice": "Sampaikan keinginanmu dengan tegas; namun kendalikan intonasi bicaramu agar tidak terkesan menuntut atau menyerang.",
                "reflectionQuestion": "Kepastian asmara apa yang saat ini paling membutuhkan ketegasan sikapmu?",
                "keywords": ["Kepastian Asmara", "Ketegasan Sikap", "Lugas Tanpa Basa-basi", "Keberanian Bicara"]
            },
            "work": {
                "title": "Eksekusi Kilat dan Menyelesaikan Masalah Mendesak",
                "summary": "Menuntaskan target kerja dalam waktu singkat dengan fokus penuh dan determinasi tinggi.",
                "meaning": "Di lingkungan kerja, kamu adalah pemecah masalah darurat. Ketika proyek menghadapi krisis atau tenggat waktu mepet, kamu terjun langsung ke medan laga memimpin penuntasan tugas dengan kecepatan dan efisiensi maksimal. Rintangan disingkirkan tanpa ampun.",
                "advice": "Pertahankan kecepatan kerjamu; pastikan kamu tetap berkomunikasi dengan baik agar rekan tim tidak tertinggal di belakangmu.",
                "reflectionQuestion": "Tugas kerja mendesak apa yang siap kamu terjang dan selesaikan tuntas dalam tempo sesingkat-singkatnya?",
                "keywords": ["Eksekusi Kilat", "Pemecah Masalah", "Kecepatan Maksimal", "Determinasi Kerja"]
            },
            "career": {
                "title": "Terobosan Karier Melalui Keberanian Berargumen",
                "summary": "Memenangkan debat profesional, membela proposal inovatif, dan menembus persaingan ketat.",
                "meaning": "Karier di bawah pengaruh Knight of Swords bergerak dengan akselerasi tinggi. Keberanianmu menyuarakan kebenaran, menantang status quo, dan menyajikan solusi brilian membuat namamu melesat cepat di mata manajemen puncak. Kamu tidak gentar bersaing dengan siapa pun.",
                "advice": "Gunakan ketajaman analisismu untuk membela kemaslahatan organisasi; hindari kesan arogan di depan rekan kerja.",
                "reflectionQuestion": "Gagasan berani apa yang siap kamu suarakan di hadapan pimpinan atau publik industri?",
                "keywords": ["Terobosan Cepat", "Menantang Status Quo", "Debat Profesional", "Keberanian Bersuara"]
            },
            "finance": {
                "title": "Tindakan Finansial Cepat untuk Menyelamatkan Aset",
                "summary": "Mengambil keputusan tegas melunasi kewajiban atau menarik modal dari instrumen berisiko tinggi.",
                "meaning": "Secara finansial, Knight of Swords menuntut respons cepat. Jika kamu melihat tanda bahaya dalam investasi atau ada kebocoran anggaran yang membesar, jangan tunda lagi: lakukan intervensi finansial seketika untuk menyelamatkan aset keluargamu.",
                "advice": "Bertindaklah cepat dan tegas dalam urusan uang; jangan biarkan keraguan membuatmu terlambat mengamankan aset.",
                "reflectionQuestion": "Tindakan penyelamatan finansial apa yang harus segera kamu eksekusi hari ini juga?",
                "keywords": ["Respons Cepat", "Intervensi Finansial", "Amankan Aset", "Tindakan Tegas"]
            },
            "selfGrowth": {
                "title": "Fokus Tunggal Tanpa Distraksi Menuju Sasaran",
                "summary": "Melesat lurus menuju tujuan hidup dengan menyingkirkan segala godaan penundaan.",
                "meaning": "Pengembangan diri kartu Knight of Swords adalah kekuatan 'laser focus'. Ketika kamu telah menetapkan target, singkirkan segala hal yang tidak relevan. Larilah secepat mungkin menembus badai keraguan. Kamu memiliki momentum luar biasa untuk mencapai lompatan prestasi pribadi.",
                "advice": "Hilangkan seluruh distraksi di sekitarmu; dedikasikan energimu sepenuhnya untuk menyelesaikan target terbesarmu.",
                "reflectionQuestion": "Sasaran hidup apa yang jika kamu kejar dengan fokus penuh selama 30 hari ke depan akan mengubah masa depanmu?",
                "keywords": ["Laser Focus", "Menembus Badai", "Hentikan Distraksi", "Momentum Luar Biasa"]
            },
            "relationships": {
                "title": "Membela Kebenaran dan Menjadi Pelindung Sahabat",
                "summary": "Berani pasang badan membela sahabat atau keluarga yang diperlakukan tidak adil oleh orang lain.",
                "meaning": "Dalam pergaulan dan keluarga, kamu adalah sosok ksatria pembela. Saat ada anggota keluarga atau sahabatmu yang dizalimi, kamu berdiri paling depan membelanya dengan kata-kata yang tegas dan argumen yang tak terbantahkan. Loyalitasmu tidak diragukan lagi.",
                "advice": "Gunakan kekuatan bicaramu untuk membela mereka yang lemah; jangan gunakan kata-katamu untuk menindas orang lain.",
                "reflectionQuestion": "Siapa di lingkaranmu yang saat ini paling membutuhkan perlindungan dan pembelaan tegas darimu?",
                "keywords": ["Ksatria Pembela", "Loyalitas Kokoh", "Membela Kebenaran", "Ketegasan Kata"]
            },
            "spirituality": {
                "title": "Semangat Juang Membela Nilai Keadilan Ilahi",
                "summary": "Menjadikan kecerdasan nalar sebagai pedang pembela nilai-nilai kebenaran dan kemanusiaan.",
                "meaning": "Secara spiritual, Knight of Swords adalah ksatria pena dan kebenaran (amar ma'ruf nahi munkar). Kamu terpanggil untuk tidak tinggal diam melihat ketidakadilan di sekitarmu. Dengan niat suci lillahi ta'ala, kamu menggunakan lidah, tulisan, dan tindakanmu untuk menegakkan hukum kebenaran Tuhan di muka bumi.",
                "advice": "Luruskan niatmu semata-mata mencari ridho Tuhan; pastikan pembelaanmu terhadap kebenaran dilandasi akhlak yang mulia.",
                "reflectionQuestion": "Bagaimana caramu memperjuangkan nilai-nilai kebaikan Tuhan tanpa terjebak dalam amarah ego sendiri?",
                "keywords": ["Amar Ma'ruf", "Pedang Pena", "Penegak Keadilan", "Niat Suci"]
            }
        }
    },
    {
        "id": "queen-of-swords",
        "name": "Queen of Swords",
        "slug": "queen-of-swords",
        "image": "/assets/tarot/cards/Queen of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "Queen",
        "uprightKeywords": ["Kejernihan Persepsi", "Kemandirian Intelektual", "Kejujuran Lurus", "Batasan Sehat", "Ketegasan Anggun"],
        "reversedKeywords": ["Kekejaman Kata-kata", "Hati yang Dingin", "Sinisme Pahit", "Menghakimi Kejam"],
        "description": "Seorang ratu anggun duduk di atas takhta batu berukir bidadari bersayap dan kupu-kupu di puncak bukit tinggi, memegang pedang tegak di tangan kanan dan mengulurkan tangan kirinya ke depan dengan gestur menerima kebenaran. Di langit biru cerah melayang awan putih kumulus. Queen of Swords melambangkan kecerdasan intelektual wanita yang matang, ketajaman melihat fakta tanpa tertipu ilusi, kemandirian mandiri, dan ketegasan moral yang anggun.",
        "readings": {
            "love": {
                "title": "Komunikasi yang Jujur, Setara, dan Mandiri",
                "summary": "Hubungan asmara yang dilandasi saling menghormati ruang pribadi, kedewasaan emosional, dan kejujuran.",
                "meaning": "Queen of Swords dalam percintaan adalah figur wanita atau pasangan yang cerdas, mandiri, dan tidak menyukai drama manipulatif. Kamu menghargai pasangan yang jujur dan lugas. Hubungan ini tumbuh subur atas dasar rasa saling menghargai batasan pribadi dan dialog intelektual yang matang.",
                "advice": "Sampaikan apa yang kamu butuhkan secara jelas dan tenang; jangan biarkan pengalaman pahit masa lalu membuat hatimu menjadi dingin membeku.",
                "reflectionQuestion": "Bagaimana caramu menjaga ketegasan prinsipmu tanpa menghilangkan kelembutan kasih sayang dalam hubungan?",
                "keywords": ["Kemandirian Asmara", "Kejujuran Lugas", "Anti Drama", "Dialog Matang"]
            },
            "work": {
                "title": "Evaluasi Objektif dan Manajemen Berintegritas",
                "summary": "Menilai kinerja tim secara transparan dan memotong inefisiensi sistem dengan keanggunan profesional.",
                "meaning": "Di lingkungan kerja, Queen of Swords adalah teladan profesionalisme murni. Kamu tidak mempan disuap atau dipengaruhi oleh hubungan kekerabatan; keputusanmu didasarkan murni pada meritokrasi, data, dan integritas aturan. Rekan kerja menghormatimu karena keadilan sikapmu.",
                "advice": "Pertahankan standarmu yang tinggi; berikan umpan balik yang jujur, konstruktif, dan tidak memihak.",
                "reflectionQuestion": "Umpan balik profesional apa yang perlu kamu sampaikan secara objektif demi perbaikan mutu tim?",
                "keywords": ["Objektivitas Murni", "Integritas Aturan", "Meritokrasi", "Umpan Balik Jujur"]
            },
            "career": {
                "title": "Puncak Otoritas Intelektual dan Kepemimpinan Adil",
                "summary": "Menduduki posisi penasihat hukum, direktur audit, peneliti senior, atau pengambil kebijakan strategis.",
                "meaning": "Karier di bawah pengaruh kartu ini menandakan pengakuan atas keahlian analisismu yang luar biasa. Kemampuanmu membedah masalah rumit menjadi langkah-langkah strategis yang jelas menjadikanmu figur kunci dalam organisasi. Pendapatmu menjadi rujukan utama.",
                "advice": "Pimpinlah dengan ketegasan yang adil; jadilah teladan bagaimana kecerdasan nalar dapat dipadukan dengan integritas moral.",
                "reflectionQuestion": "Kebijakan strategis apa yang dapat kamu susun untuk meningkatkan efisiensi dan keadilan di organisasimu?",
                "keywords": ["Otoritas Analisis", "Pengambil Kebijakan", "Kepemimpinan Adil", "Rujukan Utama"]
            },
            "finance": {
                "title": "Pengelolaan Keuangan yang Mandiri dan Rasional",
                "summary": "Disiplin alokasi kas berbasis data riil dan menolak spekulasi yang tidak masuk akal.",
                "meaning": "Secara finansial, Queen of Swords melambangkan kemandirian materi mutlak. Kamu tidak bergantung pada siapa pun untuk kebutuhan finansialmu. Setiap rupiah tercatat dengan rapi dalam neraca anggaran. Keputusan investasimu dingin, rasional, dan berorientasi perlindungan aset jangka panjang.",
                "advice": "Pertahankan kemandirian finansialmu; lakukan audit berkala terhadap seluruh portofolio investasimu.",
                "reflectionQuestion": "Apakah keputusan investasimu saat ini sudah sepenuhnya didasari analisis rasional yang bebas dari emosi?",
                "keywords": ["Kemandirian Materi", "Alokasi Rasional", "Audit Portofolio", "Disiplin Kas"]
            },
            "selfGrowth": {
                "title": "Kemerdekaan Berpikir dan Melepaskan Topeng Kelemahan",
                "summary": "Menjadi tuan atas pikiranmu sendiri dan menolak didefinisikan oleh opini orang lain.",
                "meaning": "Pengembangan diri kartu Queen of Swords adalah pembebasan kognitif. Kupu-kupu di takhtanya melambangkan transformasi ulat menjadi makhluk bersayap bebas. Kamu telah melewati badai hidup dan kini bangkit sebagai pribadi yang mandiri, cerdas, dan berdaulat penuh atas nasibmu sendiri.",
                "advice": "Tatap dunia dengan mata jernih tanpa prasangka; berbanggalah atas ketangguhan akal budi dan jiwamu.",
                "reflectionQuestion": "Bagian mana dari hidupmu yang saat ini paling membutuhkan ketegasan sikap dan kejernihan analisismu?",
                "keywords": ["Kemerdekaan Berpikir", "Kedaulatan Jiwa", "Transformasi Kupu-kupu", "Akal Budi Matang"]
            },
            "relationships": {
                "title": "Menegakkan Batasan Sehat dalam Lingkaran Keluarga",
                "summary": "Menolak dimanipulasi secara emosional dan menjaga hubungan keluarga tetap bermartabat.",
                "meaning": "Dalam pergaulan dan keluarga, kamu adalah sosok yang dihormati karena ketegasanmu. Orang lain tahu bahwa mereka tidak bisa mempermainkan atau memanfaatkan kebaikanmu. Kamu menyayangi keluarga dengan tulus, namun kamu tidak mentolerir kebohongan atau sikap tidak bertanggung jawab.",
                "advice": "Tegakkan batasanmu dengan senyuman santun; jangan biarkan rasa bersalah palsu melemahkan ketegasan prinsipmu.",
                "reflectionQuestion": "Batasan apa yang perlu kamu pertegas kepada anggota keluarga agar hubungan tetap sehat dan saling menghormati?",
                "keywords": ["Batasan Sehat", "Tolak Manipulasi", "Ketegasan Santun", "Hubungan Bermartabat"]
            },
            "spirituality": {
                "title": "Kejernihan Kalbu yang Bebas dari Khurafat dan Ilusi",
                "summary": "Menyembah Tuhan dengan akal budi yang tercerahkan dan ketundukan hati yang murni.",
                "meaning": "Secara spiritual, Queen of Swords melambangkan pembersihan akidah dari segala bentuk takhayul, khurafat, dan ilusi batin. Pedang tegaknya menunjuk ke langit sebagai simbol bahwa seluruh nalar kritisnya diserahkan kepada kebenaran wahyu ilahi. Ibadahmu jernih, lurus, dan penuh kesadaran sadar.",
                "advice": "Gunakan akal pikiranmu untuk mentadaburi ayat-ayat Tuhan; jadikan kejernihan ilmu sebagai sarana mendekat kepada-Nya.",
                "reflectionQuestion": "Bagaimana caramu memadukan ketajaman akal budi dengan kekhusyukan ibadah di hadapan Tuhan?",
                "keywords": ["Akidah Jernih", "Tadabur Ayat", "Ibadah Sadar", "Kebenaran Wahyu"]
            }
        }
    },
    {
        "id": "king-of-swords",
        "name": "King of Swords",
        "slug": "king-of-swords",
        "image": "/assets/tarot/cards/King of Swords.jpg",
        "arcana": "minor",
        "suit": "swords",
        "rank": "King",
        "uprightKeywords": ["Otoritas Intelektual", "Keadilan Hukum", "Kebenaran Objektif", "Penilaian Bijak", "Disiplin Nalar"],
        "reversedKeywords": ["Tirani Intelektual", "Dingin Kejam", "Manipulasi Hukum", "Penyalahgunaan Wewenang"],
        "description": "Seorang raja agung duduk tegak di takhta batu berukir kupu-kupu dan bidadari peniup terompet, memegang pedang keadilan tegak di tangan kanannya dengan tatapan lurus ke depan. Di lehernya berkalung jubah ungu dan merah. Di belakangnya pohon-pohon bergoyang ditiup angin kencang di bawah langit biru luas. King of Swords melambangkan penguasaan tertinggi atas elemen udara: otoritas keadilan hukum, kecerdasan analitis puncak, integritas moral tanpa kompromi, dan kepemimpinan yang adil berdasarkan fakta dan kebenaran.",
        "readings": {
            "love": {
                "title": "Komitmen Dewasa Berdasarkan Logika dan Nilai Luhur",
                "summary": "Hubungan asmara yang dilandasi kejujuran mutlak, keadilan bersikap, dan komitmen jangka panjang.",
                "meaning": "King of Swords dalam percintaan adalah figur pasangan yang bertanggung jawab, adil, dan memegang teguh kata-katanya. Ia tidak banyak mengobral rayuan gombal, melainkan membuktikan cintanya melalui kepastian tindakan, perlindungan hukum, dan keadilan dalam membagi peran rumah tangga.",
                "advice": "Bicarakan masa depan hubungan dengan rasional dan terbuka; seimbangkan ketegasan logikamu dengan kehangatan kasih sayang.",
                "reflectionQuestion": "Bagaimana kamu dan pasangan bisa menegakkan keadilan dan transparansi penuh dalam bahtera rumah tangga?",
                "keywords": ["Komitmen Nyata", "Keadilan Asmara", "Kejujuran Mutlak", "Tanggung Jawab Dewasa"]
            },
            "work": {
                "title": "Keputusan Pengadilan, Regulasi Hukum, dan Kepatuhan",
                "summary": "Menyelesaikan sengketa kerja atau menyusun perjanjian bisnis dengan presisi hukum yang sempurna.",
                "meaning": "Di lingkungan kerja, kamu berada pada posisi pengambil keputusan tertinggi atau penasihat ahli. Pedang keadilanmu digunakan untuk menegakkan kepatuhan (compliance), menyusun SOP organisasi, dan menyelesaikan perselisihan dengan adil tanpa memihak.",
                "advice": "Pegang teguh regulasi dan fakta objektif; jadilah penengah yang netral dan berani mengambil keputusan sulit.",
                "reflectionQuestion": "Keputusan organisasi sulit apa yang saat ini paling membutuhkan ketegasan dan objektivitas sikapmu?",
                "keywords": ["Kepatuhan Regulasi", "Presisi Hukum", "Keputusan Objektif", "Penegak Keadilan"]
            },
            "career": {
                "title": "Puncak Karier di Bidang Hukum, Kebijakan Publik, dan Sains",
                "summary": "Mencapai posisi hakim, pengacara senior, direktur kepatuhan, atau akademisi terkemuka.",
                "meaning": "Karier di bawah pengaruh King of Swords menandakan pengakuan atas integritas dan kepiawaian analisismu di tingkat tertinggi. Rekam jejakmu bersih tanpa cacat etika. Keputusanmu membentuk arah kebijakan industri atau penegakan keadilan masyarakat.",
                "advice": "Gunakan kekuasaan intelektualmu untuk melindungi hak-hak mereka yang tertindas; tegakkan keadilan meski terhadap diri sendiri.",
                "reflectionQuestion": "Dampak keadilan apa yang ingin kamu wujudkan bagi masyarakat luas melalui profesimu?",
                "keywords": ["Puncak Integritas", "Otoritas Hukum", "Kebijakan Publik", "Keadilan Sosial"]
            },
            "finance": {
                "title": "Pengelolaan Aset yang Legal, Tertib, dan Bebas Sengketa",
                "summary": "Memastikan seluruh aset keuangan memiliki legalitas hukum yang kuat dan bebas dari risiko sengketa.",
                "meaning": "Secara finansial, King of Swords menuntut kepatuhan legalitas aset: akta notaris, sertifikat kepemilikan tanah, pelaporan pajak yang rapi, dan perjanjian warisan yang jelas. Ketertiban administrasi hukum inilah yang akan melindungi kekayaan keluargamu dari generasi ke generasi.",
                "advice": "Rapikan seluruh dokumen kepemilikan asetmu; konsultasikan aspek hukum keuanganmu dengan notaris tepercaya.",
                "reflectionQuestion": "Apakah seluruh aset dan dokumen kepemilikan hartamu sudah memiliki dasar hukum yang sah dan tertib?",
                "keywords": ["Legalitas Aset", "Tertib Pajak", "Bebas Sengketa", "Keamanan Finansial"]
            },
            "selfGrowth": {
                "title": "Kedaulatan Nalar dan Penguasaan Disiplin Pikiran",
                "summary": "Mampu berpikir jernih tanpa dibaurkan oleh prasangka emosional atau dorongan nafsu sesaat.",
                "meaning": "Pengembangan diri kartu King of Swords adalah puncak ketajaman akal budi. Kamu telah melatih pikiranmu untuk menjadi instrumen yang sangat presisi: mampu menimbang fakta secara objektif, menolak manipulasi, dan berpegang teguh pada prinsip kebenaran universal. Kamu adalah tuan atas dirimu sendiri.",
                "advice": "Peliharalah kejernihan pikiranmu dengan terus belajar dan membaca; jangan biarkan amarah atau kebencian mengaburkan analisismu.",
                "reflectionQuestion": "Apakah keputusan-keputusan hidupmu saat ini sudah sepenuhnya dilandasi pertimbangan akal sehat dan nilai kebenaran?",
                "keywords": ["Kedaulatan Nalar", "Disiplin Pikiran", "Bebas Prasangka", "Akal Budi Tertinggi"]
            },
            "relationships": {
                "title": "Penasihat Bijak dalam Dinamika Keluarga Besar",
                "summary": "Menjadi tempat rujukan seluruh keluarga ketika membutuhkan nasihat hukum atau penyelesaian sengketa.",
                "meaning": "Dalam pergaulan dan keluarga, kamu dihormati sebagai sosok yang adil, jujur, dan tidak berpihak. Sanak saudara percaya bahwa apa pun keputusan atau nasihat yang kamu berikan pasti dilandasi fakta dan niat baik untuk menjaga keutuhan keluarga.",
                "advice": "Berikan nasihat dengan ketegasan yang dilandasi kasih; bantu saudaramu melihat solusi logis dari masalah mereka.",
                "reflectionQuestion": "Bagaimana caramu membantu menyelesaikan masalah keluarga dengan mengedepankan akal sehat dan keadilan?",
                "keywords": ["Penasihat Keluarga", "Rujukan Adil", "Penyelesaian Sengketa", "Kejujuran Sikap"]
            },
            "spirituality": {
                "title": "Hakim yang Adil di Bawah Naungan Hukum Ilahi",
                "summary": "Menyadari bahwa seluruh keadilan manusiawi bermuara pada Keadilan Mutlak Tuhan Sang Hakim Agung.",
                "meaning": "Secara spiritual, King of Swords melambangkan penegakan hukum Tuhan (Al-'Adl). Kamu memahami bahwa setiap perbuatan manusia akan ditimbang di hadapan pengadilan ilahi yang tidak bisa disuap oleh apa pun. Hidupmu diabdikan untuk menegakkan kebenaran dan menjadi saksi yang adil di muka bumi.",
                "advice": "Tegakkan keadilan di sekitarmu semata-mata karena taqwa kepada Tuhan; jadikan Al-Haq sebagai pedoman hidupmu.",
                "reflectionQuestion": "Bagaimana caramu mempersiapkan diri untuk mempertanggungjawabkan setiap keputusanmu di hadapan Hakim Maha Adil?",
                "keywords": ["Al-'Adl", "Hakim Maha Adil", "Saksi Kebenaran", "Keadilan Taqwa"]
            }
        }
    }
]

print(f"Loaded all {len(SWORDS_CARDS)} Swords cards successfully!")
