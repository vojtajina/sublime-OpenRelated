import sublime, sublime_plugin
import os.path
from converter import Converter

class OpenRelatedCommand(sublime_plugin.WindowCommand):
    def run(self):
        win = self.window
        view = win.active_view()
        current_file = view.file_name()

        for pattern in view.settings().get('open_related_patterns', []):
            file = Converter(pattern[0], pattern[1]).convert(current_file)
            if file and os.path.exists(file):
                if win.num_groups() > 1:
                    win.focus_group((win.active_group() + 1) % win.num_groups())
                self.window.open_file(file)
                return

        sublime.status_message("Cannot find related file !")

    def is_enabled(self):
        return self.window.active_view() != None

    def description(self):
        return "Open related file."
