import sys, os
from pathlib import Path
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, TextArea, Input, Button, Static

def file_eixsts(f):
    if f:
        file = Path("./" + f)
        return file.is_file()
    else:
        return False

def file_contents(f):
    if f:
        with open(str("./" + f), "r") as file:
            return file.read()
    else:
        return ""


FILE = ("Untitled" if not len(sys.argv) > 1 else sys.argv[1])
TEXT = ("" if not file_eixsts(FILE) else file_contents(FILE))

class SophEditor(App):

    CSS_PATH = "./style.toss"

    def compose(self) -> ComposeResult:
        yield Header(name="SophEditor - Untitled")
        yield Static(FILE + "*", id="status")

        editor = TextArea(language="python", show_line_numbers=True, id="text-editor")
        editor.tab_behavior = "indent"
        editor.text = TEXT
        yield editor
        yield Static("Ctrl+S - Save" + " | " + "Ctrl+C - Exit")
        yield Footer()

    def _on_key(self, event):
        self.query_one("#status").update(FILE + "*")

        if event.key == "ctrl+c":
            self.exit()

        if event.key == "ctrl+s":
            with open(str("./" + FILE), "w") as file:
                file.write(self.query_one("#text-editor").text)
                self.query_one("#status").update(FILE)
                file.close()



if __name__ == "__main__":

    app = SophEditor()
    app.theme = "dracula"
    app.run()