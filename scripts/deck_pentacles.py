#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deck Data: Suit of Pentacles (14 Cards: Ace to King)
Element of Earth: Material World, Finances, Career, Tangible Results, Health, Manifestation, Wealth.
"""

PENTACLES_CARDS = [
    {
        "id": "ace-of-pentacles",
        "name": "Ace of Pentacles",
        "slug": "ace-of-pentacles",
        "image": "/assets/tarot/cards/Ace of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "Ace",
        "uprightKeywords": ["Peluang Emas", "Kemakmuran Nyata", "Benih Kelimpahan", "Stabilitas Finansial", "Manifestasi Materi"],
        "reversedKeywords": ["Peluang Terlewat", "Kerugian Finansial", "Rencana Materi Rapuh", "Keserakahan"],
        "description": "Sebuah tangan ilahi muncul dari awan menggenggam koin emas berkilau (pentacle) di atas taman bunga mawar putih dan gerbang tanaman rimbun yang membingkai pemandangan pegunungan hijau. Ace of Pentacles melambangkan benih kemakmuran materi nyata, peluang finansial emas, kesehatan prima, dan manifestasi nyata dari kerja keras di dunia fisik.",
        "readings": {
            "love": {
                "title": "Cinta yang Stabil, Nyaman, dan Berfondasi Nyata",
                "summary": "Hubungan asmara yang dilandasi rasa aman materi, kepastian tempat tinggal, dan komitmen realistis.",
                "meaning": "Ace of Pentacles membawa rasa aman yang sangat membumi dalam cinta. Hubunganmu memasuki fase kepastian di mana kalian mulai merencanakan hal-hal konkret bersama: menabung untuk pernikahan, membeli rumah, atau membangun masa depan keluarga yang mapan. Bagi lajang, kartu ini meramalkan perjumpaan dengan pasangan yang mapan dan bertanggung jawab.",
                "advice": "Tunjukkan cintamu melalui tindakan dan dukungan nyata; bangunlah fondasi kehidupan bersama yang kokoh.",
                "reflectionQuestion": "Langkah konkret apa yang dapat kamu dan pasangan ambil untuk memperkuat rasa aman dalam hubungan?",
                "keywords": ["Fondasi Nyata", "Keamanan Asmara", "Komitmen Praktis", "Kemakmuran Bersama"]
            },
            "work": {
                "title": "Peluang Kerja Baru dan Kontrak Menguntungkan",
                "summary": "Mendapatkan tawaran pekerjaan baru, kenaikan gaji, atau proyek bernilai komersial tinggi.",
                "meaning": "Di lingkungan kerja, Ace of Pentacles adalah lampu hijau bagi keberhasilan materi. Tawaran kerja yang kamu nantikan resmi ditandatangani dengan kompensasi yang sangat memuaskan, atau proyek yang kamu ajukan disetujui anggarannya secara penuh. Peluang ini memiliki prospek jangka panjang yang luar biasa.",
                "advice": "Sambut peluang emas ini dengan dedikasi tinggi; kelola tanggung jawab barumu dengan profesionalisme prima.",
                "reflectionQuestion": "Peluang kerja baru apa yang saat ini hadir di hadapanmu dan siap kamu kembangkan secara maksimal?",
                "keywords": ["Peluang Emas", "Kenaikan Gaji", "Kontrak Menguntungkan", "Prospek Panjang"]
            },
            "career": {
                "title": "Titik Awal Karier yang Sangat Mapan",
                "summary": "Merintis bisnis dengan modal yang kuat atau memulai posisi di perusahaan bereputasi tinggi.",
                "meaning": "Karier di bawah pengaruh kartu ini menandakan peletakan batu pertama bagi imperium profesionalmu. Benih yang kamu tanam hari ini didukung oleh sarana yang lengkap dan pasar yang siap. Masa depan kariermu menjanjikan kemandirian finansial yang kokoh.",
                "advice": "Tanamkan benih usahamu di tanah yang subur; bangun sistem kerja yang rapi dan terukur sejak hari pertama.",
                "reflectionQuestion": "Fondasi keahlian atau modal apa yang perlu kamu persiapkan untuk memastikan kesuksesan bisnismu?",
                "keywords": ["Batu Pertama", "Merintis Bisnis", "Fondasi Mapan", "Kemandirian Karier"]
            },
            "finance": {
                "title": "Kelimpahan Rezeki dan Aliran Dana Segar",
                "summary": "Menerima rezeki nomplok, bonus besar, atau peluang investasi dengan potensi hasil tinggi.",
                "meaning": "Secara finansial, Ace of Pentacles adalah kartu terbaik. Ada aliran dana segar masuk ke rekeningmu: warisan, pencairan keuntungan investasi, atau modal usaha baru. Ini adalah waktu terbaik untuk menabung dan memulai investasi jangka panjang di sektor riil.",
                "advice": "Kelola dana segar ini dengan bijak; jangan habiskan untuk konsumsi sesaat, melainkan jadikan sebagai bibit pohon kekayaan masa depan.",
                "reflectionQuestion": "Instrumen investasi produktif apa yang paling tepat untuk mengembangbiakkan rezeki yang kamu terima saat ini?",
                "keywords": ["Aliran Dana Segar", "Bibit Kekayaan", "Investasi Riil", "Kemakmuran Nyata"]
            },
            "selfGrowth": {
                "title": "Kesehatan Raga dan Merawat Tubuh Fisik",
                "summary": "Menerapkan gaya hidup sehat, pola makan bernutrisi, dan kebugaran jasmani.",
                "meaning": "Pengembangan diri kartu Ace of Pentacles berpusat pada kesehatan tubuh fisikmu. Raga adalah bait suci tempat jiwamu tinggal selama di bumi. Inilah saatnya memulai rutinitas olahraga, mengonsumsi makanan bergizi, dan tidur cukup. Kebugaran fisikmu adalah modal dasar untuk mencapai impian besarmu.",
                "advice": "Mulailah kebiasaan hidup sehat hari ini juga; rawatlah tubuhmu dengan penuh rasa hormat dan kasih sayang.",
                "reflectionQuestion": "Kebiasaan fisik sehat apa yang jika kamu jalankan secara rutin akan melipatgandakan energimu?",
                "keywords": ["Kesehatan Raga", "Gaya Hidup Sehat", "Bait Suci Tubuh", "Kebugaran Fisik"]
            },
            "relationships": {
                "title": "Dukungan Nyata dan Saling Membantu dalam Keluarga",
                "summary": "Membantu keluarga dalam urusan tempat tinggal, pendidikan, atau kebutuhan materi sehari-hari.",
                "meaning": "Dalam pergaulan dan keluarga, kartu ini menandakan kebaikan yang diwujudkan dalam tindakan nyata: membantu renovasi rumah orang tua, memberi pinjaman modal lunak kepada kerabat yang membutuhkan, atau memasak makanan lezat untuk dinikmati bersama.",
                "advice": "Bantulah orang-orang tersayangmu dengan bantuan konkret yang benar-benar mereka butuhkan.",
                "reflectionQuestion": "Bantuan nyata apa yang bisa kamu berikan kepada keluargamu untuk meringankan beban mereka?",
                "keywords": ["Bantuan Nyata", "Dukungan Materi", "Keluarga Mapan", "Saling Membantu"]
            },
            "spirituality": {
                "title": "Bumi Sebagai Hamparan Berkah Sang Pencipta",
                "summary": "Menyadari bahwa materi dan rezeki duniawi adalah titipan suci untuk sarana berbuat kebajikan.",
                "meaning": "Secara spiritual, Ace of Pentacles mengajarkan bahwa dunia fisik ini bukanlah musuh spiritualitas, melainkan ladang amal tempat kita menanam benih pahala. Rezeki halal yang kamu peroleh adalah sarana untuk memakmurkan bumi dan menolong hamba-hamba Tuhan yang lemah.",
                "advice": "Niatkan setiap pencarian rezekimu sebagai ibadah; jadikan hartamu sebagai jembatan menuju keridhaan Tuhan.",
                "reflectionQuestion": "Bagaimana caramu menjadikan setiap rupiah rezeki yang kamu terima sebagai sarana mendekatkan diri kepada Tuhan?",
                "keywords": ["Ladang Amal", "Rezeki Halal", "Memakmurkan Bumi", "Titipan Suci"]
            }
        }
    },
    {
        "id": "two-of-pentacles",
        "name": "Two of Pentacles",
        "slug": "two-of-pentacles",
        "image": "/assets/tarot/cards/Two of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "2",
        "uprightKeywords": ["Keseimbangan Fleksibel", "Manajemen Multitasking", "Penyesuaian Adaptif", "Arus Kas Dinamis", "Kelincahan Hidup"],
        "reversedKeywords": ["Kehilangan Keseimbangan", "Kewalahan Beban Finansial", "Salah Prioritas", "Jadwal Berantakan"],
        "description": "Seorang pemuda berpakaian warna-warni dengan topi tinggi menari lincah sambil memainkan dua koin emas (pentacle) di dalam pita tak hingga (lemniscate). Di latar belakang, dua kapal berlayar melintasi ombak laut yang naik turun dengan mulus. Two of Pentacles melambangkan kelincahan menyeimbangkan prioritas hidup, fleksibilitas adaptif di tengah pasang surut ekonomi, dan manajemen multitasking yang cerdas.",
        "readings": {
            "love": {
                "title": "Menyeimbangkan Waktu Bersama dan Kesibukan Kerja",
                "summary": "Menemukan ritme asmara di tengah padatnya jadwal harian masing-masing pasangan.",
                "meaning": "Two of Pentacles dalam percintaan menandakan dinamika hidup yang sibuk. Kamu dan pasangan sama-sama memiliki pekerjaan, keluarga, dan tanggung jawab yang menyita waktu. Kuncinya adalah fleksibilitas dan komunikasi yang ceria: tidak perlu kencan mewah berjam-jam, momen singkat namun berkualitas sudah cukup menghangatkan cinta.",
                "advice": "Atur jadwal kencan secara fleksibel; bawa humor dan canda tawa untuk mencairkan kepenatan kesibukan bersama.",
                "reflectionQuestion": "Bagaimana kamu dan pasangan bisa saling menyisipkan waktu berkualitas di sela-sela padatnya rutinitas harian?",
                "keywords": ["Kelincahan Waktu", "Kencan Fleksibel", "Humor Asmara", "Keseimbangan Peran"]
            },
            "work": {
                "title": "Manajemen Waktu Efektif dan Multitasking Cerdas",
                "summary": "Menangani dua proyek besar sekaligus dengan koordinasi yang lincah dan tidak panik.",
                "meaning": "Di lingkungan kerja, kamu sedang memainkan peran ganda: menangani dua proyek sekaligus atau membagi waktu antara tugas operasional dan perencanaan strategis. Kelincahan adaptasimu membuat segala tugas selesai tepat waktu tanpa kekacauan.",
                "advice": "Gunakan kalender kerja dan teknik manajemen waktu (seperti time-blocking); tetaplah rileks saat menghadapi perubahan mendadak.",
                "reflectionQuestion": "Sistem pengelolaan waktu apa yang paling efektif untuk membantumu menyeimbangkan seluruh tugas kerjamu?",
                "keywords": ["Time-Blocking", "Multitasking Cerdas", "Kelincahan Kerja", "Adaptasi Cepat"]
            },
            "career": {
                "title": "Menjalani Bisnis Sampingan Bersamaan dengan Pekerjaan Utama",
                "summary": "Memadukan karier profesional di kantor dengan rintisan usaha mandiri secara seimbang.",
                "meaning": "Karier di bawah pengaruh kartu ini menandakan fenomena 'side hustle'. Kamu memiliki pekerjaan utama yang memberi stabilitas, sambil merintis bisnis impian di malam hari atau akhir pekan. Jika kamu menjaga staminamu dengan baik, kedua jalur ini akan saling menopang kesuksesanmu.",
                "advice": "Jaga stamina tubuhmu; jangan biarkan usaha sampingan mengganggu performa dan etika di pekerjaan utamamu.",
                "reflectionQuestion": "Bagaimana caramu mengelola energi agar pekerjaan utama dan bisnis sampinganmu sama-sama bertumbuh?",
                "keywords": ["Side Hustle", "Karier Ganda", "Stamina Prima", "Keseimbangan Sukses"]
            },
            "finance": {
                "title": "Kelincahan Mengatur Arus Kas Finansial (Cashflow Juggling)",
                "summary": "Mengelola pemasukan dan pengeluaran dinamis agar neraca keuangan tetap seimbang dan lancar.",
                "meaning": "Secara finansial, Two of Pentacles melambangkan perputaran uang yang sangat aktif: uang masuk dan uang keluar silih berganti. Kamu harus cermat mengatur tanggal jatuh tempo tagihan dan jadwal pembayaran klien agar arus kas tidak terputus di tengah jalan.",
                "advice": "Pantau arus kas harianmu secara cermat; siapkan pos cadangan kecil untuk mengantisipasi keterlambatan pembayaran klien.",
                "reflectionQuestion": "Apakah jadwal pembayaran dan tagihan kasmu sudah teratur dengan rapi di buku catatan keuangan?",
                "keywords": ["Cashflow Aktif", "Kelincahan Kas", "Jatuh Tempo Tertib", "Keseimbangan Anggaran"]
            },
            "selfGrowth": {
                "title": "Seni Menari di Tengah Ketidakpastian Hidup",
                "summary": "Menyikapi perubahan hidup dengan tawa dan fleksibilitas, bukan dengan kepanikan kaku.",
                "meaning": "Pengembangan diri kartu Two of Pentacles adalah seni hidup luwes (adaptability). Hidup ini seperti ombak laut: selalu naik dan turun. Jika kamu kaku, kamu akan patah; namun jika kamu lentur selayaknya penari, kamu akan berselancar di atas setiap ombak perubahan dengan anggun dan riang.",
                "advice": "Jangan terlalu serius menanggapi kerepotan kecil sehari-hari; tertawalah dan nikmati setiap tarian ritme hidupmu.",
                "reflectionQuestion": "Area hidup mana yang saat ini paling membutuhkan sikap lebih santai dan fleksibel darimu?",
                "keywords": ["Lentur Menari", "Fleksibilitas Hidup", "Selancar Ombak", "Humor Batin"]
            },
            "relationships": {
                "title": "Membagi Perhatian Antara Keluarga dan Sahabat",
                "summary": "Mengatur waktu berkumpul dengan adil agar tidak ada pihak yang merasa ditinggalkan.",
                "meaning": "Dalam pergaulan dan keluarga, kamu dicari oleh banyak lingkaran sosial. Kuncinya adalah kejujuran mengenai ketersediaan waktumu: jika kamu sedang sibuk, katakan dengan ramah dan jadwalkan pertemuan di lain waktu tanpa rasa bersalah.",
                "advice": "Hadir seutuhnya saat bersama mereka; kualitas kehadiran jauh lebih penting daripada durasi waktu yang lama.",
                "reflectionQuestion": "Bagaimana caramu membagi waktu berkumpul dengan adil antara keluarga inti dan sahabat karib?",
                "keywords": ["Kualitas Kehadiran", "Jadwal Adil", "Bagi Perhatian", "Komunikasi Santun"]
            },
            "spirituality": {
                "title": "Lambang Tak Hingga: Siklus Abadi Kehidupan di Dunia",
                "summary": "Menyadari bahwa pasang surut duniawi adalah ritme alami yang senantiasa berada dalam genggaman Tuhan.",
                "meaning": "Secara spiritual, pita lemniscate (simbol tak hingga) melambangkan siklus abadi yang tidak pernah putus. Suka dan duka, sempit dan lapang, adalah dua sisi dari kepingan kehidupan yang sama. Seorang hamba yang arif tidak mabuk saat lapang dan tidak putus asa saat sempit; hatinya senantiasa tertaut kepada Sang Penguasa Segala Keadaan.",
                "advice": "Jadikan sabar dan syukur sebagai dua kaki spiritualmu dalam melangkah menempuh jalan hidup.",
                "reflectionQuestion": "Bagaimana caramu menjaga hati agar tetap seimbang saat menghadapi pasang surut keadaan duniawi?",
                "keywords": ["Lemniscate Abadi", "Ritme Kosmis", "Sabar dan Syukur", "Keseimbangan Tauhid"]
            }
        }
    },
    {
        "id": "three-of-pentacles",
        "name": "Three of Pentacles",
        "slug": "three-of-pentacles",
        "image": "/assets/tarot/cards/Three of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "3",
        "uprightKeywords": ["Keahlian Kolaboratif", "Pengerjaan Mutu Tinggi", "Sinergi Tim", "Apresiasi Profesional", "Membangun Fondasi"],
        "reversedKeywords": ["Kurang Koordinasi", "Egoisme Kerja Tim", "Kualitas Kerja Buruk", "Miskomunikasi Peran"],
        "description": "Seorang pematung muda berdiri di atas bangku kayu sedang memahat pilar batu katedral dengan teliti. Di depannya berdiri seorang arsitek memegang cetak biru (blueprint) dan seorang biarawan yang memegang buku catatan, saling berdiskusi dan mengapresiasi karyanya. Tiga koin emas terukir di lengkungan gerbang katedral. Three of Pentacles melambangkan keahlian pertukangan mutu tinggi, kolaborasi tim profesional yang solid, dan apresiasi karya.",
        "readings": {
            "love": {
                "title": "Membangun 'Katedral Cinta' Bersama Pasangan",
                "summary": "Bekerja sama bahu-membahu membangun masa depan asmara dengan rencana konkret dan pembagian peran yang adil.",
                "meaning": "Three of Pentacles dalam percintaan menandakan hubungan yang sangat matang dan konstruktif. Kalian berdua memandang hubungan ini sebagai karya agung yang perlu dibangun bersama dengan ketelatenan, kesabaran, dan pembagian tugas yang jelas. Rasa saling menghargai keahlian masing-masing membuat hubungan ini semakin kokoh.",
                "advice": "Dengarkan masukan pasangan dengan rasa hormat; selesaikan proyek-proyek keluarga (seperti renovasi rumah atau perencanaan keuangan) sebagai tim yang solid.",
                "reflectionQuestion": "Proyek bersama apa yang saat ini paling menyenangkan untuk kamu dan pasangan kerjakan berdua?",
                "keywords": ["Membangun Bersama", "Tim Asmara", "Pembagian Peran", "Fondasi Rumah"]
            },
            "work": {
                "title": "Kolaborasi Antardisiplin yang Menghasilkan Mahakarya",
                "summary": "Bekerja sama secara harmonis antara desainer, insinyur, dan manajemen demi mutu proyek terbaik.",
                "meaning": "Di lingkungan kerja, Three of Pentacles adalah standar emas kolaborasi tim. Keahlianmu diakui dan dihargai oleh atasan dan rekan kerja. Tidak ada yang merasa paling hebat; setiap orang menyumbangkan keahlian terbaiknya demi kesuksesan proyek bersama.",
                "advice": "Tunjukkan ketelitian dan keahlian terbaikmu; dengarkan arahan cetak biru (blueprint) dan koordinasikan setiap detail dengan tim.",
                "reflectionQuestion": "Bagaimana kontribusi keahlian unikmu saat ini memperkuat mutu hasil kerja tim secara keseluruhan?",
                "keywords": ["Kolaborasi Mutu", "Keahlian Profesional", "Cetak Biru", "Sinergi Antardisiplin"]
            },
            "career": {
                "title": "Mendapatkan Pengakuan Sebagai Ahli Berkompeten",
                "summary": "Peningkatan reputasi profesional berkat ketekunan mengasah keterampilan teknis hingga mahir.",
                "meaning": "Karier di bawah pengaruh kartu ini menandakan bahwa kamu telah mencapai level keahlian (mastery) yang diakui oleh para senior di industri. Portofoliomu dipuji dan klien-klien besar mempercayakan proyek-proyek prestisius kepadamu. Reputasimu dibangun di atas karya nyata.",
                "advice": "Teruslah mengasah keterampilanmu; carilah sertifikasi atau mentor tingkat lanjut untuk menyempurnakan keahlianmu.",
                "reflectionQuestion": "Keterampilan teknis apa yang jika kamu asah hingga tingkat mahir akan melipatgandakan nilai jual profesionalmu?",
                "keywords": ["Mastery Keahlian", "Reputasi Diakui", "Karya Nyata", "Proyek Prestisius"]
            },
            "finance": {
                "title": "Investasi pada Keterampilan dan Pembayaran Setimpal",
                "summary": "Mendapatkan bayaran tinggi berkat keahlian spesialisasi yang jarang dimiliki orang lain.",
                "meaning": "Secara finansial, Three of Pentacles membuktikan bahwa 'skill pays the bills'. Uang yang kamu hasilkan berbanding lurus dengan kualitas keahlian dan jam terbangmu. Menginvestasikan uang untuk kursus, alat kerja berkualitas, atau pelatihan profesional akan menghasilkan imbal hasil yang sangat besar.",
                "advice": "Jangan ragu menetapkan tarif profesional yang sepadan dengan mutumu; teruslah berinvestasi pada peningkatan keahlian dirimu.",
                "reflectionQuestion": "Alat kerja atau pelatihan apa yang paling layak kamu beli untuk menunjang peningkatan produktivitas finansialmu?",
                "keywords": ["Tarif Profesional", "Investasi Skill", "Bayaran Setimpal", "Kualitas Bernilai"]
            },
            "selfGrowth": {
                "title": "Dedikasi Menjadi Ahli: Kesabaran Mengasah Bakat",
                "summary": "Mencintai proses belajar bertahap dan menikmati setiap goresan pahatan perbaikan diri.",
                "meaning": "Pengembangan diri kartu Three of Swords adalah filosofi pertukangan (craftsmanship). Pribadi yang unggul tidak lahir dalam semalam; ia dibentuk melalui ribuan jam latihan yang tekun dan kesediaan menerima kritik yang membangun. Nikmatilah proses memahat karaktermu sendiri hingga menjadi pribadi yang berakhlak mulia.",
                "advice": "Terimalah kritik dari orang yang ahli dengan rendah hati; jadikan setiap masukan sebagai amunisi untuk menyempurnakan dirimu.",
                "reflectionQuestion": "Bagian dari kebiasaan atau keahlianmu mana yang saat ini sedang kamu pahat dengan tekun menuju kesempurnaan?",
                "keywords": ["Filosofi Pertukangan", "Latihan Tekun", "Terima Kritik", "Memahat Karakter"]
            },
            "relationships": {
                "title": "Kerja Sama Keluarga dan Gotong Royong Komunitas",
                "summary": "Bahu-membahu bersama sanak saudara atau tetangga dalam menyelesaikan hajat bersama.",
                "meaning": "Dalam pergaulan dan keluarga, Three of Pentacles melambangkan semangat gotong royong. Saat ada renovasi rumah ibadah, hajatan pernikahan kerabat, atau bakti sosial, setiap orang menyumbangkan tenaga dan keahliannya dengan gembira. Suasana persaudaraan terasa sangat kental.",
                "advice": "Ambil peran aktif dalam kegiatan gotong royong; sumbangkan apa yang bisa kamu bantu demi keberhasilan bersama.",
                "reflectionQuestion": "Kegiatan sosial atau keluarga apa yang saat ini paling membutuhkan kontribusi tenaga dan keahlianmu?",
                "keywords": ["Gotong Royong", "Bahu-membahu", "Hajat Bersama", "Persaudaraan Nyata"]
            },
            "spirituality": {
                "title": "Membangun Bait Ibadah di Dunia dan Akhirat",
                "summary": "Menyadari bahwa setiap amal kebaikan yang dikerjakan dengan mutu ihsan adalah batu bata bagi istana surgawi.",
                "meaning": "Secara spiritual, pemahat katedral melambangkan amalan yang dikerjakan dengan derajat 'Ihsan'—menyembah dan berkarya dengan mutu terbaik seolah-olah kamu melihat Tuhan. Tiga koin di gerbang katedral adalah simbol iman, ilmu, dan amal shaleh yang berpadu kokoh membangun keselamatan jiwamu.",
                "advice": "Tingkatkan mutu ibadah dan amal perbuatanmu; kerjakan segala sesuatu dengan standar terbaik semata-mata demi keagungan Tuhan.",
                "reflectionQuestion": "Bagaimana caramu menerapkan prinsip ihsan (kualitas terbaik) dalam setiap amal ibadah dan pekerjaan harianmu?",
                "keywords": ["Derajat Ihsan", "Katedral Jiwa", "Iman Ilmu Amal", "Istana Surgawi"]
            }
        }
    },
    {
        "id": "four-of-pentacles",
        "name": "Four of Pentacles",
        "slug": "four-of-pentacles",
        "image": "/assets/tarot/cards/Four of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "4",
        "uprightKeywords": ["Konservatif Finansial", "Menjaga Aset Ketat", "Rasa Takut Miskin", "Stabilitas Terjaga", "Perlu Melepaskan"],
        "reversedKeywords": ["Kikir Berlebih", "Pemborosan Mendadak", "Kehilangan Kontrol", "Belajar Berderma"],
        "description": "Seorang pria duduk di atas bangku batu di pinggiran kota megah, mendekap erat satu koin emas di dadanya dengan kedua tangan, menduduki satu koin di kepalanya, dan menginjak dua koin di bawah kedua kakinya. Four of Pentacles melambangkan keamanan finansial yang ketat, pengendalian aset secara konservatif, namun juga memperingatkan bahaya kekikiran, rasa takut kehilangan materi, dan kekakuan batin.",
        "readings": {
            "love": {
                "title": "Rasa Takut Kehilangan dan Sikap Posesif Asmara",
                "summary": "Menyadari bahwa menggenggam pasangan terlalu erat justru dapat mencekik kebebasan dan kehangatan cinta.",
                "meaning": "Four of Pentacles dalam percintaan menandakan adanya rasa tidak aman (insecurity) yang berwujud sikap protektif berlebih atau posesif. Kamu mungkin takut dikhianati atau kehilangan pasangan hingga berusaha mengontrol jadwal dan pergaulannya. Ingatlah bahwa cinta adalah burung yang indah: jika digenggam terlalu kencang, ia akan terluka.",
                "advice": "Longgarkan genggamanmu; bangun rasa saling percaya dan beri ruang bagi pasangan untuk bernapas bebas.",
                "reflectionQuestion": "Kekhawatiran apa di dalam hatimu yang membuatmu merasa perlu mengontrol pasangan secara berlebihan?",
                "keywords": ["Hindari Posesif", "Rasa Aman Batin", "Longgarkan Genggaman", "Kepercayaan Asmara"]
            },
            "work": {
                "title": "Menjaga Posisi dan Keengganan Mengambil Risiko",
                "summary": "Bertahan pada metode kerja lama yang aman namun menghambat inovasi dan terobosan baru.",
                "meaning": "Di lingkungan kerja, kartu ini menunjukkan keengganan berbagi informasi atau keengganan mencoba teknologi baru karena takut gagal. Sikap konservatif ini memang melindungi stabilitasmu saat ini, namun jika berlebihan dapat membuatmu dicap kaku dan tidak adaptif terhadap perubahan industri.",
                "advice": "Berbagilah ilmu dengan rekan kerja; beranikan diri mengalokasikan sebagian waktu untuk bereksperimen dengan metode baru.",
                "reflectionQuestion": "Kebiasaan kerja aman apa yang saat ini mulai membatasi kreativitas dan potensi inovasimu?",
                "keywords": ["Konservatif Kerja", "Hindari Kaku", "Berbagi Ilmu", "Ruang Inovasi"]
            },
            "career": {
                "title": "Mempertahankan Jabatan dan Keamanan Finansial Karier",
                "summary": "Memilih bertahan di perusahaan mapan dengan tunjangan pasti daripada merintis usaha yang spekulatif.",
                "meaning": "Karier di bawah pengaruh Four of Pentacles memprioritaskan keamanan: dana pensiun, asuransi kesehatan, dan kepastian gaji bulanan. Ini adalah pilihan yang sangat bijak jika kamu sedang memiliki tanggungan keluarga besar. Pastikan kamu tetap mengasah keterampilan agar posisimu tetap relevan.",
                "advice": "Jaga posisimu dengan performa kerja yang andal; namun jangan biarkan rasa takut membuatmu menolak seluruh peluang promosi.",
                "reflectionQuestion": "Bagaimana kamu menjaga keseimbangan antara kebutuhan akan rasa aman karier dengan peluang pertumbuhan?",
                "keywords": ["Keamanan Karier", "Tunjangan Mapan", "Stabilitas Posisi", "Proteksi Masa Depan"]
            },
            "finance": {
                "title": "Penghematan Ketat dan Memperkuat Dana Darurat",
                "summary": "Menahan diri dari pengeluaran sekunder demi mengumpulkan cadangan kas yang sangat kokoh.",
                "meaning": "Secara finansial, Four of Pentacles adalah disiplin menabung tingkat tinggi. Kamu sangat berhati-hati mengeluarkan uang dan memprioritaskan akumulasi dana darurat di rekening bank. Kamu aman dari risiko kebangkrutan, namun jangan sampai sikap hematmu berubah menjadi kekikiran yang menyiksa diri sendiri.",
                "advice": "Pertahankan disiplin menabungmu; namun sisihkan sedikit anggaran untuk sedekah dan memanjakan keluarga secara wajar.",
                "reflectionQuestion": "Apakah kamu menabung karena memiliki rencana masa depan yang jelas atau semata-mata karena rasa cemas akan kemiskinan?",
                "keywords": ["Disiplin Tabungan", "Dana Darurat Kokoh", "Hindari Kikir", "Keamanan Kas"]
            },
            "selfGrowth": {
                "title": "Menyembuhkan 'Scarcity Mindset' (Ketakutan Selalu Kurang)",
                "summary": "Peralihan dari rasa takut kekurangan menjadi keyakinan akan kelimpahan semesta.",
                "meaning": "Pengembangan diri kartu ini adalah tentang melonggarkan genggaman ego. Koin yang didekap erat di dada melambangkan hati yang tertutup oleh rasa takut miskin. Sadarilah bahwa alam semesta ini melimpah ruah. Semakin erat kamu menggenggam, semakin sedikit tanganmu dapat menerima berkah baru.",
                "advice": "Latihlah memberi sedekah secara rutin meski nominalnya kecil; tindakan memberi akan melatih hatimu merasa kaya.",
                "reflectionQuestion": "Keterikatan materi apa yang paling membebani pikiranmu dan perlu kamu ikhlaskan?",
                "keywords": ["Scarcity Mindset", "Hati Melimpah", "Melonggarkan Genggaman", "Melatih Derma"]
            },
            "relationships": {
                "title": "Kekakuan Batasan dalam Interaksi Sosial dan Keluarga",
                "summary": "Belajar untuk lebih ramah dan tidak terlalu kaku mempertahankan privasi dari orang tua dan sahabat.",
                "meaning": "Dalam pergaulan dan keluarga, kamu mungkin terkesan tertutup atau enggan berbagi cerita karena takut dimanfaatkan orang lain. Waspada itu baik, namun jangan sampai kamu membangun dinding benteng yang membuat orang-orang tersayang merasa terasing darimu.",
                "advice": "Bukalah pintu rumah dan hatimu bagi sahabat-sahabat sejati; kehangatan silaturahmi menuntut sedikit kerentanan emosional.",
                "reflectionQuestion": "Apakah sikap protektifmu selama ini membuat orang-orang terdekatmu merasa sulit mendekatimu?",
                "keywords": ["Hindari Dinding Dingin", "Kehangatan Silaturahmi", "Buka Pintu Hati", "Keterbukaan Santun"]
            },
            "spirituality": {
                "title": "Peringatan Terhadap Bahaya Menimbun Harta Tanpa Hak",
                "summary": "Menyadari bahwa harta benda adalah titipan yang kelak akan dimintai pertanggungjawaban di akhirat.",
                "meaning": "Secara spiritual, Four of Pentacles adalah cermin bagi bahaya bakhil (kikir). Dalam ajaran suci diingatkan: 'Celakalah bagi setiap pengumpat dan pencela, yang mengumpulkan harta dan menghitung-hitungnya, mengira hartanya dapat mengekalkannya.' Pemilik mutlak seluruh perbendaharaan langit dan bumi adalah Tuhan.",
                "advice": "Keluarkan zakat dan sedekah wajibmu dengan lapang dada; bersihkan hartamu agar mengalirkan keberkahan abadi.",
                "reflectionQuestion": "Bagaimana caramu memastikan bahwa hartamu tidak menjadi berhala yang membelenggu jiwamu?",
                "keywords": ["Bahaya Bakhil", "Zakat Bersih", "Titipan Ilahi", "Pertanggungjawaban Harta"]
            }
        }
    },
    {
        "id": "five-of-pentacles",
        "name": "Five of Pentacles",
        "slug": "five-of-pentacles",
        "image": "/assets/tarot/cards/Five of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "5",
        "uprightKeywords": ["Kesulitan Materi", "Merasa Ditelantarkan", "Musim Dingin Finansial", "Pintu Bantuan Terbuka", "Ujian Ketabahan"],
        "reversedKeywords": ["Pemulihan Finansial", "Menemukan Tempat Berlindung", "Bantuan Diterima", "Berakhirnya Masa Sulit"],
        "description": "Dua orang pengemis berpakaian compang-camping melangkah tertatih-tatih melintasi badai salju dingin di malam hari. Salah satunya berjalan menggunakan kruk penyangga dengan bel di lehernya. Di atas mereka bersinar jendela kaca patri sebuah gereja hangat bergambar lima koin emas yang terang benderang. Five of Pentacles melambangkan kesulitan ekonomi sementara, rasa terasing dan kedinginan batin, namun mengingatkan bahwa pintu tempat perlindungan dan bantuan ilahi berada tepat di samping kita jika kita mendongakkan kepala.",
        "readings": {
            "love": {
                "title": "Ujian Kemiskinan dan Kebersamaan di Masa Sulit",
                "summary": "Menjaga kesetiaan cinta saat kondisi keuangan atau kesehatan pasangan sedang terpuruk.",
                "meaning": "Five of Pentacles dalam percintaan adalah ujian kesetiaan sejati: 'dalam suka maupun duka, dalam kaya maupun miskin'. Kalian berdua mungkin sedang menghadapi masalah ekonomi yang menekan atau merasa terasing dari dukungan keluarga. Jangan saling menyalahkan; saling berpegangan tanganlah menembus badai salju ini bersama-sama.",
                "advice": "Peluk pasanganmu erat-erat; ingatkan dia bahwa cinta kalian jauh lebih berharga daripada kesulitan materi yang sedang dihadapi.",
                "reflectionQuestion": "Bagaimana kamu dan pasangan bisa saling menguatkan hati di tengah masa-masa keterbatasan materi ini?",
                "keywords": ["Ujian Kesetiaan", "Setia di Masa Sulit", "Saling Menguatkan", "Menembus Badai"]
            },
            "work": {
                "title": "Masa Sulit di Tempat Kerja dan Ancaman Pemangkasan",
                "summary": "Menghadapi pemotongan anggaran, restrukturisasi perusahaan, atau rasa tidak aman dalam pekerjaan.",
                "meaning": "Di lingkungan kerja, situasi sedang berada di musim dingin: anggaran dipangkas ketat, fasilitas dikurangi, atau ada isu pemutusan hubungan kerja. Jangan putus asa dan mengurung diri dalam kepanikan. Ada pintu bantuan (rekan, serikat pekerja, atau program pelatihan) yang siap membantumu jika kamu mau bertanya.",
                "advice": "Jalin komunikasi erat dengan rekan sejawat; carilah informasi tentang program bantuan atau peluang kerja di divisi lain.",
                "reflectionQuestion": "Bantuan atau sumber daya apa di sekitarmu yang selama ini belum kamu mintai pertolongan?",
                "keywords": ["Musim Dingin Kerja", "Pemangkasan Anggaran", "Pintu Bantuan", "Solidaritas Karyawan"]
            },
            "career": {
                "title": "Menghadapi Masa Pengangguran dengan Ketabahan Mental",
                "summary": "Menolak merasa kehilangan harga diri saat belum mendapatkan pekerjaan yang diidamkan.",
                "meaning": "Karier di bawah pengaruh Five of Pentacles menandakan fase jeda yang berat: kehilangan pekerjaan atau penolakan bertubi-tubi yang menggerus rasa percaya diri. Ingatlah bahwa status pekerjaanmu bukanlah ukuran nilai kemanusiaanmu. Ini hanyalah musim dingin sementara; musim semi pasti akan tiba.",
                "advice": "Jangan ragu meminta bantuan jaringan sosial atau mengambil pekerjaan sementara demi menjaga arus kas harian.",
                "reflectionQuestion": "Keahlian apa yang bisa kamu manfaatkan untuk bertahan hidup sembari menanti peluang karier yang lebih baik?",
                "keywords": ["Ketabahan Pengangguran", "Nilai Diri Utuh", "Musim Dingin Sementara", "Pekerjaan Bertahan"]
            },
            "finance": {
                "title": "Krisis Finansial Sementara dan Pengurangan Pengeluaran Drastis",
                "summary": "Mengatasi defisit anggaran dengan memotong seluruh pos sekunder dan mencari bantuan darurat.",
                "meaning": "Secara finansial, Five of Pentacles melambangkan masa paceklik atau krisis likuiditas kas. Tabungan menipis dan tagihan mendesak. Dalam kondisi ini, kesampingkan rasa gengsi: mintalah keringanan cicilan kepada kreditur, cari bantuan keluarga, atau manfaatkan program jaring pengaman sosial.",
                "advice": "Pangkas pengeluaran hingga ke kebutuhan bertahan hidup yang paling pokok; singkirkan rasa malu untuk mencari bantuan resmi.",
                "reflectionQuestion": "Pengeluaran apa yang harus segera kamu hentikan hari ini demi memastikan kebutuhan pangan keluarga tetap aman?",
                "keywords": ["Masa Paceklik", "Defisit Kas", "Singkirkan Gengsi", "Bantuan Darurat"]
            },
            "selfGrowth": {
                "title": "Mendongakkan Kepala Menatap Jendela Harapan",
                "summary": "Berhenti terpaku pada tanah berlumpur kemalangan dan melihat bahwa bantuan selalu tersedia.",
                "meaning": "Pengembangan diri kartu Five of Pentacles adalah tentang mengubah fokus pandangan. Dua musafir di salju berjalan membungkuk menatap tanah sehingga tidak melihat jendela gereja yang hangat di atas kepala mereka. Berhentilah mengasihani diri sendiri; dongakkan kepalamu dan lihatlah bahwa ada kebaikan dan harapan yang menantimu.",
                "advice": "Katakan pada dirimu: 'Ini ujian sementara dan aku sanggup melewatinya'; bukalah dirimu untuk menerima bantuan orang lain.",
                "reflectionQuestion": "Pertolongan atau kebaikan apa yang selama ini ada di dekatmu namun tidak kamu sadari karena terlalu fokus pada penderitaanmu?",
                "keywords": ["Dongakkan Kepala", "Jendela Harapan", "Hentikan Mengasihani Diri", "Kekuatan Bertahan"]
            },
            "relationships": {
                "title": "Merasakan Siapa Sahabat Sejati di Kala Sulit",
                "summary": "Musim dingin hidup menyaring siapa yang benar-benar setia dan siapa yang hanya teman saat senang.",
                "meaning": "Dalam pergaulan dan keluarga, masa-masa sulit adalah saringan alami terbaik. Mereka yang dulu mendekat saat kamu kaya mungkin menghilang saat kamu jatuh. Namun mereka yang tetap mengetuk pintumu dan membawakan makanan hangat di tengah badai adalah saudara sejatimu.",
                "advice": "Hargai mereka yang tetap menemanimu di masa sulit; jadikan kebaikan mereka sebagai teladan untuk membalas budi kelak.",
                "reflectionQuestion": "Siapa sosok tulus yang tidak pernah berubah sikapnya kepadamu meski kamu sedang berada di titik terendah?",
                "keywords": ["Sahabat Sejati", "Saringan Kesetiaan", "Kebaikan Tulus", "Menemani di Masa Sulit"]
            },
            "spirituality": {
                "title": "Cahaya Bait Ibadah di Tengah Badai Kehidupan",
                "summary": "Menyadari bahwa pintu rumah Tuhan senantiasa terbuka menyambut jiwa-jiwa yang kedinginan dan terluka.",
                "meaning": "Secara spiritual, Five of Swords melambangkan perlindungan rumah ibadah di tengah dinginnya badai duniawi. Cahaya jendela kaca patri gereja adalah simbol kehadiran Tuhan yang hangat. Ketika dunia menolakmu dan mengusirmu, pintu kasih sayang Tuhan tidak pernah terkunci bagi hamba-Nya yang berserah.",
                "advice": "Masuklah ke tempat ibadah; basahi wajahmu dan duduklah dalam kehangatan doa memohon perlindungan kepada-Nya.",
                "reflectionQuestion": "Bagaimana caramu menjadikan doa dan ibadah sebagai tempat bernaung paling hangat saat dunia terasa dingin?",
                "keywords": ["Bait Perlindungan", "Cahaya Kaca Patri", "Pintu Rahmat Terbuka", "Kehangatan Doa"]
            }
        }
    },
    {
        "id": "six-of-pentacles",
        "name": "Six of Pentacles",
        "slug": "six-of-pentacles",
        "image": "/assets/tarot/cards/Six of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "6",
        "uprightKeywords": ["Kedermawanan Tulus", "Keseimbangan Memberi dan Menerima", "Bantuan Finansial", "Keadilan Amal", "Saling Berbagi"],
        "reversedKeywords": ["Kedermawanan Bersyarat", "Riba Menjerat", "Ketergantungan Bantuan", "Utang Budi Menekan"],
        "description": "Seorang saudagar kaya berjubah ungu memegang timbangan neraca yang berimbang di tangan kiri, sementara tangan kanannya membagikan koin emas kepada dua orang fakir yang berlutut di depannya dengan penuh rasa hormat. Six of Pentacles melambangkan kedermawanan yang adil, keseimbangan hukum memberi dan menerima, pertolongan finansial yang tepat sasaran, dan kemurahan hati.",
        "readings": {
            "love": {
                "title": "Keseimbangan Memberi dan Menerima Kasih Sayang",
                "summary": "Membangun hubungan asmara yang setara di mana kedua belah pihak saling memperhatikan dan mendukung tanpa pamrih.",
                "meaning": "Six of Pentacles dalam percintaan menyoroti neraca timbangan emosi. Hubungan asmara yang sehat membutuhkan keseimbangan: tidak boleh ada satu pihak yang selalu berkorban sementara pihak lain hanya menuntut dilayani. Ketika cinta, perhatian, dan hadiah mengalir secara timbal balik, keharmonisan akan bertahan abadi.",
                "advice": "Perhatikan kebutuhan pasanganmu; jika kamu selama ini lebih banyak menerima, inilah saatnya kamu yang memanjakannya.",
                "reflectionQuestion": "Apakah kamu dan pasangan sudah saling memberi perhatian dan pengorbanan secara berimbang?",
                "keywords": ["Keseimbangan Timbal Balik", "Saling Memperhatikan", "Cinta Berimbang", "Hadiah Kasih"]
            },
            "work": {
                "title": "Mendapatkan Bimbingan, Bonus, atau Kenaikan Gaji yang Layak",
                "summary": "Atasan yang dermawan dan adil memberikan apresiasi materi atas dedikasi kinerjamu.",
                "meaning": "Di lingkungan kerja, Six of Pentacles menandakan datangnya bantuan atau pengakuan: atasan memberikan bonus kinerja, perusahaan menyetujui beasiswa pelatihanmu, atau ada mentor senior yang bersedia meluangkan waktu membimbingmu. Segala kebaikan ini membuka jalan kemajuanmu.",
                "advice": "Terimalah bimbingan dan bantuan dengan rasa terima kasih; tunjukkan bahwa investasi mereka padamu tidak sia-sia.",
                "reflectionQuestion": "Bagaimana kamu memanfaatkan bimbingan atau bonus kerja ini untuk meningkatkan mutu kinerjamu?",
                "keywords": ["Bonus Kinerja", "Atasan Dermawan", "Beasiswa Pelatihan", "Apresiasi Layak"]
            },
            "career": {
                "title": "Mendapatkan Investor atau Menjadi Investor bagi Orang Lain",
                "summary": "Pertemuan antara penyedia modal (investor/sponsor) dengan talenta yang siap mengeksekusi visi.",
                "meaning": "Karier di bawah pengaruh kartu ini membawa kemudahan permodalan. Proposal usahamu menarik minat investor malaikat (angel investor), atau kamu mendapatkan hibah dana ventura untuk mengembangkan bisnismu. Jika kamu berada di posisi atas, inilah saatnya menjadi sponsor bagi talenta muda.",
                "advice": "Pertanggungjawabkan setiap dana yang dipercayakan kepadamu dengan transparansi laporan berkala yang prima.",
                "reflectionQuestion": "Bantuan modal atau jejaring seperti apa yang paling kamu butuhkan untuk melipatgandakan skala kariermu?",
                "keywords": ["Angel Investor", "Hibah Modal", "Sponsor Karier", "Transparansi Dana"]
            },
            "finance": {
                "title": "Kelancaran Rezeki Melalui Sedekah dan Kedermawanan",
                "summary": "Membuktikan hukum semesta: semakin banyak kamu berbagi dengan ikhlas, semakin lancar rezeki yang mengalir kembali.",
                "meaning": "Secara finansial, Six of Pentacles adalah lambang aliran dana yang bersih dan berputar sehat. Timbangan neraca mengingatkan bahwa harta yang dikeluarkan untuk menolong sesama tidak akan pernah berkurang, melainkan dibalas dengan keberkahan yang berlipat ganda dari jalan yang tak terduga.",
                "advice": "Sisihkan sebagian penghasilanmu untuk sedekah rutin; jadikan tanganmu sebagai tangan di atas yang gemar memberi.",
                "reflectionQuestion": "Berapa persentase dari rezekimu yang ingin kamu alokasikan secara khusus untuk membantu mereka yang membutuhkan?",
                "keywords": ["Hukum Sedekah", "Tangan di Atas", "Rezeki Berputar", "Keberkahan Melimpah"]
            },
            "selfGrowth": {
                "title": "Kerendahan Hati Menerima dan Kebahagiaan Memberi",
                "summary": "Mempelajari dua seni hidup agung: tidak gengsi menerima bantuan saat butuh, dan tidak sombong saat mampu memberi.",
                "meaning": "Pengembangan diri kartu Six of Pentacles adalah kebijaksanaan neraca batin. Ada saatnya kita menjadi sang dermawan yang menabur koin, dan ada saatnya kita menjadi sang peminta yang membutuhkan uluran tangan. Menerima bantuan dengan rasa syukur menuntut kerendahan hati yang sama luhurnya dengan memberi derma.",
                "advice": "Terimalah kebaikan orang lain tanpa rasa rendah diri; kelak saat kamu mampu, teruskanlah rantai kebaikan itu kepada orang lain.",
                "reflectionQuestion": "Apakah kamu merasa sulit menerima bantuan orang lain karena terhalang oleh rasa gengsi?",
                "keywords": ["Neraca Batin", "Seni Menerima", "Kebahagiaan Memberi", "Rantai Kebaikan"]
            },
            "relationships": {
                "title": "Kedermawanan Sosial dan Membantu Teman yang Kesulitan",
                "summary": "Mengulurkan tangan membantu sahabat atau kerabat tanpa membuat mereka merasa rendah diri.",
                "meaning": "Dalam pergaulan dan keluarga, kamu memiliki kelebihan rezeki untuk menjadi penolong bagi orang-orang terdekatmu. Berikan bantuan dengan keanggunan dan kehalusan budi pekerti agar harga diri saudaramu tetap terjaga dengan mulia.",
                "advice": "Bantulah saudaramu secara diam-diam; jangan mengungkit-ungkit kebaikanmu di kemudian hari.",
                "reflectionQuestion": "Bagaimana caramu membantu kerabat yang membutuhkan tanpa melukai harga dirinya?",
                "keywords": ["Bantuan Halus", "Menjaga Harga Diri", "Kedermawanan Tulus", "Menolong Diam-diam"]
            },
            "spirituality": {
                "title": "Timbangan Amal dan Sedekah Sebagai Pemadam Murka Ilahi",
                "summary": "Menyadari bahwa sedekah yang tulus memadamkan dosa dan membuka pintu gerbang surga.",
                "meaning": "Secara spiritual, Six of Pentacles adalah neraca amal kebaikan di hadapan Tuhan. Harta hakikimu bukanlah apa yang kamu simpan di brankas duniawi, melainkan apa yang telah kamu dermakan untuk kebaikan sesama. Timbangan neraca ilahi menimbang ketulusan niatmu, bukan sekadar nominal lahiriahnya.",
                "advice": "Bersedekahlah dengan tangan kanan tanpa diketahui tangan kirimu; niatkan semata-mata mencari keridhaan Tuhan.",
                "reflectionQuestion": "Bagaimana sedekah dan kebaikan yang kamu lakukan hari ini dapat menjadi tabungan keselamatan jiwamu kelak?",
                "keywords": ["Timbangan Amal", "Sedekah Sirri", "Harta Hakiki", "Ridho Ilahi"]
            }
        }
    },
    {
        "id": "seven-of-pentacles",
        "name": "Seven of Pentacles",
        "slug": "seven-of-pentacles",
        "image": "/assets/tarot/cards/Seven of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "7",
        "uprightKeywords": ["Kesabaran Menanti Panen", "Evaluasi Investasi", "Kerja Keras Jangka Panjang", "Proses Pematangan", "Keberlanjutan"],
        "reversedKeywords": ["Ketidaksabaran", "Panen Dini", "Investasi Sia-sia", "Kelelahan Tanpa Hasil"],
        "description": "Seorang petani muda bersandar pada cangkulnya menatap tanaman merambat yang lebat berbuah tujuh koin emas (pentacle). Matanya memandang buah-buah itu dengan sabar dan kontemplatif, menyadari bahwa buah tersebut membutuhkan waktu untuk benar-benar matang sebelum dipetik. Seven of Pentacles melambangkan kesabaran menanti hasil panen, evaluasi investasi jangka panjang, dan pemahaman bahwa hal-hal besar membutuhkan waktu untuk bertumbuh.",
        "readings": {
            "love": {
                "title": "Kesabaran Merawat Hubungan dan Menanti Pematangan Cinta",
                "summary": "Menyadari bahwa cinta sejati dibangun perlahan melalui proses saling mengenal dan pengorbanan harian.",
                "meaning": "Seven of Pentacles dalam percintaan mengajarkan hukum waktu alami. Hubungan yang kokoh tidak terjadi dalam semalam. Kalian telah menabur benih cinta dan menyiramnya dengan kesabaran. Sekarang adalah fase pematangan: jangan terburu-buru memaksakan keputusan besar jika situasinya masih memerlukan waktu untuk matang sempurna.",
                "advice": "Bersabarlah menghadapi proses pendewasaan pasangan; evaluasi sejauh mana hubungan kalian telah bertumbuh dengan rasa syukur.",
                "reflectionQuestion": "Pertumbuhan positif apa yang telah kamu saksikan dalam hubunganmu selama setahun terakhir?",
                "keywords": ["Pematangan Cinta", "Kesabaran Asmara", "Proses Alami", "Evaluasi Hubungan"]
            },
            "work": {
                "title": "Evaluasi Berkala Proyek dan Menanti Buah Kerja Keras",
                "summary": "Meninjau kembali kemajuan pekerjaan jangka panjang dan memastikan strategi berada di jalur yang benar.",
                "meaning": "Di lingkungan kerja, Seven of Pentacles adalah jeda evaluasi (mid-term review). Tugas-tugas berat telah kamu laksanakan dan kini saatnya mengamati hasilnya. Jangan tergoda mengubah strategi secara drastis hanya karena hasil instan belum terlihat; biarkan sistem bekerja dan buktikan efektivitasnya.",
                "advice": "Lakukan audit berkala atas pencapaian milestone kerjamu; lakukan penyesuaian kecil tanpa merusak fondasi yang sudah ada.",
                "reflectionQuestion": "Bagian dari proyek kerjamu mana yang saat ini paling membutuhkan ketelatenan dan kesabaran ekstra?",
                "keywords": ["Mid-term Review", "Audit Milestone", "Kesabaran Kerja", "Menanti Hasil"]
            },
            "career": {
                "title": "Investasi Karier Jangka Panjang dan Mengasah Jam Terbang",
                "summary": "Membangun reputasi dan keahlian secara konsisten demi memanen kesuksesan besar di masa depan.",
                "meaning": "Karier di bawah pengaruh kartu ini mengingatkan bahwa tidak ada jalan pintas menuju kemahiran sejati. Kamu sedang berada di fase menumpuk jam terbang dan portofolio. Meskipun kemajuannya terasa bertahap, fondasi yang kamu bangun saat ini akan menghasilkan reputasi yang sangat kokoh dan tak tergoyahkan.",
                "advice": "Fokuslah pada peningkatan kualitas keahlianmu; hasil finansial dan promosi jabatan akan menyusul secara alami pada waktunya.",
                "reflectionQuestion": "Investasi leher ke atas (kursus, sertifikasi, jam terbang) apa yang sedang kamu pupuk demi masa depan kariermu?",
                "keywords": ["Jam Terbang", "Karier Jangka Panjang", "Fondasi Reputasi", "Hasil Alami"]
            },
            "finance": {
                "title": "Investasi Sabar dan Bunga Berbunga (Compound Interest)",
                "summary": "Menanam modal pada instrumen jangka panjang dan membiarkan waktu melipatgandakan nilainya.",
                "meaning": "Secara finansial, Seven of Pentacles adalah filosofi investasi Warren Buffett: kekuatan waktu dan bunga berbunga (compounding effect). Jangan tergoda oleh tren trading harian yang spekulatif. Biarkan dividen dan aset propertimu bertumbuh secara organik; hasil panen di masa depan akan sangat berlimpah.",
                "advice": "Tahan godaan mencairkan investasi sebelum waktunya; biarkan modalmu bekerja melipatgandakan dirinya dalam jangka panjang.",
                "reflectionQuestion": "Apakah portofolio investasimu sudah dirancang untuk pertumbuhan jangka panjang yang berkelanjutan?",
                "keywords": ["Compound Interest", "Investasi Jangka Panjang", "Dividen Melimpah", "Kesabaran Materi"]
            },
            "selfGrowth": {
                "title": "Menghormati Ritme Alami Pertumbuhan Diri",
                "summary": "Berhenti membandingkan kecepatan prosesmu dengan orang lain dan percaya pada musim hidupmu sendiri.",
                "meaning": "Pengembangan diri kartu Seven of Pentacles adalah seni bersabar dengan diri sendiri. Pohon oak raksasa membutuhkan waktu puluhan tahun untuk menjulang tinggi. Kamu telah bekerja keras memperbaiki dirimu; jangan merasa gagal hanya karena perubahan besar belum tampak hari ini. Setiap tetes usahamu sedang bekerja di bawah permukaan tanah.",
                "advice": "Bersikaplah lembut terhadap proses belajarmu; percayalah bahwa setiap usaha baik pasti akan berbuah manis pada waktunya.",
                "reflectionQuestion": "Area pengembangan diri mana yang paling perlu kamu beri waktu dan kesabaran untuk bertumbuh alami?",
                "keywords": ["Ritme Alami", "Bersabar pada Diri", "Proses Bertumbuh", "Pohon Oak Jiwa"]
            },
            "relationships": {
                "title": "Memupuk Hubungan Keluarga dengan Konsistensi Kasih",
                "summary": "Menyadari bahwa mendidik anak dan merawat keharmonisan keluarga menuntut kesabaran bertahun-tahun.",
                "meaning": "Dalam pergaulan dan keluarga, kartu ini mengingatkan bahwa hubungan yang hangat dibangun dari ribuan momen kecil: sarapan bersama, mendengarkan cerita anak, dan saling menolong saat sakit. Hasil panen dari keluarga yang harmonis akan kamu rasakan saat anak-anakmu tumbuh menjadi pribadi yang berbakti dan berbudi luhur.",
                "advice": "Teruslah menanam benih keteladanan yang baik di rumah; kebaikan yang kamu contohkan tidak akan pernah sia-sia.",
                "reflectionQuestion": "Keteladanan apa yang paling konsisten kamu tunjukkan kepada anak-anak atau keluargamu?",
                "keywords": ["Keteladanan Rumah", "Mendidik dengan Sabar", "Momen-momen Kecil", "Panen Budi Pekerti"]
            },
            "spirituality": {
                "title": "Hukum Menabur dan Menuai di Ladang Akhirat",
                "summary": "Menyadari bahwa dunia ini adalah ladang tempat kita menanam amal untuk dipanen di keabadian akhirat.",
                "meaning": "Secara spiritual, Seven of Pentacles mengajarkan hadis kearifan: 'Ad-dunya mazra'at al-akhirah' (Dunia adalah ladang tempat menanam bagi akhirat). Setiap zikir, setiap sedekah, dan setiap kebaikan yang kamu lakukan adalah benih emas yang sedang tumbuh subur di surga. Bersabarlah; panen rayamu telah disiapkan oleh Tuhan.",
                "advice": "Teruslah menabur kebaikan tanpa mengharapkan balasan instan dari manusia; gantungkan harapan panenmu hanya kepada Tuhan.",
                "reflectionQuestion": "Benih amal shaleh apa yang paling ingin kamu perbanyak tanamannya di ladang duniamu hari ini?",
                "keywords": ["Ladang Akhirat", "Menabur dan Menuai", "Panen Surga", "Amal Shalih"]
            }
        }
    },
    {
        "id": "eight-of-pentacles",
        "name": "Eight of Pentacles",
        "slug": "eight-of-pentacles",
        "image": "/assets/tarot/cards/Eight of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "8",
        "uprightKeywords": ["Ketekunan Mahir", "Keahlian Detail", "Disiplin Jam Terbang", "Fokus Total", "Peningkatan Mutu"],
        "reversedKeywords": ["Kerja Ceroboh", "Malas Mengasah Diri", "Jalan Pintas Murahan", "Bosan Berulang"],
        "description": "Seorang pengrajin muda duduk tekun memahat koin emas dengan palu dan pahatnya di sebuah bangku kerja kayu. Enam koin hasil karyanya yang telah selesai tergantung rapi di tiang di sampingnya, satu sedang ia kerjakan di pangkuannya, dan satu koin lagi tergeletak di tanah menunggu gilirannya. Di kejauhan tampak kota kecil. Eight of Pentacles melambangkan disiplin ketekunan, pengasahan keterampilan teknis yang detail, dedikasi pada mutu kesempurnaan, dan jam terbang yang menghasilkan kemahiran sejati.",
        "readings": {
            "love": {
                "title": "Merawat Cinta Melalui Perhatian Sehari-hari",
                "summary": "Menyadari bahwa keharmonisan asmara dijaga melalui ketekunan tindakan kecil yang konsisten setiap hari.",
                "meaning": "Eight of Pentacles dalam percintaan mengajarkan bahwa cinta bukan sekadar puisi romantis sesaat, melainkan komitmen harian yang ditekuni: mendengarkan keluh kesah pasangan, memasakkan makanan kesukaannya, dan saling memaafkan kekhilafan kecil. Ketelatenanmu merawat hubungan ini membuat fondasi cinta kalian sangat kokoh.",
                "advice": "Teruslah memberikan perhatian tulus dalam detail-detail kecil; jadikan kebersamaanmu sebagai karya seni yang indah.",
                "reflectionQuestion": "Perhatian kecil sehari-hari apa yang paling disukai pasanganmu yang bisa kamu lakukan secara konsisten?",
                "keywords": ["Ketelatenan Asmara", "Komitmen Harian", "Tindakan Nyata", "Fondasi Cinta"]
            },
            "work": {
                "title": "Produktivitas Tinggi dan Penguasaan Detail Teknis",
                "summary": "Menyelesaikan pekerjaan dengan mutu tertinggi melalui konsentrasi penuh dan ketelitian prima.",
                "meaning": "Di lingkungan kerja, Eight of Pentacles adalah tanda etos kerja terbaik. Kamu masuk ke dalam zona fokus (deep work) di mana pekerjaan diselesaikan dengan rapi, presisi, dan bebas dari kesalahan ceroboh. Hasil karyamu menjadi standar mutu yang diakui oleh seluruh kantor.",
                "advice": "Matikan segala distraksi saat bekerja; nikmati proses memahat hasil kerjamu hingga mencapai tingkat kesempurnaan teknis.",
                "reflectionQuestion": "Bagian mana dari pekerjaanmu yang jika kamu kerjakan dengan fokus penuh akan menghasilkan mutu mahakarya?",
                "keywords": ["Deep Work", "Ketelitian Teknis", "Standar Mutu", "Etos Kerja Prima"]
            },
            "career": {
                "title": "Mengasah Keterampilan Menuju Tingkat Master",
                "summary": "Dedikasi tinggi mempelajari ilmu baru, mengambil pelatihan intensif, dan menguasai keahlian langka.",
                "meaning": "Karier di bawah pengaruh kartu ini menandakan masa pematangan profesionalisme yang intensif. Kamu bersedia mengulang dan berlatih berkali-kali demi menguasai teknologi atau metodologi terkini. Pasar kerja sangat menghargai para spesialis yang memiliki dedikasi teknis setinggi dirimu.",
                "advice": "Lanjutkan proses belajarmu dengan tekun; investasikan waktu untuk menguasai detail keahlian yang dihindari orang lain.",
                "reflectionQuestion": "Keahlian spesifik apa yang sedang kamu pelajari yang akan membedakanmu sebagai ahli di bidangmu?",
                "keywords": ["Tingkat Master", "Keahlian Langka", "Pelatihan Intensif", "Dedikasi Profesi"]
            },
            "finance": {
                "title": "Rezeki Mengalir Berkat Keringat dan Keahlian",
                "summary": "Pendapatan stabil yang diperoleh dari hasil karya berkualitas tinggi dan jam terbang teruji.",
                "meaning": "Secara finansial, kartu ini melambangkan 'uang halal hasil keringat sendiri'. Penghasilanmu bertumbuh seiring dengan semakin banyaknya pesanan atau proyek yang kamu tuntaskan. Tidak ada spekulasi atau jalan pintas; kekayaanmu dibangun batu demi batu di atas fondasi integritas kerja nyata.",
                "advice": "Pertahankan kualitas hasil kerjamu; reputasi mutu yang prima adalah magnet rezeki paling ampuh dan berkelanjutan.",
                "reflectionQuestion": "Bagaimana kamu bisa meningkatkan efisiensi kerjamu agar mampu menghasilkan lebih banyak karya bermutu tinggi?",
                "keywords": ["Rezeki Halal", "Hasil Keringat", "Reputasi Mutu", "Pendapatan Stabil"]
            },
            "selfGrowth": {
                "title": "Kekuatan Disiplin Harian dan Pembentukan Kebiasaan Baik",
                "summary": "Menyadari bahwa keunggulan bukanlah tindakan sesaat, melainkan kebiasaan yang diulang setiap hari.",
                "meaning": "Pengembangan diri kartu Eight of Pentacles adalah disiplin pembentukan kebiasaan (atomic habits). Seperti sang pengrajin yang memahat koin demi koin, kemajuan dirimu dibentuk dari rutinitas harian: membaca 20 halaman buku, berolahraga 30 menit, dan menulis jurnal refleksi. Perubahan kecil yang konsisten akan menghasilkan lompatan raksasa.",
                "advice": "Patuhi jadwal rutinitas harianmu; jangan biarkan rasa bosan membuatmu berhenti di tengah proses pematangan karakter.",
                "reflectionQuestion": "Kebiasaan baik harian apa yang jika kamu jalankan tanpa putus selama 90 hari akan mengubah kualitas hidupmu?",
                "keywords": ["Atomic Habits", "Disiplin Harian", "Konsistensi Rutinitas", "Keunggulan Karakter"]
            },
            "relationships": {
                "title": "Kesetiaan Melayani dan Membantu Orang Tercinta",
                "summary": "Menunjukkan kasih sayang melalui bantuan praktis sehari-hari bagi keluarga dan sahabat.",
                "meaning": "Dalam pergaulan dan keluarga, kamu adalah sosok yang dapat diandalkan untuk urusan praktis: memperbaiki perabot rumah, mengantar kerabat ke dokter, atau membantu tugas sekolah anak. Tindakan nyata dan kesediaan melayanimu adalah bahasa kasih terindah.",
                "advice": "Teruslah melayani orang-orang tersayang dengan ikhlas; kebaikanmu membawa rasa aman yang mendalam bagi mereka.",
                "reflectionQuestion": "Bantuan praktis apa yang bisa kamu berikan hari ini untuk memudahkan urusan orang tua atau sahabatmu?",
                "keywords": ["Bahasa Kasih Nyata", "Pelayanan Tulus", "Dapat Diandalkan", "Bantuan Praktis"]
            },
            "spirituality": {
                "title": "Zikir dan Amal Khusyuk yang Diulang dengan Penuh Cinta",
                "summary": "Menjadikan rutinitas ibadah harian sebagai sarana memahat hati agar senantiasa bersih dan bercahaya.",
                "meaning": "Secara spiritual, Eight of Pentacles melambangkan amalan yang dicintai Tuhan: amalan yang dilakukan secara berkesinambungan (dawam) meski sederhana. Setiap tarikan napas zikir, setiap rakaat salat, dan setiap butir tasbih adalah pahatan suci yang membersihkan karat-karat kalbumu menuju kesempurnaan iman.",
                "advice": "Jaga rutinitas ibadah harianmu secara istiqomah; jangan remehkan amal kebaikan kecil yang kamu lakukan secara rutin.",
                "reflectionQuestion": "Amalan ibadah rutin apa yang ingin kamu jaga keistiqomahannya sepanjang hayatmu?",
                "keywords": ["Amalan Dawam", "Istiqomah Ibadah", "Memahat Kalbu", "Zikir Berkelanjutan"]
            }
        }
    },
    {
        "id": "nine-of-pentacles",
        "name": "Nine of Pentacles",
        "slug": "nine-of-pentacles",
        "image": "/assets/tarot/cards/Nine of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "9",
        "uprightKeywords": ["Kemandirian Finansial", "Kemewahan Anggun", "Menikmati Hasil Jerih Payah", "Ketenangan Diri", "Kemapanan Sejati"],
        "reversedKeywords": ["Ketergantungan Materi", "Gaya Hidup Pamer", "Kesepian di Puncak", "Kerugian Aset"],
        "description": "Seorang wanita bangsawan bergaun sutra kuning bermotif bunga matahari berdiri anggun di kebun anggurnya yang lebat berbuah sembilan koin emas. Seekor burung falkon bertudung hinggap tenang di tangan kirinya yang bersarung tangan kulit, dan seekor siput kecil merayap perlahan di tanah. Di belakangnya tampak kastel megah miliknya. Nine of Pentacles melambangkan kemandirian finansial mutlak, keanggunan hidup berkelas, kenikmatan hasil jerih payah sendiri, disiplin diri yang matang, dan kedamaian batin.",
        "readings": {
            "love": {
                "title": "Cinta yang Mandiri, Anggun, dan Saling Menghargai",
                "summary": "Dua pribadi mapan yang bersatu atas dasar cinta sejati, bukan karena saling ketergantungan materi.",
                "meaning": "Nine of Pentacles dalam percintaan menandakan hubungan yang sangat elegan dan matang. Kamu merasa utuh dan mandiri secara materi maupun emosi; kamu tidak mencari pasangan untuk 'menyelamatkanmu', melainkan untuk berbagi kebahagiaan yang sudah kamu miliki. Hubungan ini diwarnai rasa saling menghormati dan liburan berkelas bersama.",
                "advice": "Pertahankan kemandirian anggunmu; cintai pasanganmu dengan kebebasan yang memuliakan martabat masing-masing.",
                "reflectionQuestion": "Bagaimana kemandirian pribadimu saat ini membuat kualitas hubungan asmaramu terasa lebih sehat dan membanggakan?",
                "keywords": ["Kemandirian Anggun", "Cinta Mapan", "Bebas Ketergantungan", "Martabat Asmara"]
            },
            "work": {
                "title": "Otonomi Penuh dan Penguasaan Proyek Berkualitas",
                "summary": "Bekerja secara independen dengan kendali penuh atas waktu, standar mutu, dan hasil kerja.",
                "meaning": "Di lingkungan kerja, Nine of Pentacles menandakan bahwa kamu telah mencapai posisi di mana kamu memiliki otonomi kerja yang luas. Kamu dipercaya mengelola proyek secara mandiri tanpa perlu diawasi terus-menerus. Hasil kerjamu selalu memiliki standar estetika dan mutu kelas satu.",
                "advice": "Manfaatkan otonomi kerjamu untuk menghasilkan mahakarya; peliharalah disiplin diri yang tinggi agar kualitas tetap prima.",
                "reflectionQuestion": "Proyek mandiri apa yang saat ini paling memberikan ruang bagi kreativitas dan standarmu yang tinggi?",
                "keywords": ["Otonomi Kerja", "Standar Kelas Satu", "Kepercayaan Penuh", "Kemandirian Eksekusi"]
            },
            "career": {
                "title": "Puncak Kemandirian Karier dan Pemilik Usaha Mapan",
                "summary": "Menikmati kebebasan waktu dan finansial dari bisnis yang berjalan sukses secara autopilot.",
                "meaning": "Karier di bawah pengaruh kartu ini mencerminkan impian setiap profesional: menjadi pemilik bisnis mapan, konsultan independen bergaji tinggi, atau investor yang hidup dari aset produktif. Kamu telah melewati masa-masa kerja keras banting tulang dan kini memetik buah kebebasan sejati.",
                "advice": "Nikmati buah dari perjuangan panjangmu; jadilah inspirasi bagi para profesional muda yang sedang merintis karier.",
                "reflectionQuestion": "Bagaimana kamu memanfaatkan kebebasan waktu dan kariermu untuk menjalani gaya hidup yang bermakna?",
                "keywords": ["Kebebasan Waktu", "Bisnis Autopilot", "Karier Mapan", "Inspirasi Profesional"]
            },
            "finance": {
                "title": "Kemakmuran Mapan, Aset Berlimpah, dan Kenyamanan Berkelas",
                "summary": "Mencapai kemandirian finansial sejati di mana seluruh kebutuhan dan gaya hidup tercukupi dari aset pribadi.",
                "meaning": "Secara finansial, Nine of Pentacles adalah lambang kemandirian finansial (financial freedom). Sembilan koin emas di kebun anggur melambangkan aset-aset produktif yang terus menghasilkan dividen dan keuntungan pasif. Kamu mampu menikmati rumah yang indah, pakaian berkelas, dan makanan terbaik tanpa kecemasan utang.",
                "advice": "Kelola asetmu dengan perlindungan asuransi dan diversifikasi yang aman; nikmati rezekimu dengan penuh rasa syukur.",
                "reflectionQuestion": "Kenyamanan dan keindahan apa yang kini dapat kamu nikmati berkat disiplin finansialmu di masa lalu?",
                "keywords": ["Financial Freedom", "Dividen Pasif", "Aset Berlimpah", "Gaya Hidup Berkelas"]
            },
            "selfGrowth": {
                "title": "Kedamaian Menikmati Kesendirian yang Anggun (Solitude)",
                "summary": "Menemukan kebahagiaan mutlak di dalam diri sendiri dan menikmati keindahan alam serta seni.",
                "meaning": "Pengembangan diri kartu Nine of Pentacles adalah keanggunan jiwa yang mandiri. Burung falkon bertudung melambangkan nafsu liar yang telah dijinakkan oleh disiplin batin. Kamu merasa damai dan bahagia saat menghabiskan waktu sendirian di taman pribadimu, membaca buku, merawat tanaman, dan menikmati secangkir teh dalam hening.",
                "advice": "Luangkan waktu berkualitas untuk menikmati kesendirianmu; hargai dan cintai dirimu sendiri selayaknya bangsawan jiwa.",
                "reflectionQuestion": "Aktivitas berkualitas apa yang paling membuatmu merasa damai dan anggun saat menikmatinya sendirian?",
                "keywords": ["Solitude Anggun", "Nafsu Terjinakkan", "Menghargai Diri", "Kedamaian Batin"]
            },
            "relationships": {
                "title": "Hubungan Sosial yang Elegan, Tenang, dan Bebas Drama",
                "summary": "Memiliki lingkaran sahabat terpilih yang saling menghormati privasi dan mengapresiasi kualitas hidup.",
                "meaning": "Dalam pergaulan dan keluarga, kamu tidak lagi tertarik pada kerumunan bising atau pesta-pesta yang dangkal. Kamu memilih menghabiskan waktu bersama orang-orang terkasih dalam suasana yang tenang, santun, dan penuh kehangatan budi pekerti.",
                "advice": "Undang sahabat-sahabat terdekatmu untuk menikmati jamuan santai di rumahmu; rawatlah persahabatan yang bermartabat.",
                "reflectionQuestion": "Siapa sahabat yang paling sefrekuensi dengan nilai-nilai ketenangan dan keanggunan hidupmu?",
                "keywords": ["Lingkaran Elegan", "Bebas Drama", "Jamuan Santun", "Persahabatan Bermartabat"]
            },
            "spirituality": {
                "title": "Taman Firdaus di Dalam Jiwa yang Bersyukur",
                "summary": "Merasakan keindahan surga duniawi yang dihadiahkan Tuhan bagi jiwa-jiwa yang tekun dan berserah.",
                "meaning": "Secara spiritual, kebun anggur Nine of Pentacles melambangkan kebun makrifat (bustanul 'arifin). Segala benih amal kebajikan yang kamu pupuk dengan kesabaran kini mekar menjadi taman kedamaian di dalam dadamu. Kamu memandang seluruh ciptaan Tuhan dengan rasa kagum dan bersyukur atas nikmat hidup yang tiada tara.",
                "advice": "Jadikan rasa syukur sebagai napas kehidupanmu; pujilah Sang Maha Pemberi Rezeki atas segala keindahan yang mengelilingimu.",
                "reflectionQuestion": "Bagaimana caramu menjadikan setiap kenikmatan materi dan keindahan alam sebagai pengingat akan keagungan Tuhan?",
                "keywords": ["Bustanul Arifin", "Taman Firdaus Kalbu", "Syukur Nikmat", "Keindahan Ilahi"]
            }
        }
    },
    {
        "id": "ten-of-pentacles",
        "name": "Ten of Pentacles",
        "slug": "ten-of-pentacles",
        "image": "/assets/tarot/cards/Ten of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "10",
        "uprightKeywords": ["Warisan Antargenerasi", "Kemakmuran Keluarga Besar", "Kekayaan Abadi", "Stabilitas Tradisi", "Legasi Kokoh"],
        "reversedKeywords": ["Sengketa Warisan", "Kerugian Harta Keluarga", "Runtuhnya Bisnis Keluarga", "Beban Tradisi"],
        "description": "Seorang kakek tua berjubah anggun duduk di halaman gerbang kastel megah mengelus anjing setianya, memandang seorang pria dan wanita muda yang sedang bercakap-cakap sementara seorang anak kecil bermain di samping mereka. Sepuluh koin emas tersusun membentuk Pohon Kehidupan Kabbalistik (Tree of Life) di atas seluruh pemandangan itu. Ten of Pentacles melambangkan kemakmuran keluarga besar lintas generasi, warisan yang melimpah, stabilitas tradisi, dan pencapaian puncak materi yang dinikmati bersama anak cucu.",
        "readings": {
            "love": {
                "title": "Cinta yang Berakar Kuat dan Bahtera Keluarga Mapan",
                "summary": "Membangun dinasti keluarga yang harmonis, didukung restu keluarga besar, dan aman secara finansial.",
                "meaning": "Ten of Pentacles dalam percintaan adalah puncak kemapanan rumah tangga. Hubungan asmaramu bukan hanya tentang dua insan, melainkan penyatuan dua keluarga besar yang saling menghormati dan mendukung. Ada rasa aman yang mendalam bahwa anak cucumu akan bertumbuh dalam lingkungan yang penuh cinta dan kelimpahan materi.",
                "advice": "Rawatlah keharmonisan dengan keluarga besar pasanganmu; bangun tradisi keluarga yang mempererat rasa persaudaraan lintas generasi.",
                "reflectionQuestion": "Tradisi atau nilai keluarga luhur apa yang ingin kamu wariskan bersama pasangan kepada anak cucumu kelak?",
                "keywords": ["Dinasti Keluarga", "Kemapanan Rumah Tangga", "Restu Keluarga Besar", "Pohon Kehidupan"]
            },
            "work": {
                "title": "Perusahaan Mapan dan Sistem Organisasi yang Kokoh",
                "summary": "Bekerja di institusi besar dengan budaya kerja yang stabil, tunjangan jangka panjang, dan masa depan terjamin.",
                "meaning": "Di lingkungan kerja, Ten of Pentacles menandakan kestabilan korporasi tingkat tinggi. Kamu berada dalam organisasi yang memiliki fondasi keuangan sangat kuat, tata kelola yang teruji, dan jenjang karier yang jelas hingga masa pensiun. Sistem kerja berjalan dengan sangat tertib.",
                "advice": "Patuhi dan pelajari sistem organisasi yang telah teruji; berikan kontribusi terbaikmu untuk keberlanjutan institusi jangka panjang.",
                "reflectionQuestion": "Bagaimana caramu berkontribusi pada stabilitas dan keberlanjutan sistem di tempat kerjamu?",
                "keywords": ["Institusi Mapan", "Tata Kelola Teruji", "Jaminan Pensiun", "Keberlanjutan Organisasi"]
            },
            "career": {
                "title": "Membangun Bisnis Keluarga dan Legasi Profesional Abadi",
                "summary": "Mencapai puncak prestasi karier yang dapat diwariskan kepada generasi penerus.",
                "meaning": "Karier di bawah pengaruh kartu ini adalah tentang menciptakan 'legacy' (warisan abadi). Bisnis yang kamu rintis telah bertransformasi menjadi perusahaan keluarga yang mapan, atau reputasi profesionalmu menjadi mercusuar yang membanggakan bagi seluruh keturunanmu. Karya hidupmu abadi melampaui usiamu.",
                "advice": "Siapkan rencana suksesi kepemimpinan; didiklah generasi muda agar siap meneruskan tongkat estafet kariermu.",
                "reflectionQuestion": "Legasi profesional apa yang ingin kamu tinggalkan yang akan terus memberi manfaat bagi generasi setelahmu?",
                "keywords": ["Legasi Abadi", "Bisnis Keluarga", "Rencana Suksesi", "Warisan Prestasi"]
            },
            "finance": {
                "title": "Kekayaan Antargenerasi (Generational Wealth) dan Aset Warisan",
                "summary": "Mencapai kemakmuran materi tingkat tertinggi yang menjamin kesejahteraan keluarga hingga anak cucu.",
                "meaning": "Secara finansial, Ten of Pentacles adalah lambang 'generational wealth'. Sepuluh koin yang membentuk Pohon Kehidupan menandakan bahwa portofolio asetmu (properti, saham, trust fund) telah tertata sedemikian rupa sehingga mampu menopang kesejahteraan seluruh keturunanmu dengan aman dan bebas dari sengketa.",
                "advice": "Susun perencanaan warisan dan wasiat secara hukum yang sah dan adil; pastikan seluruh aset terlindungi dari sengketa keluarga.",
                "reflectionQuestion": "Langkah apa yang perlu kamu siapkan untuk membangun dan mengamankan kekayaan antargenerasi bagi keluargamu?",
                "keywords": ["Generational Wealth", "Aset Warisan", "Trust Fund", "Keamanan Finansial Abadi"]
            },
            "selfGrowth": {
                "title": "Kebijaksanaan Sesepuh: Melihat Pohon Kehidupan Seutuhnya",
                "summary": "Menyadari bahwa hidupmu adalah bagian dari rantai panjang sejarah leluhur dan masa depan.",
                "meaning": "Pengembangan diri kartu Ten of Pentacles adalah kesadaran kosmologis. Kakek tua yang tenang memandang anak cucunya adalah cerminan jiwa yang telah menyelesaikan tugas duniawinya dengan gemilang. Kamu menyadari bahwa kamu adalah penerus estafet para leluhurmu dan pembuka jalan bagi generasi mendatang. Hidupmu bermakna dan penuh kehormatan.",
                "advice": "Hormati asal-usul dan akar keluargamu; jadilah jembatan emas yang menghubungkan kearifan masa lalu dengan harapan masa depan.",
                "reflectionQuestion": "Bagaimana caramu menghormati perjuangan orang tua dan leluhurmu dalam setiap langkah hidupmu hari ini?",
                "keywords": ["Rantai Sejarah", "Kearifan Leluhur", "Jembatan Emas", "Kehormatan Hidup"]
            },
            "relationships": {
                "title": "Reuni Akbar Keluarga Besar dan Kehangatan Tiga Generasi",
                "summary": "Momen kumpul keluarga besar yang dipenuhi kebanggaan, rasa syukur, dan kebahagiaan antargenerasi.",
                "meaning": "Dalam pergaulan dan keluarga, Ten of Pentacles adalah pesta keluarga besar (tiga generasi berkumpul bersama). Kakek-nenek, orang tua, dan anak-anak bercengkerama dalam damai. Hubungan kekeluargaan sangat rukun, saling menopang, dan menjadi benteng perlindungan terkuat bagi setiap anggotanya.",
                "advice": "Jaga kerukunan antarsanak saudara; jadikan musyawarah keluarga sebagai sarana menyelesaikan segala urusan dengan damai.",
                "reflectionQuestion": "Bagaimana caramu menjaga tali silaturahmi agar seluruh sanak saudara tetap rukun dan saling peduli?",
                "keywords": ["Tiga Generasi", "Kerukunan Keluarga", "Silaturahmi Akbar", "Benteng Persaudaraan"]
            },
            "spirituality": {
                "title": "Pohon Kehidupan Ilahi (Tree of Life) dan Keberkahan Turun-temurun",
                "summary": "Menyadari bahwa amal jariyah dan doa anak shaleh adalah bekal keabadian yang tak pernah terputus.",
                "meaning": "Secara spiritual, sepuluh koin yang membentuk Tree of Life (Pohon Kehidupan) melambangkan sepuluh sefirot emanasi ilahi yang menerangi alam semesta. Amalan yang kamu lakukan—terutama mendidik anak menjadi pribadi shaleh dan membangun wakaf produktif—akan menjadi amal jariyah yang pahalanya terus mengalir kepadamu di alam kubur.",
                "advice": "Tinggalkan amal jariyah dan wakaf yang terus mengalirkan manfaat; doakan kebaikan bagi keturunanmu hingga akhir zaman.",
                "reflectionQuestion": "Amal jariyah apa yang ingin kamu bangun hari ini yang pahalanya akan terus mengalir bahkan setelah kamu tiada?",
                "keywords": ["Amal Jariyah", "Pohon Kehidupan", "Doa Anak Shaleh", "Wakaf Produktif"]
            }
        }
    },
    {
        "id": "page-of-pentacles",
        "name": "Page of Pentacles",
        "slug": "page-of-pentacles",
        "image": "/assets/tarot/cards/Page of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "Page",
        "uprightKeywords": ["Semangat Belajar", "Rencana Finansial Baru", "Ketelitian Tekun", "Peluang Beasiswa", "Menanam Benih Sukses"],
        "reversedKeywords": ["Malas Belajar", "Kurang Disiplin", "Boros Uang Saku", "Rencana Tanpa Komitmen"],
        "description": "Seorang pemuda berbusana hijau berdiri di padang rumput subur dengan latar belakang pepohonan dan ladang yang baru dibajak. Ia menatap dengan penuh takjub dan konsentrasi pada koin emas tunggal yang melayang seimbang di atas kedua telapak tangannya. Page of Pentacles melambangkan mahasiswa tekun, bibit kemakmuran baru, semangat belajar ilmu praktis, dan komitmen menanam benih kesuksesan jangka panjang.",
        "readings": {
            "love": {
                "title": "Cinta yang Tulus, Realistis, dan Berkomitmen Belajar Bersama",
                "summary": "Hubungan asmara yang dilandasi niat baik untuk saling mendukung studi dan membangun masa depan bersama.",
                "meaning": "Page of Pentacles membawa ketenangan dan keseriusan dalam cinta muda. Kalian mungkin baru memulai hubungan atau sedang merintis karier dari nol bersama, namun ada komitmen nyata untuk saling setia dan saling menyemangati. Hubungan ini membumi, bebas dari drama, dan menghargai kepastian langkah nyata.",
                "advice": "Tunjukkan keseriusanmu melalui tindakan nyata; dukunglah impian pendidikan atau karier pasanganmu dengan sabar.",
                "reflectionQuestion": "Langkah konkret apa yang bisa kalian rencanakan berdua untuk mempersiapkan masa depan hubungan?",
                "keywords": ["Komitmen Nyata", "Cinta Membumi", "Belajar Bersama", "Saling Mendukung"]
            },
            "work": {
                "title": "Etos Belajar Tinggi dan Tugas yang Dikerjakan dengan Rapi",
                "summary": "Menyerap instruksi kerja dengan cepat dan menunjukkan ketelitian tinggi dalam tugas harian.",
                "meaning": "Di lingkungan kerja, Page of Pentacles adalah sosok karyawan baru atau pemagang teladan. Kamu sangat teliti dalam mencatat instruksi atasan, memeriksa data sebelum diserahkan, dan antusias mempelajari prosedur teknis baru. Sikap rajinmu membuat atasan sangat terkesan.",
                "advice": "Jadilah pembelajar yang tekun; jangan ragu mencatat setiap detail penting dan pelajari sistem kerja secara menyeluruh.",
                "reflectionQuestion": "Prosedur atau keterampilan kerja baru apa yang saat ini paling ingin kamu kuasai dengan sempurna?",
                "keywords": ["Karyawan Teladan", "Ketelitian Data", "Catatan Rapi", "Antusiasme Belajar"]
            },
            "career": {
                "title": "Peluang Beasiswa, Pelatihan Kerja, dan Awal Karier Mapan",
                "summary": "Mendapatkan kesempatan magang bergengsi, beasiswa studi, atau sertifikasi profesi pertama.",
                "meaning": "Karier di bawah pengaruh kartu ini menandakan masa penanaman benih profesional. Kamu mungkin menerima beasiswa lanjutan, tawaran management trainee (MT), atau memulai proyek wirausaha pertamamu. Peluang ini akan menjadi fondasi emas bagi kesuksesan jangka panjangmu.",
                "advice": "Manfaatkan kesempatan belajar ini sebaik-baiknya; bangun rekam jejak yang disiplin dan profesional sejak awal.",
                "reflectionQuestion": "Program pelatihan atau sertifikasi apa yang saat ini paling krusial untuk membuka gerbang kariermu?",
                "keywords": ["Beasiswa Prestasi", "Management Trainee", "Penanaman Benih", "Fondasi Emas"]
            },
            "finance": {
                "title": "Memulai Rencana Menabung dan Literasi Keuangan",
                "summary": "Membuka rekening tabungan baru, belajar investasi pemula, dan mengatur anggaran saku dengan tertib.",
                "meaning": "Secara finansial, Page of Pentacles adalah langkah pertama menuju kecerdasan finansial. Kamu mulai membaca buku tentang pengelolaan uang, membuka rekening reksadana pertama, atau menyisihkan uang saku harian dengan disiplin. Disiplin kecil ini akan mengubah nasib keuanganmu kelak.",
                "advice": "Mulailah menabung secara konsisten meski nominalnya kecil; pelajari instrumen investasi yang aman bagi pemula.",
                "reflectionQuestion": "Kebiasaan menabung kecil apa yang siap kamu mulai secara disiplin mulai hari ini?",
                "keywords": ["Literasi Keuangan", "Tabungan Pertama", "Investasi Pemula", "Disiplin Uang Saku"]
            },
            "selfGrowth": {
                "title": "Dedikasi Menuntut Ilmu dan Membangun Karakter Tangguh",
                "summary": "Menghargai proses belajar bertahap dan memfokuskan pikiran pada peningkatan kompetensi diri.",
                "meaning": "Pengembangan diri kartu Page of Pentacles adalah komitmen menjadi pembelajar seumur hidup (lifelong learner). Menatap koin emas di tangan melambangkan konsentrasi penuh pada apa yang sedang dipelajari. Kamu tidak terburu-buru mengejar hasil instan; kamu menikmati proses menyerap ilmu dan melatih diri.",
                "advice": "Dedikasikan satu jam setiap hari untuk membaca buku atau melatih keahlian baru; peliharalah ketekunan belajarmu.",
                "reflectionQuestion": "Ilmu atau buku berbobot apa yang saat ini sedang kamu pelajari untuk memperkaya wawasanmu?",
                "keywords": ["Lifelong Learner", "Konsentrasi Belajar", "Pembelajar Tekun", "Peningkatan Kompetensi"]
            },
            "relationships": {
                "title": "Sahabat yang Dapat Diandalkan dan Setia Berbagi Ilmu",
                "summary": "Membentuk kelompok belajar bersama teman-teman yang memiliki ambisi positif untuk sukses.",
                "meaning": "Dalam pergaulan dan keluarga, kamu adalah teman yang rajin dan tidak pelit berbagi catatan pelajaran atau informasi beasiswa. Kamu dikelilingi oleh teman-teman yang saling memotivasi untuk berprestasi dan saling mengingatkan dalam kebaikan.",
                "advice": "Bentuklah kelompok belajar atau diskusi yang suportif; saling bantu teman yang sedang kesulitan memahami materi.",
                "reflectionQuestion": "Siapa teman belajarmu yang selalu membuatmu termotivasi untuk terus berprestasi?",
                "keywords": ["Kelompok Belajar", "Berbagi Catatan", "Motivasi Positif", "Sahabat Rajin"]
            },
            "spirituality": {
                "title": "Menuntut Ilmu Sebagai Kewajiban Suci Ibadah",
                "summary": "Menyadari bahwa menuntut ilmu yang bermanfaat adalah jalan termudah menuju surga Tuhan.",
                "meaning": "Secara spiritual, Page of Pentacles melambangkan thalabul 'ilmi (kewajiban menuntut ilmu). Koin emas di tangannya adalah mutiara hikmah yang diturunkan Tuhan ke bumi. Setiap langkah kakimu menuju majelis ilmu atau meja belajar dicatat sebagai langkah ibadah yang dimuliakan oleh para malaikat.",
                "advice": "Luruskan niat menuntut ilmumu semata-mata mencari ridho Tuhan dan memberi manfaat bagi umat manusia.",
                "reflectionQuestion": "Bagaimana caramu mengamalkan ilmu yang kamu peroleh agar menjadi berkah bagi orang banyak?",
                "keywords": ["Thalabul Ilmi", "Mutiara Hikmah", "Ibadah Belajar", "Ilmu Bermanfaat"]
            }
        }
    },
    {
        "id": "knight-of-pentacles",
        "name": "Knight of Pentacles",
        "slug": "knight-of-pentacles",
        "image": "/assets/tarot/cards/Knight of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "Knight",
        "uprightKeywords": ["Kerja Keras Tak Kenal Lelah", "Keandalan Mutlak", "Ketekunan Sabar", "Tanggung Jawab Setia", "Hasil Terjamin"],
        "reversedKeywords": ["Keras Kepala Kaku", "Bosan Monoton", "Terlalu Lambat", "Perfeksionisme Melelahkan"],
        "description": "Seorang ksatria berbaju zirah kokoh menunggang kuda perang hitam berbadan besar yang berdiri tenang dan kokoh di tengah ladang gandum yang baru dibajak. Di tangannya, ksatria memegang koin emas dengan tatapan penuh tanggung jawab dan kesetiaan. Knight of Pentacles melambangkan ksatria paling tekun dan dapat diandalkan: tidak terburu-buru, bekerja keras tanpa mengeluh, menepati setiap janji, dan menjamin keberhasilan melalui konsistensi baja.",
        "readings": {
            "love": {
                "title": "Kesetiaan Kokoh, Tanggung Jawab Nyata, dan Perlindungan Asmara",
                "summary": "Pasangan yang sangat dapat diandalkan, setia tanpa ragu, dan membuktikan cinta lewat kerja keras harian.",
                "meaning": "Knight of Pentacles dalam percintaan adalah lambang pasangan yang paling setia dan dapat dipercaya seumur hidup. Ia mungkin bukan tipe yang suka mengobral kata-kata manis gombal, namun ia selalu ada saat kamu butuh bantuan, menepati setiap janjinya, dan bekerja keras memastikan keluarganya hidup nyaman dan berkecukupan.",
                "advice": "Hargai kesetiaan dan kerja keras pasanganmu; tunjukkan rasa terima kasih atas segala pengorbanan nyatanya.",
                "reflectionQuestion": "Bagaimana tindakan nyata dan konsistensi pasanganmu memberikan rasa aman yang tak ternilai bagi hatimu?",
                "keywords": ["Kesetiaan Kokoh", "Dapat Diandalkan", "Tindakan Nyata", "Rasa Aman Asmara"]
            },
            "work": {
                "title": "Etos Kerja Luar Biasa dan Eksekusi Proyek yang Sempurna",
                "summary": "Menyelesaikan seluruh tanggung jawab kerja dengan ketelitian tinggi dan ketepatan waktu tanpa cela.",
                "meaning": "Di lingkungan kerja, Knight of Pentacles adalah tulang punggung organisasi. Ketika tugas diberikan kepadamu, atasan tidak perlu khawatir lagi karena mereka tahu kamu akan mengerjakannya hingga tuntas dengan standar mutu terbaik. Kamu tidak pernah mengeluh atau mencari alasan.",
                "advice": "Pertahankan reputasi keandalanmu; jadilah sosok yang selalu menepati tenggat waktu dan menjaga mutu kerja.",
                "reflectionQuestion": "Tanggung jawab kerja apa yang saat ini paling mengandalkan konsistensi dan ketekunanmu?",
                "keywords": ["Tulang Punggung Tim", "Tepat Waktu", "Standar Terbaik", "Keandalan Mutlak"]
            },
            "career": {
                "title": "Kenaikan Karier yang Pasti Melalui Konsistensi Teruji",
                "summary": "Membangun reputasi profesional yang solid selangkah demi selangkah hingga mencapai posisi kunci.",
                "meaning": "Karier di bawah pengaruh kartu ini bergerak seperti kereta api berat yang tak terhentikan. Kamu mungkin tidak melompat secara instan, namun setiap langkahmu menancap kokoh di tanah. Manajemen perusahaan tahu bahwa kamu adalah orang yang paling layak dipromosikan ketika membutuhkan stabilitas.",
                "advice": "Tetaplah konsisten pada jalurmu; reputasi sebagai profesional yang dapat diandalkan adalah kunci kenaikan kariermu.",
                "reflectionQuestion": "Langkah konsisten apa yang perlu kamu jalankan setiap hari untuk memastikan tercapainya target kariermu?",
                "keywords": ["Konsistensi Teruji", "Karier Pasti", "Promosi Layak", "Reputasi Solid"]
            },
            "finance": {
                "title": "Akumulasi Kekayaan yang Disiplin dan Investasi Aman",
                "summary": "Menabung secara rutin setiap bulan dan mengalokasikan dana pada instrumen berisiko rendah yang pasti untung.",
                "meaning": "Secara finansial, Knight of Pentacles adalah disiplin anggaran baja. Kamu menyisihkan 20–30% dari penghasilanmu setiap gajian tanpa kompromi. Investasimu di sektor emas, deposito, atau reksadana obligasi terus bertambah secara teratur. Dalam beberapa tahun, tabunganmu akan menjadi benteng kekayaan yang kokoh.",
                "advice": "Pertahankan sistem autodebet tabunganmu; jangan tergoda mencairkan dana sebelum target waktu yang kamu tetapkan.",
                "reflectionQuestion": "Berapa target nominal tabungan atau aset yang ingin kamu kumpulkan dalam tiga tahun ke depan?",
                "keywords": ["Disiplin Anggaran", "Autodebet Rutin", "Investasi Aman", "Akumulasi Kekayaan"]
            },
            "selfGrowth": {
                "title": "Kekuatan Ketekunan: Mengalahkan Bakat Melalui Kerja Keras",
                "summary": "Menyadari bahwa konsistensi dan ketekunan harian jauh lebih unggul daripada bakat yang malas.",
                "meaning": "Pengembangan diri kartu Knight of Pentacles adalah pepatah kearifan: 'Hard work beats talent when talent fails to work hard.' Kamu mungkin merasa bukan orang paling jenius di ruangan, namun tekadmu untuk bangun pagi, bekerja keras, dan tidak pernah menyerah membuatmu melampaui mereka yang hanya mengandalkan bakat alami.",
                "advice": "Tetaplah rendah hati dan tekun; berbanggalah atas etos kerja dan daya tahan mentalmu yang luar biasa.",
                "reflectionQuestion": "Bagaimana ketekunan dan kerja kerasmu selama ini telah membuktikan keberhasilan yang melampaui ekspektasi orang lain?",
                "keywords": ["Kerja Keras Kalahkan Bakat", "Daya Tahan Mental", "Ketekunan Harian", "Konsistensi Baja"]
            },
            "relationships": {
                "title": "Sahabat yang Selalu Menepati Janji dan Siap Membantu",
                "summary": "Menjadi pilar keandalan di lingkaran pertemanan dan keluarga yang kata-katanya selalu dapat dipegang.",
                "meaning": "Dalam pergaulan dan keluarga, kamu dikenal sebagai orang yang 'sekali berjanji, pantang ingkar'. Jika kamu berkata akan datang membantu pindahan rumah atau menjemput di bandara, orang lain tahu kamu pasti datang tepat waktu. Integritasmu membuatmu sangat dicintai dan dihormati.",
                "advice": "Teruslah menjaga integritas janjimu; jadilah sahabat yang senantiasa membawa rasa aman bagi orang lain.",
                "reflectionQuestion": "Janji apa yang telah kamu buat kepada keluarga yang saat ini sedang kamu penuhi dengan sungguh-sungguh?",
                "keywords": ["Menepati Janji", "Integritas Kata", "Sahabat Andalan", "Rasa Aman Sosial"]
            },
            "spirituality": {
                "title": "Ibadah yang Berkelanjutan: Amalan yang Paling Dicintai Tuhan",
                "summary": "Menghayati ajaran bahwa amal yang paling mulia adalah amal yang rutin dikerjakan meski sedikit.",
                "meaning": "Secara spiritual, ksatria di atas kuda hitam yang kokoh melambangkan keistiqomahan ibadah. Nabi bersabda: 'Amalan yang paling dicintai oleh Allah adalah amalan yang berkelanjutan (adwamuhu) meskipun sedikit.' Salat tepat waktu, sedekah subuh rutin, dan zikir harianmu adalah persembahan yang sangat dicintai oleh Tuhan.",
                "advice": "Pertahankan kebiasaan ibadah harianmu tanpa putus; jadikan istiqomah sebagai mahkota spiritualmu.",
                "reflectionQuestion": "Amalan kecil apa yang telah menjadi rutinitas harianmu yang membawa ketenangan bagi jiwamu?",
                "keywords": ["Istiqomah Sejati", "Amalan Berkelanjutan", "Dicintai Tuhan", "Keteguhan Ruhani"]
            }
        }
    },
    {
        "id": "queen-of-pentacles",
        "name": "Queen of Pentacles",
        "slug": "queen-of-pentacles",
        "image": "/assets/tarot/cards/Queen of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "Queen",
        "uprightKeywords": ["Pengasuhan Hangat", "Kecukupan Praktis", "Kemakmuran Rumah Tangga", "Cinta Alam", "Kedermawanan Membumi"],
        "reversedKeywords": ["Kecemasan Finansial", "Mengabaikan Diri Sendiri", "Ketergantungan Materi", "Terlalu Protektif"],
        "description": "Seorang ratu anggun duduk di atas takhta batu berukir bidadari, buah pir, dan binatang hutan di tengah padang rumput bertabur bunga liar merah. Ia memangku satu koin emas besar di pangkuannya dengan tatapan penuh kasih sayang dan perawatan. Di depannya seekor kelinci melompat ceria. Queen of Pentacles melambangkan permaisuri bumi yang pengasih, pengelola rumah tangga yang makmur dan hangat, keseimbangan antara karier dan keluarga, serta kemurahan hati yang membumi.",
        "readings": {
            "love": {
                "title": "Cinta yang Mengasuh, Hangat, dan Nyaman Seperti Rumah",
                "summary": "Hubungan asmara yang dilandasi kenyamanan lahir batin: masakan lezat, pelukan hangat, dan masa depan yang aman.",
                "meaning": "Queen of Pentacles dalam percintaan adalah figur pasangan yang paling meneduhkan dan penuh perhatian. Kamu atau pasangan mampu menciptakan rumah tangga yang nyaman, rapi, dan penuh kehangatan. Hubungan ini saling merawat kesehatan fisik dan emosional, memastikan kebutuhan bersama terpenuhi dengan limpahan kasih.",
                "advice": "Tunjukkan kasih sayangmu lewat sentuhan perawatan nyata: siapkan hidangan hangat, pijatan lembut, dan ciptakan suasana rumah yang menenangkan.",
                "reflectionQuestion": "Bagaimana caramu membuat pasanganmu merasa begitu dimanja, dirawat, dan disayangi dalam keseharian?",
                "keywords": ["Pengasuhan Hangat", "Kenyamanan Rumah", "Merawat Pasangan", "Cinta Membumi"]
            },
            "work": {
                "title": "Manajemen Sumber Daya yang Efisien dan Merawat Tim",
                "summary": "Mengelola anggaran kerja dan logistik proyek dengan sangat cermat sembari memelihara kesejahteraan tim.",
                "meaning": "Di lingkungan kerja, Queen of Pentacles adalah manajer operasional yang luar biasa. Kamu mampu menekan pemborosan anggaran tanpa mengurangi kualitas hasil kerja, sekaligus memastikan anggota tim merasa nyaman dan tidak kelelahan. Kantor terasa seperti rumah kedua yang menyenangkan.",
                "advice": "Perhatikan kesejahteraan dan beban kerja rekan timmu; efisiensi sejati tercapai saat manusia di dalamnya merasa bahagia.",
                "reflectionQuestion": "Langkah praktis apa yang dapat kamu ambil untuk meningkatkan kenyamanan dan efisiensi lingkungan kerjamu?",
                "keywords": ["Manajer Operasional", "Efisiensi Anggaran", "Kesejahteraan Karyawan", "Suasana Menyenangkan"]
            },
            "career": {
                "title": "Karier Mapan yang Selaras dengan Nilai Keberlanjutan",
                "summary": "Meraih kesuksesan di bidang kuliner, properti, kesehatan, lingkungan hidup, atau bisnis ramah keluarga.",
                "meaning": "Karier di bawah pengaruh kartu ini berkembang subur di sektor-sektor yang memberi makan raga dan jiwa: agribisnis, desain interior, nutrisi, perhotelan, atau kewirausahaan sosial. Reputasimu dikenal karena produkmu berkualitas tinggi, higienis, dan membawa kebaikan bagi konsumen.",
                "advice": "Rancang bisnismu dengan prinsip keberlanjutan (sustainability); kesuksesan jangka panjang lahir dari pelayanan yang tulus.",
                "reflectionQuestion": "Produk atau layanan apa yang ingin kamu kembangkan yang dapat meningkatkan kualitas hidup banyak orang?",
                "keywords": ["Bisnis Berkelanjutan", "Kuliner dan Properti", "Produk Berkualitas", "Pelayanan Tulus"]
            },
            "finance": {
                "title": "Kemakmuran Finansial dan Pengelolaan Aset yang Cerdas",
                "summary": "Keuangan keluarga yang sangat sehat, mampu berhemat cerdas tanpa mengorbankan kualitas hidup.",
                "meaning": "Secara finansial, Queen of Pentacles adalah ahli mengelola anggaran rumah tangga. Kamu tahu persis di mana harus berhemat dan di mana harus berinvestasi pada kualitas. Uangmu mengalir untuk hal-hal yang bernilai tinggi: makanan bergizi, pendidikan anak, dan perbaikan kenyamanan rumah.",
                "advice": "Kelola asetmu dengan keseimbangan yang sehat antara menabung dan menikmati hidup; pastikan keluargamu hidup dalam kecukupan.",
                "reflectionQuestion": "Bagaimana caramu mengalokasikan keuangan keluarga agar tetap hemat namun tetap menikmati kualitas hidup terbaik?",
                "keywords": ["Pengelolaan Cerdas", "Kecukupan Rumah", "Hemat Berkualitas", "Keuangan Sehat"]
            },
            "selfGrowth": {
                "title": "Mencintai Tubuh Fisik dan Terhubung dengan Bumi",
                "summary": "Mempraktikkan perawatan diri lahir batin melalui nutrisi baik, berkebun, dan relaksasi alam.",
                "meaning": "Pengembangan diri kartu Queen of Pentacles adalah seni memanjakan diri sendiri (self-nourishment). Kelinci di kartu melambangkan kesuburan dan vitalitas hidup. Berhentilah mengorbankan waktu istirahat dan makanmu demi pekerjaan. Rawatlah tubuhmu dengan makanan sehat, berjalan di atas rumput hijau, dan rasakan denyut kehidupan bumi yang menenangkan.",
                "advice": "Masaklah makanan sehat untuk dirimu sendiri hari ini; luangkan waktu di taman atau di alam terbuka untuk membumikan energimu.",
                "reflectionQuestion": "Kapan terakhir kali kamu benar-benar merawat tubuhmu dengan makanan bernutrisi dan istirahat yang cukup?",
                "keywords": ["Self-Nourishment", "Koneksi Bumi", "Kesehatan Tubuh", "Relaksasi Alami"]
            },
            "relationships": {
                "title": "Ibu Rumah Tangga yang Menyatukan Seluruh Keluarga",
                "summary": "Menjadi pusat kehangatan keluarga besar tempat semua orang berkumpul untuk makan bersama dan bercerita.",
                "meaning": "Dalam pergaulan dan keluarga, kamu adalah sosok yang selalu memastikan semua orang kenyang dan merasa nyaman. Rumahmu selalu harum oleh aroma masakan lezat dan pintu rumahmu selalu terbuka bagi siapa pun yang membutuhkan tempat istirahat.",
                "advice": "Adakan jamuan makan keluarga santai di rumahmu; kehangatan hidangan yang dimasak dengan cinta akan mempererat silaturahmi.",
                "reflectionQuestion": "Menu masakan atau jamuan apa yang ingin kamu siapkan untuk membahagiakan keluargamu akhir pekan ini?",
                "keywords": ["Pusat Kehangatan", "Jamuan Lezat", "Rumah Terbuka", "Merawat Keluarga"]
            },
            "spirituality": {
                "title": "Ibu Pertiwi dan Bersyukur Atas Rahmat Rezeki Bumi",
                "summary": "Menyadari bahwa setiap butir beras dan tetes air adalah mukjizat kasih sayang Tuhan bagi makhluk-Nya.",
                "meaning": "Secara spiritual, Queen of Pentacles mengajarkan rasa syukur mendalam atas rezeki materi yang terhampar di bumi. Setiap suapan makanan yang kamu makan, pakaian yang kamu kenakan, dan atap yang menaungimu adalah bukti pemeliharaan Tuhan Yang Maha Pemberi Rezeki (Ar-Razzaq).",
                "advice": "Makanlah dengan penuh kesadaran dan doa syukur; rawatlah alam dan lingkungan sekitarmu sebagai bentuk syukur kepada Sang Pencipta.",
                "reflectionQuestion": "Bagaimana rasa syukur atas makanan dan kenyamanan hidup membuat hatimu senantiasa mengingat kemurahan Tuhan?",
                "keywords": ["Ar-Razzaq", "Mukjizat Rezeki", "Syukur Bumi", "Menjaga Alam"]
            }
        }
    },
    {
        "id": "king-of-pentacles",
        "name": "King of Pentacles",
        "slug": "king-of-pentacles",
        "image": "/assets/tarot/cards/King of Pentacles.jpg",
        "arcana": "minor",
        "suit": "pentacles",
        "rank": "King",
        "uprightKeywords": ["Puncak Kemakmuran", "Sentuhan Emas Midas", "Kestabilan Bisnis", "Kepemimpinan Materi", "Kemurahan Hati Mapan"],
        "reversedKeywords": ["Keserakahan Harta", "Materialistis Buta", "Kebangkrutan Bisnis", "Kikir dan Sombong"],
        "description": "Seorang raja agung duduk di takhta batu berukir kepala banteng dan buah anggur di tengah taman bunga mekar di luar kastelnya. Jubahnya dihiasi sulaman buah anggur ungu lebat, tangan kanannya memegang tongkat kerajaan dan tangan kirinya menopang koin emas besar di atas lututnya. Kakinya berbaju zirah menginjak kepala binatang buas bertanduk. King of Pentacles melambangkan penguasaan tertinggi atas elemen bumi: sentuhan emas Midas (apapun yang disentuh menjadi berhasil), kemakmuran materi puncak, kestabilan bisnis, dan kepemimpinan finansial yang dermawan.",
        "readings": {
            "love": {
                "title": "Cinta yang Mapan, Melindungi, dan Menyediakan Segala Kebutuhan",
                "summary": "Hubungan asmara yang dilandasi kepastian materi, keamanan jangka panjang, dan kesetiaan mutlak.",
                "meaning": "King of Pentacles dalam percintaan adalah figur pasangan idaman yang telah mencapai puncak kemapanan hidup. Ia adalah pelindung dan penyedia utama (provider) yang memastikan pasangannya hidup dalam kenyamanan, kemuliaan, dan rasa aman lahir batin. Hubungan ini stabil selayaknya gunung karang.",
                "advice": "Tunjukkan cintamu melalui penyediaan dan perlindungan nyata; bimbing keluargamu menuju stabilitas masa depan yang terjamin.",
                "reflectionQuestion": "Bagaimana kemapanan materi yang kamu miliki dapat kamu gunakan untuk membahagiakan pasangan dan anak-anakmu?",
                "keywords": ["Penyedia Utama", "Provider Hebat", "Kemapanan Asmara", "Keamanan Finansial"]
            },
            "work": {
                "title": "Keberhasilan Bisnis, Manajemen Aset, dan Kepemimpinan Komersial",
                "summary": "Memimpin divisi komersial atau perusahaan dengan kejelian bisnis yang menghasilkan keuntungan masif.",
                "meaning": "Di lingkungan kerja, kamu adalah sosok bertangan dingin dalam urusan finansial. Setiap proyek yang kamu pimpin menghasilkan profit yang tinggi dan efisiensi biaya yang luar biasa. Manajemen puncak mempercayaimu untuk mengelola portofolio anggaran terbesar.",
                "advice": "Pimpinlah dengan integritas komersial yang tinggi; pastikan setiap keputusan bisnismu memberi keuntungan bagi seluruh pemangku kepentingan.",
                "reflectionQuestion": "Strategi bisnis apa yang siap kamu terapkan untuk melipatgandakan keuntungan dan efisiensi perusahaanmu?",
                "keywords": ["Sentuhan Midas", "Keuntungan Masif", "Manajemen Portofolio", "Integritas Bisnis"]
            },
            "career": {
                "title": "Puncak Karier Pengusaha dan Konglomerasi Sukses",
                "summary": "Mencapai status pemilik bisnis besar, investor senior, atau komisaris utama yang berpengaruh.",
                "meaning": "Karier di bawah pengaruh King of Pentacles adalah titik tertinggi kesuksesan duniawi. Bisnis yang kamu rintis telah berakar kokoh dan menjadi institusi yang disegani. Kamu memiliki otoritas materi untuk mendanai proyek-proyek besar dan menciptakan lapangan kerja bagi ribuan orang.",
                "advice": "Gunakan pengaruh kekayaanmu untuk memberdayakan masyarakat; jadilah pemimpin bisnis yang dermawan dan berjiwa sosial tinggi.",
                "reflectionQuestion": "Dampak sosial dan ekonomi apa yang ingin kamu wujudkan melalui imperium bisnismu?",
                "keywords": ["Konglomerat Sukses", "Puncak Materi", "Menciptakan Lapangan Kerja", "Filantropi Bisnis"]
            },
            "finance": {
                "title": "Puncak Kekayaan Materi dan Portofolio Berkelanjutan",
                "summary": "Kekayaan materi berlimpah, arus kas pasif sangat besar, dan kebebasan finansial total.",
                "meaning": "Secara finansial, King of Pentacles adalah kartu kekayaan tertinggi dalam tarot. Aset properti, portofolio saham, dan tabunganmu telah berada pada tingkat mandiri. Kamu tidak perlu lagi bekerja demi uang; uanglah yang bekerja keras menghasilkan kekayaan untukmu.",
                "advice": "Kelola asetmu dengan pengawasan profesional yang ketat; gunakan kekayaanmu untuk membangun proyek filantropi dan wakaf yang abadi.",
                "reflectionQuestion": "Bagaimana caramu mengalokasikan sebagian dari kekayaanmu untuk program pemberdayaan ekonomi masyarakat miskin?",
                "keywords": ["Kekayaan Puncak", "Aset Mandiri", "Uang Bekerja", "Filantropi Abadi"]
            },
            "selfGrowth": {
                "title": "Kematangan Karakter: Menguasai Harta Bukan Dikuasai Harta",
                "summary": "Menyadari bahwa kekayaan sejati adalah ketenangan jiwa dan kedermawanan hati.",
                "meaning": "Pengembangan diri kartu King of Pentacles adalah kemenangan atas godaan keserakahan. Kaki berbaju zirah yang menginjak kepala binatang buas melambangkan penguasaan mutlak atas nafsu materi. Harta ada di tanganmu, bukan di dalam hatimu. Kamu tenang, dermawan, dan tidak diperbudak oleh uang.",
                "advice": "Jaga hatimu agar tetap bersih dan rendah hati; nikmati berkah hidupmu tanpa pernah memandang rendah orang yang miskin.",
                "reflectionQuestion": "Apakah kamu sudah berhasil meletakkan harta kekayaan hanya di tanganmu dan bukan di dalam hatimu?",
                "keywords": ["Menguasai Harta", "Bebas dari Serakah", "Kerendahan Hati Mapan", "Ketenangan Jiwa"]
            },
            "relationships": {
                "title": "Tiang Penyangga Kesejahteraan Keluarga Besar",
                "summary": "Menjadi pelindung dan penjamin kesejahteraan bagi sanak saudara dan komunitas sekitarmu.",
                "meaning": "Dalam pergaulan dan keluarga, kamu adalah sosok sesepuh yang murah hati. Kamu siap membantu membiayai pendidikan keponakan, menanggung pengobatan kerabat yang sakit, dan menjamin hari tua orang tua dengan penuh bakti dan kemuliaan.",
                "advice": "Bantulah keluargamu dengan bijak dan berkelanjutan; ajari mereka keterampilan agar mampu mandiri secara finansial.",
                "reflectionQuestion": "Bagaimana caramu membantu anggota keluarga lain agar bisa mandiri dan meraih kesuksesan finansial mereka sendiri?",
                "keywords": ["Tiang Kesejahteraan", "Bakti Orang Tua", "Bantuan Bijak", "Pemberdayaan Keluarga"]
            },
            "spirituality": {
                "title": "Saudagar Dermawan di Jalan Ridho Ilahi",
                "summary": "Meneladani sahabat-sahabat nabi yang kaya raya namun seluruh hartanya diinfakkan untuk kejayaan umat.",
                "meaning": "Secara spiritual, King of Pentacles melambangkan saudagar shaleh yang menggunakan kekayaannya untuk membela agama dan menolong sesama (seperti teladan Abdurrahman bin Auf). Bagimu, kekayaan dunia hanyalah titipan amanah dari Tuhan untuk didistribusikan kepada mereka yang berhak. Tanganmu selalu terbuka memberi.",
                "advice": "Jadikan hartamu sebagai kendaraan menuju surga; berinfaklah di jalan Tuhan dengan hati yang tulus dan penuh kerinduan.",
                "reflectionQuestion": "Bagaimana caramu mempertanggungjawabkan setiap rupiah kekayaanmu di hadapan Tuhan kelak di hari akhir?",
                "keywords": ["Saudagar Shaleh", "Amanah Harta", "Infak Terbaik", "Kendaraan Surga"]
            }
        }
    }
]

print(f"Loaded all {len(PENTACLES_CARDS)} Pentacles cards successfully!")
