#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deck Data: Major Arcana (22 Cards: 0 to 21)
Complete traditional symbolism and 7-category Indonesian interpretations.
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
                "meaning": "Dalam asmara, The Fool menandakan energi segar dan keterbukaan emosional yang murni. Kamu mungkin berada di ambang koneksi baru yang tak terduga atau merasa terdorong melepaskan pola kaku dalam hubungan yang ada. Kartu ini mengajakmu menyambut cinta dengan kepolosan yang tulus tanpa prasangka.",
                "advice": "Beranikan diri membuka hati dan nikmati momen kebersamaan tanpa tergesa-gesa menuntut kepastian masa depan.",
                "reflectionQuestion": "Bagian mana dari hatimu yang masih ragu untuk percaya kembali pada keindahan cinta?",
                "keywords": ["Cinta Baru", "Spontanitas", "Keterbukaan", "Optimisme"]
            },
            "work": {
                "title": "Eksplorasi Pendekatan dan Tugas Baru",
                "summary": "Membawa perspektif segar dan kemauan belajar dalam rutinitas kerja harian.",
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
        "description": "The Magician berdiri dengan satu tangan menunjuk ke langit dan satu tangan ke bumi. Di mejanya terdapat cawan, pedang, tongkat, dan koin—simbol penguasaan atas empat elemen untuk memanifestasikan kehendak batin menjadi realitas nyata.",
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
    },
    {
        "id": "the-hermit",
        "number": 9,
        "name": "The Hermit",
        "slug": "the-hermit",
        "image": "/assets/tarot/cards/The Hermit.jpg",
        "arcana": "major",
        "uprightKeywords": ["Introspeksi", "Pencarian Batin", "Kesendirian Suci", "Bimbingan Jiwa", "Kebijaksanaan"],
        "reversedKeywords": ["Isolasi Diri", "Kesepian Menyakitkan", "Menolak Bantuan", "Keras Kepala"],
        "description": "Seorang pertapa tua berjubah abu-abu berdiri di puncak gunung salju memegang lentera bersinar bintang bersudut enam dan tongkat musafir. The Hermit melambangkan penarikan diri sejenak dari hiruk-pikuk dunia untuk menemukan cahaya kebenaran abadi di dalam relung jiwa.",
        "readings": {
            "love": {
                "title": "Keheningan untuk Memahami Kebutuhan Hati",
                "summary": "Mengambil jeda dari drama asmara demi menemukan kejelasan perasaan sejati.",
                "meaning": "The Hermit dalam asmara menunjukkan bahwa kamu atau pasangan membutuhkan ruang pribadi untuk merenung. Ini bukan tanda penolakan, melainkan kebutuhan alami untuk menyelami apa yang sebenarnya kamu harapkan dari sebuah hubungan sebelum melangkah lebih jauh.",
                "advice": "Hormati kebutuhan ruang pribadi masing-masing; gunakan kesendirian untuk mengenal kembali dirimu sendiri.",
                "reflectionQuestion": "Apakah kamu mencari pasangan untuk melengkapi kesepian atau untuk berbagi kebahagiaan yang sudah utuh?",
                "keywords": ["Ruang Pribadi", "Kejernihan Hati", "Mengenal Diri", "Kemandirian Emosional"]
            },
            "work": {
                "title": "Fokus Mendalam dan Analisis Mandiri",
                "summary": "Menyelesaikan pekerjaan yang membutuhkan konsentrasi tinggi tanpa interupsi.",
                "meaning": "Di tempat kerja, The Hermit mendukung tugas-tugas riset, penulisan, audit, dan perencanaan strategis independen. Kualitas karyamu saat ini akan jauh lebih prima jika kamu diberikan ruang kerja yang tenang dan bebas dari rapat-rapat yang tidak esensial.",
                "advice": "Matikan notifikasi yang mengganggu saat menyelesaikan pekerjaan penting; jadilah ahli yang teliti.",
                "reflectionQuestion": "Bagian pekerjaan mana yang membutuhkan peninjauan mendalam tanpa tergesa-gesa?",
                "keywords": ["Konsentrasi Penuh", "Riset Mendalam", "Kemandirian Kerja", "Ketelitian"]
            },
            "career": {
                "title": "Menjadi Spesialis Terpandang dan Mentor Tepercaya",
                "summary": "Menemukan keahlian unik yang langka dan membimbing orang lain dengan kearifan.",
                "meaning": "Karier di bawah pengaruh The Hermit mengindikasikan peralihan menjadi konsultan ahli, peneliti, atau pembimbing independen. Pengalaman panjangmu telah mengkristal menjadi kebijaksanaan berharga yang dicari oleh orang-orang yang membutuhkan arahan jelas.",
                "advice": "Berbagilah ilmu dan pengalamanmu sebagai pelita penerang bagi mereka yang baru memulai perjalanan karier.",
                "reflectionQuestion": "Kearifan profesional apa yang dapat kamu bagikan kepada rekan-rekan kerjamu?",
                "keywords": ["Konsultan Ahli", "Pelita Karier", "Mentor Tepercaya", "Kearifan Profesional"]
            },
            "finance": {
                "title": "Kesederhanaan Hidup dan Tinjauan Anggaran",
                "summary": "Menerapkan gaya hidup hemat dan mengevaluasi prioritas pengeluaran dengan bijak.",
                "meaning": "The Hermit mengajarkan filosofi kesederhanaan. Kamu disarankan untuk meninjau kembali tagihan rutin dan memangkas pengeluaran yang tidak memberi nilai tambah nyata pada hidupmu. Kekayaan sejati kartu ini adalah ketenangan pikiran, bukan timbunan barang mewah.",
                "advice": "Evaluasi kebutuhan pokokmu secara jujur; temukan kebahagiaan dalam hal-hal sederhana yang tidak membutuhkan biaya tinggi.",
                "reflectionQuestion": "Pengeluaran materi apa yang sebenarnya bisa kamu kurangi tanpa menurunkan kebahagiaan hidupmu?",
                "keywords": ["Kesederhanaan", "Audit Anggaran", "Ketenangan Pikiran", "Hemat Bijak"]
            },
            "selfGrowth": {
                "title": "Retret Jiwa dan Dialog Batin yang Jujur",
                "summary": "Menyepi sejenak dari keramaian media sosial demi mendengarkan kompas nuranimu.",
                "meaning": "Pengembangan diri The Hermit adalah momen retret spiritual. Menjauh dari hiruk-pikuk opini luar memungkinkanmu mendengar suara nuranimu sendiri yang selama ini tertutup bisingnya dunia. Di dalam keheningan inilah transformasi batin yang paling murni terjadi.",
                "advice": "Lakukan detoksifikasi digital berkala dan luangkan waktu berjalan sendiri di alam hening.",
                "reflectionQuestion": "Kapan terakhir kali kamu duduk hening tanpa gawai dan benar-benar mendengarkan dirimu sendiri?",
                "keywords": ["Retret Batin", "Detoks Digital", "Kompas Nurani", "Keheningan Suci"]
            },
            "relationships": {
                "title": "Memilih Lingkaran Pertemanan yang Bermakna",
                "summary": "Memprioritaskan kualitas hubungan daripada kuantitas koneksi yang dangkal.",
                "meaning": "Dalam pergaulan, The Hermit menandakan fase selektif. Kamu mungkin merasa lelah dengan basa-basi sosial dan lebih memilih menghabiskan waktu bersama satu atau dua sahabat karib yang memahami jiwamu secara mendalam.",
                "advice": "Rawatlah persahabatan yang bermakna dan jangan merasa bersalah jika perlu menolak ajakan kumpul yang menguras energimu.",
                "reflectionQuestion": "Siapa sahabat sejatimu yang keberadaannya selalu membawa ketenangan dan kedewasaan bagi jiwamu?",
                "keywords": ["Kualitas Hubungan", "Selektif Sosial", "Persahabatan Mendalam", "Ketenangan"]
            },
            "spirituality": {
                "title": "Membawa Lentera Nur Ilahi di Tengah Gelap",
                "summary": "Menemukan cahaya Tuhan di dalam lubuk hati yang paling sunyi.",
                "meaning": "The Hermit adalah sang mistik sejati. Lentera di tangannya melambangkan cahaya bimbingan ilahi yang hanya dapat menyala ketika ego padam dalam keheningan tafakur. Jalan spiritualmu adalah perjalanan ke dalam, menemukan bahwa Tuhan lebih dekat daripada urat lehermu sendiri.",
                "advice": "Jadikan keheningan malam sebagai waktu berkhalwat dan bersujud dalam kepasrahan total.",
                "reflectionQuestion": "Bagaimana caramu menjaga lentera keimanan tetap menyala terang saat dunia di sekitarmu terasa gelap?",
                "keywords": ["Tafakur Sunyi", "Lentera Jiwa", "Khalwat Batin", "Cahaya Ilahi"]
            }
        }
    },
    {
        "id": "the-wheel-of-fortune",
        "number": 10,
        "name": "The Wheel of Fortune",
        "slug": "the-wheel-of-fortune",
        "image": "/assets/tarot/cards/The Wheel of Fortune.jpg",
        "arcana": "major",
        "uprightKeywords": ["Perubahan Takdir", "Roda Kehidupan", "Keberuntungan", "Siklus Tak Terhindarkan", "Peluang Kosmis"],
        "reversedKeywords": ["Nasib Buruk Sementara", "Menolak Perubahan", "Keterlambatan Siklus", "Merasa Frustrasi"],
        "description": "Roda raksasa berputar di langit diapit oleh empat makhluk bersayap di setiap sudutnya (manusia, elang, singa, lembu). Pada roda terukir huruf TARO/ROTA dan simbol alkimia. Kartu ini melambangkan hukum abadi tentang pasang surut takdir dan pergantian musim kehidupan manusia.",
        "readings": {
            "love": {
                "title": "Titik Balik Takdir dan Pertemuan Bermakna",
                "summary": "Perubahan tak terduga dalam dinamika asmara yang membuka babak baru.",
                "meaning": "The Wheel of Fortune membawa angin perubahan takdir dalam percintaan. Situasi hubungan yang sebelumnya buntu bisa tiba-tiba menemukan titik terang. Bagi yang masih sendiri, ada potensi pertemuan kebetulan yang bermakna (serendipity) yang mengubah pandanganmu tentang cinta.",
                "advice": "Terimalah perubahan dengan pikiran terbuka; jangan terpaku pada ekspektasi kaku tentang bagaimana cinta seharusnya datang.",
                "reflectionQuestion": "Bagaimana caramu menyikapi pasang surut emosi dalam hubungan agar cintamu tetap tumbuh dewasa?",
                "keywords": ["Titik Balik Asmara", "Serendipity", "Musim Baru Cinta", "Keterbukaan Takdir"]
            },
            "work": {
                "title": "Peluang Tak Terduga dan Adaptasi Cepat",
                "summary": "Pergantian dinamika proyek yang membawa momentum keberuntungan kerja.",
                "meaning": "Di tempat kerja, roda nasib sedang berputar menguntungkanmu. Ada restrukturisasi, tawaran proyek mendadak, atau perubahan kebijakan yang membuka celah bagi peran barumu. Kemampuanmu beradaptasi secara fleksibel akan memaksimalkan peluang emas ini.",
                "advice": "Manfaatkan momentum baik saat kesempatan terbuka; jangan menunda-nunda tindakan saat peluang muncul.",
                "reflectionQuestion": "Peluang kerja baru apa yang saat ini hadir di hadapanmu dan siap kamu sambut?",
                "keywords": ["Momentum Positif", "Adaptasi Fleksibel", "Peluang Emas", "Dinamika Baru"]
            },
            "career": {
                "title": "Lompatan Karier Berkat Siklus Keberuntungan",
                "summary": "Waktu yang tepat berada di tempat yang tepat untuk mempercepat kemajuan profesi.",
                "meaning": "Karier di bawah Wheel of Fortune menandakan lompatan signifikan yang sering kali dipicu oleh faktor keberuntungan yang berpadu dengan kesiapan kompetensimu. Jerih payahmu di masa lalu akhirnya bertemu dengan waktu yang tepat (divine timing).",
                "advice": "Tetaplah rendah hati saat berada di puncak roda; bangun reputasi yang solid agar fondasimu tetap kokoh di segala musim.",
                "reflectionQuestion": "Bagaimana kamu mempersiapkan dirimu agar selalu siap ketika peluang besar datang tiba-tiba?",
                "keywords": ["Divine Timing", "Lompatan Karier", "Musim Kejayaan", "Kerendahan Hati"]
            },
            "finance": {
                "title": "Perbaikan Arus Rezeki dan Kehati-hatian Siklus",
                "summary": "Rezeki tak terduga yang datang berbarengan dengan pengingat untuk menabung.",
                "meaning": "Secara finansial, kartu ini mengindikasikan perbaikan arus kas atau pendapatan tak terduga. Namun, roda selalu berputar: manfaatkan masa panen ini untuk melunasi kewajiban dan mempertebal tabungan sebelum musim berganti.",
                "advice": "Kelola dana surplus dengan bijak; jangan langsung meningkatkan gaya hidup saat rezekimu sedang berlimpah.",
                "reflectionQuestion": "Apakah kamu sudah menyisihkan sebagian keuntunganmu untuk mengantisipasi masa-masa sulit?",
                "keywords": ["Rezeki Melimpah", "Dana Cadangan", "Siklus Finansial", "Bijak Mengelola"]
            },
            "selfGrowth": {
                "title": "Menemukan Kedamaian di Pusat Roda Kehidupan",
                "summary": "Belajar tetap tenang di tengah perubahan eksternal yang bergerak cepat.",
                "meaning": "Pengembangan diri kartu ini adalah tentang melatih 'titik hening' di pusat poros roda. Di tepi roda, hidup berputar naik dan turun dengan liar. Tetapi di titik tengahnya, segalanya tetap seimbang dan damai. Latihlah dirimu untuk tidak terombang-ambing oleh pujian maupun celaan dunia.",
                "advice": "Latihlah sikap ikhlas dan penerimaan; sadarilah bahwa baik suka maupun duka adalah guru kehidupan yang silih berganti.",
                "reflectionQuestion": "Bagaimana caramu menjaga ketenangan batin ketika keadaan di sekitarmu berubah tanpa kepastian?",
                "keywords": ["Titik Poros Batin", "Keteguhan Jiwa", "Penerimaan Ikhlas", "Keseimbangan Hidup"]
            },
            "relationships": {
                "title": "Pergantian Dinamika Sosial dan Rekonsiliasi",
                "summary": "Waktu yang menyembuhkan ketegangan lama dan membawa wajah-wajah baru dalam lingkaranmu.",
                "meaning": "Dalam hubungan sosial dan keluarga, roda takdir membawa penyelesaian alami bagi perselisihan yang sempat berlarut-larut. Hubungan yang dulu menjauh bisa kembali akrab melalui peristiwa tak terduga yang mempertemukan kembali kalian.",
                "advice": "Buka pintu maaf dan sambut kembali sahabat atau kerabat yang datang dengan niat baik.",
                "reflectionQuestion": "Hubungan kekeluargaan mana yang siap kamu pulihkan seiring berjalannya waktu?",
                "keywords": ["Rekonsiliasi Alami", "Waktu Menyembuhkan", "Pergantian Dinamika", "Pintu Maaf"]
            },
            "spirituality": {
                "title": "Menyerah pada Ketetapan Takdir Ilahi",
                "summary": "Memahami rahasia hukum karma dan hikmah di balik setiap perputaran takdir.",
                "meaning": "Secara spiritual, The Wheel of Fortune mengajarkan kepasrahan kepada ketetapan Tuhan (Qadar). Tidak ada yang terjadi secara kebetulan; setiap peristiwa suka dan duka telah dirancang dengan presisi kosmis demi pematangan jiwamu.",
                "advice": "Berserahlah kepada kehendak ilahi dengan hati yang ridho; yakinlah bahwa setiap takdir membawa kebaikan tersembunyi.",
                "reflectionQuestion": "Hikmah spiritual apa yang telah kamu pelajari dari peristiwa tersulit dalam hidupmu?",
                "keywords": ["Hukum Karma", "Kepasrahan Ridho", "Hikmah Ilahi", "Rancangan Kosmis"]
            }
        }
    },
    {
        "id": "justice",
        "number": 11,
        "name": "Justice",
        "slug": "justice",
        "image": "/assets/tarot/cards/Justice.jpg",
        "arcana": "major",
        "uprightKeywords": ["Keadilan", "Kebenaran", "Sebab-Akibat", "Integritas", "Kejujuran"],
        "reversedKeywords": ["Ketidakadilan", "Kecurangan", "Menghindari Tanggung Jawab", "Prasangka Berat Sebelah"],
        "description": "Duduk anggun di antara dua pilar dengan pedang tegak di tangan kanan dan timbangan berimbang di tangan kiri, Justice adalah perwujudan kebenaran mutlak, hukum sebab-akibat universal, dan penilaian moral yang tak memihak.",
        "readings": {
            "love": {
                "title": "Keseimbangan Timbal Balik dan Kejujuran Asmara",
                "summary": "Membangun hubungan cinta yang setara, adil, dan transparan tanpa rahasia.",
                "meaning": "Justice menuntut kejujuran dan keseimbangan memberi serta menerima dalam hubungan. Jika ada masalah yang mengganjal, inilah saatnya membicarakannya secara dewasa dan objektif. Hubungan yang sehat membutuhkan kedua pihak untuk sama-sama berinvestasi secara adil.",
                "advice": "Bersikaplah adil terhadap pasangan; akui kesalahanmu jika kamu keliru dan sampaikan keberatanmu dengan tenang.",
                "reflectionQuestion": "Apakah kamu dan pasangan sudah saling memberi dan menerima secara berimbang?",
                "keywords": ["Keseimbangan Asmara", "Kejujuran Total", "Kesetaraan Hubungan", "Tanggung Jawab Bersama"]
            },
            "work": {
                "title": "Integritas Profesional dan Keputusan Objektif",
                "summary": "Menyelesaikan kontrak kerja, negosiasi hukum, dan evaluasi kinerja secara adil.",
                "meaning": "Di lingkungan kerja, Justice mengingatkan pentingnya kepatuhan terhadap perjanjian kerja, objektivitas dalam menilai rekan, dan etika profesi yang lurus. Hasil kerja kerasmu akan dinilai secara transparan dan mendapatkan pengakuan yang sepadan.",
                "advice": "Baca dokumen dan kontrak dengan teliti sebelum menandatanganinya; pertahankan integritas etismu di atas segalanya.",
                "reflectionQuestion": "Apakah keputusan kerjamu saat ini sudah benar-benar adil bagi semua pihak yang terlibat?",
                "keywords": ["Integritas Etis", "Objektivitas", "Keadilan Kerja", "Kepatuhan Kontrak"]
            },
            "career": {
                "title": "Kompensasi Setimpal dan Reputasi Lurus",
                "summary": "Mendapatkan apa yang layak kamu terima berdasarkan dedikasi dan kejujuranmu.",
                "meaning": "Karier di bawah pengaruh Justice membawa penyelesaian sengketa yang adil atau promosi yang memang sudah menjadi hakmu. Jika kamu telah bekerja dengan jujur dan tulus, hukum sebab-akibat akan memastikan penghargaan profesionalmu tiba pada waktunya.",
                "advice": "Bekerjalah dengan rekam jejak yang bersih dan transparan; integritas adalah aset karier termahalmu.",
                "reflectionQuestion": "Bagaimana integritas kerjamu selama ini membentuk reputasi profesionalmu hari ini?",
                "keywords": ["Hak Setimpal", "Rekam Jejak Bersih", "Kompensasi Adil", "Integritas Karier"]
            },
            "finance": {
                "title": "Keseimbangan Neraca dan Tanggung Jawab Legal",
                "summary": "Menyelesaikan kewajiban pajak, utang piutang, dan pencatatan keuangan secara tertib.",
                "meaning": "Secara keuangan, kartu ini menuntut transparansi dan keteraturan neraca kas. Pastikan semua kewajiban hukum, pembayaran pajak, dan utang diselesaikan tepat waktu. Jangan tergoda oleh celah yang merugikan orang lain demi keuntungan pribadi.",
                "advice": "Rapikan dokumen keuanganmu; bayar kewajibanmu tepat waktu agar rezekimu senantiasa bersih dan berkah.",
                "reflectionQuestion": "Apakah seluruh urusan finansial dan kewajiban legalmu sudah tercatat dengan rapi dan jujur?",
                "keywords": ["Neraca Bersih", "Kewajiban Legal", "Transparansi Dana", "Rezeki Berkah"]
            },
            "selfGrowth": {
                "title": "Kejujuran Radikal Terhadap Diri Sendiri",
                "summary": "Mengambil tanggung jawab penuh atas konsekuensi dari setiap pilihan hidupmu.",
                "meaning": "Pengembangan diri kartu Justice adalah tentang berhenti mencari kambing hitam di luar diri. Apa pun posisimu hari ini adalah buah dari pilihan-pilihan masa lalumu. Saat kamu berani mengakui hal ini tanpa menghakimi diri secara kejam, kamu memperoleh kekuatan untuk mengubah masa depan.",
                "advice": "Pandang dirimu di cermin dengan kejujuran tulus; maafkan kekeliruan masa lalu dan ambil langkah perbaikan nyata.",
                "reflectionQuestion": "Kebenaran tentang dirimu sendiri apa yang selama ini paling enggan kamu akui secara jujur?",
                "keywords": ["Tanggung Jawab Diri", "Kejujuran Radikal", "Hukum Sebab-Akibat", "Kematangan Emosi"]
            },
            "relationships": {
                "title": "Keadilan Bersikap dan Menyelesaikan Perselisihan",
                "summary": "Mendengarkan kedua belah pihak secara berimbang demi memulihkan keharmonisan keluarga.",
                "meaning": "Dalam keluarga dan persahabatan, Justice memintamu bertindak sebagai penengah yang adil. Jangan memihak karena kedekatan emosional semata; gunakan akal sehat dan kasih sayang untuk melihat akar masalah yang sebenarnya.",
                "advice": "Dengarkan penjelasan orang lain dengan pikiran jernih tanpa prasangka sebelum memberikan penilaian.",
                "reflectionQuestion": "Bagaimana caramu bersikap adil terhadap anggota keluarga yang memiliki perbedaan pandangan?",
                "keywords": ["Penengah Adil", "Tanpa Prasangka", "Akal Sehat", "Keadilan Keluarga"]
            },
            "spirituality": {
                "title": "Hukum Karma dan Keseimbangan Semesta",
                "summary": "Menyadari bahwa setiap getaran niat dan amal perbuatan akan kembali kepada pelakunya.",
                "meaning": "Secara spiritual, Justice adalah neraca timbangan amal di hadapan hukum ilahi. Apa yang kamu tanam dalam batin—baik itu kebencian, cinta, kebohongan, atau kejujuran—pasti akan kamu tuai hasilnya. Kemurnian niat adalah kunci keselamatan jiwa.",
                "advice": "Tanamlah benih-benih kebaikan tanpa pamrih; percayalah bahwa keadilan Tuhan bekerja dengan amat teliti.",
                "reflectionQuestion": "Benih kebajikan apa yang ingin kamu tabur hari ini bagi kebaikan alam semesta?",
                "keywords": ["Timbangan Amal", "Keadilan Ilahi", "Kemurnian Niat", "Hukum Abadi"]
            }
        }
    },
    {
        "id": "the-hanged-man",
        "number": 12,
        "name": "The Hanged Man",
        "slug": "the-hanged-man",
        "image": "/assets/tarot/cards/The Hanged Man.jpg",
        "arcana": "major",
        "uprightKeywords": ["Perspektif Baru", "Pengorbanan Ikhlas", "Jeda Sadar", "Pelepasan Ego", "Pencerahan Sunyi"],
        "reversedKeywords": ["Keras Kepala", "Menolak Melepaskan", "Penundaan Sia-sia", "Merasa Menjadi Korban"],
        "description": "Seorang pria tergantung terbalik pada satu kaki di pohon kayu berbentuk huruf T yang bertunas daun hijau. Wajahnya tenang dan bercahaya (halo keemasan) di sekitar kepalanya. The Hanged Man melambangkan pencerahan yang diperoleh saat seseorang rela melepaskan kendali ego dan melihat dunia dari sudut pandang terbalik.",
        "readings": {
            "love": {
                "title": "Melihat Sudut Pandang Pasangan dengan Ikhlas",
                "summary": "Melepaskan keharusan untuk selalu benar demi menjaga kedamaian dan keharmonisan asmara.",
                "meaning": "The Hanged Man dalam cinta mengajakmu untuk berhenti memaksakan kehendak. Terkadang hubungan membutuhkan jeda dari perdebatan agar masing-masing bisa melihat persoalan dari kacamata pasangan. Pengorbanan kecil atas ego pribadimu akan membuka jalan menuju kedekatan yang lebih suci.",
                "advice": "Berhentilah membela diri sejenak; cobalah benar-benar memahami perasaan pasangan dari sudut pandangnya.",
                "reflectionQuestion": "Ego asmara apa yang siap kamu korbankan demi kebahagiaan hubungan jangka panjang?",
                "keywords": ["Pelepasan Ego", "Perspektif Pasangan", "Jeda Menyejukkan", "Keikhlasan Asmara"]
            },
            "work": {
                "title": "Jeda Strategis Sebelum Melangkah Lebih Lanjut",
                "summary": "Menunda eksekusi tergesa-gesa demi meninjau kembali arah proyek dari sudut pandang unik.",
                "meaning": "Di tempat kerja, memaksakan jalan buntu saat ini hanya akan membuang energi. Kartu ini menyarankanmu untuk berhenti sejenak, mengamati situasi dari perspektif yang sama sekali berbeda, dan membiarkan solusi kreatif muncul tanpa tekanan.",
                "advice": "Jangan terburu-buru mengambil tindakan reaktif; gunakan waktu jeda ini untuk mengevaluasi strategi secara menyeluruh.",
                "reflectionQuestion": "Bagaimana jika masalah kerja yang rumit ini sebenarnya adalah kesempatan untuk menemukan cara baru yang lebih efisien?",
                "keywords": ["Jeda Strategis", "Perspektif Unik", "Solusi Kreatif", "Hindari Reaktif"]
            },
            "career": {
                "title": "Reorientasi Visi dan Pengorbanan Bermakna",
                "summary": "Rela mengorbankan kenyamanan sesaat demi mencapai lompatan karier yang lebih bernilai.",
                "meaning": "Karier di bawah pengaruh The Hanged Man mungkin terasa melambat atau mengalami jeda sementara. Namun, masa penantian ini sangat bernilai untuk memikirkan kembali apakah jalur yang kamu tempuh benar-benar bermakna bagimu. Sering kali, pengorbanan status atau kenyamanan saat ini membuka pintu takdir yang jauh lebih besar.",
                "advice": "Terimalah fase penantian ini dengan lapang dada; gunakan untuk menata kembali prioritas kariermu.",
                "reflectionQuestion": "Apa yang perlu kamu relakan agar kamu bisa bertumbuh menuju versi terbaik dari dirimu?",
                "keywords": ["Reorientasi Karier", "Penantian Bernilai", "Pengorbanan Bermakna", "Fase Inkubasi"]
            },
            "finance": {
                "title": "Menunda Keputusan Finansial dan Mengubah Sikap Materi",
                "summary": "Menahan diri dari investasi terburu-buru dan menyadari bahwa uang bukanlah satu-satunya ukuran nilai.",
                "meaning": "Secara keuangan, The Hanged Man menyarankan untuk membekukan pengeluaran besar dan menunda komitmen finansial baru sampai situasinya benar-benar jelas. Ubahlah cara pandangmu terhadap materi: kekayaan sejati tidak hanya diukur dari angka di rekening, melainkan dari ketenangan jiwa.",
                "advice": "Tahan keinginan berbelanja atau berinvestasi saat ini; tunggu hingga perspektif finansialmu lebih jernih.",
                "reflectionQuestion": "Apakah kamu bersedia menunda kesenangan materi sesaat demi keamanan finansial jangka panjang?",
                "keywords": ["Tunda Pengeluaran", "Perspektif Materi", "Ketenangan Jiwa", "Kehati-hatian"]
            },
            "selfGrowth": {
                "title": "Seni Melepaskan Kendali dan Menyerah Total",
                "summary": "Menyadari bahwa pencerahan sejati lahir saat kita berhenti melawan kenyataan.",
                "meaning": "Pengembangan diri kartu The Hanged Man adalah lompatan kesadaran tertinggi. Berhentilah berjuang melawan hal-hal yang berada di luar kendalimu. Saat kamu menerima situasi apa adanya dengan ikhlas, resistensi batinmu lenyap dan kamu merasakan kedamaian mendalam yang tak tergoyahkan.",
                "advice": "Latihlah sikap berserah; lepaskan kebutuhan untuk mengendalikan hasil dan biarkan semesta bekerja.",
                "reflectionQuestion": "Beban apa yang selama ini begitu erat kamu genggam dan sudah saatnya kamu lepaskan?",
                "keywords": ["Seni Berserah", "Pelepasan Kendali", "Pencerahan Batin", "Penerimaan Ikhlas"]
            },
            "relationships": {
                "title": "Kesabaran Menghadapi Dinamika yang Mandek",
                "summary": "Memberikan ruang bagi keluarga atau sahabat tanpa memaksakan perubahan instan.",
                "meaning": "Dalam hubungan sosial dan keluarga, The Hanged Man menandakan pentingnya kesabaran. Ada situasi di mana nasihat terbaik adalah tidak memberikan nasihat sama sekali, melainkan hadir dengan tenang dan membiarkan orang lain menemukan jalannya sendiri.",
                "advice": "Tahan keinginan untuk 'memperbaiki' orang lain; dampingi mereka dengan kesabaran dan cinta tanpa pamrih.",
                "reflectionQuestion": "Siapa dalam keluargamu yang saat ini paling membutuhkan penerimaan apa adanya tanpa tuntutan?",
                "keywords": ["Kesabaran Murni", "Tanpa Tuntutan", "Mendampingi Tenang", "Penerimaan Penuh"]
            },
            "spirituality": {
                "title": "Pencerahan Mistis Melalui Pengorbanan Nafsu",
                "summary": "Cahaya halo keemasan yang memancar saat ego tunduk di hadapan Sang Pencipta.",
                "meaning": "Secara spiritual, The Hanged Man adalah simbol penyucian diri (fana). Dengan menggantungkan keinginan duniawi terbalik di bawah bimbingan ilahi, pikiranmu disinari oleh cahaya pencerahan hakiki. Ketergantungan pada Tuhan adalah kemerdekaan tertinggi bagi jiwa.",
                "advice": "Bermeditasilah dalam keheningan total; rasakan nikmatnya berserah sepenuhnya ke dalam pemeliharaan Tuhan.",
                "reflectionQuestion": "Bagaimana caramu menjadikan setiap ujian hidup sebagai sarana pensucian jiwa?",
                "keywords": ["Penyucian Diri", "Cahaya Halo", "Fana fi Allah", "Kemerdekaan Jiwa"]
            }
        }
    },
    {
        "id": "death",
        "number": 13,
        "name": "Death",
        "slug": "death",
        "image": "/assets/tarot/cards/Death.jpg",
        "arcana": "major",
        "uprightKeywords": ["Transformasi Besar", "Akhir Sebuah Siklus", "Kelahiran Kembali", "Pelepasan Masa Lalu", "Membuka Lembaran Baru"],
        "reversedKeywords": ["Takut Berubah", "Bertahan pada Masa Lalu", "Kebuntuan", "Menolak Kenyataan"],
        "description": "Seorang ksatria berbaju zirah hitam menunggang kuda putih membawa bendera bergambar mawar putih mistis (simbol kehidupan baru). Di kejauhan, matahari terbit di antara dua menara gerbang abadi. Death bukanlah kematian fisik, melainkan metamorfosis radikal: akhir mutlak dari fase lama demi terbitnya fajar kehidupan baru.",
        "readings": {
            "love": {
                "title": "Transformasi Mendalam dan Pelepasan Pola Usang",
                "summary": "Mengakhiri kebiasaan toxic atau merelakan hubungan yang telah tuntas siklusnya demi pertumbuhan sejati.",
                "meaning": "Death dalam cinta membawa angin perubahan radikal yang tak terelakkan. Entah itu transformasi menyeluruh dalam cara berkomunikasi dengan pasangan, atau keputusan berani melepaskan ikatan yang sudah tidak sehat. Sesuatu harus gugur agar cinta yang lebih autentik dapat bersemi.",
                "advice": "Lepaskan genggamanmu pada kenangan masa lalu; terimalah kenyataan agar hatimu siap menyambut fajar cinta yang baru.",
                "reflectionQuestion": "Pola emosi atau luka masa lalu apa yang harus kamu kubur agar hatimu bisa kembali mencintai dengan tulus?",
                "keywords": ["Metamorfosis Cinta", "Pelepasan Luka", "Akhir Siklus", "Fajar Baru Asmara"]
            },
            "work": {
                "title": "Penutupan Proyek Lama dan Restrukturisasi Total",
                "summary": "Menuntaskan fase kerja yang usang demi merintis metodologi baru yang lebih segar.",
                "meaning": "Di tempat kerja, Death menandakan berakhirnya sebuah sistem kerja, kontrak proyek, atau dinamika tim lama. Jangan meratapi apa yang telah usai; akhir ini membuka ruang kosong yang mutlak diperlukan untuk kelahiran inovasi dan struktur kerja yang jauh lebih modern.",
                "advice": "Selesaikan seluruh kewajiban lama dengan rapi; bersiaplah menyambut peran dan tanggung jawab baru.",
                "reflectionQuestion": "Metode kerja atau kebiasaan usang apa di tempat kerja yang sudah saatnya ditinggalkan?",
                "keywords": ["Restrukturisasi", "Akhir Proyek", "Inovasi Baru", "Pembersihan Sistem"]
            },
            "career": {
                "title": "Kelahiran Kembali Jalur Profesional",
                "summary": "Peralihan drastis menuju bidang karier yang benar-benar baru dan bermakna.",
                "meaning": "Karier di bawah pengaruh Death adalah sinyal penutupan babak profesional lama. Kamu mungkin mengalami pemutusan hubungan kerja, banting stir profesi, atau merombak total model bisnismu. Ini adalah proses pembongkaran fondasi lama agar gedung impian yang lebih kokoh dapat berdiri.",
                "advice": "Jangan takut pada ketidakpastian transisi; percayalah bahwa setiap pintu yang tertutup akan membuka gerbang takdir yang lebih mulia.",
                "reflectionQuestion": "Identitas profesional masa lalu apa yang sudah tidak lagi mencerminkan siapa dirimu hari ini?",
                "keywords": ["Transisi Radikal", "Karier Baru", "Pintu Tertutup", "Peluang Lebih Mulia"]
            },
            "finance": {
                "title": "Perombakan Total Kebiasaan Keuangan",
                "summary": "Memutus rantai utang lama dan menyusun tata kelola aset dari lembaran baru.",
                "meaning": "Secara finansial, Death menuntut keputusan tegas untuk menghentikan kebocoran anggaran dan kebiasaan belanja yang merugikan. Ini adalah waktu terbaik untuk melunasi tanggungan lama secara tuntas dan memulai perencanaan anggaran yang sepenuhnya baru dan sehat.",
                "advice": "Hentikan pengeluaran konsumtif yang membebani hidupmu; buat komitmen tegas untuk memulai lembaran finansial yang bersih.",
                "reflectionQuestion": "Kebiasaan finansial buruk apa yang harus kamu akhiri hari ini juga demi masa depanmu?",
                "keywords": ["Perombakan Finansial", "Hentikan Kebocoran", "Lembaran Baru", "Disiplin Materi"]
            },
            "selfGrowth": {
                "title": "Metamorfosis Jiwa dari Ulat Menjadi Kupu-kupu",
                "summary": "Kematian ego lama demi bangkitnya kesadaran diri yang lebih bijak dan bercahaya.",
                "meaning": "Pengembangan diri kartu Death adalah inisiasi transformasi batin yang paling agung. Versi dirimu yang penuh ketakutan dan prasangka lama sedang gugur, layaknya daun kering di musim gugur. Rangkul proses ini; kamu sedang dilahirkan kembali menjadi pribadi yang lebih tangguh dan autentik.",
                "advice": "Izinkan dirimu berduka atas apa yang telah berlalu, lalu bangkitlah dengan keyakinan penuh akan keindahan babak barumu.",
                "reflectionQuestion": "Siapakah dirimu yang sesungguhnya jika kamu melepaskan seluruh ketakutan masa lalumu?",
                "keywords": ["Metamorfosis Diri", "Kelahiran Kembali", "Gugurnya Ego", "Pribadi Baru"]
            },
            "relationships": {
                "title": "Pembersihan Dinamika Sosial dan Perpisahan Damai",
                "summary": "Merelakan relasi yang sudah tidak sefrekuensi dan memperbarui ikatan keluarga.",
                "meaning": "Dalam pergaulan dan keluarga, Death menandakan fase pembersihan alami. Pertemanan yang didasari kepalsuan akan memudar dengan sendirinya, sementara hubungan yang tulus akan mengalami pembaruan yang menyegarkan. Terimalah perpisahan dengan lapang dada dan doa terbaik.",
                "advice": "Lepaskan orang-orang yang memilih pergi dengan rasa ikhlas; hargai mereka yang tetap setia mendampingimu.",
                "reflectionQuestion": "Hubungan sosial mana yang sudah saatnya kamu ikhlaskan untuk pergi dari hidupmu?",
                "keywords": ["Pembersihan Alami", "Perpisahan Ikhlas", "Pembaruan Ikatan", "Lapang Dada"]
            },
            "spirituality": {
                "title": "Fajar Matahari Terbit di Balik Gerbang Keabadian",
                "summary": "Menyadari bahwa ketiadaan lahiriah adalah gerbang menuju kepenuhan hakiki di hadirat Tuhan.",
                "meaning": "Secara spiritual, Death adalah misteri kebangkitan jiwa. Di balik kegelapan malam selalu ada matahari terbit yang telah disiapkan oleh Sang Maha Pencipta. Melepaskan keterikatan pada ilusi dunia fana membuka mata batinmu untuk memandang cahaya abadi yang tak pernah padam.",
                "advice": "Pandanglah setiap kehilangan sebagai jalan Tuhan untuk mengosongkan hatimu agar dapat diisi oleh cinta-Nya semata.",
                "reflectionQuestion": "Bagaimana caramu memandang akhir dari sesuatu sebagai awal dari berkah ilahi yang baru?",
                "keywords": ["Matahari Terbit", "Misteri Kebangkitan", "Cahaya Abadi", "Kepasrahan Hakiki"]
            }
        }
    },
    {
        "id": "temperance",
        "number": 14,
        "name": "Temperance",
        "slug": "temperance",
        "image": "/assets/tarot/cards/Temperance.jpg",
        "arcana": "major",
        "uprightKeywords": ["Keseimbangan", "Moderasi", "Kesabaran", "Penyatuan Harmonis", "Penyembuhan Batin"],
        "reversedKeywords": ["Ketidakseimbangan", "Ekstremitas", "Ketidaksabaran", "Konflik Batin"],
        "description": "Malaikat agung bersayap merah berdiri dengan satu kaki di air dan satu kaki di tanah, menuangkan cairan kehidupan dari satu cawan emas ke cawan lainnya tanpa tumpah setetes pun. Temperance melambangkan alkimia keseimbangan, moderasi, dan penyembuhan harmonis di segala bidang kehidupan.",
        "readings": {
            "love": {
                "title": "Cinta yang Damai, Setara, dan Menyembuhkan",
                "summary": "Hubungan asmara yang dilandasi saling menghormati, kompromi indah, dan kedewasaan emosional.",
                "meaning": "Temperance membawa kesejukan dan harmoni dalam hubungan asmara. Ketegangan mereda melalui dialog yang tenang dan penuh pengertian. Hubunganmu mengalir seperti air jernih, di mana perbedaan latar belakang justru berpadu indah menjadi harmoni yang saling melengkapi.",
                "advice": "Carilah jalan tengah dalam setiap perbedaan pendapat; sirami hubunganmu dengan kesabaran dan kata-kata lembut.",
                "reflectionQuestion": "Bagaimana kamu dan pasangan bisa menciptakan keseimbangan antara waktu bersama dan ruang pribadi?",
                "keywords": ["Harmoni Asmara", "Kompromi Indah", "Penyembuhan Cinta", "Keseimbangan Emosi"]
            },
            "work": {
                "title": "Integrasi Tim yang Selaras dan Ritme Kerja Seimbang",
                "summary": "Memadukan berbagai keahlian tim menjadi hasil kerja yang terukur dan stabil.",
                "meaning": "Di tempat kerja, Temperance menandakan kemampuan luar biasa untuk menjadi mediator dan penyeimbang dinamika tim. Kamu mampu menggabungkan ide-ide yang bertentangan menjadi solusi bersama yang sangat aplikatif dan memuaskan semua pihak.",
                "advice": "Pertahankan ritme kerja yang stabil; hindari gaya kerja ekstrem yang memicu burnout bagi dirimu maupun tim.",
                "reflectionQuestion": "Bagian proses kerja mana yang perlu kamu seimbangkan agar tidak terjadi kejenuhan kerja?",
                "keywords": ["Mediator Ulung", "Ritme Kerja Stabil", "Sinergi Tim", "Solusi Terpadu"]
            },
            "career": {
                "title": "Pertumbuhan Karier yang Berkelanjutan dan Terarah",
                "summary": "Membangun masa depan profesional secara bertahap melalui ketekunan dan kesabaran.",
                "meaning": "Karier di bawah pengaruh Temperance berkembang dengan cara yang sangat sehat dan berkelanjutan. Kamu tidak terburu-buru mengejar hasil instan, melainkan menenun kompetensi, etika kerja, dan jejaring secara berkesinambungan. Kesuksesanmu akan bertahan lama.",
                "advice": "Bersabarlah menikmati proses pematangan kariermu; reputasi yang kokoh dibangun dari konsistensi harian.",
                "reflectionQuestion": "Langkah bertahap apa yang perlu kamu jalankan secara konsisten demi impian karier jangka panjangmu?",
                "keywords": ["Pertumbuhan Berkelanjutan", "Konsistensi", "Pematangan Karier", "Kesuksesan Abadi"]
            },
            "finance": {
                "title": "Keseimbangan Pengeluaran dan Arus Kas Sehat",
                "summary": "Mengelola keuangan dengan prinsip moderasi: tidak boros dan tidak pelit terhadap diri sendiri.",
                "meaning": "Secara finansial, Temperance adalah lambang neraca kas yang sangat ideal. Pemasukan dan pengeluaran berada dalam harmoni yang sempurna. Kamu mampu memenuhi kebutuhan pokok, menabung untuk masa depan, sekaligus menikmati rezeki secukupnya dengan penuh rasa syukur.",
                "advice": "Terapkan prinsip jalan tengah dalam keuangan; hindari pengeluaran ekstrem dan nikmati rezeki secara proporsional.",
                "reflectionQuestion": "Apakah alokasi keuanganmu saat ini sudah mencerminkan keseimbangan yang sehat antara tabungan dan kebutuhan?",
                "keywords": ["Moderasi Finansial", "Neraca Seimbang", "Arus Kas Sehat", "Rasa Syukur"]
            },
            "selfGrowth": {
                "title": "Alkimia Jiwa: Menyatukan Pertentangan Batin",
                "summary": "Menemukan titik temu antara logika dan perasaan, ambisi dan kepasrahan.",
                "meaning": "Pengembangan diri kartu Temperance adalah seni hidup berimbang. Kamu diajak mendamaikan aspek-aspek yang tampaknya bertentangan di dalam dirimu: keberanian dengan kehati-hatian, kerja keras dengan istirahat, berbicara dengan mendengarkan. Jiwamu menjadi wadah alkimia yang mengubah kekacauan menjadi kedamaian.",
                "advice": "Latihlah moderasi dalam segala hal; jangan membiarkan satu aspek kehidupan menenggelamkan aspek penting lainnya.",
                "reflectionQuestion": "Area mana dalam hidupmu yang saat ini paling membutuhkan sentuhan keseimbangan dan penyembuhan?",
                "keywords": ["Alkimia Batin", "Moderasi Hidup", "Penyembuhan Diri", "Titik Temu"]
            },
            "relationships": {
                "title": "Kedamaian dan Keharmonisan Lingkaran Terdekat",
                "summary": "Menjadi penyejuk suasana di tengah dinamika keluarga dan persahabatan.",
                "meaning": "Dalam pergaulan dan keluarga, energimu membawa efek menenangkan bagi orang-orang di sekitarmu. Saat orang lain bertengkar atau gelisah, kehadiranmu yang sabar dan kata-katamu yang menyejukkan mampu memulihkan kehangatan hubungan.",
                "advice": "Jadilah jembatan perdamaian bagi mereka yang berselisih; ajak orang lain berdialog dengan kepala dingin.",
                "reflectionQuestion": "Bagaimana kamu bisa membawa lebih banyak kedamaian dan kehangatan ke dalam rumah tanggamu?",
                "keywords": ["Penyejuk Hati", "Jembatan Damai", "Keharmonisan Keluarga", "Dialog Sejuk"]
            },
            "spirituality": {
                "title": "Aliran Rahmat Ilahi yang Tak Pernah Putus",
                "summary": "Menyadari bahwa jiwa terhubung erat dengan sumber kehidupan ilahi melalui doa yang tenang.",
                "meaning": "Secara spiritual, Temperance adalah aliran rahmat Tuhan yang mengalir tanpa henti ke dalam cawan hatimu. Dalam ketenangan batin, kamu menyadari kehadiran Yang Maha Pengasih dalam setiap tarikan napas. Jiwamu disucikan oleh air kehidupan yang membawa kedamaian abadi.",
                "advice": "Luangkan waktu untuk berdoa dan bermeditasi secara teratur; biarkan rahmat ilahi mengalir memenuhi seluruh relung jiwamu.",
                "reflectionQuestion": "Bagaimana caramu menjaga keterhubungan batin dengan Tuhan di tengah kesibukan aktivitas harian?",
                "keywords": ["Rahmat Ilahi", "Air Kehidupan", "Doa Tenang", "Kedamaian Suci"]
            }
        }
    },
    {
        "id": "the-devil",
        "number": 15,
        "name": "The Devil",
        "slug": "the-devil",
        "image": "/assets/tarot/cards/The Devil.jpg",
        "arcana": "major",
        "uprightKeywords": ["Keterikatan Semu", "Belenggu Material", "Godaan Hawa Nafsu", "Ilusi Tak Berdaya", "Menyadari Bayangan"],
        "reversedKeywords": ["Memutus Rantai", "Kemerdekaan Batin", "Sadar dari Ilusi", "Pembebasan Diri"],
        "description": "Makhluk bertanduk bertengger di atas altar batu tempat seorang pria dan wanita terikat longgar dengan rantai di leher mereka. Rantai tersebut sebenarnya cukup longgar untuk dilepas kapan saja. The Devil melambangkan ilusi keterikatan pada hawa nafsu, ketakutan materi, dan bayangan batin (shadow self) yang hanya memiliki kuasa jika kita membiarkannya.",
        "readings": {
            "love": {
                "title": "Mengenali Hubungan Kodependen dan Obsesi Semu",
                "summary": "Menyadari pola asmara yang mengekang atau keterikatan yang didasari rasa takut kehilangan.",
                "meaning": "The Devil dalam cinta memperingatkan tentang hubungan yang diwarnai posesif berlebih, kecemburuan buta, atau ketergantungan emosional yang tidak sehat. Kamu mungkin merasa terjebak, padahal kunci pembebasan ada di tanganmu sendiri saat kamu berani menetapkan batasan yang sehat.",
                "advice": "Lepaskan kebiasaan mengontrol pasangan; bangun cinta yang merdekakan jiwa, bukan yang membelenggunya dalam ketakutan.",
                "reflectionQuestion": "Apakah kamu bertahan dalam hubungan ini karena cinta sejati atau karena rasa takut akan kesepian?",
                "keywords": ["Lepaskan Belenggu", "Hindari Posesif", "Cinta Sehat", "Kemandirian Asmara"]
            },
            "work": {
                "title": "Terjebak Rutinitas Toxic dan Tekanan Berlebih",
                "summary": "Menyadari lingkungan kerja yang memeras energimu tanpa penghargaan yang sepadan.",
                "meaning": "Di lingkungan kerja, kartu ini menyoroti situasi di mana kamu merasa terikat oleh politik kantor, beban kerja berlebih, atau manipulasi rekan kerja. Sadarilah bahwa kamu memiliki pilihan untuk menolak eksploitasi dan menegakkan batasan profesionalisme.",
                "advice": "Tetapkan batas tegas antara pekerjaan dan waktu istirahat; jangan biarkan rasa takut kehilangan pekerjaan merusak kesehatanmu.",
                "reflectionQuestion": "Kompensasi atau ketakutan apa yang membuatmu tetap bertahan dalam lingkungan kerja yang merugikanmu?",
                "keywords": ["Batasan Profesional", "Hindari Eksploitasi", "Kesehatan Kerja", "Kemerdekaan Sikap"]
            },
            "career": {
                "title": "Godaan Ambisi Buta dan Perangkap Status Semu",
                "summary": "Mengingatkan agar tidak mengorbankan integritas moral demi mengejar jabatan atau materi sesaat.",
                "meaning": "Karier di bawah pengaruh The Devil membawa godaan jalan pintas, kompromi etika, atau terjebak dalam sangkar emas demi prestise lahiriah. Jangan gadaikan nilai-nilai kejujuranmu hanya untuk menyenangkan atasan atau mengejar status sosial yang semu.",
                "advice": "Pilihlah kehormatan dan kejujuran di atas kekayaan instan; reputasi yang dibangun dari intrik akan runtuh pada waktunya.",
                "reflectionQuestion": "Nilai moral apa yang tidak boleh kamu korbankan demi kemajuan kariermu?",
                "keywords": ["Integritas Moral", "Hindari Jalan Pintas", "Sangkar Emas", "Karier Bersih"]
            },
            "finance": {
                "title": "Waspada Jebakan Utang dan Perilaku Konsumtif",
                "summary": "Menghentikan jeratan utang konsumtif dan keterikatan pada gaya hidup di luar kemampuan.",
                "meaning": "Secara keuangan, The Devil adalah alarm bahaya terhadap ketergantungan pada kartu kredit, pinjaman berbunga tinggi, atau perjudian spekulatif. Rantai materi ini diciptakan oleh ilusi gengsi sesaat. Kamu harus berani memutus rantai ini dengan hidup hemat dan melunasi kewajiban.",
                "advice": "Hentikan segera utang baru; buat rencana pelunasan yang disiplin dan sederhanakan gaya hidupmu.",
                "reflectionQuestion": "Keinginan gengsi materi apa yang paling sering menjebak keuanganmu dalam kesulitan?",
                "keywords": ["Jeratan Utang", "Gengsi Semu", "Disiplin Finansial", "Memutus Rantai"]
            },
            "selfGrowth": {
                "title": "Menghadapi Bayangan Batin (Shadow Work)",
                "summary": "Mengakui ketakutan, kecanduan, dan pola pikir negatif yang selama ini membatasi potensimu.",
                "meaning": "Pengembangan diri kartu The Devil adalah proses shadow work yang mendalam. Rantai yang melilit lehermu sesungguhnya longgar: ketidakberdayaanmu selama ini adalah ilusi pikiranmu sendiri. Saat kamu berani menatap langsung bayangan ketakutanmu, kuasanya atas dirimu akan lenyap seketika.",
                "advice": "Kenali pemicu kecanduan atau kebiasaan burukmu; gantikan pola lama dengan tindakan yang memberdayakan dirimu.",
                "reflectionQuestion": "Keterikatan atau kebiasaan buruk apa yang paling merampas kebebasan dan kebahagiaan batinmu?",
                "keywords": ["Shadow Work", "Memutus Ilusi", "Kemerdekaan Diri", "Pemberdayaan"]
            },
            "relationships": {
                "title": "Memutus Pola Hubungan Toxic dalam Lingkaran Sosial",
                "summary": "Menjauhkan diri dari pertemanan yang manipulatif atau saling menjatuhkan di belakang.",
                "meaning": "Dalam pergaulan dan keluarga, The Devil mengingatkan adanya manipulasi emosional atau rasa bersalah palsu (guilt-tripping) yang digunakan orang lain untuk mengendalikanmu. Sadarilah hakmu untuk menolak dan menjauh dari lingkaran pergaulan yang merusak kedamaian hatimu.",
                "advice": "Tolak manipulasi dengan tenang namun tegas; kelilingi dirimu dengan orang-orang yang tulus mendukung kebaikanmu.",
                "reflectionQuestion": "Siapa dalam lingkaran pergaulanmu yang energinya selalu membuatmu merasa bersalah atau tidak berdaya?",
                "keywords": ["Hindari Manipulasi", "Lingkaran Sehat", "Tolak Rasa Bersalah", "Batasan Sosial"]
            },
            "spirituality": {
                "title": "Pembebasan Jiwa dari Belenggu Materialisme",
                "summary": "Menyadari bahwa jiwa adalah percikan suci yang tak dapat dipenjarakan oleh ilusi duniawi.",
                "meaning": "Secara spiritual, The Devil melambangkan keterikatan jiwa pada hawa nafsu duniawi yang melupakan asal-usul ketuhanannya. Doa dan kesadaran spiritual adalah pedang pemutus rantai ilusi tersebut. Jiwamu merdeka saat kamu menyembah Sang Pencipta, bukan ciptaan-Nya.",
                "advice": "Perbanyak doa perlindungan dan zikir pembersih hati; ingatlah bahwa dunia ini hanyalah persinggahan sementara.",
                "reflectionQuestion": "Keterikatan duniawi apa yang paling sering menghalangi kekhusyukan ibadahmu?",
                "keywords": ["Pembebasan Jiwa", "Pembersih Hati", "Kekhusyukan Doa", "Kemerdekaan Rohani"]
            }
        }
    },
    {
        "id": "the-tower",
        "number": 16,
        "name": "The Tower",
        "slug": "the-tower",
        "image": "/assets/tarot/cards/The Tower.jpg",
        "arcana": "major",
        "uprightKeywords": ["Runtuhnya Ilusi", "Kejutan Tak Terduga", "Pembersihan Fondasi Palsu", "Terobosan Radikal", "Pembebasan Mendadak"],
        "reversedKeywords": ["Menghindari Bencana", "Takut Menghadapi Fakta", "Menunda Kehancuran Keniscayaan", "Penyangkalan Diri"],
        "description": "Petir kilat menyambar mahkota menara batu tinggi yang dibangun di atas puncak tebing, meruntuhkannya dan melempar figur manusia ke bawah bersama kobaran api. The Tower melambangkan hancurnya ilusi ego dan kebohongan yang dibangun di atas fondasi rapuh, demi terbukanya kebenaran sejati.",
        "readings": {
            "love": {
                "title": "Kebenaran yang Terungkap dan Runtuhnya Topeng",
                "summary": "Peristiwa mengejutkan yang membongkar kepura-puraan demi memulihkan kejujuran hakiki dalam asmara.",
                "meaning": "The Tower dalam percintaan menandakan momen goncangan emosional atau pengungkapan rahasia yang mengejutkan. Meskipun terasa menyakitkan pada awalnya, kehancuran ini mutlak diperlukan untuk meruntuhkan topeng kepalsuan. Hubungan yang sejati akan bertahan dan dibangun kembali di atas fondasi kejujuran.",
                "advice": "Hadapi kebenaran tanpa penyangkalan; biarkan apa yang rapuh runtuh agar cinta yang sejati dapat berdiri tegak.",
                "reflectionQuestion": "Kepalsuan atau ilusi apa dalam hubunganmu yang selama ini kamu pertahankan demi kenyamanan semu?",
                "keywords": ["Runtuhnya Topeng", "Kebenaran Murni", "Goncangan Asmara", "Fondasi Jujur"]
            },
            "work": {
                "title": "Perubahan Mendadak dan Restrukturisasi Cepat",
                "summary": "Krisis tak terduga yang menuntut perombakan total cara kerja dan pemecahan masalah segera.",
                "meaning": "Di lingkungan kerja, The Tower membawa perubahan drastis: pembatalan proyek secara tiba-tiba, pergantian manajemen puncak, atau krisis operasional. Jangan panik; krisis ini adalah katalisator untuk menyingkirkan sistem yang tidak efisien dan memulai perbaikan radikal.",
                "advice": "Tetaplah berkepala dingin di tengah kekacauan; jadilah sosok yang menawarkan solusi nyata dan menenangkan tim.",
                "reflectionQuestion": "Bagaimana kamu bisa mengubah krisis kerja yang terjadi saat ini menjadi momentum pembaruan sistem?",
                "keywords": ["Krisis Katalis", "Solusi Cepat", "Kepala Dingin", "Pembaruan Radikal"]
            },
            "career": {
                "title": "Terobosan dari Sangkar Kenyamanan Profesional",
                "summary": "Kehilangan posisi yang ternyata menjadi jalan pembuka menuju panggilan karier sesungguhnya.",
                "meaning": "Karier di bawah pengaruh The Tower sering kali diawali dengan peristiwa yang terasa seperti musibah profesional: kegagalan bisnis, pemutusan kerja, atau proyek yang kandas. Namun dalam retrospeksi, peristiwa inilah yang membebaskanmu dari karier yang salah dan memaksamu mengejar potensimu yang sebenarnya.",
                "advice": "Jangan meratapi reruntuhan masa lalu; bersihkan debunya dan mulailah membangun kariermu di atas fondasi yang lebih kokoh.",
                "reflectionQuestion": "Arah baru apa yang kini terbuka bagimu setelah runtuhnya rencana lamamu?",
                "keywords": ["Terobosan Bebas", "Fondasi Baru", "Peluang Tersembunyi", "Kebangkitan Karier"]
            },
            "finance": {
                "title": "Kewaspadaan Menghadapi Pengeluaran Tak Terduga",
                "summary": "Evaluasi darurat atas stabilitas keuangan dan mitigasi risiko secara cepat.",
                "meaning": "Secara finansial, The Tower memperingatkan potensi biaya darurat yang tak terduga atau kerugian investasi yang fluktuatif. Ini adalah teguran keras dari semesta untuk berhenti berspekulasi dan segera membangun dana darurat yang benar-benar likuid dan aman.",
                "advice": "Amankan asetmu segera; pangkas seluruh pengeluaran sekunder dan fokuskan dana untuk kebutuhan darurat.",
                "reflectionQuestion": "Seberapa siap dana daruratmu dalam menghadapi skenario keuangan yang paling tak terduga?",
                "keywords": ["Dana Darurat", "Mitigasi Risiko", "Amankan Aset", "Teguran Finansial"]
            },
            "selfGrowth": {
                "title": "Hancurnya Penjara Ego dan Kelahiran Jiwa Autentik",
                "summary": "Meruntuhkan ilusi kesombongan dan menemukan kekuatan sejati di balik kerapuhan manusiawi.",
                "meaning": "Pengembangan diri kartu The Tower adalah momen katarsis yang membebaskan. Menara batu melambangkan benteng kesombongan dan konsep diri yang palsu yang kita bangun untuk melindungi ego. Sambaran petir kesadaran meruntuhkannya agar jiwa murnimu dapat bernapas bebas tanpa kepura-puraan.",
                "advice": "Rangkul kerentanan dan kerapuhan dirimu; di sanalah letak awal mula kekuatan sejatimu.",
                "reflectionQuestion": "Konsep diri palsu atau kesombongan batin apa yang sedang dibersihkan dari dirimu saat ini?",
                "keywords": ["Katarsis Batin", "Hancurnya Ego", "Kekuatan Kerentanan", "Jiwa Autentik"]
            },
            "relationships": {
                "title": "Penyelesaian Konflik yang Meledak Demi Pemulihan Hubungan",
                "summary": "Ledakan emosi yang akhirnya membuka jalan bagi percakapan jujur yang tertunda bertahun-tahun.",
                "meaning": "Dalam keluarga dan persahabatan, The Tower menandakan konfrontasi yang tak terhindarkan setelah ketegangan terpendam sekian lama. Meskipun perdebatan terasa sengit, hal ini jauh lebih sehat daripada kepalsuan yang dingin. Dari reruntuhan konflik, rekonsiliasi yang tulus dapat terwujud.",
                "advice": "Kendalikan amarah agar tidak melukai harga diri orang lain; fokuslah menyelesaikan akar masalah secara terbuka.",
                "reflectionQuestion": "Percakapan jujur apa yang selama ini kamu hindari dan kini sudah tidak bisa ditunda lagi?",
                "keywords": ["Konfrontasi Jujur", "Penyelesaian Tuntas", "Rekonsiliasi Sejati", "Keterbukaan Keluarga"]
            },
            "spirituality": {
                "title": "Petir Petunjuk Ilahi yang Menghancurkan Berhala Duniawi",
                "summary": "Menyadari bahwa hanya Tuhanlah pilar abadi yang tak akan pernah runtuh di dunia ini.",
                "meaning": "Secara spiritual, The Tower adalah karunia agung berupa runtuhnya berhala-berhala duniawi yang sempat kamu dewakan (harta, status, atau kekuasaan). Ketika segala sandaran fana hancur, kamu menyadari bahwa satu-satunya tempat bersandar yang sejati dan abadi hanyalah Sang Maha Pencipta.",
                "advice": "Bersujudlah dalam kepasrahan total; serahkan seluruh hidupmu ke dalam perlindungan Tuhan Yang Maha Esa.",
                "reflectionQuestion": "Sandaran hidup mana yang selama ini sempat melalaikan ingatanmu kepada Tuhan?",
                "keywords": ["Sandaran Abadi", "Hancurnya Berhala", "Kepasrahan Total", "Cahaya Petunjuk"]
            }
        }
    },
    {
        "id": "the-star",
        "number": 17,
        "name": "The Star",
        "slug": "the-star",
        "image": "/assets/tarot/cards/The Star.jpg",
        "arcana": "major",
        "uprightKeywords": ["Harapan", "Inspirasi", "Penyembuhan", "Kedamaian Batin", "Bimbingan Kosmis"],
        "reversedKeywords": ["Putus Asa Sementara", "Kehilangan Keyakinan", "Pikiran Pesimistis", "Ragu Masa Depan"],
        "description": "Seorang wanita tanpa busana berlutut di tepi danau di bawah langit malam bertabur delapan bintang bercahaya, menuangkan air dari dua kendi ke dalam air dan ke atas tanah subur. The Star melambangkan fajar harapan baru, penyembuhan luka batin, kedamaian surgawi, dan rasa percaya pada bimbingan kosmis.",
        "readings": {
            "love": {
                "title": "Harapan Bersemi dan Penyembuhan Luka Asmara",
                "summary": "Memulihkan rasa percaya dan optimisme dalam hubungan setelah melewati badai.",
                "meaning": "The Star adalah pelita harapan yang sangat indah dalam percintaan. Jika kamu baru saja mengalami patah hati atau perselisihan, kartu ini menandakan bahwa masa penyembuhan sedang berlangsung. Hatimu kembali terbuka untuk menerima cinta dengan kelembutan, ketulusan, dan optimisme yang murni.",
                "advice": "Tataplah masa depan hubunganmu dengan penuh harapan; biarkan kasih sayang menyembuhkan sisa-sisa trauma masa lalu.",
                "reflectionQuestion": "Bagian mana dari hatimu yang kini mulai merasakan kembali kehangatan dan keindahan cinta?",
                "keywords": ["Harapan Baru", "Penyembuhan Asmara", "Optimisme Cinta", "Kehangatan Jiwa"]
            },
            "work": {
                "title": "Inspirasi Kreatif dan Visi Masa Depan yang Cerah",
                "summary": "Mendapatkan ide-ide brilian yang membawa angin segar bagi perkembangan proyek kerja.",
                "meaning": "Di lingkungan kerja, The Star membawa inspirasi mengalir tanpa hambatan. Proyek yang sempat macet kini menemukan solusi elegan. Atmosfer kerja menjadi lebih suportif dan penuh rasa saling percaya antarrekan kerja.",
                "advice": "Bagikan visi positifmu kepada rekan tim; inspirasi yang kamu tularkan akan memicu antusiasme kerja bersama.",
                "reflectionQuestion": "Gagasan kreatif apa yang membuatmu kembali bersemangat dalam menyelesaikan pekerjaanmu?",
                "keywords": ["Inspirasi Brilian", "Optimisme Kerja", "Atmosfer Positif", "Visi Cerah"]
            },
            "career": {
                "title": "Menemukan Panggilan Jiwa dan Jalan Terang Profesi",
                "summary": "Karier yang semakin selaras dengan bakat alami dan membawa manfaat bagi sesama.",
                "meaning": "Karier di bawah pengaruh The Star menandakan fase di mana profesimu mulai selaras dengan tujuan hidup luhurmu. Pengakuan, reputasi baik, dan peluang masa depan yang cerah mulai terlihat jelas di cakrawala. Karyamu menjadi sumber inspirasi bagi banyak orang.",
                "advice": "Tetaplah setia pada nilai-nilai autentikmu; berkaryalah dengan niat memberi manfaat seluas-luasnya.",
                "reflectionQuestion": "Bagaimana kariermu dapat menjadi sarana untuk menyebarkan kebaikan dan harapan bagi orang lain?",
                "keywords": ["Panggilan Jiwa", "Bintang Penuntun", "Reputasi Positif", "Karya Bermakna"]
            },
            "finance": {
                "title": "Pemulihan Finansial dan Kemudahan Rezeki",
                "summary": "Arus kas kembali membaik dan keyakinan akan masa depan materi semakin stabil.",
                "meaning": "Secara finansial, The Star membawa kabar gembira berupa pemulihan kondisi keuangan setelah masa sulit. Kamu mulai melihat jalan keluar dari masalah utang atau kekurangan. Rezeki mengalir dengan tenang dan memberikan rasa aman yang menyejukkan hati.",
                "advice": "Kelola rezeki pemulihan ini dengan rasa syukur; buatlah rencana tabungan masa depan yang penuh harapan namun tetap realistis.",
                "reflectionQuestion": "Apakah kamu sudah mempercayai bahwa rezekimu senantiasa dicukupi oleh Tuhan?",
                "keywords": ["Pemulihan Finansial", "Rezeki Mengalir", "Ketenangan Materi", "Rasa Aman"]
            },
            "selfGrowth": {
                "title": "Kedamaian Jiwa dan Menghubungi Diri Sejati",
                "summary": "Menerima diri apa adanya dalam kepolosan dan memancarkan cahaya batin yang murni.",
                "meaning": "Pengembangan diri kartu The Star adalah ketenangan setelah badai mereda. Kamu merasa damai dengan tubuh, pikiran, dan riwayat hidupmu. Tiada lagi kepalsuan atau topeng pelindung; kamu berani tampil autentik dan memancarkan cahaya kebaikanmu ke dunia sekitar.",
                "advice": "Luangkan waktu menatap bintang di malam hari atau bermeditasi; rasakan betapa berharganya keberadaan dirimu di alam semesta ini.",
                "reflectionQuestion": "Cahaya kebaikan apa di dalam dirimu yang siap kamu pancarkan lebih terang kepada dunia?",
                "keywords": ["Cahaya Batin", "Penerimaan Autentik", "Ketenangan Jiwa", "Penyembuhan Diri"]
            },
            "relationships": {
                "title": "Persahabatan yang Menyejukkan dan Penuh Kepercayaan",
                "summary": "Dikelilingi oleh orang-orang yang tulus mendukung impian dan kebahagiaanmu.",
                "meaning": "Dalam pergaulan dan keluarga, The Star membawa suasana penuh kasih dan saling menguatkan. Kamu terhubung dengan sahabat-sahabat sejati yang menerima kekuranganmu dan senantiasa mengingatkanmu pada potensi terbaikmu.",
                "advice": "Jadilah bintang penuntun bagi sahabat yang sedang berduka; berikan dukungan moral dan doa yang tulus.",
                "reflectionQuestion": "Siapa sahabat yang selalu mampu mengingatkanmu akan harapan di saat kamu merasa terpuruk?",
                "keywords": ["Persahabatan Sejati", "Saling Menguatkan", "Dukungan Tulus", "Bintang Penuntun"]
            },
            "spirituality": {
                "title": "Koneksi Langsung dengan Rahmat Kosmis Semesta",
                "summary": "Merasakan kehadiran bimbingan ilahi yang membisikkan rasa aman di setiap langkah hidup.",
                "meaning": "Secara spiritual, The Star adalah lambang anugerah ilahi (grace). Keyakinanmu kepada Tuhan dipulihkan seutuhnya. Kamu merasakan bahwa alam semesta tidak pernah meninggalkanmu sendirian; doa-doamu didengar dan bimbingan malaikat senantiasa menaungi jiwamu.",
                "advice": "Bersyukurlah atas setiap berkah lembut yang kamu terima hari ini; jadikan hidupmu sebagai saluran rahmat bagi sesama.",
                "reflectionQuestion": "Bagaimana caramu menjaga harapan dan rasa percaya kepada Tuhan tetap menyala di hatimu?",
                "keywords": ["Anugerah Ilahi", "Rahmat Semesta", "Keyakinan Suci", "Bimbingan Malaikat"]
            }
        }
    },
    {
        "id": "the-moon",
        "number": 18,
        "name": "The Moon",
        "slug": "the-moon",
        "image": "/assets/tarot/cards/The Moon.jpg",
        "arcana": "major",
        "uprightKeywords": ["Ilusi Batin", "Ketakutan Bawah Sadar", "Ketidakpastian", "Ketajaman Intuisi", "Misteri Jiwa"],
        "reversedKeywords": ["Keluarnya Kebohongan", "Ketakutan Mereda", "Melihat Kebenaran", "Kejernihan Pikiran"],
        "description": "Bulan purnama bersinar muram di langit malam, meneteskan embun yod ke bumi. Seekor anjing dan serigala melolong ke arah bulan di samping jalan berliku yang diapit dua menara, sementara seekor kepiting merayap keluar dari kedalaman air. The Moon melambangkan labirin alam bawah sadar, ilusi ketakutan, dan navigasi malam jiwa.",
        "readings": {
            "love": {
                "title": "Menghadapi Keraguan Hati dan Firasat Terselubung",
                "summary": "Membedakan antara kecurigaan ilutif dengan intuisi sejati dalam dinamika asmara.",
                "meaning": "The Moon dalam asmara mengindikasikan adanya kabut ketidakpastian, kecemasan emosional, atau hal-hal yang belum terungkap jelas. Jangan biarkan imajinasi buruk menciptakan drama yang belum tentu nyata. Namun, jangan pula abaikan sinyal halus jika ada ketidaksesuaian antara kata dan perbuatan pasangan.",
                "advice": "Tunggu hingga kabut emosi mereda sebelum mengambil keputusan besar; bicarakan keraguanmu secara tenang tanpa menuduh.",
                "reflectionQuestion": "Kecemasan asmaramu saat ini apakah berakar dari fakta nyata atau sekadar trauma masa lalu yang berbisik?",
                "keywords": ["Kabut Asmara", "Intuisi Hati", "Hindari Prasangka", "Kejernihan Emosi"]
            },
            "work": {
                "title": "Menavigasi Informasi yang Kurang Jelas di Kantor",
                "summary": "Waspada terhadap desas-desus atau kesepakatan terselubung di lingkungan kerja.",
                "meaning": "Di lingkungan kerja, situasi sedang diselimuti ketidakjelasan informasi atau arah kebijakan yang berubah-ubah. Hindari terlibat dalam gosip kantor atau mengambil asumsi sepihak. Lakukan konfirmasi tertulis dan periksa kembali rincian data penting.",
                "advice": "Verifikasi setiap informasi dari sumber primer; jangan membuat komitmen baru sebelum semua syarat tertulis jelas.",
                "reflectionQuestion": "Informasi kerja apa yang saat ini masih ambigu dan memerlukan klarifikasi langsung?",
                "keywords": ["Klarifikasi Data", "Waspada Asumsi", "Informasi Primer", "Navigasi Hati-hati"]
            },
            "career": {
                "title": "Masa Transisi Samar Menuju Terang",
                "summary": "Menghadapi keraguan arah karier dengan mengasah ketajaman firasat dan insting profesional.",
                "meaning": "Karier di bawah pengaruh The Moon menandakan fase transisi yang terasa membingungkan di mana arah masa depan belum tampak benderang. Jangan memaksakan diri melihat jauh ke depan; fokuslah melangkah satu langkah demi satu langkah mengikuti panduan intuisimu yang terdalam.",
                "advice": "Percayai insting kreatifmu dalam menyelesaikan tantangan yang tidak memiliki panduan baku.",
                "reflectionQuestion": "Pilihan karier apa yang secara logis membingungkan namun secara batin terus menarik perhatianmu?",
                "keywords": ["Insting Tajam", "Langkah Bertahap", "Transisi Samar", "Kreativitas Intuisi"]
            },
            "finance": {
                "title": "Waspada Terhadap Tawaran Finansial yang Manipulatif",
                "summary": "Hindari investasi yang tidak transparan atau janji keuntungan yang terlalu indah untuk menjadi kenyataan.",
                "meaning": "Secara finansial, kartu The Moon adalah peringatan keras terhadap penipuan, biaya tersembunyi, atau klausul kontrak yang membingungkan. Jangan pernah menginvestasikan uang pada hal yang tidak kamu pahami sepenuhnya. Simpan dan amankan likuiditasmu saat ini.",
                "advice": "Tolak tekanan untuk berinvestasi terburu-buru; konsultasikan dokumen finansial dengan pihak independen yang tepercaya.",
                "reflectionQuestion": "Apakah ada rincian keuangan atau kontrak bisnis yang sengaja kamu abaikan karena rasa enggan memeriksa?",
                "keywords": ["Hindari Penipuan", "Transparansi Dana", "Periksa Klausul", "Kehati-hatian Materi"]
            },
            "selfGrowth": {
                "title": "Menyelami Rimba Mimpi dan Ketakutan Primitif",
                "summary": "Mengenali bagaimana trauma dan ilusi pikiran bawah sadar mempengaruhi reaksi emosionalmu.",
                "meaning": "Pengembangan diri kartu The Moon adalah ekspedisi ke dalam samudra psikologis. Anjing dan serigala melambangkan naluri jinak dan liar yang bergolak di dalam batinmu. Sadarilah bahwa ketakutan terbesarmu sering kali hanyalah proyeksi bayangan yang membesar di dalam kegelapan pikiranmu sendiri.",
                "advice": "Catat mimpimu dalam jurnal dan amati pola emosimu tanpa menghakimi; bawalah terang kesadaran ke dalam kegelapan batinmu.",
                "reflectionQuestion": "Ketakutan masa lalu apa yang selama ini paling sering mengendalikan reaksi emosimu secara otomatis?",
                "keywords": ["Jurnal Mimpi", "Proyeksi Bayangan", "Ketakutan Ilutif", "Kesadaran Bawah Sadar"]
            },
            "relationships": {
                "title": "Menyaring Prasangka dalam Komunikasi Keluarga",
                "summary": "Menghindari kesalahpahaman sosial yang timbul akibat asumsi tak terverifikasi.",
                "meaning": "Dalam hubungan persahabatan dan keluarga, The Moon mengingatkan bahwa emosi yang tidak terungkap dapat menciptakan dinding kecurigaan. Seseorang di lingkaranmu mungkin menyembunyikan kesedihan atau kekecewaannya di balik senyum palsu.",
                "advice": "Dengarkan dengan empati halus; tanyakan kabar orang-orang tersayangmu secara lebih mendalam dari sekadar basa-basi.",
                "reflectionQuestion": "Siapa di keluargamu yang gerak-geriknya menunjukkan ada sesuatu yang sedang disembunyikan?",
                "keywords": ["Empati Halus", "Klarifikasi Tulus", "Bebas Prasangka", "Kejujuran Hati"]
            },
            "spirituality": {
                "title": "Malam Gelap Jiwa Menuju Fajar Pencerahan",
                "summary": "Melewati fase ujian keimanan di mana Tuhan terasa sunyi namun senantiasa mengawasi.",
                "meaning": "Secara spiritual, The Moon menggambarkan 'Dark Night of the Soul'—fase ujian batin di mana kepastian logika runtuh dan kamu dituntut untuk tetap berpegang teguh pada tali keimanan semata-mata karena cinta, bukan karena keajaiban yang tampak. Di ujung jalan berliku ini, fajar The Sun telah menanti.",
                "advice": "Tetaplah beribadah dan berdoa meski hatimu sedang terasa hampa; keteguhan iman di saat sunyi memiliki nilai yang amat luhur.",
                "reflectionQuestion": "Bagaimana caramu menjaga nyala doa saat hatimu sedang dilanda keraguan dan kehampaan?",
                "keywords": ["Dark Night of Soul", "Ujian Keimanan", "Keteguhan Batin", "Tafakur Malam"]
            }
        }
    },
    {
        "id": "the-sun",
        "number": 19,
        "name": "The Sun",
        "slug": "the-sun",
        "image": "/assets/tarot/cards/The Sun.jpg",
        "arcana": "major",
        "uprightKeywords": ["Kebahagiaan Murni", "Vitalitas", "Kesuksesan Gemilang", "Kejelasan", "Optimisme Hangat"],
        "reversedKeywords": ["Pesimisme Sementara", "Awan Mendung Sesaat", "Kurang Bersyukur", "Terlalu Percaya Diri"],
        "description": "Matahari raksasa dengan wajah tersenyum hangat memancarkan sinar emas ke atas seorang anak kecil telanjang bertopi mahkota bunga yang menunggang kuda putih dengan gembira di depan pagar bunga matahari. The Sun adalah kartu paling positif dalam tarot: melambangkan kebahagiaan murni, kejelasan hakiki, kejayaan, dan sukacita hidup.",
        "readings": {
            "love": {
                "title": "Sukacita Asmara yang Hangat dan Transparan",
                "summary": "Kebahagiaan cinta yang murni, saling menghargai, dan penuh kehangatan tawa bersama.",
                "meaning": "The Sun membawa cahaya terang benderang ke dalam ranah asmara. Segala keraguan masa lalu lenyap digantikan oleh kepastian, kehangatan, dan kebahagiaan bersama. Hubunganmu dipenuhi oleh tawa riang, chemistry yang menyala, dan optimisme menyongsong masa depan yang indah.",
                "advice": "Rayakan kebersamaanmu dengan pasangan; tunjukkan rasa sayangmu secara terbuka dan nikmati momen bahagia ini dengan penuh syukur.",
                "reflectionQuestion": "Hal sederhana apa bersama pasangan yang paling sering menghadirkan tawa tulus di wajahmu?",
                "keywords": ["Sukacita Asmara", "Kehangatan Cinta", "Kejelasan Hati", "Tawa Bersama"]
            },
            "work": {
                "title": "Pencapaian Gemilang dan Pengakuan Publik",
                "summary": "Proyek kerja selesai dengan sukses besar dan mendapat pujian luas dari semua pihak.",
                "meaning": "Di lingkungan kerja, The Sun adalah tanda kemenangan yang cemerlang. Kerja keras dan dedikasimu membuahkan hasil luar biasa yang diakui secara luas oleh atasan dan rekan kerja. Ide-idemu diterima dengan antusias dan membawa dampak positif bagi kemajuan tim.",
                "advice": "Manfaatkan momentum kesuksesan ini untuk memotivasi timmu; rayakan pencapaian bersama dengan penuh kebanggaan.",
                "reflectionQuestion": "Pencapaian kerja apa yang paling layak kamu syukuri dan rayakan hari ini?",
                "keywords": ["Kemenangan Kerja", "Pengakuan Luas", "Sukses Gemilang", "Energi Positif"]
            },
            "career": {
                "title": "Puncak Kejayaan dan Reputasi Cemerlang",
                "summary": "Masa keemasan profesional di mana peluang, promosi, dan keberhasilan mengalir lancar.",
                "meaning": "Karier di bawah pengaruh The Sun berada pada titik tertingginya. Reputasimu bersinar terang sebagai figur tepercaya dan berprestasi tinggi. Kamu memiliki energi, karisma, dan kepercayaan diri yang kuat untuk memimpin inisiatif-inisiatif strategis berskala besar.",
                "advice": "Gunakan pengaruh cemerlangmu untuk membuka jalan bagi orang lain; jadilah pemimpin yang menginspirasi dengan kehangatan.",
                "reflectionQuestion": "Bagaimana kamu dapat memanfaatkan puncak kejayaan kariermu untuk memberi manfaat bagi masyarakat luas?",
                "keywords": ["Puncak Kejayaan", "Reputasi Cemerlang", "Kepemimpinan Hangat", "Karisma Positif"]
            },
            "finance": {
                "title": "Kelimpahan Materi dan Kemakmuran Nyata",
                "summary": "Arus rezeki mengalir berlimpah dan hasil investasi membuahkan keuntungan manis.",
                "meaning": "Secara finansial, The Sun adalah kabar paling membahagiakan: stabilitas ekonomi tercapai, keuntungan usaha melampaui target, dan masalah keuangan terselesaikan dengan tuntas. Rezekimu melimpah dan membawa kelegaan nyata bagi keluargamu.",
                "advice": "Syukuri kelimpahan ini dan sisihkan sebagian rezekimu untuk berbagi kepada mereka yang membutuhkan; rezeki yang disedekahkan akan semakin berkah.",
                "reflectionQuestion": "Kebaikan apa yang ingin kamu wujudkan dengan kelimpahan rezeki yang kamu terima saat ini?",
                "keywords": ["Kemakmuran", "Keberlimpahan", "Rezeki Berkah", "Berbagi Kebaikan"]
            },
            "selfGrowth": {
                "title": "Kembalinya Kepolosan dan Vitalitas Jiwa",
                "summary": "Menemukan kembali kegembiraan anak kecil di dalam dirimu yang bebas dari beban palsu.",
                "meaning": "Pengembangan diri kartu The Sun adalah pemulihan total energi kehidupan (vitalitas). Kamu merasa bersemangat, sehat, percaya diri, dan mencintai hidup apa adanya. Segala trauma masa lalu telah terbakar habis oleh cahaya matahari kesadaran, menyisakan jiwa murni yang siap bersinar.",
                "advice": "Nikmati sinar matahari pagi, berolahragalah dengan gembira, dan biarkan kepribadian autentikmu bersinar tanpa rasa minder.",
                "reflectionQuestion": "Aktivitas apa yang paling membuatmu merasa hidup, berenergi, dan bersukacita seutuhnya?",
                "keywords": ["Vitalitas Jiwa", "Sukacita Hidup", "Percaya Diri", "Cahaya Kesadaran"]
            },
            "relationships": {
                "title": "Keharmonisan Keluarga yang Penuh Canda Tawa",
                "summary": "Momen-momen indah bersama keluarga dan sahabat yang mempererat tali persaudaraan.",
                "meaning": "Dalam pergaulan dan keluarga, The Sun membawa suasana pesta kebahagiaan. Momen kumpul keluarga dipenuhi tawa renyah, cerita inspiratif, dan pelukan hangat. Tiada lagi kecurigaan atau ganjalan hati; segalanya terang dan menyenangkan.",
                "advice": "Ciptakan momen-momen menyenangkan bersama orang-orang tersayang; kenangan indah yang kamu rajut hari ini akan menjadi harta abadi.",
                "reflectionQuestion": "Bagaimana caramu membawa lebih banyak keceriaan dan tawa ke dalam lingkungan keluargamu?",
                "keywords": ["Canda Tawa", "Kehangatan Keluarga", "Momen Bahagia", "Persaudaraan Erat"]
            },
            "spirituality": {
                "title": "Pencerahan Hakiki dan Cahaya Ilahi yang Meliputi Semesta",
                "summary": "Merasakan kemanunggalan jiwa dengan Sang Maha Terang dalam kepenuhan syukur.",
                "meaning": "Secara spiritual, The Sun adalah puncak pencerahan rohani. Tirai kegelapan telah tersingkap sepenuhnya; kamu menyaksikan keindahan wajah Tuhan di setiap ciptaan-Nya. Hati dipenuhi cinta yang meluap-luap, kedamaian sejati, dan rasa syukur yang abadi.",
                "advice": "Jadikan rasa syukur sebagai napas ibadahmu; pancarkan kehangatan kasih Tuhan kepada setiap makhluk yang kamu temui.",
                "reflectionQuestion": "Bagaimana rasa syukur atas rahmat Tuhan dapat kamu wujudkan dalam perbuatan nyata sehari-hari?",
                "keywords": ["Cahaya Ilahi", "Pencerahan Hakiki", "Syukur Abadi", "Kemanunggalan Jiwa"]
            }
        }
    },
    {
        "id": "judgement",
        "number": 20,
        "name": "Judgement",
        "slug": "judgement",
        "image": "/assets/tarot/cards/Judgement.jpg",
        "arcana": "major",
        "uprightKeywords": ["Panggilan Jiwa", "Kebangkitan Kesadaran", "Penebusan", "Evaluasi Mendalam", "Kelahiran Baru"],
        "reversedKeywords": ["Menghakimi Diri Sendiri", "Ragu Menjawab Panggilan", "Menunda Keputusan", "Merasa Bersalah"],
        "description": "Malaikat agung meniup sangkakala emas berbendera salib merah di langit berawan. Di bawah, pria, wanita, dan anak-anak bangkit dari peti mati batu dengan tangan terangkat menyambut panggilan suci. Judgement melambangkan hari kebangkitan kesadaran, panggilan jiwa yang tak dapat diabaikan, dan pembebasan dari belenggu masa lalu.",
        "readings": {
            "love": {
                "title": "Pembaruan Hubungan dan Pengampunan Sejati",
                "summary": "Membebaskan diri dari dendam masa lalu demi membangun kembali cinta di atas komitmen dewasa.",
                "meaning": "Judgement dalam percintaan menandakan momen kebangkitan hubungan. Kamu dan pasangan diajak untuk saling memaafkan secara tulus, mengubur luka lama, dan memulai babak baru dengan pemahaman yang jauh lebih dewasa. Bagi lajang, ini adalah panggilan untuk berhenti mengulangi pola toxic masa lalu.",
                "advice": "Ampuni kesalahan masa lalu, baik kesalahan pasangan maupun kesalahanmu sendiri; sambutlah kesempatan kedua ini dengan hati yang bersih.",
                "reflectionQuestion": "Luka masa lalu apa yang siap kamu maafkan seutuhnya demi membuka jalan bagi kebahagiaan cinta yang baru?",
                "keywords": ["Pengampunan Tulus", "Pembaruan Cinta", "Kesempatan Kedua", "Kedewasaan Asmara"]
            },
            "work": {
                "title": "Evaluasi Kinerja yang Membuka Peluang Baru",
                "summary": "Meninjau kembali seluruh perjalanan kerja dan melangkah menuju tanggung jawab yang lebih mulia.",
                "meaning": "Di lingkungan kerja, Judgement adalah waktu evaluasi menyeluruh. Hasil kerja kerasmu dinilai secara adil dan kamu mendapatkan apresiasi yang layak. Ini juga waktu terbaik untuk menyelesaikan perselisihan profesional dan menyatukan kembali visi kerja tim.",
                "advice": "Lakukan refleksi objektif atas kinerjamu; belajarlah dari setiap kekeliruan dan tingkatkan standarmu ke tingkat yang lebih tinggi.",
                "reflectionQuestion": "Pelajaran terpenting apa yang kamu petik dari perjalanan kerjamu selama setahun terakhir?",
                "keywords": ["Evaluasi Adil", "Refleksi Objektif", "Standar Tinggi", "Peningkatan Mutu"]
            },
            "career": {
                "title": "Menjawab Panggilan Profesi Sejati (Vocation)",
                "summary": "Mendengar panggilan nurani untuk menjalani karier yang memiliki makna dan dampak mulia.",
                "meaning": "Karier di bawah pengaruh Judgement menandakan panggilan hidup (calling). Pekerjaanmu bukan lagi sekadar sarana mencari nafkah, melainkan wahana pengabdian jiwamu. Kamu merasa terdorong mengambil langkah besar untuk mewujudkan karya yang memberi arti bagi kemanusiaan.",
                "advice": "Jangan ragu menjawab panggilan nuranimu; persiapkan dirimu dan melangkahlah dengan keyakinan penuh menuju peran barumu.",
                "reflectionQuestion": "Panggilan profesi luhur apa yang selama ini terus bergema di dalam hatimu?",
                "keywords": ["Panggilan Hidup", "Vocation", "Pengabdian Karier", "Langkah Berani"]
            },
            "finance": {
                "title": "Penyelesaian Utang dan Transformasi Finansial",
                "summary": "Menyelesaikan seluruh tanggungan masa lalu dan membangun kebebasan finansial yang bertanggung jawab.",
                "meaning": "Secara finansial, kartu ini menuntut akuntabilitas total. Inilah saatnya melunasi seluruh kewajiban masa lalu, mengaudit aset, dan mengambil keputusan finansial yang matang demi masa depan keluarga. Keputusan bijak yang kamu ambil hari ini akan membebaskanmu dari kecemasan materi selamanya.",
                "advice": "Tuntaskan kewajiban finansial yang masih tertunda; jadikan kebebasan finansial sebagai komitmen utama masa depanmu.",
                "reflectionQuestion": "Kewajiban finansial apa yang jika kamu tuntaskan hari ini akan memberikan kelegaan terbesar bagi jiwamu?",
                "keywords": ["Akuntabilitas Total", "Bebas Utang", "Kebebasan Finansial", "Keputusan Matang"]
            },
            "selfGrowth": {
                "title": "Kebangkitan Kesadaran Tinggi dan Penebusan Diri",
                "summary": "Mendengar suara sangkakala batin yang mengajakmu bangun dari tidur panjang ketidaksadaran.",
                "meaning": "Pengembangan diri kartu Judgement adalah pembebasan dari rasa bersalah masa lalu. Peti mati batu melambangkan penjara masa lalu yang membelenggumu. Saat kamu mendengar panggilan kesadaran, kamu bangkit sebagai manusia baru yang merdeka, bijak, dan siap mengaktualisasikan seluruh potensi dirimu.",
                "advice": "Berhentilah menghakimi dirimu sendiri dengan kejam; pandang masa lalumu sebagai laboratorium pematangan jiwamu.",
                "reflectionQuestion": "Pribadi seperti apa yang siap kamu hidupkan kembali setelah melepaskan seluruh rasa bersalah masa lalumu?",
                "keywords": ["Kebangkitan Batin", "Penebusan Diri", "Bebas Rasa Bersalah", "Manusia Baru"]
            },
            "relationships": {
                "title": "Rekonsiliasi Tulus dan Penyembuhan Garis Keturunan",
                "summary": "Membuka pintu maaf bagi keluarga dan memulihkan keretakan hubungan antargenerasi.",
                "meaning": "Dalam keluarga dan persahabatan, Judgement menandakan rekonsiliasi yang mengharukan. Konflik antargenerasi atau perselisihan lama dapat disembuhkan melalui percakapan hati ke hati yang dilandasi kerendahan hati dan keinginan saling memaafkan.",
                "advice": "Ambil inisiatif untuk meminta maaf atau memaafkan; jadilah pemutus rantai dendam dalam keluargamu.",
                "reflectionQuestion": "Hubungan keluarga mana yang paling membutuhkan inisiatif permohonan maaf dan rekonsiliasi darimu?",
                "keywords": ["Rekonsiliasi Keluarga", "Pintu Maaf", "Penyembuhan Garis Keturunan", "Kerendahan Hati"]
            },
            "spirituality": {
                "title": "Panggilan Sangkakala Ilahi Menuju Kehidupan Abadi",
                "summary": "Menyadari bahwa jiwa dipanggil untuk bangkit dari kubur kelalaian menuju hadirat Tuhan.",
                "meaning": "Secara spiritual, Judgement adalah hari hisab kesadaran pribadi. Kamu diundang untuk merenungkan pertanggungjawaban hidupmu di hadapan Sang Maha Kuasa. Pintu taubat dan pengampunan terbuka selebar-lebarnya; kembalilah kepada Tuhan dengan hati yang suci dan penuh kerinduan.",
                "advice": "Perbanyak istigfar dan introspeksi diri; perbarui janji setiamu untuk senantiasa berjalan di jalan ridho-Nya.",
                "reflectionQuestion": "Seberapa siap jiwamu jika hari ini kamu dipanggil untuk menghadap Sang Maha Pencipta?",
                "keywords": ["Hari Hisab Batin", "Pintu Taubat", "Panggilan Suci", "Kesadaran Abadi"]
            }
        }
    },
    {
        "id": "the-world",
        "number": 21,
        "name": "The World",
        "slug": "the-world",
        "image": "/assets/tarot/cards/The World.jpg",
        "arcana": "major",
        "uprightKeywords": ["Kepenuhan", "Penyelesaian Sempurna", "Pencapaian Puncak", "Keutuhan Jiwa", "Harmoni Universal"],
        "reversedKeywords": ["Hampir Selesai", "Ketiadaan Penutupan", "Penundaan Tahap Akhir", "Keengganan Mengakhiri"],
        "description": "Seorang penari anggun diselimuti selendang ungu menari di dalam lingkaran karangan daun salam hijau yang diikat pita merah berbentuk angka delapan (lemniscate). Di empat sudutnya tampak empat makhluk kosmis (manusia, elang, singa, lembu). The World adalah kartu terakhir dari perjalanan Fool: melambangkan penyelesaian sempurna, integrasi utuh, dan keharmonisan agung dengan alam semesta.",
        "readings": {
            "love": {
                "title": "Cinta yang Utuh, Matang, dan Sempurna",
                "summary": "Pencapaian kebahagiaan asmara paripurna yang dilandasi penerimaan seutuhnya.",
                "meaning": "The World adalah perwujudan tertinggi dari cinta sejati. Hubunganmu telah melewati segala rintangan dan kini tiba pada fase kepenuhan, kedamaian, dan keharmonisan total. Bagi yang lajang, kamu merasa utuh di dalam dirimu sendiri, dan keutuhan inilah yang akan menarik pasangan hidup yang setara.",
                "advice": "Syukuri perjalanan cintamu yang luar biasa; rayakan kebersamaan ini sebagai berkah terindah dalam hidupmu.",
                "reflectionQuestion": "Bagaimana keutuhan batinmu saat ini memperkaya kualitas cintamu kepada orang lain?",
                "keywords": ["Cinta Paripurna", "Keutuhan Asmara", "Harmoni Total", "Penyelesaian Indah"]
            },
            "work": {
                "title": "Keberhasilan Menyelesaikan Proyek Monumental",
                "summary": "Menuntaskan tanggung jawab besar dengan hasil yang sempurna dan mendapat apresiasi global.",
                "meaning": "Di lingkungan kerja, The World menandakan keberhasilan gemilang menuntaskan proyek berskala besar atau jangka panjang. Seluruh target tercapai dengan mutu tertinggi. Kamu menutup siklus kerja ini dengan rasa bangga dan membuka peluang kerja sama yang lebih luas.",
                "advice": "Dokumentasikan keberhasilanmu dan rayakan bersama seluruh tim yang telah berjuang bersamamu.",
                "reflectionQuestion": "Pencapaian monumental apa yang berhasil kamu tuntaskan dengan gemilang dalam kerjamu?",
                "keywords": ["Proyek Tuntas", "Mutu Tertinggi", "Apresiasi Luas", "Keberhasilan Paripurna"]
            },
            "career": {
                "title": "Puncak Pencapaian Profesional dan Pengakuan Dunia",
                "summary": "Mencapai puncak cita-cita karier dengan reputasi internasional atau prestasi paripurna.",
                "meaning": "Karier di bawah pengaruh The World adalah titik kulminasi dari seluruh perjuangan profesionalmu. Gelar diraih, bisnis berhasil berekspansi, atau karya diakui secara luas. Dunia membuka pintunya untukmu; kamu siap melangkah ke panggung yang lebih agung.",
                "advice": "Gunakan pencapaianmu untuk menjadi berkat bagi sesama; persiapkan dirimu menyambut siklus pengembaraan baru yang lebih luhur.",
                "reflectionQuestion": "Warisan atau legasi profesional apa yang ingin kamu tinggalkan bagi generasi penerus?",
                "keywords": ["Puncak Prestasi", "Kulminasi Karier", "Pintu Dunia", "Legasi Abadi"]
            },
            "finance": {
                "title": "Kemakmuran Utuh dan Kemerdekaan Finansial",
                "summary": "Mencapai stabilitas dan kebebasan finansial jangka panjang yang kokoh.",
                "meaning": "Secara finansial, The World adalah lambang kemerdekaan materi. Target aset tercapai, portofolio investasi seimbang dan produktif, serta keamanan finansial keluarga terjamin. Kamu tidak lagi dikejar kecemasan uang dan mampu menikmati berkah hidup dengan tenang.",
                "advice": "Kelola asetmu untuk keberlanjutan generasi dan berbagilah rezeki untuk kegiatan filantropi yang bermakna.",
                "reflectionQuestion": "Bagaimana caramu memanfaatkan kemerdekaan finansialmu untuk melayani tujuan hidup yang lebih luhur?",
                "keywords": ["Kemerdekaan Finansial", "Kemakmuran Utuh", "Keamanan Aset", "Filantropi Mulia"]
            },
            "selfGrowth": {
                "title": "Keutuhan Batin dan Integrasi Diri Paripurna",
                "summary": "Menyatukan seluruh aspek jiwa menjadi satu kesatuan yang harmonis dan damai.",
                "meaning": "Pengembangan diri kartu The World adalah akhir dari perjalanan pahlawan (hero's journey). Kamu telah melewati jurang The Fool, bayangan The Devil, runtuhnya The Tower, hingga mencapai integrasi diri sejati. Kamu merasa utuh, tenang, dan selaras dengan seluruh ciptaan di alam semesta.",
                "advice": "Hormati seluruh perjalanan hidupmu—baik suka maupun duka; segalanya telah membentukmu menjadi pribadi yang bijak dan anggun.",
                "reflectionQuestion": "Bagaimana kamu memandang seluruh fase kehidupanmu sebagai mozaik indah yang saling melengkapi?",
                "keywords": ["Keutuhan Jiwa", "Integrasi Diri", "Hero's Journey", "Harmoni Agung"]
            },
            "relationships": {
                "title": "Lingkaran Kasih yang Luas dan Menyatu",
                "summary": "Memiliki keluarga dan sahabat yang harmonis, saling mendukung, dan merayakan kehidupan bersama.",
                "meaning": "Dalam pergaulan dan keluarga, The World menandakan keharmonisan sosial yang menyeluruh. Hubungan antarkeluarga berada dalam damai dan sukacita. Kamu memiliki jejaring sahabat yang tulus dari berbagai latar belakang yang saling memperkaya hidup satu sama lain.",
                "advice": "Peliharalah lingkaran kasih ini dengan kebaikan yang tulus; jadilah perekat kebersamaan di mana pun kamu berada.",
                "reflectionQuestion": "Bagaimana caramu merawat jalinan persahabatan agar tetap hangat dan abadi sepanjang masa?",
                "keywords": ["Lingkaran Kasih", "Harmoni Sosial", "Persahabatan Sejati", "Sukacita Bersama"]
            },
            "spirituality": {
                "title": "Manunggal dengan Keagungan Semesta Ilahi",
                "summary": "Menyadari kesatuan kosmis di mana jiwa berenang di dalam samudra kasih Tuhan.",
                "meaning": "Secara spiritual, The World adalah kesadaran kosmis (cosmic consciousness). Tiada lagi keterpisahan antara dirimu dan ciptaan Tuhan. Setiap helai rumput, bintang di langit, dan desah angin menyanyikan pujian atas keagungan Sang Pencipta. Jiwamu telah pulang ke rumah hakikinya dalam kedamaian mutlak.",
                "advice": "Tinggallah dalam rasa syukur dan cinta tanpa henti; biarkan seluruh hidupmu menjadi tarian pujian bagi Sang Maha Pengasih.",
                "reflectionQuestion": "Bagaimana rasanya menyadari bahwa dirimu senantiasa dipeluk oleh kasih Tuhan yang tak bertepi?",
                "keywords": ["Kesadaran Kosmis", "Manunggal Kasih", "Rumah Hakiki", "Kedamaian Mutlak"]
            }
        }
    }
]

print(f"Loaded all {len(MAJOR_ARCANA)} Major Arcana cards successfully!")
