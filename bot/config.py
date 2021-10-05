class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    SUPPORT_CHAT_LINK = ""
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""
    ENV = "Anything"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**Hai {}.**\n__Saya Budy Uploader Bot.Anda dapat menggunakan saya untuk mengunggah file / video apa pun ke Google Drive dari tautan langsung atau File Telegram.__\n__Anda bisa tahu lebih banyak dari perintah /help.__"

    HELP_MSG = [
        ".",
        "**budi Uploader**\n__Saya dapat mengunggah file dari tautan langsung atau File Telegram ke Google Drive Anda. Yang saya butuhkan hanyalah mengautentikasi saya ke Akun Google Drive Anda dan mengirim tautan unduhan langsung atau File Telegram.__\n\nSaya memiliki lebih banyak fitur ... ! Ingin tahu tentangnya? Cukup telusuri tutorial ini dan baca pesannya dengan cermat.",
        
        f"**Otentikasi Google Drive**\n__kirim  perintah /{BotCommands.Authorize[0]} dan Anda akan menerima URL, kunjungi URL dan ikuti langkah-langkahnya dan kirim kode yang diterima di sini. Gunakan /{BotCommands.Revoke[0]} untuk mencabut Akun Google Drive Anda yang saat ini masuk.__\n\n**Note: Saya tidak akan mendengarkan perintah atau pesan apa pun (selain perintah /{BotCommands.Authorize[0]} ) sampai Anda mengizinkan saya.\nJadi, Otorisasi adalah wajib !**",
        
        f"**Direct Links**\n__Kirimi saya tautan unduhan langsung untuk sebuah file dan saya akan mengunduhnya di server saya dan mengunggahnya ke Akun Google Drive Anda. Anda dapat mengganti nama file sebelum mengunggah ke Akun GDrive. Kirimkan saja saya URL dan nama file baru yang dipisahkan dgn ' | '.__\n\n**__Contoh:__**\n```https://Contoh.com/AFileWithDirectDownloadLink.mkv | Nama File Baru.mkv```\n\n**Telegram Files**\n__Untuk Mengunggah file telegram di Akun Google drive Anda, kirimkan saya file dan saya akan mengunduh dan mengunggahnya ke Akun Google Drive Anda. Note: Pengunduhan File Telegram lambat. mungkin butuh waktu lebih lama untuk file besar.__\n\n**YouTube-DL didukung**\n__Unduh file melalui youtube-dl.\nGunakan /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Tautan situs yang didukung)__",
        
        f"**Folder Khusus untuk Upload**\n__Ingin mengunggah di folder khusus atau di__ **TeamDrive** __ ?\nGunakan /{BotCommands.SetFolder[0]} (Folder URL) untuk mengatur upload folder khusus.\nSemua file diunggah di folder khusus yang Anda berikan.__",
        
        f"**Hapus File Google Drive**\n__Hapus file google drive. Menggunakan /{BotCommands.Delete[0]} (File/Folder URL) untuk menghapus file atau membalas /{BotCommands.Delete[0]} ke pesan bot.\nAnda juga dapat mengosongkan file sampah menggunakan /{BotCommands.EmptyTrash[0]}\nNote: File dihapus secara permanen. Proses ini tidak dapat dibatalkan.\n\n**Salin File Google Drive**\n__Ya, Kloning atau Salin File Google Drive.\n__Gunakan /{BotCommands.Clone[0]} (File id / Folder id or URL) untuk menyalin File Google Drive di Akun Google Drive Anda.__",
        
        "**Aturan & Tindakan Pencegahan**\n__1. Jangan menyalin File/Folder Google Drive BESAR. Ini mungkin menggantung bot dan file Anda mungkin rusak.\n2. Kirim Satu permintaan pada satu waktu kecuali bot akan menghentikan semua proses.\n3. Jangan kirim slow link @transload dulu.\n4. Jangan menyalahgunakan, membebani, atau menyalahgunakan layanan gratis ini.__",
        
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Batas Nilai Terlampaui.**\n__User rate limit exceeded try after 24 hours.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder tidak ditemukan.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **URL Google Drive tidak valid**\nMake sure the Google Drive URL is in valid format."
    
    COPIED_SUCCESSFULLY = "✅ **berhasil disalin.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **Anda belum mengautentikasi saya untuk mengunggah ke akun mana pun.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Mengunggah Berkas...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Berhasil Diunggah.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Downloader Gagal**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Sudah mengotorisasi Akun Google Drive Anda.**\n__gunakan /revoke untuk mencabut akun saat ini.__\n__Kirimi saya tautan langsung atau File untuk Diunggah di Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Jalankan {BotCommands.Authorize[0]} dulu.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Akun Google Drive Resmi Berhasil.**'
    
    INVALID_AUTH_CODE = '❗ **Kode salah**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **Untuk Mengotorisasi akun Google Drive Anda, kunjungi ini [URL]({}) dan kirim kode yang dihasilkan di sini.**\n__Kunjungi URL > Izinkan izin > Anda akan mendapatkan kode > salin > Kirim ke sini__"
    
    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Nama file:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Tautan Folder Kustom berhasil disetel.**\n__ID folder khusus Anda - {}\ngunakan__ ```/{} clear``` __untuk membersihkannya.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **ID Folder Kustom Berhasil Dihapus.**\n__gunakan__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __untuk mengaturnya kembali__.'
    
    CURRENT_PARENT = "🆔 **ID Folder Kustom Anda Saat Ini - {}**\n__gunakan__ ```/{} (Folder link)``` __untuk mengubahnya.__"
    
    REVOKED = f"🔓 **Berhasil mencabut akun yang masuk saat ini.**\n__gunakan /{BotCommands.Authorize[0]} untuk mengautentikasi lagi dan menggunakan bot ini.__"
    
    NOT_FOLDER_LINK = "❗ **Tautan folder tidak valid.**\n__Tautan yang Anda kirim bukan milik folder.__"
    
    CLONING = "🗂️ **Kloning ke Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Berikan URL Google Drive yang valid bersama dengan perintah.**\n__Penggunaan - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **Anda tidak memiliki izin yang cukup untuk file ini.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Berhasil Dihapus.**\n__File dihapus secara permanen !\nFile id- {}__"
    
    WENT_WRONG = "⁉️ **KESALAHAN: ADA YANG SALAH**\n__Coba lagi nanti.__"
    
    EMPTY_TRASH = "🗑️🚮**Sampah Berhasil Dikosongkan !**"
    
    PROVIDE_YTDL_LINK = "❗**Berikan tautan yang didukung YouTube-DL yang valid.**"
