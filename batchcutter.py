from textual import on
from textual.app import App
from textual.widgets import DirectoryTree, Label, Static, Header, Footer, Input, Button, Checkbox, ProgressBar, RichLog
from textual.screen import Screen
from textual.containers import ScrollableContainer, Horizontal, Container, Center

class Timestamp(Static):
    def compose(self):
        yield Label("Name", id="label_name")
        yield Label("Start Time", id="label_start_time")
        yield Label("End Time", id="label_end_time")
        yield Input("", id="input_name")
        yield Input("00:00:00", id="input_start_time")
        yield Input("00:00:00", id="input_end_time")

class TimestampHeader(Static):
    def compose(self):
        with Horizontal(classes="left"):
            yield Button("Add", variant="primary", id="timestamp_add")
            yield Button("Remove", variant="default", id="timestamp_remove")
        with Horizontal(classes="right"):
            yield Button("Back", variant="error", id="timestamp_back")
        
class TimestampFooter(Static):
    def compose(self):
        with Horizontal(classes="left"):
            yield Button("Save", variant="default", id="timestamp_save")
            yield Button("Load", variant="default", id="timestamp_load")
        with Horizontal(classes="right"):
            yield Button("Start", variant="success", id="timestamp_start")
            yield Checkbox("Convert to Mp3", id="mp3_checkbox")
        

class TimestampsView(Screen):
    def compose(self):
        yield Header()
        yield TimestampHeader()
        with ScrollableContainer(id="timestamps"):
            yield Timestamp()
            yield Timestamp()
        yield TimestampFooter()
        yield Footer()
        

class DirectoryView(Screen):
    def compose(self):
        yield Header()
        yield Footer()
        yield Label("Select your video", id="label_directory")
        yield DirectoryTree("/", id="directory_tree")
        
class ProcessingView(Screen):
        
    def compose(self):
        yield Header()
        with Container():
            yield Label("Processing...", id="label_processing")
            yield ProgressBar(id="progress_processing")
        yield Footer()

class BatchCutterApp(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark_mode", "Toggle Dark Mode"),
        ("f", "push_screen('directory')", "Debug Directory"),
        ("g", "push_screen('timestamps')", "Debug Timestamps"),
        ("h", "push_screen('processing')", "Debug Processing"),
    ]
    SCREENS = {"directory": DirectoryView, "timestamps": TimestampsView, "processing": ProcessingView}
    
    CSS_PATH = "styles.tcss"
    
    def action_toggle_dark_mode(self):
        self.dark = not self.dark
        
    def on_mount(self):
        self.push_screen(DirectoryView())

if __name__ == '__main__':
    BatchCutterApp().run()