import sublime
import sublime_plugin
import sys
import re

class AddFrozenStringLiteral(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    syntax = view.settings().get("syntax")
    find_frozen_string_literal = view.find_all("\A# frozen_string_literal: (true|false)")

    if ("Ruby" in syntax or "RSpec" in syntax) and not find_frozen_string_literal:
      file_path = view.window().extract_variables()['file_path']
      ruby_version_raw = subprocess.check_output(['ruby', '-v'], cwd=file_path).decode('utf')
      ruby_version = (float)(re.search('(\d\.\d)\.\d', ruby_version_raw).group(1))
      if ruby_version >= 2.3:
        view.run_command('add_frozen_string_literal')

class AddFrozenStringLiteralCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, '# frozen_string_literal: true\n\n')
