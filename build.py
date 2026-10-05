"""Build index.html (the installable phone app) from src/game.html.

src/game.html     the game itself, same file as the claude.ai artifact
src/head.html     <head> tags for the phone app (icons, manifest, safe-area styles)
src/sw-register.js  registers the offline worker and reloads on updates

Run: python3 build.py   then bump CACHE in sw.js, commit and push.
"""
from pathlib import Path

root = Path(__file__).parent
game = (root / "src/game.html").read_text()
head = (root / "src/head.html").read_text()
reg = (root / "src/sw-register.js").read_text()

split = game.index('<div class="phone"')
page = head + game[:split] + "</head>\n<body>\n" + game[split:]
end = page.rindex("</script>")
page = page[:end] + reg + page[end:] + "\n</body>\n</html>\n"
(root / "index.html").write_text(page)
print("built index.html")
