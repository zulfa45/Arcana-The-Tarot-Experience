#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
from dataset_utils import format_card_entry, format_reading_entry, READINGS_DIR, SRC_DATA_DIR

major_cards_data = [
    {
        "id": "the-fool",
        "number": 0,
        "name": "The Fool",
        "slug": "the-fool",
        "image": "/assets/tarot/cards/The Fool.jpg",
        "arcana": "major",
        "uprightKeywords": ["Awal Baru", "Kepolosan", "Spontanitas", "Keberanian", "Potensi Murni"],
        "reversedKeywords": ["Kecerobohan", "Ragu Melangkah", "Naif", "Ketakutan Berlebih"],
        "description": "The Fool melambangkan jiwa pengelana yang berdiri di tepi jurang dengan tas kecil dan bunga mawar putih. Kartu ini adalah titik nol, lompatan keyakinan menuju ketidaktahuan dengan hati murni dan rasa percaya pada alam semesta.",
        "readings": {
            "love": {
                "title": "Lompatan Hati dan Lembaran Baru",
                "summary": "Keterbukaan untuk memulai kisah baru tanpa dibayangi luka masa lalu.",
                "meaning": "Dalam ranah asmara, The Fool menandakan energi segar dan keterbukaan emosional yang murni. Kamu mungkin berada di ambang koneksi baru yang tak terduga atau merasa terdorong melepaskan pola kaku dalam hubungan yang ada. Kartu ini mengajakmu menyambut cinta dengan kepolosan yang tulus tanpa prasangka.",
                "advice": "Beranikan diri membuka hati dan nikmati momen kebersamaan tanpa tergesa-gesa menuntut kepastian masa depan.",
                "reflectionQuestion": "Bagian mana dari hatimu yang masih ragu untuk percaya kembali pada keindahan cinta?",
                "keywords": ["Cinta Baru", "Spontanitas", "Keterbukaan", "Optimisme"]
            },
            "work": {
                "title": "Eksplorasi Pendekatan dan Tugas Baru",
                "summary": "Membawa perspektif segar dan kemauan belajar dalam rutinitas kerja harian.",
                "meaning": "Di lingkungan kerja, The Fool mencerminkan antusiasme memulai tugas atau proyek dengan sudut pandang unik. Jangan takut menjadi 'pemula' yang bertanya dan bereksperimen. Keberanian berpikir out-of-the-box justru menjadi keunggulan terbesarmu saat ini.",
                "advice": "Rangkul kurva pembelajaran dengan rendah hati, dengarkan saran rekan kerja, dan bawa ide kreatif ke meja diskusi.",
                "reflectionQuestion": "Keterampilan baru apa yang selama ini ingin kamu pelajari di tempat kerja namun tertunda oleh rasa takut terlihat belum mahir?",
                "keywords": ["Inovasi", "Belajar", "Segar", "Eksperimen"]
            },
            "career": {
                "title": "Awal Jalur Profesional yang Dinamis",
                "summary": "Keberanian mengambil arah karier baru atau memulai langkah independen.",
                "meaning": "The Fool dalam karier adalah tanda lompatan besar menuju aspirasi sejati. Kamu mungkin terpikir beralih profesi, merintis usaha mandiri, atau melamar posisi yang menantang batas nyamanmu. Potensi keberhasilan sangat terbuka asalkan diiringi persiapan yang bijak.",
                "advice": "Jangan biarkan status quo membelenggu potensimu; susun langkah terukur lalu mulailah melangkah dengan keyakinan penuh.",
                "reflectionQuestion": "Panggilan profesi apa yang terus mengetuk nuranimu walau tampaknya tidak lazim bagi orang lain?",
                "keywords": ["Langkah Berani", "Aspirasi", "Peralihan", "Potensi"]
            },
            "finance": {
                "title": "Peluang Baru dan Pengelolaan Waspada",
                "summary": "Sikap terbuka terhadap sumber pemasukan baru yang diimbangi kehati-hatian materi.",
                "meaning": "Dari sisi keuangan, The Fool membawa angin segar berupa potensi peluang rezeki atau investasi awal. Namun, kepolosan kartu ini juga mengingatkan agar tidak terlalu impulsif atau mudah tergiur janji keuntungan instan tanpa riset matang.",
                "advice": "Gunakan uang dengan kesadaran penuh; hindari spekulasi berisiko tinggi dan prioritaskan tabungan dasar sebelum memulai usaha baru.",
                "reflectionQuestion": "Apakah keputusan finansialmu belakangan ini didasari perhitungan matang atau sekadar dorongan sesaat?",
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
                "reflectionQuestion": "Bagaimana caramu membawa lebih banyak kehangatan dan kejenakaan ke dalam interaksi keluargamu?",
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
        "description": "The Magician berdiri dengan satu tangan menunjuk ke langit dan satu tangan ke bumi. Di mejanya terdapat tongkat, cawan, pedang, dan koin—simbol penguasaan atas empat elemen untuk memanifestasikan kehendak batin menjadi realitas nyata.",
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
                "meaning": "Secara spiritual, The Magician mengartikan konsep 'seperti di atas, begitu pula di bawah'. Doa, meditasi, dan afirmasimu memiliki daya getar kuat. Latihlah kesadaran penuh bahwa setiap tindakan fisikmu adalah wujud ibadah dan dedikasi jiwa.",
                "advice": "Jaga kejernihan niat spiritualmu; gunakan kemampuan batinmu untuk melayani kebaikan bersama.",
                "reflectionQuestion": "Bagaimana kamu mempraktikkan kesadaran spiritual dalam rutinitas keseharianmu?",
                "keywords": ["Kanal Energi", "Afirmasi Kuat", "Kesadaran Penuh", "Kebaikan Universal"]
            }
        }
    }
]

print(f"Sample major cards loaded: {len(major_cards_data)}")
