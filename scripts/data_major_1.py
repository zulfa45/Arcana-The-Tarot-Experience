#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
All 22 Major Arcana Cards with complete 7-category Indonesian readings.
"""

MAJOR_ARCANA = [
    {
        "id": "the-fool",
        "number": 0,
        "name": "The Fool",
        "slug": "the-fool",
        "image": "/assets/tarot/cards/The Fool.jpg",
        "arcana": "major",
        "uprightKeywords": ["Awal Baru", "Kepolosan", "Spontanitas", "Keberanian", "Potensi Murni"],
        "reversedKeywords": ["Kecerobohan", "Ragu Melangkah", "Naif", "Ketakutan Berlebih"],
        "description": "The Fool melambangkan jiwa pengelana yang berdiri di tepi jurang dengan tas kecil dan setangkai mawar putih. Kartu ini adalah titik nol, lompatan keyakinan menuju ketidaktahuan dengan hati murni dan rasa percaya penuh pada bimbingan semesta.",
        "readings": {
            "love": {
                "title": "Lompatan Hati dan Lembaran Baru",
                "summary": "Keterbukaan untuk memulai kisah baru tanpa dibayangi luka masa lalu.",
                "meaning": "Dalam asmara, The Fool menandakan energi segar dan keterbukaan emosional yang murni. Kamu mungkin berada di ambang koneksi baru yang tak terduga atau merasa terdorong melepaskan pola kaku dalam hubungan yang ada. Kartu ini mengajakmu menyambut cinta dengan kepolosan yang tulus.",
                "advice": "Beranikan diri membuka hati dan nikmati momen kebersamaan tanpa tergesa-gesa menuntut kepastian masa depan.",
                "reflectionQuestion": "Bagian mana dari hatimu yang masih ragu untuk percaya kembali pada keindahan cinta?",
                "keywords": ["Cinta Baru", "Spontanitas", "Keterbukaan", "Optimisme"]
            },
            "work": {
                "title": "Eksplorasi Pendekatan dan Tugas Baru",
                "summary": "Membawa perspektif segar dan kemauan belajar dalam rutinitas harian.",
                "meaning": "Di lingkungan kerja, The Fool mencerminkan antusiasme memulai tugas atau proyek dengan sudut pandang unik. Jangan takut menjadi pemula yang banyak bertanya dan bereksperimen. Keberanian berpikir berbeda justru menjadi keunggulan terbesarmu saat ini.",
                "advice": "Rangkul kurva pembelajaran dengan rendah hati, dengarkan masukan rekan kerja, dan bawa ide kreatif ke meja diskusi.",
                "reflectionQuestion": "Keterampilan baru apa yang selama ini ingin kamu pelajari di tempat kerja?",
                "keywords": ["Inovasi", "Belajar", "Segar", "Eksperimen"]
            },
            "career": {
                "title": "Awal Jalur Profesional yang Dinamis",
                "summary": "Keberanian mengambil arah karier baru atau memulai langkah independen.",
                "meaning": "The Fool dalam karier adalah tanda lompatan besar menuju aspirasi sejati. Kamu mungkin terpikir beralih profesi, merintis usaha mandiri, atau melamar posisi yang menantang batas nyamanmu. Potensi keberhasilan sangat terbuka asalkan diiringi persiapan yang bijak.",
                "advice": "Jangan biarkan status quo membelenggu potensimu; susun langkah terukur lalu mulailah melangkah dengan keyakinan penuh.",
                "reflectionQuestion": "Panggilan profesi apa yang terus mengetuk nuranimu walau tampak tidak lazim bagi orang lain?",
                "keywords": ["Langkah Berani", "Aspirasi", "Peralihan", "Potensi"]
            },
            "finance": {
                "title": "Peluang Baru dan Pengelolaan Waspada",
                "summary": "Sikap terbuka terhadap sumber rezeki baru yang diimbangi kehati-hatian materi.",
                "meaning": "Dari sisi keuangan, The Fool membawa angin segar berupa potensi peluang penghasilan atau investasi awal. Namun, kepolosan kartu ini juga mengingatkan agar tidak terlalu impulsif atau mudah tergiur janji keuntungan instan tanpa riset matang.",
                "advice": "Gunakan uang dengan kesadaran penuh; hindari spekulasi berisiko tinggi dan prioritaskan tabungan dasar.",
                "reflectionQuestion": "Apakah keputusan finansialmu belakangan ini didasari perhitungan matang atau dorongan sesaat?",
                "keywords": ["Peluang", "Riset Materi", "Hindari Impulsif", "Awal Finansial"]
            },
            "selfGrowth": {
                "title": "Membangkitkan Jiwa Eksplorasi Diri",
                "summary": "Melepaskan beban identitas usang demi menemukan esensi autentik pribadimu.",
                "meaning": "Pengembangan diri di bawah naungan The Fool adalah tentang membebaskan diri dari ekspektasi sosial dan prasangka batin. Kamu diajak menjadi diri sendiri apa adanya, menerima ketidaksempurnaan sebagai ruang bertumbuh, dan menikmati setiap fase perjalanan hidup.",
                "advice": "Maafkan kekeliruan masa lalumu dan pandang hari ini sebagai kertas putih yang bebas kamu lukis kembali.",
                "reflectionQuestion": "Beban ekspektasi siapa yang selama ini paling menghalangi langkahmu untuk menjadi diri sendiri?",
                "keywords": ["Autentik", "Kemerdekaan Batin", "Reinventing Diri", "Menerima"]
            },
            "relationships": {
                "title": "Koneksi Sosial yang Segar dan Tulus",
                "summary": "Memperluas pertemanan dan meruntuhkan batasan ego dalam keluarga.",
                "meaning": "The Fool membawa suasana ceria dan riang dalam pergaulan. Dalam persahabatan dan keluarga, sikap lugas tanpa intrik akan mencairkan ketegangan. Kamu memiliki kesempatan bertemu lingkaran pertemanan baru yang memperkaya wawasan hidupmu.",
                "advice": "Hadir dengan tulus, dengarkan tanpa menghakimi, dan ajak orang-orang tersayang tertawa bersama.",
                "reflectionQuestion": "Bagaimana caramu membawa lebih banyak kehangatan dan kejenakaan ke dalam interaksi sosialmu?",
                "keywords": ["Lingkaran Baru", "Ketulusan", "Kebersamaan", "Kejujuran"]
            },
            "spirituality": {
                "title": "Perjalanan Jiwa Menuju Ketidaktahuan Kudus",
                "summary": "Menyerahkan kendali ego kepada bimbingan intuisi dan semesta.",
                "meaning": "Secara spiritual, The Fool adalah peziarah murni. Kartu ini mengajakmu melepaskan kebutuhan mengontrol setiap detail takdir dan mulai mempercayai aliran semesta. Kedamaian sejati ditemukan saat kamu berani berserah dan hadir utuh di saat ini.",
                "advice": "Luangkan waktu hening untuk mendengarkan bisikan halus intuisimu tanpa terburu-buru menganalisisnya dengan logika sempit.",
                "reflectionQuestion": "Apa yang terjadi jika kamu sepenuhnya percaya bahwa alam semesta sedang mendukung langkahmu?",
                "keywords": ["Berserah", "Intuisi", "Ziarah Batin", "Kepercayaan Semesta"]
            }
        }
    },
    {
        "id": "the-magician",
        "number": 1,
        "name": "The Magician",
        "slug": "the-magician",
        "image": "/assets/tarot/cards/The Magician.jpg",
        "arcana": "major",
        "uprightKeywords": ["Manifestasi", "Kekuatan Kehendak", "Keahlian", "Kreativitas", "Fokus"],
        "reversedKeywords": ["Manipulasi", "Bakat Terpendam", "Kurang Fokus", "Trik Murahan"],
        "description": "The Magician berdiri dengan tangan kanan menunjuk ke langit dan tangan kiri ke bumi. Di mejanya terdapat cawan, pedang, tongkat, dan koin—simbol penguasaan atas empat elemen untuk memanifestasikan kehendak batin menjadi realitas nyata.",
        "readings": {
            "love": {
                "title": "Daya Tarik Magnetis dan Niat Nyata",
                "summary": "Kemampuan mewujudkan komunikasi yang harmonis dan chemistry yang mendalam.",
                "meaning": "Dalam percintaan, The Magician menunjukkan bahwa kamu memiliki daya pikat dan kemampuan komunikasi yang luar biasa. Jika lajang, niat kuatmu mampu menarik seseorang yang sefrekuensi. Bagi yang berpasangan, kartu ini mendorong inisiatif menciptakan momen romantis yang segar.",
                "advice": "Nyatakan perasaanmu dengan jelas dan ambil langkah proaktif untuk menyalakan kembali kehangatan asmara.",
                "reflectionQuestion": "Bagaimana niat dan energimu saat ini mempengaruhi dinamika hubungan cintamu?",
                "keywords": ["Daya Tarik", "Komunikasi Aktif", "Manifestasi Cinta", "Inisiatif"]
            },
            "work": {
                "title": "Penguasaan Keterampilan dan Solusi Efektif",
                "summary": "Memanfaatkan seluruh sarana dan bakat yang ada untuk menyelesaikan pekerjaan dengan gemilang.",
                "meaning": "The Magician di dunia kerja adalah lambang kompetensi tinggi dan kelincahan berpikir. Segala sumber daya yang kamu butuhkan sudah ada di tanganmu. Kamu mampu menghubungkan orang, alat, dan ide menjadi eksekusi proyek yang sangat produktif.",
                "advice": "Fokuskan konsentrasimu pada satu sasaran utama dan hindari multitasking yang memecah ketajaman analisismu.",
                "reflectionQuestion": "Sumber daya atau keterampilan apa yang belum kamu optimalkan dalam tugas kerjamu saat ini?",
                "keywords": ["Kompetensi", "Eksekusi", "Konsentrasi", "Kepiawaian"]
            },
            "career": {
                "title": "Mewujudkan Visi Profesional",
                "summary": "Peluang emas untuk menunjukkan kepemimpinan dan meluncurkan inisiatif mandiri.",
                "meaning": "Karier di bawah pengaruh The Magician menandakan waktu terbaik untuk mewujudkan rencana besar. Portofolio, pengalaman, dan jejaringmu telah cukup matang untuk membawa posisimu ke jenjang yang lebih tinggi atau memulai usaha profesionalmu sendiri.",
                "advice": "Tunjukkan kemampuanmu secara percaya diri tanpa keraguan; bertindaklah sebagai pemimpin bagi visi kariermu.",
                "reflectionQuestion": "Proyek besar apa yang siap kamu wujudkan jika kamu sepenuhnya meyakini kemampuan dirimu?",
                "keywords": ["Visi Nyata", "Kepemimpinan", "Pencapaian", "Peluang Emas"]
            },
            "finance": {
                "title": "Kecakapan Membangun Kelimpahan",
                "summary": "Kemampuan mengubah ide kreatif menjadi nilai ekonomi dan sumber penghasilan.",
                "meaning": "The Magician menandakan kelihaian mengelola dan menciptakan aliran dana baru. Bakat atau keahlian yang kamu miliki memiliki nilai jual yang nyata. Kuncinya adalah mengubah ide di kepala menjadi aksi terstruktur yang terukur.",
                "advice": "Diversifikasi keterampilanmu menjadi peluang produktif; perhatikan rincian kontrak dan negosiasikan nilaimu dengan tegas.",
                "reflectionQuestion": "Bagaimana kamu bisa memanfaatkan keahlian unikmu untuk menciptakan stabilitas finansial tambahan?",
                "keywords": ["Kelimpahan", "Nilai Jual", "Negosiasi", "Kreasi Materi"]
            },
            "selfGrowth": {
                "title": "Menyadari Kekuatan Pencipta di Dalam Diri",
                "summary": "Peralihan dari sikap pasif menjadi pencipta aktif jalan hidupmu sendiri.",
                "meaning": "Pengembangan diri bersama The Magician menyadarkanmu bahwa kamu bukanlah korban keadaan. Kamu memiliki kekuatan pikiran, tekad batin, dan kapasitas emosional untuk mengubah arah nasibmu sendiri menuju kondisi yang lebih selaras.",
                "advice": "Selaraskan pikiran, ucapan, dan tindakanmu agar energimu terarah utuh tanpa kebocoran mental.",
                "reflectionQuestion": "Kebiasaan atau narasi diri apa yang perlu kamu ubah agar sejalan dengan tujuan tertinggimu?",
                "keywords": ["Kehendak Sadar", "Pemberdayaan", "Fokus Batin", "Penyelarasan"]
            },
            "relationships": {
                "title": "Komunikasi yang Menghubungkan dan Menginspirasi",
                "summary": "Menjadi perekat harmoni dan jembatan pemahaman di antara orang-orang terdekat.",
                "meaning": "The Magician membawa kefasihan dan pesona dalam interaksi sosial. Kamu mampu meredakan kesalahpahaman keluarga dengan penjelasan yang tenang dan bijak. Teman-temanmu melihatmu sebagai sosok inspiratif yang membawa energi positif.",
                "advice": "Gunakan pengaruh bicaramu untuk mengangkat semangat orang lain dan menghindari kata-kata manipulatif.",
                "reflectionQuestion": "Apakah caramu berkomunikasi saat ini sudah sepenuhnya jujur dan membangun bagi orang di sekitarmu?",
                "keywords": ["Inspirasi", "Jembatan Harmoni", "Artikulasi", "Kehangatan Sosial"]
            },
            "spirituality": {
                "title": "Penyatuan Makrokosmos dan Mikrokosmos",
                "summary": "Menjadi saluran perantara kehendak luhur ke dalam realitas duniawi.",
                "meaning": "Secara spiritual, The Magician mengartikan konsep 'seperti di atas, begitu pula di bawah'. Doa, meditasi, dan afirmasimu memiliki daya getar kuat. Latihlah kesadaran penuh bahwa setiap tindakan fisikmu adalah wujud dedikasi jiwa.",
                "advice": "Jaga kejernihan niat spiritualmu; gunakan kemampuan batinmu untuk melayani kebaikan bersama.",
                "reflectionQuestion": "Bagaimana kamu mempraktikkan kesadaran spiritual dalam rutinitas keseharianmu?",
                "keywords": ["Kanal Energi", "Afirmasi Kuat", "Kesadaran Penuh", "Kebaikan Universal"]
            }
        }
    },
    {
        "id": "the-high-priestess",
        "number": 2,
        "name": "The High Priestess",
        "slug": "the-high-priestess",
        "image": "/assets/tarot/cards/The High Priestess.jpg",
        "arcana": "major",
        "uprightKeywords": ["Intuisi", "Rahasia Ilahi", "Bawah Sadar", "Ketenangan Batin", "Kebijaksanaan"],
        "reversedKeywords": ["Mengabaikan Intuisi", "Rahasia Tersembunyi", "Dangkal", "Ketidakstabilan Emosi"],
        "description": "Duduk di antara pilar hitam Boaz dan pilar putih Jachin di depan tabir bermotif delima, The High Priestess memegang gulungan TORA. Ia adalah penjaga misteri alam bawah sadar, kebijaksanaan sunyi, dan intuisi terdalam jiwa.",
        "readings": {
            "love": {
                "title": "Kedalaman Hati dan Ikatan Jiwa",
                "summary": "Mendengarkan getaran batin yang tak terucapkan dalam hubungan asmara.",
                "meaning": "The High Priestess mengindikasikan adanya keheningan bermakna atau koneksi batin yang kuat. Ada perasaan atau rahasia yang sedang berkembang di bawah permukaan. Jangan memaksakan jawaban tergesa-gesa; percayai firasatmu mengenai niat seseorang.",
                "advice": "Beri ruang bagi hubungan untuk bernapas; dengarkan apa yang dirasakan hatimu melampaui kata-kata lahiriah.",
                "reflectionQuestion": "Kebenaran apa tentang hubunganmu yang sebenarnya sudah kamu ketahui namun enggan kamu akui?",
                "keywords": ["Ikatan Batin", "Firasat Asmara", "Keheningan Bermakna", "Misteri Hati"]
            },
            "work": {
                "title": "Pengamatan Cermat Sebelum Bertindak",
                "summary": "Menyimpan strategi kunci dan membaca dinamika terselubung di lingkungan kerja.",
                "meaning": "Di tempat kerja, kartu ini menyarankan sikap tenang dan observatif. Tidak semua hal perlu diumumkan ke publik sekarang. Ada dinamika kantor atau informasi penting yang belum terungkap penuh; jadilah pengamat yang bijak sebelum mengambil sikap.",
                "advice": "Jaga kerahasiaan rencana penting dan percayai nalurimu dalam menilai motif rekan atau klien.",
                "reflectionQuestion": "Informasi atau sinyal halus apa di tempat kerja yang perlu kamu perhatikan lebih saksama?",
                "keywords": ["Observasi", "Kebijaksanaan Sunyi", "Diplomasi Halus", "Kerahasiaan"]
            },
            "career": {
                "title": "Panggilan Karier Berbasis Nilai Mendalam",
                "summary": "Memadukan keahlian analitis dengan ketajaman intuisi dalam profesimu.",
                "meaning": "Dalam pengembangan karier, The High Priestess menunjukkan waktu untuk menggali pengetahuan lebih dalam, mungkin melalui riset, studi lanjutan, atau bidang keahlian khusus. Jawaban atas arah kariermu terletak pada apa yang benar-benar memuaskan nuranimu.",
                "advice": "Kembangkan keahlian khusus yang bernilai langka dan biarkan reputasimu bertumbuh melalui karya berkualitas.",
                "reflectionQuestion": "Bidang studi atau keilmuan apa yang paling memikat rasa ingin tahumu saat ini?",
                "keywords": ["Studi Mendalam", "Keahlian Langka", "Panggilan Jiwa", "Pengetahuan Luhur"]
            },
            "finance": {
                "title": "Pertimbangan Tenang dan Menjaga Privasi Finansial",
                "summary": "Hindari spekulasi terburu-buru dan simpan rencana keuangan untuk dirimu sendiri.",
                "meaning": "Secara finansial, kartu ini menasehati agar kamu tidak membicarakan aset atau rencana investasimu kepada pihak yang tidak relevan. Ada aspek dari kondisi keuanganmu yang memerlukan tinjauan cermat dan ketenangan pikiran sebelum membuat komitmen baru.",
                "advice": "Tunda pengeluaran besar jika hatimu merasa belum mantap; lakukan pengecekan ulang terhadap dokumen keuangan.",
                "reflectionQuestion": "Apakah kamu merasa tertekan untuk membelanjakan uang demi citra di hadapan orang lain?",
                "keywords": ["Privasi Finansial", "Ketelitian", "Tinjauan Cermat", "Ketenangan Materi"]
            },
            "selfGrowth": {
                "title": "Menyelami Samudra Bawah Sadar",
                "summary": "Memahami mimpi, bayangan psikologis, dan intuisi terdalam dirimu.",
                "meaning": "The High Priestess adalah pemandu perjalanan batin. Momen ini mengundangmu untuk bermeditasi, menulis jurnal mimpi, dan mengenali pola emosi yang berakar di alam bawah sadar. Kedamaian sejati tercapai ketika kamu berani menerima seluruh lapisan jiwamu.",
                "advice": "Luangkan waktu sendirian dalam keheningan teratur untuk memulihkan kejernihan energimu.",
                "reflectionQuestion": "Pesan apa yang sering muncul dalam mimpi atau firasatmu belakangan ini?",
                "keywords": ["Bawah Sadar", "Jurnal Jiwa", "Meditasi", "Keheningan"]
            },
            "relationships": {
                "title": "Kehadiran yang Menenangkan Tanpa Menghakimi",
                "summary": "Menjadi ruang aman dan pendengar setia bagi keluarga dan sahabat.",
                "meaning": "Dalam hubungan persahabatan dan keluarga, kamu menjadi sosok penenang yang dipercaya menyimpan rahasia dan mencurahkan isi hati. Kamu mampu merasakan kesedihan orang lain tanpa mereka perlu mengucapkannya.",
                "advice": "Hormati batas privasi orang lain dan jaga kepercayaan yang telah dititipkan kepadamu sebaik-baiknya.",
                "reflectionQuestion": "Siapa dalam lingkaranmu yang membutuhkan telinga tulus tanpa diberi nasihat menggurui?",
                "keywords": ["Pendengar Setia", "Ruang Aman", "Empati Halus", "Penjaga Rahasia"]
            },
            "spirituality": {
                "title": "Gerbang Menuju Kearifan Mistis",
                "summary": "Memasuki dimensi hening tempat suara ilahi berbicara tanpa kata.",
                "meaning": "Pada tataran spiritual, kartu ini menandakan pembukaan mata batin dan sinkronisitas kosmis. Kamu diajak melampaui dogma lahiriah menuju penghayatan spiritual yang langsung dan personal. Alam semesta sedang berkomunikasi lewat simbol dan firasat lembut.",
                "advice": "Percayalah pada getaran batinmu saat berdoa atau bermeditasi; kebijaksanaan tertinggi tinggal di dalam dirimu.",
                "reflectionQuestion": "Bagaimana caramu menjaga kesucian ruang batinmu di tengah kebisingan dunia modern?",
                "keywords": ["Sinkronisitas", "Mata Batin", "Misteri Suci", "Kearifan Ilahi"]
            }
        }
    },
    {
        "id": "the-empress",
        "number": 3,
        "name": "The Empress",
        "slug": "the-empress",
        "image": "/assets/tarot/cards/The Empress.jpg",
        "arcana": "major",
        "uprightKeywords": ["Kesuburan", "Kelimpahan", "Pengasuhan", "Kreativitas", "Kehangatan Alam"],
        "reversedKeywords": ["Ketergantungan", "Kekeringan Kreatif", "Kelelahan Merawat", "Protektif Berlebih"],
        "description": "Duduk di tengah ladang gandum yang menguning dengan mahkota dua belas bintang dan jubah berhias delima, The Empress adalah perwujudan Ibu Pertiwi. Ia melambangkan cinta tanpa syarat, kesuburan ide, dan kenikmatan hidup indrawi.",
        "readings": {
            "love": {
                "title": "Cinta yang Mengasuh dan Mengalir Hangat",
                "summary": "Pertumbuhan kasih sayang yang penuh empati, kelembutan, dan ketertarikan timbal balik.",
                "meaning": "The Empress membawa kehangatan yang merengkuh dalam ranah cinta. Hubunganmu sedang atau berpotensi memasuki fase yang sangat romantis, subur, dan penuh penerimaan. Ada keinginan untuk saling merawat, menciptakan kenyamanan bersama, dan membangun masa depan yang harmonis.",
                "advice": "Tunjukkan kasih sayangmu lewat sentuhan lembut, perhatian tulus, dan ciptakan suasana rumah yang nyaman bagi pasangan.",
                "reflectionQuestion": "Bagaimana caramu menunjukkan rasa cinta tanpa melupakan kebutuhan untuk merawat dirimu sendiri?",
                "keywords": ["Kasih Sayang", "Kelembutan", "Romantisme", "Pengasuhan"]
            },
            "work": {
                "title": "Masa Panen Kreatif dan Kolaborasi Harmonis",
                "summary": "Ide-ide kerja bermekaran dan proyek-proyek penting berkembang dengan subur.",
                "meaning": "Di tempat kerja, The Empress menandakan iklim kerja yang kondusif di mana kreativitas dan empati dihormati. Pendekatanmu yang ramah dan memelihara hubungan baik antartim membawa hasil yang jauh lebih efektif dibandingkan tekanan koersif.",
                "advice": "Beri waktu bagi proyek-proyekmu untuk matang secara alami; sirami dengan ketekunan tanpa terburu-buru memaksakan deadline.",
                "reflectionQuestion": "Ide atau inisiatif kerja apa yang saat ini paling membutuhkan sentuhan perhatian dan ketelatenanmu?",
                "keywords": ["Kreativitas Subur", "Kolaborasi Ramah", "Proses Alami", "Kelancaran Kerja"]
            },
            "career": {
                "title": "Pertumbuhan Karier yang Organik dan Melimpah",
                "summary": "Membangun reputasi melalui karya yang memberikan nilai nyata dan menyentuh banyak orang.",
                "meaning": "Karier di bawah pengaruh The Empress mengarah pada kepuasan batin dan pencapaian yang memberi kehidupan. Profesi di bidang kreatif, perawatan, pengajaran, desain, atau pelayanan publik sangat diuntungkan. Usahamu mulai menampakkan buah yang ranum.",
                "advice": "Rancang karya yang membawa kebaikan dan kenyamanan bagi audiensmu; pertumbuhanmu akan mengikuti secara organik.",
                "reflectionQuestion": "Dampak positif apa yang ingin kamu berikan kepada lingkungan sekitarmu melalui kariermu?",
                "keywords": ["Pertumbuhan Organik", "Dampak Nyata", "Kelimpahan Karier", "Karya Indah"]
            },
            "finance": {
                "title": "Kelimpahan Rezeki dan Stabilitas Kenyamanan",
                "summary": "Arus keuangan yang mengalir lancar dan penghargaan terhadap kenikmatan hidup yang sehat.",
                "meaning": "The Empress adalah salah satu kartu paling positif untuk keuangan. Ini menandakan fase kemakmuran, kestabilan materi, dan keamanan aset. Kamu mampu menikmati hasil jerih payahmu sambil tetap menabur bibit investasi yang menjanjikan.",
                "advice": "Syukuri kelimpahanmu dan nikmati hidup secukupnya; investasikan sebagian rezekimu pada hal-hal yang meningkatkan kualitas hidup jangka panjang.",
                "reflectionQuestion": "Apakah kamu sudah merasa cukup dan bersyukur atas apa yang telah kamu miliki hari ini?",
                "keywords": ["Kemakmuran", "Panen Rezeki", "Kenyamanan Sehat", "Rasa Syukur"]
            },
            "selfGrowth": {
                "title": "Mencintai dan Menghargai Raga serta Jiwa",
                "summary": "Mempraktikkan self-love sejati melalui perawatan diri, nutrisi baik, dan relaksasi.",
                "meaning": "Pengembangan diri di bawah kartu ini menekankan kebaikan hati terhadap diri sendiri. Berhentilah mengkritik tubuh atau kekuranganmu. Kamu diajak terhubung kembali dengan alam, menikmati keindahan seni, dan memperlakukan dirimu selayaknya anak yang sangat disayangi.",
                "advice": "Jadwalkan waktu istirahat yang berkualitas, jalan-jalan di alam terbuka, dan manjakan indramu dengan hal-hal positif.",
                "reflectionQuestion": "Kapan terakhir kali kamu benar-benar memanjakan dan merawat tubuhmu dengan rasa terima kasih?",
                "keywords": ["Self-Care", "Penerimaan Tubuh", "Koneksi Alam", "Kebaikan Hati"]
            },
            "relationships": {
                "title": "Rumah Hati yang Selalu Terbuka",
                "summary": "Membangun kehangatan keluarga dan pertemanan yang saling mendukung tanpa pamrih.",
                "meaning": "Dalam lingkaran keluarga dan sahabat, energimu memancarkan rasa aman yang membuat orang lain merasa diterima seutuhnya. Momen berkumpul, makan bersama, dan berbagi cerita hangat menjadi sumber kebahagiaan bersama yang mendalam.",
                "advice": "Jadilah tuan rumah yang ramah bagi hati orang-orang terkasihmu, namun tetap tetapkan batasan agar energimu tidak terkuras habis.",
                "reflectionQuestion": "Bagaimana kamu bisa mempererat tali silaturahmi dengan anggota keluarga yang sempat merenggang?",
                "keywords": ["Kehangatan Keluarga", "Kebaikan Sosial", "Kenyamanan Bersama", "Dukungan Tulus"]
            },
            "spirituality": {
                "title": "Kekudusan dalam Ciptaan dan Kehidupan Nyata",
                "summary": "Menemukan kehadiran ilahi di setiap helai daun, tetes hujan, dan detak jantung kehidupan.",
                "meaning": "The Empress mengajarkan spiritualitas imanen: bahwa yang ilahi hadir secara nyata di dalam kehidupan duniawi. Doa dan rasa syukur terwujud saat kamu mengagumi ciptaan, menghormati ritme alam, dan merayakan berkah kehidupan dengan hati bersukacita.",
                "advice": "Luangkan waktu hening di bawah pohon atau di dekat air mengalir; rasakan bahwa bumi tempatmu berpijak adalah berkah kudus.",
                "reflectionQuestion": "Bagaimana kamu dapat memandang keindahan alam sebagai pengingat akan kasih semesta yang tak terbatas?",
                "keywords": ["Ibu Pertiwi", "Spiritualitas Alami", "Rasa Syukur Kudus", "Berkah Hidup"]
            }
        }
    },
    {
        "id": "the-emperor",
        "number": 4,
        "name": "The Emperor",
        "slug": "the-emperor",
        "image": "/assets/tarot/cards/The Emperor.jpg",
        "arcana": "major",
        "uprightKeywords": ["Otoritas", "Struktur", "Stabilitas", "Kepemimpinan", "Disiplin"],
        "reversedKeywords": ["Tirani", "Kekakuan", "Kehilangan Kendali", "Penyalahgunaan Kuasa"],
        "description": "Duduk kokoh di atas takhta batu berhias empat kepala domba jantan dengan tongkat ankh di tangan, The Emperor adalah figur pelindung, pembuat ketertiban, dan pilar stabilitas yang memadukan tekad baja dengan visi praktis.",
        "readings": {
            "love": {
                "title": "Komitmen yang Kokoh dan Perlindungan Nyata",
                "summary": "Hubungan asmara yang dilandasi kepastian, rasa aman, dan tanggung jawab bersama.",
                "meaning": "The Emperor menunjukkan komitmen yang mantap dan keseriusan dalam cinta. Kamu atau pasangan menginginkan kejelasan status dan fondasi yang stabil untuk masa depan. Hubungan ini menghargai loyalitas, perlindungan emosional, dan kepastian tindakan nyata.",
                "advice": "Tunjukkan cintamu melalui tindakan konsisten dan penuhilah janji-janji yang telah kamu buat.",
                "reflectionQuestion": "Apakah kamu sudah menciptakan rasa aman dan kepastian bagi orang yang kamu sayangi?",
                "keywords": ["Komitmen Kuat", "Fondasi Stabil", "Tanggung Jawab", "Kepastian Asmara"]
            },
            "work": {
                "title": "Ketertiban Sistem dan Manajemen Efisien",
                "summary": "Menerapkan struktur kerja yang disiplin untuk mencapai target secara terukur.",
                "meaning": "Di lingkungan kerja, The Emperor menuntut kedisiplinan, SOP yang jelas, dan manajemen waktu yang presisi. Pendekatan terorganisasi dan kemampuan memimpin proyek besar akan membawamu mencapai hasil optimal tanpa kekacauan.",
                "advice": "Susun rencana kerja tertulis, delegasikan wewenang dengan jelas, dan patuhi tenggat waktu secara tegas.",
                "reflectionQuestion": "Sistem kerja apa yang perlu kamu rapikan agar produktivitas tim meningkat?",
                "keywords": ["Kedisiplinan", "SOP Jelas", "Manajemen Waktu", "Ketertiban Kerja"]
            },
            "career": {
                "title": "Puncak Kepemimpinan dan Otoritas Terpercaya",
                "summary": "Pengakuan atas integritas, kapasitas kepemimpinan, dan visi strategismu.",
                "meaning": "Karier di bawah pengaruh The Emperor menunjukkan peningkatan posisi menjadi penanggung jawab utama, manajer, atau pendiri bisnis. Otoritasmu diakui karena kamu memiliki ketegasan bersikap dan rekam jejak yang dapat diandalkan.",
                "advice": "Pimpinlah dengan keteladanan dan keadilan; jadilah figur yang mengayomi dan membimbing bawahannya.",
                "reflectionQuestion": "Bagaimana caramu mengelola kekuasaan dan tanggung jawab profesional agar tetap adil bagi semua pihak?",
                "keywords": ["Otoritas", "Promosi Posisi", "Ketegasan Visi", "Kepemimpinan Adil"]
            },
            "finance": {
                "title": "Stabilitas Finansial dan Alokasi Terencana",
                "summary": "Pengelolaan aset dengan ketat, rasional, dan berorientasi perlindungan jangka panjang.",
                "meaning": "Secara finansial, kartu ini mengindikasikan kondisi keuangan yang terkendali dengan baik. Kamu memiliki perencanaan anggaran yang kokoh, dana darurat yang memadai, dan investasi yang aman dari gejolak spekulasi.",
                "advice": "Pertahankan disiplin anggaranmu; lakukan audit berkala terhadap pengeluaran dan hindari utang konsumtif.",
                "reflectionQuestion": "Seberapa kokoh fondasi dana darurat dan perlindungan asetmu saat ini?",
                "keywords": ["Anggaran Ketat", "Dana Darurat", "Perlindungan Aset", "Stabilitas Finansial"]
            },
            "selfGrowth": {
                "title": "Membangun Disiplin Batin dan Batasan Diri",
                "summary": "Menguasai dorongan impulsif demi mencapai kemandirian dan integritas karakter.",
                "meaning": "Pengembangan diri The Emperor berpusat pada kedaulatan atas diri sendiri. Kamu diajak menetapkan batasan yang sehat, menepati komitmen kepada diri sendiri, dan melatih kebiasaan positif yang membentuk ketangguhan mental.",
                "advice": "Terapkan rutinitas pagi yang disiplin dan pegang teguh prinsip integritas dalam setiap keputusan.",
                "reflectionQuestion": "Area kehidupan mana yang saat ini paling membutuhkan ketegasan dan kedisiplinan pribadimu?",
                "keywords": ["Kedaulatan Diri", "Integritas Karakter", "Batasan Sehat", "Ketangguhan Mental"]
            },
            "relationships": {
                "title": "Pilar Keandalan dalam Lingkaran Keluarga",
                "summary": "Menjadi sandaran tepercaya yang memberikan arahan bijak dan perlindungan keluarga.",
                "meaning": "Dalam keluarga dan komunitas, kamu dipandang sebagai tiang penyangga yang diandalkan ketika terjadi krisis. Nasihatmu dicari karena kamu mampu berpikir jernih tanpa terbawa arus emosi yang berlebihan.",
                "advice": "Bimbinglah orang-orang tersayang dengan ketegasan yang dilandasi cinta, bukan sikap mendikte.",
                "reflectionQuestion": "Bagaimana kamu menyeimbangkan ketegasan prinsip dengan kehangatan kasih dalam keluargamu?",
                "keywords": ["Tiang Penyangga", "Nasihat Bijak", "Perlindungan Keluarga", "Keandalan"]
            },
            "spirituality": {
                "title": "Penegakan Hukum Moral dan Ketertiban Jiwa",
                "summary": "Menemukan keheningan sakral melalui keteraturan hidup dan komitmen spiritual.",
                "meaning": "Secara spiritual, The Emperor melambangkan ketertiban kosmis dan hukum moral universal. Praktik spiritual yang teratur dan konsisten setiap hari—seperti doa terjadwal atau meditasi rutin—akan membawa kestabilan jiwa yang tak tergoyahkan.",
                "advice": "Jadikan latihan spiritualmu sebagai komitmen harian yang sakral dan tak tergoyahkan oleh kesibukan duniawi.",
                "reflectionQuestion": "Apakah rutinitas ibadah atau meditasimu sudah cukup konsisten dalam membentuk ketenangan hatimu?",
                "keywords": ["Ketertiban Kosmis", "Disiplin Ibadah", "Hukum Moral", "Kestabilan Jiwa"]
            }
        }
    },
    {
        "id": "the-hierophant",
        "number": 5,
        "name": "The Hierophant",
        "slug": "the-hierophant",
        "image": "/assets/tarot/cards/The Hierophant.jpg",
        "arcana": "major",
        "uprightKeywords": ["Tradisi", "Kearifan Leluhur", "Pendidikan", "Bimbingan Rohani", "Nilai Bersama"],
        "reversedKeywords": ["Dogmatisme Kaku", "Pemberontakan", "Ketidaksesuaian Nilai", "Kemunafikan"],
        "description": "Duduk di antara dua pilar suci dengan mengenakan tiga mahkota tiara dan memegang tongkat salib tripel, The Hierophant adalah pembimbing spiritual dan penjaga nilai-nilai luhur yang menghubungkan manusia dengan ajaran abadi.",
        "readings": {
            "love": {
                "title": "Penyelarasan Nilai dan Hubungan Bermakna",
                "summary": "Membangun ikatan asmara yang didasarkan pada prinsip moral dan keselarasan visi hidup.",
                "meaning": "The Hierophant menandakan hubungan yang menghargai komitmen tradisional, restu keluarga, dan keselarasan nilai-nilai hidup. Hubungan ini tumbuh subur saat kedua belah pihak saling menghormati prinsip moral dan memiliki pandangan yang sama tentang pernikahan dan masa depan.",
                "advice": "Bicarakan nilai-nilai fundamental hidupmu secara terbuka dan libatkan keluarga dengan penuh rasa hormat.",
                "reflectionQuestion": "Apakah nilai spiritual dan prinsip moralmu selaras dengan pasanganmu saat ini?",
                "keywords": ["Keselarasan Nilai", "Restu Keluarga", "Prinsip Moral", "Komitmen Sah"]
            },
            "work": {
                "title": "Belajar dari Mentor dan Mengikuti Prosedur Baku",
                "summary": "Mematuhi standar profesional dan menghormati pengalaman rekan yang lebih senior.",
                "meaning": "Di lingkungan kerja, kartu ini menyarankan untuk menghormati budaya organisasi, regulasi resmi, dan metodologi yang telah teruji. Mencari mentor atau mengikuti pelatihan tersertifikasi akan mempercepat kemajuanmu secara signifikan.",
                "advice": "Rendahkan hati untuk belajar dari para ahli dan patuhi kode etik profesi dengan sungguh-sungguh.",
                "reflectionQuestion": "Siapa sosok senior atau mentor yang dapat membimbingmu mengatasi tantangan kerja saat ini?",
                "keywords": ["Mentorship", "Kode Etik", "Metodologi Teruji", "Standar Baku"]
            },
            "career": {
                "title": "Pengakuan Institusional dan Pendidikan Lanjutan",
                "summary": "Meningkatkan kredibilitas profesional melalui sertifikasi, institusi terkemuka, atau pengajaran.",
                "meaning": "Karier di bawah pengaruh The Hierophant sering kali terhubung dengan institusi mapan, dunia akademis, hukum, keagamaan, atau lembaga pelatihan. Kredibilitasmu dibangun di atas fondasi keilmuan yang sah dan reputasi etis yang bersih.",
                "advice": "Tingkatkan kualifikasi formalmu dan bagikan ilmumu melalui bimbingan kepada generasi penerus.",
                "reflectionQuestion": "Langkah sertifikasi atau pendidikan apa yang perlu kamu tempuh untuk memperkuat posisi kariermu?",
                "keywords": ["Kredibilitas", "Kualifikasi Sah", "Edukasi", "Reputasi Etis"]
            },
            "finance": {
                "title": "Instrumen Keuangan Konvensional dan Terpercaya",
                "summary": "Memilih jalur investasi aman dan meminta nasihat dari perencana keuangan resmi.",
                "meaning": "Dalam hal keuangan, The Hierophant memperingatkan agar tidak tergiur oleh skema cepat kaya atau instrumen keuangan yang tidak jelas legalitasnya. Pilihlah bank konvensional, instrumen berizin resmi, dan rencana tabungan jangka panjang yang terstruktur.",
                "advice": "Konsultasikan rencana finansialmu dengan ahli yang berkompeten dan hindari jalan pintas finansial.",
                "reflectionQuestion": "Apakah keputusan investasimu sudah sesuai dengan instrumen yang terpercaya dan legal?",
                "keywords": ["Investasi Resmi", "Keamanan Finansial", "Nasihat Ahli", "Hindari Spekulasi"]
            },
            "selfGrowth": {
                "title": "Mendalami Kearifan Filosofis dan Bimbingan Batin",
                "summary": "Membaca karya-karya klasik, mendalami filsafat hidup, dan menemukan guru sejati.",
                "meaning": "Pengembangan diri kartu ini adalah tentang memperdalam pemahaman etika dan filsafat hidup. Kamu diundang untuk merenungkan warisan kearifan masa lalu, menemukan makna di balik ritual sehari-hari, dan menyelaraskan egomu dengan hukum kebaikan universal.",
                "advice": "Pelajari ajaran kebijaksanaan dari para pemikir besar dan jadikan prinsip kebajikan sebagai kompas tindakanmu.",
                "reflectionQuestion": "Prinsip moral apa yang menjadi kompas hidup utamamu saat menghadapi dilema sulit?",
                "keywords": ["Filsafat Hidup", "Kearifan Leluhur", "Kompas Kebajikan", "Etika Luhur"]
            },
            "relationships": {
                "title": "Menghormati Adat dan Kebersamaan Komunitas",
                "summary": "Mempererat tali kekeluargaan melalui tradisi bersama dan silaturahmi yang santun.",
                "meaning": "Dalam hubungan sosial dan keluarga, The Hierophant menekankan pentingnya menghargai tradisi keluarga, menghadiri perayaan penting, dan menjaga tata krama. Hubungan yang harmonis terjaga saat kamu memperlakukan orang yang lebih tua dengan penuh takzim.",
                "advice": "Hadirilah pertemuan keluarga dengan hati gembira dan rawatlah jalinan silaturahmi antargenerasi.",
                "reflectionQuestion": "Tradisi keluarga apa yang bernilai luhur dan perlu terus kamu lestarikan?",
                "keywords": ["Tata Krama", "Silaturahmi", "Tradisi Keluarga", "Penghormatan"]
            },
            "spirituality": {
                "title": "Pencarian Makna Melalui Ajaran Suci",
                "summary": "Menghubungkan diri dengan tradisi spiritual luhur dan doa yang khusyuk.",
                "meaning": "Secara spiritual, The Hierophant membuka jalan pemahaman terhadap kitab suci, ritual ibadah, dan bimbingan rohani. Kamu didorong untuk tidak sekadar menjalankan ritual secara mekanis, melainkan memahami esensi kasih dan ketundukan hati di dalamnya.",
                "advice": "Tingkatkan kekhusyukan ibadahmu dan cari bimbingan dari guru rohani yang berakhlak mulia.",
                "reflectionQuestion": "Seberapa dalam kamu menghayati makna doa-doa yang kamu panjatkan setiap hari?",
                "keywords": ["Kekhusyukan", "Bimbingan Rohani", "Ajaran Suci", "Ibadah Tulus"]
            }
        }
    },
    {
        "id": "the-lovers",
        "number": 6,
        "name": "The Lovers",
        "slug": "the-lovers",
        "image": "/assets/tarot/cards/The Lovers.jpg",
        "arcana": "major",
        "uprightKeywords": ["Cinta Sejati", "Pilihan Moral", "Harmoni", "Ketertarikan Batin", "Kemitraan"],
        "reversedKeywords": ["Ketidakharmonisan", "Konflik Nilai", "Pilihan Salah", "Ragu Berkomitmen"],
        "description": "Di bawah naungan Malaikat Raphael yang merentangkan tangan memberkati, Adam dan Hawa berdiri di depan Pohon Kehidupan dan Pohon Pengetahuan. Kartu ini melambangkan penyatuan dua kutub jiwa, daya tarik cinta sejati, dan keputusan moral yang menentukan jalan hidup.",
        "readings": {
            "love": {
                "title": "Penyatuan Jiwa dan Chemistry yang Mendalam",
                "summary": "Koneksi asmara yang indah, saling melengkapi, dan penuh daya tarik emosional.",
                "meaning": "The Lovers adalah lambang cinta sejati dan resonansi batin yang luar biasa. Jika berpasangan, hubunganmu berada dalam keharmonisan manis di mana kejujuran dan rasa saling percaya mengalir alami. Jika lajang, kamu berpeluang bertemu seseorang yang memikat nuranimu secara mendalam.",
                "advice": "Bicarakan perasaanmu dengan kejujuran tanpa topeng; biarkan ketulusan menjadi jembatan penyatuan hatimu.",
                "reflectionQuestion": "Apakah kamu sudah sepenuhnya jujur terhadap apa yang kamu dambakan dalam sebuah hubungan cinta?",
                "keywords": ["Cinta Sejati", "Resonansi Batin", "Chemistry Manis", "Penyatuan Jiwa"]
            },
            "work": {
                "title": "Kolaborasi Selaras dan Kemitraan Sinergis",
                "summary": "Bekerja sama secara harmonis dengan rekan kerja yang saling melengkapi keahlian.",
                "meaning": "Di tempat kerja, The Lovers menunjukkan kemitraan bisnis atau kolaborasi tim yang sangat solid. Kesuksesan dicapai melalui kompromi sehat, komunikasi terbuka, dan penghargaan terhadap kelebihan masing-masing individu.",
                "advice": "Pilihlah mitra kerja yang memiliki integritas dan visi yang sejalan dengan prinsip kerjamu.",
                "reflectionQuestion": "Bagaimana kamu bisa meningkatkan rasa saling percaya dalam kolaborasi tim kerjamu?",
                "keywords": ["Sinergi", "Kemitraan Solid", "Kompromi Sehat", "Komunikasi Terbuka"]
            },
            "career": {
                "title": "Persimpangan Pilihan Karier yang Menentukan",
                "summary": "Membuat keputusan penting mengenai arah profesi yang sesuai dengan kata hati.",
                "meaning": "Karier di bawah naungan The Lovers menandakan momen persimpangan jalan. Kamu mungkin dihadapkan pada dua tawaran menarik atau harus memilih antara mengejar status finansial semata atau pekerjaan yang benar-benar kamu cintai.",
                "advice": "Pilihlah jalur yang paling selaras dengan nilai moral dan passion terdalammu, bukan sekadar iming-iming sesaat.",
                "reflectionQuestion": "Pilihan karier mana yang membuat hatimu merasa hidup dan bangga menjalaninya?",
                "keywords": ["Pilihan Moral", "Arah Profesi", "Keselarasan Hati", "Persimpangan Karier"]
            },
            "finance": {
                "title": "Keputusan Keuangan yang Bijak dan Berimbang",
                "summary": "Menyeimbangkan antara kebutuhan menikmati hidup dan komitmen tabungan masa depan.",
                "meaning": "Dalam ranah keuangan, kartu ini mengingatkan pentingnya membuat pilihan yang bertanggung jawab. Jangan biarkan godaan belanja impulsif mengorbankan rencana keuangan jangka panjang. Diskusikan keputusan pengeluaran besar bersama pasangan jika keuangan dikelola bersama.",
                "advice": "Buatlah kesepakatan bersama mengenai prioritas anggaran dan selaraskan tujuan finansialmu dengan pasangan.",
                "reflectionQuestion": "Apakah caramu mengalokasikan uang saat ini sudah selaras dengan nilai-nilai hidup yang kamu yakini?",
                "keywords": ["Keseimbangan Anggaran", "Prioritas Bersama", "Pilihan Finansial", "Tanggung Jawab"]
            },
            "selfGrowth": {
                "title": "Penyatuan Aspek Maskulin dan Feminin Batin",
                "summary": "Menerima seluruh bagian dirimu sendiri dan membuat pilihan yang autentik.",
                "meaning": "Pengembangan diri kartu The Lovers adalah tentang integrasi batin. Kamu diajak mendamaikan logika dan perasaan, ketegasan dan kelembutan. Cinta sejati terhadap orang lain hanya bisa mekar sempurna jika kamu telah mencintai dan menerima dirimu sendiri seutuhnya.",
                "advice": "Hargai intuisimu sebagaimana kamu menghargai analisismu; jangan mengkhianati kata hatimu demi menyenangkan orang lain.",
                "reflectionQuestion": "Bagian mana dari dirimu yang selama ini paling sulit kamu terima dengan penuh kasih?",
                "keywords": ["Integrasi Batin", "Penerimaan Diri", "Autentisitas", "Cinta Diri"]
            },
            "relationships": {
                "title": "Harmoni dan Kehangatan Persahabatan Sejati",
                "summary": "Menjalin pertemanan yang didasarkan pada rasa saling menghargai dan keterbukaan hati.",
                "meaning": "Dalam pergaulan dan keluarga, The Lovers membawa suasana damai dan saling memaafkan. Konflik masa lalu dapat diselesaikan dengan duduk bersama secara tulus. Kamu dikelilingi oleh sahabat yang benar-benar peduli pada kebahagiaanmu.",
                "advice": "Jadilah sahabat yang setia dan luangkan waktu berkualitas untuk memelihara tali persahabatan yang tulus.",
                "reflectionQuestion": "Siapa sahabat karib yang saat ini paling membutuhkan kehadiran dan dukungan tulusmu?",
                "keywords": ["Persahabatan Tulus", "Memaafkan", "Harmoni Sosial", "Waktu Berkualitas"]
            },
            "spirituality": {
                "title": "Penyatuan Cinta Kasih Universal",
                "summary": "Menyadari bahwa cinta kasih adalah hakikat tertinggi penciptaan alam semesta.",
                "meaning": "Secara spiritual, The Lovers melambangkan perkawinan mistis antara jiwa manusia dengan Sang Maha Pengasih. Seluruh ibadah dan laku batinmu bermuara pada satu hal: memancarkan kasih tanpa syarat kepada sesama makhluk ciptaan Tuhan.",
                "advice": "Jadikan kasih sayang sebagai motivasi utama dalam setiap doa dan perbuatan baikmu sepanjang hari.",
                "reflectionQuestion": "Bagaimana caramu menjadikan cinta kasih sebagai energi penggerak seluruh aktivitas hidupmu?",
                "keywords": ["Kasih Universal", "Perkawinan Mistis", "Ketulusan Jiwa", "Cinta Tanpa Syarat"]
            }
        }
    },
    {
        "id": "the-chariot",
        "number": 7,
        "name": "The Chariot",
        "slug": "the-chariot",
        "image": "/assets/tarot/cards/The Chariot.jpg",
        "arcana": "major",
        "uprightKeywords": ["Kemenangan", "Tekad Baja", "Kendali Diri", "Fokus", "Mengatasi Rintangan"],
        "reversedKeywords": ["Kehilangan Kendali", "Agresi Berlebih", "Kandas", "Kurang Disiplin"],
        "description": "Seorang pejuang berbaju zirah berdiri di atas kereta perang yang ditarik oleh dua sphinx (hitam dan putih) yang menghadap arah berlawanan. The Chariot melambangkan keberhasilan mengendalikan dorongan-dorongan batin yang bertentangan demi melesat maju mencapai tujuan mulia.",
        "readings": {
            "love": {
                "title": "Memperjuangkan Cinta dengan Ketulusan dan Keteguhan",
                "summary": "Mengatasi rintangan hubungan melalui komitmen kuat dan kedewasaan emosional.",
                "meaning": "The Chariot menandakan hubungan asmara yang membutuhkan usaha bersama untuk melewati tantangan eksternal (jarak, perbedaan pandangan, atau restu). Hubungan ini akan berhasil jika kedua belah pihak memiliki tekad kuat dan mampu mengarahkan emosi secara konstruktif.",
                "advice": "Tentukan arah masa depan hubunganmu bersama pasangan dan hadapi masalah secara bahu-membahu tanpa saling menyalahkan.",
                "reflectionQuestion": "Rintangan bersama apa yang saat ini paling membutuhkan keteguhan komitmenmu dan pasangan?",
                "keywords": ["Keteguhan Asmara", "Mengatasi Rintangan", "Komitmen Bersama", "Kemenangan Cinta"]
            },
            "work": {
                "title": "Melesat Menuju Target Melalui Disiplin Penuh",
                "summary": "Fokus pada penyelesaian proyek kerja dengan mengesampingkan distraksi yang menghambat.",
                "meaning": "Di lingkungan kerja, The Chariot adalah dorongan energi yang sangat dinamis. Kamu memiliki determinasi tinggi untuk menuntaskan target yang menantang. Kuncinya adalah mengendalikan dinamika tim dan mempertahankan ritme kerja yang stabil tanpa terbakar kejenuhan.",
                "advice": "Kunci fokusmu pada prioritas terpenting; tolak kompromi yang mengikis kualitas hasil kerjamu.",
                "reflectionQuestion": "Distraksi apa yang paling sering mengalihkan fokusmu dari target kerja utamamu?",
                "keywords": ["Determinasi", "Fokus Kuat", "Menuntaskan Target", "Disiplin Kerja"]
            },
            "career": {
                "title": "Terobosan Karier dan Kemenangan Profesional",
                "summary": "Mencapai puncak prestasi kerja melalui kerja keras, keberanian, dan tekad baja.",
                "meaning": "Karier di bawah pengaruh The Chariot menunjukkan kemajuan pesat dan kemenangan atas persaingan. Kamu berada pada posisi memimpin inisiatif besar atau memenangkan tender bergengsi. Reputasimu sebagai profesional tangguh semakin diperhitungkan.",
                "advice": "Manfaatkan momentum kesuksesan ini untuk mengamankan posisi yang lebih strategis bagi masa depanmu.",
                "reflectionQuestion": "Sasaran karier ambisius apa yang ingin kamu taklukkan dalam enam bulan ke depan?",
                "keywords": ["Terobosan", "Prestasi Gemilang", "Kemenangan", "Kemajuan Pesat"]
            },
            "finance": {
                "title": "Kendali Penuh Atas Arus Kas Finansial",
                "summary": "Disiplin ketat dalam melunasi kewajiban dan mengakumulasi tabungan modal.",
                "meaning": "Secara keuangan, kartu ini menuntutmu memegang kendali penuh atas pemasukan dan pengeluaran. Jangan biarkan keinginan konsumtif mengalahkan tujuan keuangan jangka panjangmu. Dengan tekad yang bulat, kamu mampu melunasi utang atau mencapai target tabungan tertentu.",
                "advice": "Tetapkan target angka tabungan yang terukur dan disiplinkan diri untuk tidak menyentuhnya sebelum waktunya.",
                "reflectionQuestion": "Langkah disiplin finansial apa yang harus kamu ambil mulai hari ini untuk mengamankan masa depanmu?",
                "keywords": ["Disiplin Tabungan", "Kendali Kas", "Target Finansial", "Pelunasan Kewajiban"]
            },
            "selfGrowth": {
                "title": "Menguasai Dorongan Ego dan Emosi Batin",
                "summary": "Menyelaraskan ambisi lahiriah dengan kedamaian nurani agar tidak terpecah belah.",
                "meaning": "Pengembangan diri The Chariot adalah tentang seni menguasai diri sendiri. Dua sphinx yang berbeda warna melambangkan emosi positif dan negatif yang ada di dalam dirimu. Kemenangan sejati terjadi saat kamu mampu mengarahkan kedua energi tersebut menuju tujuan yang bernilai.",
                "advice": "Latihlah kesabaran di saat marah dan latihlah kerendahan hati di saat sukses agar energimu tetap seimbang.",
                "reflectionQuestion": "Emosi atau kebiasaan apa di dalam dirimu yang saat ini paling membutuhkan kendali sadarmu?",
                "keywords": ["Penguasaan Diri", "Keseimbangan Emosi", "Kemenangan Batin", "Determinasi Jiwa"]
            },
            "relationships": {
                "title": "Membela Orang Terkasih dan Menyelesaikan Friksi",
                "summary": "Ketegasan bersikap untuk melindungi keluarga dan menjaga batas pergaulan yang sehat.",
                "meaning": "Dalam keluarga dan persahabatan, The Chariot mencerminkan jiwa pelindung. Kamu siap berdiri di garis depan membela kehormatan keluargamu. Namun, hindari sikap mendominasi atau memaksakan kehendak kepada orang lain di sekitarmu.",
                "advice": "Gunakan kekuatanmu untuk mengayomi, bukan untuk menundukkan pendapat orang lain dalam musyawarah.",
                "reflectionQuestion": "Apakah caramu melindungi orang tersayang sudah cukup lembut dan menghargai ruang pribadi mereka?",
                "keywords": ["Jiwa Pelindung", "Ketegasan Positif", "Batas Sehat", "Solidaritas"]
            },
            "spirituality": {
                "title": "Kendaraan Jiwa Menuju Tingkat Kesadaran Tinggi",
                "summary": "Menjadikan raga dan pikiran sebagai wahana suci bagi perjalanan evolusi jiwa.",
                "meaning": "Secara spiritual, The Chariot (Merkabah) adalah kendaraan kesadaran rohani. Kamu diajak melihat bahwa tubuh fisikmu adalah bait suci yang harus dijaga kebersihannya agar jiwamu dapat melesat mendekat kepada Sang Pencipta dengan penuh kepasrahan.",
                "advice": "Jaga kemurnian niat dan disiplin ibadahmu; biarkan jiwamu menjadi nakhoda bagi raga dan pikiranmu.",
                "reflectionQuestion": "Bagaimana kamu menjaga kesucian raga dan kejernihan pikiranmu dalam rutinitas ibadah?",
                "keywords": ["Bait Suci", "Evolusi Jiwa", "Merkabah", "Kesadaran Tinggi"]
            }
        }
    },
    {
        "id": "strength",
        "number": 8,
        "name": "Strength",
        "slug": "strength",
        "image": "/assets/tarot/cards/Strength.jpg",
        "arcana": "major",
        "uprightKeywords": ["Kekuatan Lembut", "Keberanian Batin", "Kesabaran", "Welas Asih", "Penguasaan Hawa Nafsu"],
        "reversedKeywords": ["Kelemahan Batin", "Keraguan Diri", "Kemarahan Mentah", "Kehilangan Kesabaran"],
        "description": "Seorang wanita bergaun putih dengan lambang tak hingga di atas kepalanya dengan lembut mengelus dan menutup rahang seekor singa merah. Strength mengajarkan bahwa kelembutan welas asih dan kesabaran batin jauh lebih perkasa daripada kekerasan fisik atau amarah mentah.",
        "readings": {
            "love": {
                "title": "Kelembutan yang Menaklukkan Gejolak Emosi",
                "summary": "Menyelesaikan konflik asmara dengan kesabaran, welas asih, dan empati mendalam.",
                "meaning": "Strength dalam cinta menunjukkan kekuatan cinta yang mengampuni dan memahami. Saat pasangan sedang gundah atau terpancing emosi, respons tenang dan pelukan hangatmu mampu meredakan badai kemarahan jauh lebih ampuh daripada kata-kata bantahan.",
                "advice": "Redakan ego batinmu; dengarkan keluh kesah pasangan dengan telinga welas asih tanpa buru-buru membela diri.",
                "reflectionQuestion": "Bagaimana kelembutan hatimu bisa membantu meredakan ketegangan dalam hubungan saat ini?",
                "keywords": ["Welas Asih", "Kesabaran Asmara", "Kelembutan Hati", "Memaafkan"]
            },
            "work": {
                "title": "Ketahanan Mental Menghadapi Tekanan Berat",
                "summary": "Tetap tenang dan profesional di tengah situasi kerja yang penuh intrik atau tenggat waktu mepet.",
                "meaning": "Di lingkungan kerja, kartu ini menandakan stamina mental dan kemampuan bernegosiasi dengan pihak yang sulit. Kamu mampu melunakkan pihak oposisi bukan dengan ancaman, melainkan dengan argumen yang tenang, santun, dan sangat berbobot.",
                "advice": "Tahan diri untuk tidak terpancing emosi di rapat kerja; kendalikan situasi dengan kepala dingin dan etika prima.",
                "reflectionQuestion": "Situasi kerja rumit apa yang paling membutuhkan kesabaran dan ketenangan sikapmu saat ini?",
                "keywords": ["Ketahanan Mental", "Negosiasi Santun", "Kepala Dingin", "Profesionalisme"]
            },
            "career": {
                "title": "Keberhasilan Berkelanjutan Berkat Integritas Batin",
                "summary": "Reputasi profesional yang kokoh karena konsistensi moral dan ketenangan kepemimpinan.",
                "meaning": "Karier di bawah pengaruh Strength membawa kehormatan sejati. Kamu dihargai bukan karena kamu menakutkan, melainkan karena kamu memiliki karisma welas asih yang membuat orang lain sukarela mengikutimu. Ini adalah waktu terbaik untuk memimpin perubahan budaya kerja.",
                "advice": "Jadilah teladan dalam kesabaran dan keadilan; bimbing timmu dengan penghargaan dan apresiasi tulus.",
                "reflectionQuestion": "Bagaimana caramu memimpin orang lain tanpa perlu mengandalkan rasa takut atau tekanan?",
                "keywords": ["Karisma Welas Asih", "Integritas Batin", "Keteladanan", "Kepemimpinan Tenang"]
            },
            "finance": {
                "title": "Kesabaran Membangun Aset Jangka Panjang",
                "summary": "Menolak godaan konsumtif sesaat demi mengamankan kesejahteraan masa depan.",
                "meaning": "Secara keuangan, Strength mengajarkan pengendalian hawa nafsu berbelanja. Kamu memiliki ketahanan diri untuk tidak terbawa gaya hidup berlebihan atau fomo terhadap tren investasi spekulatif. Pertumbuhan finansialmu mungkin terasa bertahap, namun sangat stabil.",
                "advice": "Kendalikan keinginan konsumtifmu; bersabarlah menanti hasil investasi yang memerlukan waktu matang.",
                "reflectionQuestion": "Keinginan belanja impulsif apa yang paling perlu kamu jinakkan demi tujuan finansialmu?",
                "keywords": ["Pengendalian Diri", "Ketahanan Finansial", "Investasi Sabar", "Kestabilan"]
            },
            "selfGrowth": {
                "title": "Menjinakkan Singa Amarah di Dalam Diri",
                "summary": "Mengubah energi kemarahan, ketakutan, dan luka batin menjadi kekuatan cinta kasih.",
                "meaning": "Pengembangan diri bersama kartu Strength adalah proses alkimia batin. Singa merah melambangkan naluri primitif kita: kemarahan, kecemburuan, dan ketakutan. Alih-alih menekannya, kamu diajak merangkul bayangan batinmu itu dengan penerimaan penuh kasih agar ia bertransformasi menjadi keberanian suci.",
                "advice": "Berdamailah dengan kelemahanmu; perlakukan dirimu sendiri dengan kelembutan yang sama seperti kamu memperlakukan sahabat terkasih.",
                "reflectionQuestion": "Bagian dari emosi batinmu yang mana yang selama ini paling sering kamu hakimi secara kasar?",
                "keywords": ["Alkimia Batin", "Penerimaan Diri", "Welas Asih Diri", "Menjinakkan Ego"]
            },
            "relationships": {
                "title": "Ketabahan Menjaga Keutuhan Keluarga",
                "summary": "Menjadi perekat perdamaian saat terjadi friksi antarkeluarga atau sahabat.",
                "meaning": "Dalam hubungan sosial dan keluarga, Strength menandakan kemampuanmu menjadi penengah yang teduh. Kamu tidak membalas cercaan dengan makian, melainkan menawarkan pengertian yang menyejukkan hati semua pihak yang sedang berselisih.",
                "advice": "Berikan ruang bagi orang lain untuk meluapkan unek-uneknya; jadilah samudra yang menampung keluh kesah tanpa meluap.",
                "reflectionQuestion": "Siapa di keluargamu yang saat ini paling membutuhkan pelukan pengertian tanpa penghakiman?",
                "keywords": ["Penengah Teduh", "Kedamaian Keluarga", "Pengertian Mendalam", "Keikhlasan"]
            },
            "spirituality": {
                "title": "Kekuatan Abadi dari Kerendahan Hati",
                "summary": "Menyadari bahwa kuasa sejati lahir saat ego batin tunduk sepenuhnya kepada kehendak ilahi.",
                "meaning": "Secara spiritual, kartu Strength melambangkan penaklukan nafsu ammarah menuju nafsu muthmainnah (jiwa yang tenang). Melalui laku kesabaran dan zikir hening, kamu merasakan hadirat ilahi yang menyelimuti seluruh relung jiwamu dengan kedamaian abadi.",
                "advice": "Jadikan sabar dan syukur sebagai dua sayap ibadahmu dalam menempuh jalan spiritual.",
                "reflectionQuestion": "Apakah kamu sudah mampu melihat setiap ujian kesabaran sebagai sarana pembersihan jiwa?",
                "keywords": ["Jiwa Tenang", "Sabar dan Syukur", "Pembersihan Hati", "Kedamaian Abadi"]
            }
        }
    }
]

print(f"Major Arcana part 1 loaded: {len(MAJOR_ARCANA)} cards")
