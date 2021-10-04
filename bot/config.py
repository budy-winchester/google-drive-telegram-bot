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
    START_MSG = "**Hai {}.**\n__Saya budi Uploader Bot.Anda dapat menggunakan saya untuk mengunggah file / video apa pun ke Google Drive dari tautan langsung atau File Telegram.__\n__Anda bisa tahu lebih banyak dari perintah /help.__"

    HELP_MSG = [
        ".",
        "**budi Uploader**\n__Saya dapat mengunggah file dari tautan langsung atau File Telegram ke Google Drive Anda. Yang saya butuhkan hanyalah mengautentikasi saya ke Akun Google Drive Anda dan mengirim tautan unduhan langsung atau File Telegram.__\n\nSaya memiliki lebih banyak fitur ... ! Ingin tahu tentangnya? Cukup telusuri tutorial ini dan baca pesannya dengan cermat.",
        
        f"**Otentikasi Google Drive**\n__kirim /{BotCommands.Authorize[0]} perintah dan Anda akan menerima URL, kunjungi URL dan ikuti langkah-langkahnya dan kirim kode yang diterima di sini. Use /{BotCommands.Revoke[0]} untuk mencabut Akun Google Drive Anda yang saat ini masuk.__\n\n**Note: Saya tidak akan mendengarkan perintah atau pesan apa pun (selain /{BotCommands.Authorize[0]} command) sampai Anda mengizinkan saya.\nJadi, Otorisasi adalah wajib !**",
        
        f"**Direct Links**\n__Kirimi saya tautan unduhan langsung untuk sebuah file dan saya akan mengunduhnya di server saya dan mengunggahnya ke Akun Google Drive Anda. Anda dapat mengganti nama file sebelum mengunggah ke Akun GDrive. Kirimkan saja saya URL dan nama file baru yang dipisahkan dgn ' | '.__\n\n**__Contoh:__**\n```https://Contoh.com/AFileWithDirectDownloadLink.mkv | Nama File Baru.mkv```\n\n**Telegram Files**\n__Untuk Mengunggah file telegram di Akun Google drive Anda, kirimkan saya file dan saya akan mengunduh dan mengunggahnya ke Akun Google Drive Anda. Note: Pengunduhan File Telegram lambat. mungkin butuh waktu lebih lama untuk file besar.__\n\n**YouTube-DL didukung**\n__Unduh file melalui youtube-dl.\nUse /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Tautan situs yang didukung)__",
        
        f"**Folder Khusus untuk Upload**\n__Ingin mengunggah di folder khusus atau di__ **TeamDrive** __ ?\nGunakan /{BotCommands.SetFolder[0]} (Folder URL) untuk mengatur upload folder khusus.\nSemua file diunggah di folder khusus yang Anda berikan.__",
        
        f"**Hapus File Google Drive**\n__Hapus file google drive. Menggunakan /{BotCommands.Delete[0]} (File/Folder URL) untuk menghapus file atau membalas /{BotCommands.Delete[0]} ke pesan bot.\nAnda juga dapat mengosongkan file sampah menggunakan /{BotCommands.EmptyTrash[0]}\nNote: File dihapus secara permanen. Proses ini tidak dapat dibatalkan.\n\n**Salin File Google Drive**\n__Ya, Kloning atau Salin File Google Drive.\n__Gunakan /{BotCommands.Clone[0]} (File id / Folder id or URL) untuk menyalin File Google Drive di Akun Google Drive Anda.__",
        
        "**Aturan & Tindakan Pencegahan**\n__1. Jangan menyalin File/Folder Google Drive BESAR. Ini mungkin menggantung bot dan file Anda mungkin rusak.\n2. Kirim Satu permintaan pada satu waktu kecuali bot akan menghentikan semua proses.\n3. Jangan kirim slow link @transload dulu.\n4. Jangan menyalahgunakan, membebani, atau menyalahgunakan layanan gratis ini.__",
        
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder not found.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."
    
    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Uploaded Successfully.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"
    
    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Cleared Successfuly.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__The link you send its not belong to a folder.__"
    
    CLONING = "🗂️ **Cloning into Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
