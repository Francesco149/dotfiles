c.aliases = {
    'wq': 'quit --save',
    'q': 'quit',
    'w': 'session-save',
    'animu': 'open https://myanimelist.net/anime/season',
}

c.auto_save.session = True
c.content.headers.custom = { 'Masturbates-To-Anime-Girls': 'yes' }
c.content.headers.do_not_track = True
#c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

c.fonts.completion.category = 'bold 8pt monospace'
c.fonts.completion.entry = '8pt monospace'
c.fonts.debug_console = '8pt monospace'
c.fonts.downloads = '8pt monospace'
c.fonts.hints = 'bold 10pt monospace'
c.fonts.keyhint = '8pt monospace'
c.fonts.messages.error = '8pt monospace'
c.fonts.messages.info = '8pt monospace'
c.fonts.messages.warning = '8pt monospace'
c.fonts.prompts = '8pt sans-serif'
c.fonts.statusbar = '8pt monospace'
c.fonts.tabs = '8pt monospace'
c.url.auto_search = 'naive'

c.url.default_page = 'https://www.google.it'
c.url.searchengines = {
    'DEFAULT': 'https://www.google.it/search?q={}',
    '4': 'https://boards.4chan.org/{}',
    '8': 'https://8ch.net/{}',
    'r': 'https://www.reddit.com/r/{}',
    't': 'https://twitter.com/{}',
    'aw': 'https://wiki.archlinux.org/index.php?search={}',
    'gw': 'https://wiki.gentoo.org/index.php?search={}',
    'y': 'https://www.youtube.com/results?search_query={}',
    'f': 'https://www.facebook.com/{}',
    'weeb': 'http://weeb.ddns.net/{}',
    'mg': 'https://maplestory.global/{}',
    'gh': 'https://github.com/{}',
    'nyaa': 'https://nyaa.si/?f=0&c=0_0&q={}',
    'fap': 'https://sukebei.nyaa.si/?f=0&c=0_0&q={}',
    'mal': 'https://myanimelist.net/search/all?q={}',
    'exh': 'https://exhentai.org/?f_doujinshi=1&f_manga=1&f_artistcg=1&f_gamecg=1&f_western=0&f_non-h=1&f_imageset=1&f_cosplay=0&f_asianporn=0&f_misc=1&f_search={}&f_apply=Apply+Filter',
    'eh': 'https://g.e-hentai.org/?f_doujinshi=1&f_manga=1&f_artistcg=1&f_gamecg=1&f_western=0&f_non-h=1&f_imageset=1&f_cosplay=0&f_asianporn=0&f_misc=1&f_search={}&f_apply=Apply+Filter',
}

c.url.start_pages = ['https://www.google.it']
