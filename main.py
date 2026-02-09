from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Footer, Header, TextArea, Input, Button

class SaveDialog(HorizontalGroup):
    def compose(self):
        yield Input(placeholder="Filename", id="txt-filename")
        yield Button("Save", id="btn-save")

    def _on_key(self, event):
        if event.key == "ctrl+s":
            self.screen.styles.display = "block"

class SophEditor(App):

    CSS_PATH = "./style.toss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header(name="SophEditor")
        yield TextArea(language="cpp", show_line_numbers=True, )
        yield SaveDialog()
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def _on_key(self, event):
        if event.key == "ctrl+c":
            self.exit()


if __name__ == "__main__":
    app = SophEditor()
    app.theme = "dracula"
    app.run()